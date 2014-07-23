import sys
from kvlang.kvTokenLexer import kvTokenLexer
from kvlang.kvParser import kvParser

from antlr3.main import ParserMain

class kvParserMain(ParserMain):
	def __init__(self, lexerClass, parserClass):
		ParserMain.__init__(self, lexerClass.__name__, parserClass)
		self.lexerClass = lexerClass
	
	def setUp(self, options):
		pass

def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
	## fix version numbers
	#kvLexer.antlr_version = kvParser.antlr_version = (3, 1, 3, 0)
	#kvLexer.antlr_version_str = kvParser.antlr_version_str = "3.1.3"
	
	# fix hash function
	pyhash = __builtins__.hash
	hash32 = lambda value: pyhash(value) & 0x7fffffff
	__builtins__.hash = hash32
	
	main = kvParserMain(kvTokenLexer, kvParser)
	
	main.stdin = stdin
	main.stdout = stdout
	main.stderr = stderr
	#ipython --pdb kvParser.py -- --rule=kvfile --port=49100 --lexer=kvTokenLexer tstyle.kv	
	args = argv[0:1] + ['--rule=kvfile', '--port=49100'] + argv[1:]
	main.execute(args)

if __name__ == '__main__':
	main(sys.argv)
