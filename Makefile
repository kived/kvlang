
.PHONY: all compilegrammar clean test demo kivydemo

all: compilegrammar

compilegrammar:
	cd g; $(MAKE)

clean:
	find . -name '*.pyc' -delete
	cd g; $(MAKE) clean

test:
	/usr/bin/env python2.7 kvTest.py debug

demo:
	PYTHONPATH=../kivy /usr/bin/env python2.7 kvAst.py test.kv

kivydemo:
	PYTHONPATH=../kivy /usr/bin/env python2.7 kvAst.py tstyle.kv
