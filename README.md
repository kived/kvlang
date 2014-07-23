kvlang
======

ANTLRv3-based grammar for parsing kv and generating abstract syntax trees.

Requires ANTLR Python runtime v3.1.3. i.e.:
    `pip install http://www.antlr.org/download/antlr-3.1.3.tar.gz`


###Building

Run `make` from the top-level folder.


###Testing

* `make test`: show lexer and parser output for test.kv
* `make demo`: start Kivy AST demo for test.kv
* `make kivydemo`: start Kivy AST demo for tstyle.kv
* `make loader`: start a demo app using AST loader instead of Builder loader

test.kv is a simple kv file to test the grammar.

tstyle.kv is Kivy's style.kv with spacing fixed (the grammar is more strict than Kivy's kv parser and handles indents in a way more similar to CPython).

