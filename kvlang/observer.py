from kivy import Logger
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import StringProperty, AliasProperty, ObjectProperty, NumericProperty
from kvlang.ast import _ASTBase, kvOutput, parsestring, ASTBuilder


class ASTObserver(_ASTBase, EventDispatcher):
	_source = StringProperty('')
	source = AliasProperty(_ASTBase.get_source, _ASTBase.set_source, bind=('_source',))

	_filename = StringProperty('<source>')
	filename = AliasProperty(_ASTBase.get_filename, _ASTBase.set_filename, bind=('_filename',))

	compiler = ObjectProperty(kvOutput)
	parser = ObjectProperty(parsestring)

	generate_delay = NumericProperty(300)

	def __init__(self, **kwargs):
		kwargs.setdefault('logger', Logger)

		super(ASTObserver, self).__init__(**kwargs)

		self.register_event_type('on_generate')
		self.register_event_type('on_compile')
		self.register_event_type('on_tree_changed')

		self._generate_ast_timer = None
		self.auto_generate_ast = Clock.create_trigger(self._generate_ast_schedule)
		
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

	def _generate_ast_schedule(self, _dt):
		if self._generate_ast_timer:
			self._generate_ast_timer.cancel()
		self._generate_ast_timer = Clock.schedule_once(self._generate_ast, self.generate_delay / 1000.)

	def _generate_ast(self, *_):
		super(ASTObserver, self)._generate_ast()
		self.dispatch('on_generate', self.tree)

	def compile(self):
		output = super(ASTObserver, self).compile()
		self.dispatch('on_compile', output)
		return output

	def _dispatch_tree_changed(self, *_):
		self.dispatch('on_tree_changed', self.tree)
	
	
Builder = ASTBuilder(ASTObserver)
