from antlr3 import CommonToken
from antlr3.tree import CommonTree


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


class Node(CommonTree):
	_tokens = None
	
	def __init__(self, token):
		payload = CommonToken(token, '')
		self.toString = self.__str__
		super(Node, self).__init__(payload)
	
	@classmethod
	def get_tokens(cls):
		return Node._tokens
	
	@classmethod
	def set_tokens(cls, tokens):
		Node._tokens = tokens
	
	@classmethod
	def get_text(cls, start, stop):
		return Node._text[start:stop]
	
	@classmethod
	def set_text_source(cls, source):
		Node._text = source

class TextNode(Node):
	def __init__(self, token, text):
		super(TextNode, self).__init__(token)
		self.textnode = text
		self.startIndex = self.tokenStartIndex = text.start
		self.stopIndex = self.tokenStopIndex = text.stop
	
	def __str__(self):
		return str(self.textnode.text)

class DirectiveNode(TextNode):
	pass

class CommentNode(TextNode):
	pass

class WidgetLikeNode(Node):
	# def __init__(self, token):
	# 	super(WidgetLikeNode, self).__init__(token)
	# 	
	
	def properties(self):
		for child in self.getChildren():
			if isinstance(child, PropertyNode):
				yield child
	
	def widgets(self):
		for child in self.getChildren():
			if isinstance(child, WidgetNode):
				yield child
	
	def canvasblocks(self):
		for child in self.getChildren():
			if isinstance(child, CanvasNode):
				yield child

class WidgetNode(TextNode, WidgetLikeNode):
	pass
	# def __init__(self, token, name):
	# 	super(WidgetNode, self).__init__(token, name)
	# 	self.namenode = name
	# 
	# def __str__(self):
	# 	return str(self.namenode.text)

class ClassRuleNode(WidgetLikeNode):
	def __init__(self, token, classes):
		super(ClassRuleNode, self).__init__(token)
		self.classes = classes

	def __str__(self):
		# if self.classes.text == 'CLASSLIST':
		# 	s = ','.join(str(c) for c in self.classes.getChildren())
		# else:
		s = str(self.classes)
		return '<' + s + '>'

class TemplateRuleNode(ClassRuleNode):
	def __str__(self):
		# if self.classes.text == 'CLASSLIST':
		# 	s = ','.join(str(c) for c in self.classes.getChildren())
		# else:
		s = str(self.classes)
		return '[' + s + ']'

class PropertyNode(Node):
	def __init__(self, token, name, value):
		super(PropertyNode, self).__init__(token)
		self.namenode = name
		self.valuenode = value
	
	@property
	def name(self):
		return str(self.namenode.text)
	
	@property
	def value(self):
		return str(self.valuenode)
	
	def __str__(self):
		return '%s: %s' % (self.name, self.value)

class PythonNode(Node):
	def __init__(self, token, codetree):
		super(PythonNode, self).__init__(token)
		self.codetree = codetree
	
	def __str__(self):
		textrange = gettextrange(self, self.get_tokens())
		if textrange:
			return self.get_text(*textrange)
		return ''

class CanvasNode(TextNode):
	pass

class InstructionNode(TextNode):
	pass

class ClassListNode(Node):
	def __init__(self, token, separator):
		super(ClassListNode, self).__init__(token)
		self.separator = str(separator.text)
	
	def __str__(self):
		return self.separator.join(str(c) for c in self.getChildren())

class AutoClassNode(Node):
	def __init__(self, token, widgetlist, classlist):
		super(AutoClassNode, self).__init__(token)
		self.widgetlist = widgetlist
		self.classlist = classlist
	
	def __str__(self):
		return str(self.widgetlist) + '@' + str(self.classlist)

class BlankNode(Node):
	def __str__(self):
		return ''

class ResetRuleNode(TextNode):
	def __str__(self):
		return '-' + super(ResetRuleNode, self).__str__()
