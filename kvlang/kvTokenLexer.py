import antlr3
from kvLexer import kvLexer
from kvTokenSource import kvTokenSource

def kvTokenLexer(stream):
	lexer = kvLexer(stream)
	tokens = antlr3.CommonTokenStream(lexer)
	tokens.discardOffChannelTokens = True
	return kvTokenSource(tokens)

