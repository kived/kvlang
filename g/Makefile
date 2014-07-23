
.PHONY: all grammar clean

all: grammar

debug: debuggrammar

grammar:
	./antlr -o ../kvlang/ -make kv.g

debuggrammar:
	./antlr -o ../kvlang/ -debug -make kv.g

clean:
	rm ../kvlang/kvLexer.py ../kvlang/kvParser.py ../kvlang/kv.tokens ||:
