import sys
import os.path
import antlr3
import kvlang
from kvlang.kvLexer import kvLexer
from kvlang.kvTree import Node, WidgetLikeNode
from kvlang.kvParser import kvParser
from kvlang.kvTokenSource import kvTokenSource

debug = 'debug' in sys.argv
if debug:
	sys.argv.remove('debug')


def loadtokens():
	tokens = {}
	for line in open(os.path.join(os.path.dirname(kvlang.__file__), 'kv.tokens')):
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


def parsefile(filename):
	cStream = antlr3.ANTLRFileStream(filename)
	lexer = kvLexer(cStream)
	
	if debug:
		print 'Lexer'
		print '-----'
		for token in lexer:
			printtoken(token)
		
		print
		
		lexer.reset()
	
	tokens = antlr3.CommonTokenStream(lexer)
	
	if debug:
		print 'Initial Token Stream'
		print '--------------------'
		token_list = tokens.getTokens()
		for token in token_list:
			printtoken(token)
		
		print
	
	tokens.discardOffChannelTokens = True
	indentedSource = kvTokenSource(tokens)
	tokens = antlr3.CommonTokenStream(indentedSource)
	
	if debug:
		print 'Token Stream'
		print '------------'
		for token in tokens.getTokens():
			printtoken(token)
		
		print
	
	Node.set_tokens(tokens.getTokens())
	Node.set_text_source(file(filename).read())
	
	parser = kvParser(tokens)
	result = parser.kvfile()
	return result


def printresult(result):
	print 'Parser Result'
	print '-------------'
	
	from pprint import pprint
	
	if hasattr(result, 'tree'):
		if result.tree is not None:
			pprint(buildtree(result.tree))
		else:
			pprint(repr(result))
	
	print '--'
	print result.tree.toStringTree()
	
	print '--'
	pprint(buildwidgettree(result.tree))


def buildtree(tree):
	if tree.isNil():
		return _buildtree(tree.getChildren())
	else:
		return _buildtree([tree])

def _buildtree(nodes):
	d = []
	for child in nodes:
		text = str(child)
		if child.getChildCount():
			d.append((text, _buildtree(child.getChildren())))
		else:
			d.append(text)
	return d

def buildwidgettree(tree):
	if tree.isNil():
		return _buildwidgettree(tree.getChildren())
	else:
		return _buildwidgettree([tree])

def _buildwidgettree(nodes):
	d = []
	for child in nodes:
		text = str(child)
		if isinstance(child, WidgetLikeNode):
			d.append((text, {'properties': _buildproperties(child),
			                 'canvas': _buildcanvas(child),
			                 'widgets': _buildwidgets(child)}))
		elif child.getChildCount():
			d.append((text, _buildwidgettree(child.getChildren())))
		else:
			d.append(text)
	return d

def _buildproperties(node):
	d = {}
	for prop in node.properties():
		d[prop.name] = prop.value
	return d

def _buildcanvas(node):
	d = []
	for canvas in node.canvasblocks():
		d.append((str(canvas), _buildwidgettree(canvas.getChildren())))
	return d

def _buildwidgets(node):
	d = []
	for widget in node.widgets():
		d.append(_buildwidgettree([widget]))
	return d


if __name__ == '__main__':
	printresult(parsefile(sys.argv[1] if len(sys.argv) > 1 else 'test.kv'))
