import os
from time import time
import re
import antlr3
from antlr3.tree import CommonTree

from kvlang.kvParser import kvParser
from kvlang.kvTokenLexer import kvTokenLexer
from kvlang.kvTree import Node, WidgetLikeNode, PropertyNode, PythonNode, CanvasNode, WidgetNode


def loadtokens():
	tokens = {}
	for line in open(os.path.join(os.path.dirname(__file__), 'kv.tokens')):
		name, _, id = line.partition('=')
		tokens[int(id)] = name
	return tokens

tokens = loadtokens()


def printtoken(token):
	try:
		tval = str(token).split(',')
		toktype = tokens[int((tval[-1] if tval[-1][0] == '<' else tval[-2])[1:-1])]
		print toktype + '\t' + ','.join(tval)
	except Exception:
		print 'UNKNOWN\t' + str(token)


def parsestring(kvstring, logger=None):
	start_time = time()
	cStream = antlr3.ANTLRStringStream(kvstring)
	lexer = kvTokenLexer(cStream)
	tokenstream = antlr3.CommonTokenStream(lexer)
	for token in tokenstream.getTokens():
		printtoken(token)
	parser = kvParser(tokenstream)

	Node.set_source(tokenstream.getTokens(), kvstring)

	result = parser.kvfile()
	finish_time = time()
	if logger:
		logger('debug', 'kvlang: parsed kv file in %0.4fs' % (finish_time - start_time))
	return tokenstream, result, parser.root_node


class kvOutput(object):
	def __init__(self, tree, tokens, source, logger=None):
		self.indent_level = 0
		self.output = []

		self.tokens = tokens
		self.source = source

		if not tree:
			raise Exception('cannot generate output with no tree')

		start_time = time()
		if tree.isNil():
			self.build(tree.getChildren())
		else:
			self.build([tree])
		finish_time = time()
		
		if logger:
			logger('debug', 'kvlang: compiled kv output in %0.4fs' % (finish_time - start_time))

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


class _ASTBase(object):
	def __init__(self, **kwargs):
		self._logger = kwargs.pop('logger', None)
		self._immediate_load = False
		self._inited = False
		self._filename = '<source>'
		self._source = ''

		super(_ASTBase, self).__init__(**kwargs)
		self.token_stream = None
		self.result = None
		self.root_node = None
		self.tree = None
		self.tokens = []
		self._inited = True

	def logger(self, level, message):
		if self._logger:
			lmessage = '[' + level + '] ' + message
			if self._logger == 'print':
				print lmessage
			elif hasattr(self._logger, level):
				getattr(self._logger, level)(message)
			elif callable(self._logger):
				try:
					self._logger(level, message)
				except TypeError:
					self._logger(lmessage)
	
	def get_filename(self):
		return self._filename
	def set_filename(self, filename):
		if filename != self._filename:
			if filename:
				self._filename = filename
				self._load_file()
			else:
				self._filename = '<source>'
	
	def get_source(self):
		return self._source
	def set_source(self, source):
		if source != self._source:
			self._source = self._tab(source)
			if self._inited:
				if self._immediate_load:
					self._generate_ast()
				else:
					self.auto_generate_ast()

	def load(self, filename=None, source=None):
		try:
			self._immediate_load = True
			if filename:
				self.filename = filename
			elif source:
				self.source = source
		finally:
			self._immediate_load = False
	
	def _load_file(self):
		with open(self.filename) as f:
			self.source = f.read()

	@staticmethod
	def _tab(string):
		ts = re.compile(r'^ {4}', re.M)
		string, count = ts.subn(r'\t', string)
		i = 1
		while count > 0:
			subpatt = re.compile(r'^\t{' + str(i) + '} {4}', re.M)
			i += 1
			string, count = subpatt.subn('\t' * i, string)
		return string

	def _generate_ast(self, *_):
		self.token_stream, self.result, self.root_node = self.parser(self.source, self.logger)
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
		
		self.logger('debug', 'kvlang: root node: %s' % str(self.root_node))
	
	def generate_ast(self, *_):
		self._generate_ast()
	
	def auto_generate_ast(self, *_):
		self._generate_ast()

	def compile(self):
		output = ''
		if self.tree:
			output = str(self.compiler(self.tree, self.tokens, self.source, self.logger))
		return output
	
	def dispatch_tree_changed(self):
		pass

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
			try:
				children.remove(node)
			except ValueError:
				pass
			children = children[:index] + [node] + children[index:]
			parent.children = children
			parent.freshenParentAndChildIndexes()

			self.dispatch_tree_changed()

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

	# def get_parser_result(self):
	# 	return ASTParser(ast=self)


class AST(_ASTBase):
	def __init__(self, **kwargs):
		kwargs.setdefault('logger', 'print')
		
		source = kwargs.pop('source', '')
		filename = kwargs.pop('filename', '<source>')
		self.compiler = kwargs.pop('compiler', kvOutput)
		self.parser = kwargs.pop('parser', parsestring)
		self.generate_delay = kwargs.pop('generate_delay', 300)
		
		super(AST, self).__init__(**kwargs)
		
		self.load(filename=filename, source=source)
	
	filename = property(_ASTBase.get_filename, _ASTBase.set_filename)
	source = property(_ASTBase.get_source, _ASTBase.set_source)


class ASTBuilder(object):
	def __init__(self, ast_impl=AST):
		self._logger = None
		self._builder = None
		self._load_ast = None
		self.ast_impl = ast_impl
	
	def _create_ast(self, source=None, filename=None):
		if not self._logger:
			from kivy.logger import Logger
			self._logger = Logger
		ast = self.ast_impl(source=source, filename=filename, logger=self._logger)
		# print ast.compile()
		return self.load_ast(ast, filename=filename)

	def load_file(self, filename):
		return self._create_ast(filename=filename)

	def load_string(self, source):
		return self._create_ast(source=source)
	
	def load_ast(self, tree, **kwargs):
		if not self._builder:
			from kivy.lang import Builder
			from kvlang.ast_parser import load_ast
			self._builder = Builder
			self._load_ast = load_ast
		return tree, self._load_ast(self._builder, tree, **kwargs)


Builder = ASTBuilder()
