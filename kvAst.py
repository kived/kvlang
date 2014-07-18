import sys
from time import time

import kivy
from kivy.clock import Clock

kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.treeview import TreeViewLabel
from kivy.properties import StringProperty, ObjectProperty
from kivy.logger import Logger

from kvlang.ast import AST

root_kv = '''
<AstNode>:
	markup: True
	text: '%s [color=666666][%s][/color]' % (self.rule_text, self.rule_type)

BoxLayout:
	orientation: 'vertical'
	Label:
		size_hint_y: None
		height: '24sp'
		text: 'AST for {}'
	
	BoxLayout:
		size_hint_y: None
		height: '24sp'
		
		canvas.before:
			Color:
				rgba: 0.3, 0.3, 0.3, 1
			Rectangle:
				pos: self.pos
				size: self.size
		
		FloatLayout:
			Label:
				text: 'Source'
				size_hint: 1, 1
				pos: self.parent.pos
			ToggleButton:
				id: source_edit
				text: 'Edit'
				size_hint: None, None
				width: self.texture_size and (self.texture_size[0] + 24)
				height: self.parent.height - 8
				y: self.parent.y + 4
				x: self.parent.x + 8
		Label:
			text: 'AST'
		Label:
			text: 'Output'
	
	BoxLayout:
		ScrollView:
			id: sv_source_text
			TextInput:
				id: source_text
				size_hint_y: None
				height: max(self.minimum_height, sv_source_text.height)
				readonly: source_edit.state == 'normal'
		BoxLayout:
			orientation: 'vertical'
			
			BoxLayout:
				orientation: 'horizontal'
				size_hint_y: None
				height: sp(64)
				
				Button:
					id: btn_moveup
					text: '^'
				Button:
					id: btn_movedown
					text: 'v'
				Button:
					id: btn_addprop
					text: '+'
				Button:
					id: btn_removenode
					text: '-'
			
			ScrollView:
				TreeView:
					id: treeview
					hide_root: True
					height: self.minimum_height
					size_hint_y: None
		ScrollView:
			id: sv_output_text
			TextInput:
				id: output_text
				size_hint_y: None
				height: max(self.minimum_height, sv_output_text.height)
				readonly: True
'''


class AstNode(TreeViewLabel):
	rule_text = StringProperty()
	rule_type = StringProperty()
	tree_node = ObjectProperty()


def cleartreeview(tree_view):
	nodes = list(tree_view.iterate_all_nodes())
	for node in nodes:
		tree_view.remove_node(node)

def buildtreeview(tree, tree_view):
	start_time = time()
	parent = None
	cleartreeview(tree_view)
	populatetreeview(tree_view, parent, tree, True)
	finish_time = time()
	Logger.debug('kvAst: tree built in %0.4fs' % (finish_time - start_time))


def populatetreeview(tree_view, parent, tree, is_open=False):
	tree_node = parent
	if not tree.isNil():
		rule_type = type(tree).__name__
		if rule_type.endswith('Node'):
			rule_type = rule_type[:-4]
		tree_node = tree_view.add_node(AstNode(rule_text=str(tree), rule_type=rule_type,
		                                       tree_node=tree, is_open=is_open), parent)

	for child in tree.getChildren():
		populatetreeview(tree_view, tree_node, child, is_open=is_open)


class AstApp(App):
	def __init__(self, filename):
		super(AstApp, self).__init__()
		self.ast_file = filename
		self.ast = AST()
		self.selected = None
	
	def build(self):
		root = Builder.load_string(root_kv.format(self.ast_file))
		st = root.ids.source_text
		self.ast.bind(source=st.setter('text'))
		st.bind(text=self.ast.setter('source'))
		
		self.ast.bind(on_generate=lambda _, tree: buildtreeview(tree, root.ids.treeview))
		
		self.ast.bind(on_generate=lambda *_: setattr(self, 'output', self.ast.compile()))
		self.ast.bind(on_compile=lambda _, output: setattr(root.ids.output_text, 'text', output))
		self.ast.bind(on_compile=self.save_outfile)
		
		self.ast.bind(on_tree_changed=self.refresh)
		
		Clock.schedule_once(self.load)
		
		root.ids.treeview.bind(selected_node=self.update_selection)
		
		root.ids.btn_movedown.bind(on_press=lambda *_: self.move_node(1))
		root.ids.btn_moveup.bind(on_press=lambda *_: self.move_node(-1))
		root.ids.btn_addprop.bind(on_press=self.add_property)
		root.ids.btn_removenode.bind(on_press=self.remove_node)
		
		return root
	
	def refresh(self, *_):
		self.selected = None
		buildtreeview(self.ast.tree, self.root.ids.treeview)
		self.ast.compile()
	
	def move_node(self, dir):
		if self.selected:
			tree = self.selected.tree_node
			if tree.parent:
				parent = tree.parent
				count = parent.getChildCount()
				if count > 1:
					index = tree.childIndex
					destindex = index + dir
					if destindex < 0:
						destindex = count - 1
					elif destindex >= count:
						destindex = 0
					self.ast.shift_node(tree, destindex)
	
	def add_property(self, *_):
		if self.selected:
			try:
				key = 'prop'
				value = "'val'"
				self.ast.widget_add_property(self.selected.tree_node, key, value)
			except ValueError, e:
				print str(e)
	
	def remove_node(self, *_):
		if self.selected:
			self.ast.remove_node(self.selected.tree_node)
	
	def load(self, _dt):
		self.ast.load(filename=self.ast_file)
	
	def save_outfile(self, ast, output):
		ast.unbind(on_compile=self.save_outfile)
		with open(self.ast_file + '.out', 'w') as f:
			f.write(output)
	
	def update_scroll(self, sv, ti):
		srow, scol = ti.get_cursor_from_index(ti.selection_from)
		ti.cursor = srow, scol
		spos = (ti.cursor_pos[0], ti.cursor_pos[1] - sv.height)
		x, y = sv.convert_distance_to_scroll(*spos)
		sv.scroll_y = min(1., max(0., y))
		sv.update_from_scroll()
	
	def update_selection(self, _, selection):
		if selection:
			assert isinstance(selection, AstNode)
			self.selected = selection
			node = selection.tree_node
			textrange = node.get_textrange()
			if textrange:
				st = self.root.ids.source_text
				st.select_text(*textrange)
				self.update_scroll(self.root.ids.sv_source_text, st)
			
			try:
				ot = self.root.ids.output_text
				ot.select_text(node.output_start, node.output_stop)
				self.update_scroll(self.root.ids.sv_output_text, ot)
			except Exception:
				pass
	

if __name__ == '__main__':
	AstApp(sys.argv[1]).run()
