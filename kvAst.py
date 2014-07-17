import sys
import antlr3
from kvlang.kvTokenLexer import kvTokenLexer
from kvlang.kvParser import kvParser

import kivy
kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.treeview import TreeViewLabel
from kivy.properties import StringProperty, ObjectProperty

from time import time
from kvlang.kvTree import Node


def parsefile(filename):
	start_time = time()
	cStream = antlr3.ANTLRFileStream(filename)
	lexer = kvTokenLexer(cStream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = kvParser(tokens)
	
	Node.set_tokens(tokens.getTokens())
	Node.set_text_source(file(filename).read())
	
	result = parser.kvfile()
	finish_time = time()
	print 'kvfile parsed in %0.4fs' % (finish_time - start_time)
	return tokens, result


def buildtreeview(result, tree_view):
	start_time = time()
	tree = result.tree
	parent = None
	populatetreeview(tree_view, parent, tree, True)
	finish_time = time()
	print 'tree built in %0.4fs' % (finish_time - start_time)


class AstNode(TreeViewLabel):
	rule_text = StringProperty()
	rule_type = StringProperty()
	tree_node = ObjectProperty()


def populatetreeview(tree_view, parent, tree, is_open=False):
	tree_node = parent
	if not tree.isNil():
		rule_type = type(tree).__name__[:-4] if isinstance(tree, Node) else type(tree).__name__
		tree_node = tree_view.add_node(AstNode(rule_text=str(tree), rule_type=rule_type,
		                                       tree_node=tree, is_open=is_open), parent)
	
	for child in tree.getChildren():
		populatetreeview(tree_view, tree_node, child, is_open=is_open)


def gettextrange(tree, tokens):
	tstart = tree.tokenStartIndex
	tstop = min(tree.tokenStopIndex, len(tokens) - 1)
	
	while tstart < tstop and not hasattr(tokens[tstart], 'start'):
		tstart += 1
	
	while tstop >= tstart and not hasattr(tokens[tstop], 'stop'):
		tstop -= 1
	
	if tstart > tstop:
		return None
	
	return tokens[tstart].start, tokens[tstop].stop + 1

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
		
		print 'compiled kv output in %0.4fs' % (finish_time - start_time)
		
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
		
		Label:
			text: 'Source'
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
				readonly: True
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

class AstApp(App):
	def __init__(self, filename):
		super(AstApp, self).__init__()
		self.ast_file = filename
		self.source = file(self.ast_file).read()
		self.token_stream, self.result = parsefile(filename)
		self.tokens = self.token_stream.getTokens()
	
	def build(self):
		root = Builder.load_string(root_kv.format(self.ast_file))
		root.ids.source_text.text = self.source
		buildtreeview(self.result, root.ids.treeview)
		output = str(kvOutput(self.result.tree, self.tokens, self.source))
		file(self.ast_file + '.out', 'w').write(output)
		root.ids.output_text.text = output
		
		root.ids.treeview.bind(selected_node=self.update_selection)
		return root
	
	def update_scroll(self, sv, ti):
		srow, scol = ti.get_cursor_from_index(ti.selection_from)
		ti.cursor = srow, scol
		spos = (ti.cursor_pos[0], ti.cursor_pos[1] - sv.height)
		x, y = sv.convert_distance_to_scroll(*spos)
		sv.scroll_y = min(1., max(0., y))
		sv.update_from_scroll()
	
	def update_selection(self, _, selection):
		assert isinstance(selection, AstNode)
		node = selection.tree_node
		textrange = gettextrange(node, self.tokens)
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
