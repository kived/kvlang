from functools import partial
import weakref
from kivy.compat import iteritems
from kivy.factory import Factory
from kivy.lang import ParserRuleProperty, Parser, ParserException, ParserRule as kivy_ParserRule, Builder as kivy_Builder
from kivy.logger import Logger
from kivy.weakproxy import WeakProxy
from kvlang.kvTree import DirectiveNode, WidgetNode, WidgetLikeNode, PropertyNode, CanvasNode, InstructionNode


class ParserRule(kivy_ParserRule):
	__slots__ = ('ast_node', '__weakref__')


def load_ast(self, ast, **kwargs):
	kwargs.setdefault('rulesonly', False)
	self._current_filename = fn = kwargs.get('filename', None)

	if fn in self.files:
		Logger.warning(
			'kvlang: The file {} is loaded multiple times, '
		    'you might have unwanted behaviors.'.format(fn))
	
	try:
		parser = ASTParser(ast=ast)
	
		self.rules.extend(parser.rules)
		self._clear_matchcache()
	
		for name, cls, template in parser.templates:
			self.templates[name] = (cls, template, fn)
			Factory.register(name, cls=partial(self.template, name), is_template=True)
	
		for name, baseclasses in iteritems(parser.dynamic_classes):
			Factory.register(name, baseclasses=baseclasses, filename=fn)
		
		if kwargs['rulesonly'] and parser.root:
			filename = kwargs.get('rulesonly', '<string>')
			raise Exception('The file <%s> contains also non-rules '
							'directives' % filename)
		
		if fn and (parser.templates or
				   parser.dynamic_classes or parser.rules):
			self.files.append(fn)
		
		if parser.root:
			widget = Factory.get(parser.root.name)()
			self._apply_rule(widget, parser.root, parser.root)
			return widget
	finally:
		self._current_filename = None


Builder_apply_rule = kivy_Builder._apply_rule


def _apply_rule(self, widget, rule, *args, **kwargs):
	Builder_apply_rule(widget, rule, *args, **kwargs)
	if hasattr(rule, 'ast_node'):
		widget.ast_node = rule.ast_node
		widget.ast_node.ast_widget = widget.proxy_ref

kivy_Builder._apply_rule = partial(_apply_rule, kivy_Builder)


class ASTParser(Parser):
	
	def __init__(self, **kwargs):
		self.ast = kwargs.get('ast', None)
		if self.ast is None:
			raise ValueError('No AST passed')
		kwargs['content'] = self.ast
		super(ASTParser, self).__init__(**kwargs)
	
	def execute_directives(self):
		for directive in self.ast.find_all(DirectiveNode):
			self.directives.append((directive.token.line,
			                        str(directive).strip()[2:]))
		super(ASTParser, self).execute_directives()
	
	def parse(self, ast):
		lines = ast.source.splitlines()
		if not lines:
			return
		num_lines = len(lines)
		lines = list(zip(list(range(num_lines)), lines))
		self.sourcecode = lines[:]
		
		self.execute_directives()
		
		rules = self.parse_tree(ast.tree)

		for rule in rules:
			rule.precompile()
	
	def parse_tree(self, root):
		if not root:
			return []
		nodes = root.children if root.isNil() else [root]
		return self.parse_nodes(nodes)
	
	def parse_nodes(self, nodes, level=0):
		objects = []
		
		for node in [n for n in nodes if isinstance(n, WidgetLikeNode)]:
			ln = node.get_sourceline()
			
			name = str(node)
			if (level != 0
			        and name not in self.PROP_ALLOWED 
			        and any(ord(z) not in self.PROP_RANGE for z in name)):
				raise ParserException(self, ln, 'Invalid class name')

			current_object = ParserRule(self, ln, name, level)
			objects.append(current_object)
			
			node.ast_rule = weakref.proxy(current_object)
			current_object.ast_node = weakref.proxy(node)
			
			for child in node.interesting_children():
				if isinstance(child, PropertyNode):
					name = child.name
					value = child.parsevalue
					if name == 'id':
						if len(value) == 0:
							raise ParserException(self, ln, 'Empty id')
						if value in ('self', 'root'):
							raise ParserException(self, ln,
							                      'Invalid id, cannot be "self" or "root"')
						current_object.id = value
					elif len(value):
						rule = ParserRuleProperty(self, ln, name, value)
						if name[:3] == 'on_':
							current_object.handlers.append(rule)
						else:
							current_object.properties[name] = rule
				elif isinstance(child, CanvasNode):
					canvas = self.parse_nodes([child], level + 2)
					setattr(current_object, child.canvas_object, canvas[0])
				elif isinstance(child, (WidgetNode, InstructionNode)):
					children = self.parse_nodes([child], level + 1)
					children_set = getattr(current_object, 'children', [])
					children_set += children
					current_object.children = children_set
		
		return objects
