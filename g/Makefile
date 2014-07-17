
.PHONY: all grammar clean

all: grammar

grammar:
	./antlr -o ../kvlang/ -make kv.g

clean:
	rm ../kvlang/kvLexer.py ../kvlang/kvParser.py ../kvlang/kv.tokens
