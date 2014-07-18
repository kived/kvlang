from time import time
import antlr3
from kivy.clock import Clock

from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import StringProperty, AliasProperty, ObjectProperty, NumericProperty

from kvlang.kvParser import kvParser
from kvlang.kvTokenLexer import kvTokenLexer
from kvlang.kvTree import Node


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
	return tokens, result


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
		self.output += [('\t' * self.indent_level) + str(text)]

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
	source = StringProperty('')
	
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
	filename = AliasProperty(get_filename, set_filename)
	
	compiler = ObjectProperty(kvOutput)
	parser = ObjectProperty(parsestring)
	
	generate_delay = NumericProperty(300)
	
	def __init__(self, **kwargs):
		self.token_stream = None
		self.result = None
		self.tokens = []
		
		super(AST, self).__init__(**kwargs)
		
		self.register_event_type('on_generate')
		self.register_event_type('on_compile')
		
		self._generate_ast_timer = None
		self._generate_ast_trigger = Clock.create_trigger(self._generate_ast_schedule)
		self.bind(source=self._generate_ast_trigger)
		
		if self.source:
			self._generate_ast()
	
	def on_generate(self, tree):
		pass
	
	def on_compile(self, output):
		pass
	
	def load(self, filename):
		self.filename = filename
	
	def _load(self):
		with open(self.filename) as f:
			self.source = f.read()
	
	def _generate_ast_schedule(self, _dt):
		if self._generate_ast_timer:
			self._generate_ast_timer.cancel()
		self._generate_ast_timer = Clock.schedule_once(self._generate_ast, self.generate_delay / 1000.)
	
	def _generate_ast(self, *_):
		self.token_stream, self.result = self.parser(self.source)
		self.tree = self.result.tree
		self.tokens = self.token_stream.getTokens()
		self.dispatch('on_generate', self.tree)
	
	def compile(self):
		output = str(self.compiler(self.tree, self.tokens, self.source))
		self.dispatch('on_compile', output)
		return output
