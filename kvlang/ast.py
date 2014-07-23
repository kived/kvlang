import re
from time import time
import antlr3
from antlr3.tree import CommonTree
from kivy.clock import Clock

from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import StringProperty, AliasProperty, ObjectProperty, NumericProperty
from kvlang.ast_parser import ASTParser, load_ast

from kvlang.kvParser import kvParser
from kvlang.kvTokenLexer import kvTokenLexer
from kvlang.kvTree import Node, WidgetLikeNode, PropertyNode, PythonNode, CanvasNode, WidgetNode


def parsestring(kvstring):
	start_time = time()
	cStream = antlr3.ANTLRStringStream(kvstring)
	lexer = kvTokenLexer(cStream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = kvParser(tokens)

	Node.set_source(tokens.getTokens(), kvstring)

	result = parser.kvfile()
	finish_time = time()
	Logger.debug('kvlang: parsed kv file in %0.4fs' % (finish_time - start_time))
	return tokens, result, parser.root_node


class kvOutput(object):
	def __init__(self, tree, tokens, source):
		self.indent_level = 0
		self.output = []

		self.tokens = tokens
		self.source = source

		start_time = time()
		if tree.isNil():
			self.build(tree.getChildren())
		else:
			self.build([tree])
		finish_time = time()

		Logger.debug('kvlang: compiled kv output in %0.4fs' % (finish_time - start_time))

		if self.output[-1]:
			self.output += ['']

	def __str__(self):
		return '\n'.join(self.output)

	def build(self, children):
		for child in children:
			nodetype = str(type(child).__name__).lower()
			if hasattr(self, nodetype):
				child.output_start = len(str(self))
				getattr(self, nodetype)(child)
				child.output_stop = len(str(self))

	def indent(self):
		self.indent_level += 1

	def dedent(self):
		self.indent_level -= 1
		assert self.indent_level >= 0

	def write(self, text):
		self.output += [(('\t' * self.indent_level) + str(t)) for t in text.split('\n')]

	def blanknode(self, tree):
		if self.output and self.output[-1]:
			# squash multiple blank lines
			self.write('')

	def directivenode(self, tree):
		self.write(str(tree))

	def commentnode(self, tree):
		self.write(str(tree))

	def canvasnode(self, tree):
		self.write(str(tree) + ':')
		self.indent()
		self.build(tree.getChildren())
		self.dedent()

	def instructionnode(self, tree):
		self.write(str(tree) + ':')
		self.indent()
		self.build(tree.getChildren())
		self.dedent()

	def classrulenode(self, tree):
		self.write(str(tree) + ':')
		self.indent()
		self.build(tree.getChildren())
		self.dedent()

	def templaterulenode(self, tree):
		self.write(str(tree) + ':')
		self.indent()
		self.build(tree.getChildren())
		self.dedent()

	def widgetnode(self, tree):
		self.write(str(tree) + ':')
		self.indent()
		self.build(tree.getChildren())
		self.dedent()

	def propertynode(self, tree):
		self.write(str(tree))


class AST(EventDispatcher):
	_source = StringProperty('')
	
	def get_source(self):
		return self._source
	def set_source(self, source):
		self._source = self._tab(source)
	source = AliasProperty(get_source, set_source, bind=('_source',))
	
	_filename = StringProperty('<source>')
	
	def get_filename(self):
		return self._filename
	def set_filename(self, filename):
		if filename != self._filename:
			if filename is None:
				self._filename = '<source>'
			else:
				self._filename = filename
				self._load()
	filename = AliasProperty(get_filename, set_filename, bind=('_filename',))
	
	compiler = ObjectProperty(kvOutput)
	parser = ObjectProperty(parsestring)
	
	generate_delay = NumericProperty(300)
	
	def __init__(self, **kwargs):
		self.token_stream = None
		self.result = None
		self.root_node = None
		self.tree = None
		self.tokens = []
		
		super(AST, self).__init__(**kwargs)
		
		self.register_event_type('on_generate')
		self.register_event_type('on_compile')
		self.register_event_type('on_tree_changed')
		
		self._generate_ast_timer = None
		self._generate_ast_trigger = Clock.create_trigger(self._generate_ast_schedule)
		self.bind(source=self._generate_ast_trigger)
		
		self.generate_ast = Clock.create_trigger(self._generate_ast)
		self.dispatch_tree_changed = Clock.create_trigger(self._dispatch_tree_changed)
		
		if self.source:
			self._generate_ast()
	
	def on_generate(self, tree):
		pass
	
	def on_compile(self, output):
		pass
	
	def on_tree_changed(self, tree):
		pass
	
	def load_now(self, filename=None, source=None):
		if filename:
			self._filename = filename
			self._load()
		elif source:
			self._filename = '<source>'
			self._source = self._tab(source)
		self._generate_ast()
	
	def load(self, filename=None, source=None):
		if filename:
			self.filename = filename
		elif source:
			self.filename = None
			self.source = source
			
	
	def _load(self):
		with open(self.filename) as f:
			self.source = f.read()
	
	def _generate_ast_schedule(self, _dt):
		if self._generate_ast_timer:
			self._generate_ast_timer.cancel()
		self._generate_ast_timer = Clock.schedule_once(self._generate_ast, self.generate_delay / 1000.)
	
	def _tab(self, string):
		ts = re.compile(r'^ {4}', re.M)
		string, count = ts.subn(r'\t', string)
		i = 1
		while count > 0:
			subpatt = re.compile(r'^\t{' + str(i) + '} {4}', re.M)
			i += 1
			string, count = subpatt.subn('\t' * i, string)
		return string
	
	def _generate_ast(self, *_):
		self.token_stream, self.result, self.root_node = self.parser(self.source)
		self.tree = self.result.tree
		self.tokens = self.token_stream.getTokens()
		
		fail_root = None
		if not self.root_node:
			try:
				if self.tree.get_name() == 'RootWidget':
					self.root_node = self.tree
			except Exception:
				pass
			
			if not self.root_node:
				for child in self.tree.getChildren():
					if isinstance(child, WidgetLikeNode):
						fail_root = child
						if child.get_name() == 'RootWidget':
							self.root_node = child
							break
				if fail_root and not self.root_node:
					self.root_node = fail_root
		
		Logger.debug('kvlang: root node: %s' % str(self.root_node))
		
		self.dispatch('on_generate', self.tree)
	
	def __gen_widget(self, widget):
		yield widget
		for child in widget.children:
			for w in self.__gen_widget(child):
				yield w
	
	def __gen_tree(self, tree):
		yield tree
		for child in tree.widgets():
			for c in self.__gen_tree(child):
				yield c
	
	def instrument(self, root):
		gen_tree = self.__gen_tree(self.tree)
		gen_widget = self.__gen_widget(root)
		try:
			while True:
				t, w = next(gen_tree), next(gen_widget)
				print 'instrument', t, '<=>', w
				t._ast_widget = w
				w._ast_tree = t
		except StopIteration:
			print 'instrumentation finished'
	
	def compile(self):
		output = str(self.compiler(self.tree, self.tokens, self.source))
		self.dispatch('on_compile', output)
		return output
	
	def swap_node(self, node, index):
		if node and node.parent:
			parent = node.parent
			if index < 0 or index >= parent.getChildCount():
				raise IndexError(index)
			
			previndex = node.childIndex
			dest = parent.getChild(index)
			
			parent.setChild(index, node)
			parent.setChild(previndex, dest)
			
			self.dispatch_tree_changed()
	
	def shift_node(self, node, index):
		if node and node.parent:
			parent = node.parent
			
			if index < 0 or index >= parent.getChildCount():
				raise IndexError(index)
			
			children = parent.children[:]
			children.remove(node)
			children = children[:index] + [node] + children[index:]
			parent.children = children
			parent.freshenParentAndChildIndexes()
			
			self.dispatch_tree_changed()
	
	def _dispatch_tree_changed(self, *_):
		self.dispatch('on_tree_changed', self.tree)
	
	def move_node(self, node, parent, index=None):
		if node and parent:
			if node.parent:
				node.parent.deleteChild(node.childIndex)
			parent.addChild(node)
			
			if index:
				self.shift_node(node, index)
			
			self.dispatch_tree_changed()
	
	def widget_add_property(self, node, key, value):
		if node and key:
			if not isinstance(node, WidgetLikeNode):
				raise ValueError('node <%s> is not widget-like' % str(node))
			
			keytoken = antlr3.ClassicToken(text=key)
			keynode = CommonTree(keytoken)
			valnode = PythonNode(None, None)
			valnode.sourcetext = value
			propnode = PropertyNode(None, keynode, valnode)
			node.addChild(propnode)
			
			index = None
			i = 0
			count = node.getChildCount()
			while i < count:
				if isinstance(node.getChild(i), (WidgetNode, CanvasNode)):
					index = i
					break
				i += 1
			
			if index:
				self.shift_node(propnode, index)
			
			self.dispatch_tree_changed()
	
	def remove_node(self, node, remove_root=False):
		if node:
			if node is not self.root_node and node.parent:
				node.parent.deleteChild(node.childIndex)
				self.dispatch_tree_changed()
	
	def find_all(self, type_):
		for node in self._find_all(self.tree, type_):
			yield node
	
	def _find_all(self, tree, type_):
		if isinstance(tree, type_):
			yield tree
		for child in tree.children:
			for node in self._find_all(child, type_):
				yield node
	
	def get_parser_result(self):
		return ASTParser(ast=self)
	
	@classmethod
	def _create_ast(cls, source=None, filename=None):
		ast = cls()
		ast.load_now(source=source, filename=filename)
		#print ast.compile()
		return load_ast(Builder, ast, filename=filename)
	
	@classmethod
	def load_file(cls, filename):
		return cls._create_ast(filename=filename)
	
	@classmethod
	def load_string(cls, source):
		return cls._create_ast(source=source)
	

