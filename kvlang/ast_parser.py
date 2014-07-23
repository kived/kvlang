from copy import copy
from functools import partial
from types import CodeType
import sys
from kivy.compat import iteritems, iterkeys
from kivy.factory import Factory
from kivy.lang import global_idmap, BuilderException, ParserRuleProperty, create_handler, custom_callback, Parser, \
	ParserException, ParserRule
from kivy.logger import Logger
from kivy.utils import QueryDict
from kvlang.kvTree import DirectiveNode, WidgetNode, WidgetLikeNode, PropertyNode, CanvasNode, InstructionNode


def load_ast(self, ast, **kwargs):
	kwargs.setdefault('rulesonly', False)
	self._current_filename = fn = kwargs.get('filename', None)
	
	if fn in self.files:
		Logger.warning(
			'kvlang: The file {} is loaded multiple times, '
		    'you might have unwanted behaviors.'.format(fn))
	
	try:
		parser = ast.get_parser_result()
	
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
			# widget._ast_node = weakref.proxy(ast.tree)
			#ast.tree._ast_widget = widget.proxy_ref
			#_apply_ast_rule(self, widget, ast.tree, parser.root, parser.root)
			self._apply_rule(widget, parser.root, parser.root)
			return widget
	finally:
		self._current_filename = None


def _apply_ast_rule(self, widget, node, rule, rootrule, template_ctx=None):
	assert (rule not in self.rulectx)
	self.rulectx[rule] = rctx = {
		'ids': {'root': widget.proxy_ref},
		'set': [], 'hdl': []}

	assert (rootrule in self.rulectx)
	rctx = self.rulectx[rootrule]

	if template_ctx is not None:
		rctx['ids']['ctx'] = QueryDict(template_ctx)

	if rule.id:
		rule.id = rule.id.split('#', 1)[0].strip()
		rctx['ids'][rule.id] = widget.proxy_ref

		_ids = dict(rctx['ids'])
		_root = _ids.pop('root')
		_new_ids = _root.ids
		for _key in iterkeys(_ids):
			if _ids[_key] == _root:
				continue
			_new_ids[_key] = _ids[_key]
		_root.ids = _new_ids

	rule.create_missing(widget)

	if rule.canvas_before:
		with widget.canvas.before:
			self._build_canvas(widget.canvas.before, widget,
			                   rule.canvas_before, rootrule)
	if rule.canvas_root:
		with widget.canvas:
			self._build_canvas(widget.canvas, widget,
			                   rule.canvas_root, rootrule)
	if rule.canvas_after:
		with widget.canvas.after:
			self._build_canvas(widget.canvas, widget,
			                   rule.canvas_after, rootrule)

	Factory_get = Factory.get
	Factory_is_template = Factory.is_template
	for crule in rule.children:
		cname = crule.name

		cls = Factory_get(cname)

		if Factory_is_template(cname):
			ctx = {}
			idmap = copy(global_idmap)
			idmap.update({'root': rctx['ids']['root']})
			if 'ctx' in rctx['ids']:
				idmap.update({'ctx': rctx['ids']['ctx']})
			try:
				for prule in crule.properties.values():
					value = prule.co_value
					if type(value) is CodeType:
						value = eval(value, idmap)
					ctx[prule.name] = value
				for prule in crule.handlers:
					value = eval(prule.value, idmap)
					ctx[prule.name] = value
			except Exception as e:
				tb = sys.exc_info()[2]
				raise BuilderException(
					prule.ctx, prule.line,
					'{}: {}'.format(e.__class__.__name__, e), cause=tb)

			child = cls(**ctx)
			widget.add_widget(child)

			if crule.id:
				rctx['ids'][crule.id] = child

		else:
			child = cls(__no_builder=True)
			widget.add_widget(child)
			self.apply(child)
			_apply_ast_rule(self, child, None, crule, rootrule)

	if rule.properties:
		rctx['set'].append((widget.proxy_ref, list(rule.properties.values())))

	if rule.handlers:
		rctx['hdl'].append((widget.proxy_ref, rule.handlers))

	if rootrule is not rule:
		del self.rulectx[rule]
		return

	try:
		rule = None
		for widget_set, rules in reversed(rctx['set']):
			for rule in rules:
				assert (isinstance(rule, ParserRuleProperty))
				key = rule.name
				value = rule.co_value
				if type(value) is CodeType:
					value = create_handler(widget_set, widget_set, key,
					                       value, rule, rctx['ids'])
				setattr(widget_set, key, value)
	except Exception as e:
		if rule is not None:
			tb = sys.exc_info()[2]
			raise BuilderException(rule.ctx, rule.line,
			                       '{}: {}'.format(e.__class__.__name__, e), cause=tb)
		raise e

	try:
		crule = None
		for widget_set, rules in rctx['hdl']:
			for crule in rules:
				assert (isinstance(crule, ParserRuleProperty))
				assert (crule.name.startswith('on_'))
				key = crule.name
				if not widget_set.is_event_type(key):
					key = key[3:]
				idmap = copy(global_idmap)
				idmap.update(rctx['ids'])
				idmap['self'] = widget_set.proxy_ref
				widget_set.bind(**{key: partial(custom_callback, crule, idmap)})

				if crule.name == 'on_parent':
					Factory.Widget.parent.dispatch(widget_set.__self__)
	except Exception as e:
		if crule is not None:
			tb = sys.exc_info()[2]
			raise BuilderException(
				crule.ctx, crule.line,
				'{}: {}'.format(e.__class__.__name__, e), cause=tb)
		raise e

	del self.rulectx[rootrule]


class ASTParser(Parser):
	
	def __init__(self, **kwargs):
		self.rules = []
		self.templates = []
		self.root = None
		self.sourcecode = []
		self.directives = []
		self.dynamic_classes = {}
		self.filename = kwargs.get('filename', None)

		self.ast = kwargs.get('ast', None)
		if self.ast is None:
			raise ValueError('No AST passed')
		self.parse(self.ast)
	
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

		def print_obj(obj, f):
			print >> f, ('\t' * obj.level) + str(obj)
			for pn, pv in obj.properties.iteritems():
				print >> f, ('\t' * obj.level) + '-- ' + str(pn) + ': ' + str(pv)
			for h in obj.handlers:
				print >> f, ('\t' * obj.level) + '-- ' + str(h)
			for c in obj.children:
				print_obj(c, f)
			pass

		for obj in rules:
			print_obj(obj, file('kvparse.out', 'w+'))
	
		for rule in rules:
				rule.precompile()
	
	def parse_tree(self, root):
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
			
			for child in node.interesting_children():
				if isinstance(child, PropertyNode):
					name = child.name
					value = child.value
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
