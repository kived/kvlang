
.PHONY: all compilegrammar clean demo

all: compilegrammar

compilegrammar:
	cd g; $(MAKE)

clean:
	find . -name '*.pyc' -delete
	cd g; $(MAKE) clean

demo:
	PYTHONPATH=../kivy /usr/bin/env python2.7 kvAst.py tstyle.kv
