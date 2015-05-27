import os
import antlr3
from kvLexer import kvLexer
from kvTokenSource import kvTokenSource


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


def kvTokenLexer(stream):
	lexer = kvLexer(stream)
	tokens = antlr3.CommonTokenStream(lexer)
	print '\n=================='
	for token in tokens.getTokens():
		printtoken(token)
	print '==================\n'
	tokens.discardOffChannelTokens = True
	return kvTokenSource(tokens)

