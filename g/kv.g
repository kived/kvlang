/** kv Grammar for Kivy 1.8.1
 * 
 * The MIT License (MIT)
 * 
 * Copyright (c) 2014 Ryan Pessa
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 * 
 * 
 * 
 * Python Grammar
 * --------------
 * Portions of this grammar are based on the Python 2.5 Grammar
 * by Terence Parr and Loring Craymer, with updates by Aaron
 * Maxwell.
 * 
 * https://github.com/antlr/examples-v3/blob/master/Python/python/Python.g
 * 
 * [The 'BSD licence']
 * Copyright (c) 2004 Terence Parr and Loring Craymer
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

grammar kv;

options {
    language = Python;
    output = AST;
}


tokens {
    INDENT;
    DEDENT;
    
    BLANKLINE;
    COMMENT;
    DIRECTIVE;
    WIDGET;
    PROPERTY;
    CANVASRULE;
    CLASSRULE;
    TEMPLATERULE;
    MULTITEMPLATERULE;
    MULTICLASSRULE;
    CLASSLIST;
    PYTHON;
    INSTRUCTION;
    RESETRULE;
    AUTOCLASS;
}

@lexer::init {
	self.startPos = -1
	self.nested = 0
	def nextToken():
		self.startPos = self.getCharPositionInLine()
		return Lexer.nextToken(self)
	self.nextToken = nextToken
}

@parser::header {
	from kvTree import *
}

@parser::init {	
	self.root_node = None
	def found_root(node):
		if self.root_node:
			raise DuplicateRootError(self.input)
		self.root_node = node
	self.found_root = found_root
}

kvfile
    : (blank | line)*;

blank : NEWLINE -> ^(BLANKLINE<BlankNode>) ;

line
	: directive
	| root_rule
	| class_rule
	| template_rule
	| comment ;

directive
	: DIRECTIVETEXT NEWLINE -> ^(DIRECTIVE<DirectiveNode>[$DIRECTIVETEXT]) ;

comment
    : COMMENTTEXT NEWLINE -> ^(COMMENT<CommentNode>[$COMMENTTEXT]) ;

root_rule
	:	w=widget {self.found_root($w.tree)};

widget 
	:	WNAME COLON? NEWLINE -> ^(WIDGET<WidgetNode>[$WNAME])
	|	WNAME COLON? widget_body -> ^(WIDGET<WidgetNode>[$WNAME] widget_body) ;

class_rule
	:	'<' a=class_widget '>' COLON? NEWLINE -> ^(CLASSRULE<ClassRuleNode>[$a.tree])
	|	'<' a=class_widget '>' COLON? widget_body -> ^(CLASSRULE<ClassRuleNode>[$a.tree] widget_body) ;

class_widget
	:	widget_comp ;

widget_comp
	:   widget_list -> widget_list
	|   a=widget_list AT b=widget_base -> ^(AUTOCLASS<AutoClassNode>[$a.tree,$b.tree]) ;

widget_list
	:   widget_name -> widget_name
	|   widget_name (m=COMMA widget_name)+ -> ^(CLASSLIST<ClassListNode>[$m] widget_name*) ;

widget_base
	:   widget_name -> widget_name
	|   widget_name (m=PLUS widget_name)+ -> ^(CLASSLIST<ClassListNode>[$m] widget_name*) ;

widget_name
	:   WNAME -> WNAME
	|   MINUS WNAME -> ^(RESETRULE<ResetRuleNode>[$WNAME]) ;

class_list
	:	WNAME (PLUS WNAME)* ;

template_rule
	:	'[' a=class_widget ']' COLON? NEWLINE -> ^(TEMPLATERULE<TemplateRuleNode>[$a.tree])
	|	'[' a=class_widget ']' COLON? widget_body -> ^(TEMPLATERULE<TemplateRuleNode>[$a.tree] widget_body) ;

widget_body
    : NEWLINE! INDENT! (stmt)+ DEDENT! ;

canvas_body
	: NEWLINE! INDENT! (canvas_stmt)+ DEDENT! ;

stmt
	: widget
	| canvas
	| prop
	| comment
	| blank ;

canvas_stmt 
	: instruction
	| comment
	| blank ;

instruction 
	: WNAME COLON? NEWLINE -> ^(INSTRUCTION<InstructionNode>[$WNAME])
	| WNAME COLON? instruction_body -> ^(INSTRUCTION<InstructionNode>[$WNAME] instruction_body) ;

instruction_body 
	: NEWLINE! INDENT! (instruction_stmt)+ DEDENT! ;

instruction_stmt 
	: prop
	| comment
	| blank ;

canvas 
	:	CANVAS COLON canvas_body -> ^(CANVASRULE<CanvasNode>[$CANVAS] canvas_body);

prop
	: NAME COLON WS* p=property_body -> ^(PROPERTY<PropertyNode>[$NAME,$p.tree])
	| NAME COLON WS* p=prop_value NEWLINE -> ^(PROPERTY<PropertyNode>[$NAME,$p.tree]) ;

property_body
	: NEWLINE! INDENT! prop_value (NEWLINE! prop_value)* DEDENT! ;

prop_value
	:	p=python -> ^(PYTHON<PythonNode>[$p.tree]);

/*
 * Python parser rules
 */
python
	:   simple_stmt
	|   compound_stmt ;

simple_stmt
	:	small_stmt (options {greedy=true;}:SEMI small_stmt)* (SEMI)? ;

small_stmt 
	:	expr_stmt
	|   print_stmt
	|   del_stmt
	|   pass_stmt
	|   flow_stmt
	|   exec_stmt
	|   assert_stmt ;

varargslist
	:	defparameter (options {greedy=true;}:COMMA defparameter)* (COMMA ( STAR identifier (COMMA DOUBLESTAR identifier)? | DOUBLESTAR identifier )? )?
	|	STAR identifier (COMMA DOUBLESTAR identifier)?
	|	DOUBLESTAR identifier ;

defparameter
	:	fpdef (ASSIGN test)? ;

fpdef
	:	identifier
	|	LPAREN fplist RPAREN ;

fplist
	:	fpdef (options {greedy=true;}:COMMA fpdef)* (COMMA)? ;

expr_stmt 
	:	testlist (augassign yield_expr | augassign testlist | assigns)? ;

assigns 
	:	assign_testlist+ | assign_yield+ ;

assign_testlist 
	:	ASSIGN testlist ;

assign_yield 
	:	ASSIGN yield_expr ;

augassign 
	:	PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL
	|	VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL 
	|	DOUBLESTAREQUAL | DOUBLESLASHEQUAL ;

print_stmt
	:   'print' (printlist | RIGHTSHIFT printlist)? ;

printlist returns [newline]
	:   test (options {k=2;}: COMMA test)* (COMMA)? ;

del_stmt
	:   'del' exprlist ;

pass_stmt
	:   'pass' ;

flow_stmt
	:   break_stmt
	|   continue_stmt
	//|   return_stmt
	|   raise_stmt
	|   yield_stmt ;

break_stmt
	:   'break' ;

continue_stmt
	:   'continue' ;

yield_stmt
	:	yield_expr ;

raise_stmt
	:	'raise' (test (COMMA test (COMMA test)?)?)? ;

exec_stmt
	:   'exec' expr ('in' test (COMMA test)?)? ;

assert_stmt
	:   'assert' test (COMMA test)? ;

compound_stmt
	:   if_stmt
	|   while_stmt
	|   for_stmt
	|   try_stmt
	|   with_stmt
	//|   funcdef
	//|   classdef
	;

if_stmt
	:   'if' test COLON suite elif_clause* ('else' COLON suite)? ;

elif_clause
	:   'elif' test COLON suite ;

while_stmt
	:   'while' test COLON suite ('else' COLON suite)? ;

for_stmt
	:   'for' exprlist 'in' testlist COLON suite ('else' COLON suite)? ;

try_stmt
	:   'try' COLON suite
			( except_clause+ ('else' COLON suite)? ('finally' COLON suite)?
			| 'finally' COLON suite ) ;

with_stmt
	:   'with' test (with_var)? COLON suite ;

with_var
	:   ('as' | identifier) expr ;

except_clause
	:   'except' (test (COMMA test)?)? COLON suite ;

suite
	:   simple_stmt
	|   NEWLINE INDENT (stmt)+ DEDENT
	;

test
	:	or_test
		( ( 'if' or_test 'else' ) => 'if' or_test 'else' test )?
	| lambdef ;

or_test
	:	and_test (OR and_test)* ;

and_test
	:	not_test (AND not_test)* ;

not_test
	:	NOT not_test
	|	comparison ;

comparison
	:	expr (comp_op expr)* ;

comp_op
	:	LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL
	|	'in' | NOT 'in' | 'is' | NOT 'is' ;

expr
	:	xor_expr (VBAR xor_expr)* ;

xor_expr
	:	and_expr (CIRCUMFLEX and_expr)* ;

and_expr
	:	shift_expr (AMPER shift_expr)* ;

shift_expr
	:	arith_expr ((LEFTSHIFT|RIGHTSHIFT) arith_expr)* ;

arith_expr
	:	term ((PLUS|MINUS) term)* ;

term
	:	factor ((STAR | SLASH | PERCENT | DOUBLESLASH ) factor)* ;

factor
	:	PLUS factor | MINUS factor | TILDE factor | power ;

power
	:	atom (trailer)* (options {greedy=true;}:DOUBLESTAR factor)? ;

atom
	:	LPAREN ( yield_expr | testlist_gexp )? RPAREN
	|	LBRACK (listmaker)? RBRACK
	|	LCURLY (dictmaker)? RCURLY
	|	BACKQUOTE testlist BACKQUOTE
	|	identifier
	|   NONE
	|	INT
	|	LONGINT
	|	FLOAT
	|	COMPLEX
	|	(STRING)+ ;

listmaker
	:	test (list_for | (options {greedy=true;}:COMMA test)* ) (COMMA)? ;

testlist_gexp
	:	test ( (options {k=2;}: COMMA test)* (COMMA)? | gen_for ) ;

lambdef
	:	'lambda' (varargslist)? COLON test ;

trailer
	:	LPAREN (arglist)? RPAREN
	|	LBRACK subscriptlist RBRACK
	|	DOT identifier ;

subscriptlist
	:	subscript (options {greedy=true;}:COMMA subscript)* (COMMA)? ;

subscript
	:	DOT DOT DOT
	|	test (COLON (test)? (sliceop)?)?
	|	COLON (test)? (sliceop)? ;

sliceop
	:	COLON (test)? ;

exprlist
	:	expr (options {k=2;}: COMMA expr)* (COMMA)? ;

testlist
	:	test (options {k=2;}: COMMA test)* (COMMA)? ;

dictmaker
	:	test COLON test (options {k=2;}: COMMA test COLON test)* (COMMA)? ;

arglist
	:	argument (COMMA argument)* ( COMMA ( STAR test (COMMA DOUBLESTAR test)? | DOUBLESTAR test )? )?
	|	STAR test (COMMA DOUBLESTAR test)?
	|	DOUBLESTAR test ;

argument
	:	test ( ( ASSIGN test ) | gen_for )? ;

list_iter
	:	list_for | list_if ;

list_for
	:	'for' exprlist 'in' testlist (list_iter)? ;

list_if
	:	'if' test (list_iter)? ;

gen_iter
	:	gen_for | gen_if ;

gen_for
	:	'for' exprlist 'in' or_test gen_iter? ;

gen_if
	:	'if' test gen_iter? ;

yield_expr
	:	'yield' testlist? ;

LPAREN :		'(' {self.nested += 1} ;
RPAREN :		')' {self.nested -= 1} ;
LBRACK :		'[' {self.nested += 1} ;
RBRACK :		']' {self.nested -= 1} ;
COLON :			':' ;
COMMA :			',' ;
SEMI :			';' ;
PLUS :			'+' ;
MINUS :			'-' ;
STAR :			'*' ;
SLASH :			'/' ;
VBAR :			'|' ;
AMPER :			'&' ;
LESS :			'<' ;
GREATER :		'>' ;
ASSIGN :		'=' ;
PERCENT :		'%' ;
BACKQUOTE :		'`' ;
LCURLY :		'{' {self.nested += 1} ;
RCURLY :		'}' {self.nested -= 1} ;
CIRCUMFLEX :	'^' ;
TILDE :			'~' ;
EQUAL :			'==' ;
NOTEQUAL :		'!=' ;
ALT_NOTEQUAL :	'<>' ;
LESSEQUAL :		'<=' ;
LEFTSHIFT :		'<<' ;
GREATEREQUAL :	'>=' ;
RIGHTSHIFT :	'>>' ;
PLUSEQUAL :		'+=' ;
MINUSEQUAL :	'-=' ;
DOUBLESTAR :	'**' ;
STAREQUAL :		'*=' ;
DOUBLESLASH :	'//' ;
SLASHEQUAL :	'/=' ;
VBAREQUAL :		'|=' ;
PERCENTEQUAL :	'%=' ;
AMPEREQUAL :	'&=' ;
CIRCUMFLEXEQUAL : '^=' ;
LEFTSHIFTEQUAL : '<<=' ;
RIGHTSHIFTEQUAL : '>>=' ;
DOUBLESTAREQUAL : '**=' ;
DOUBLESLASHEQUAL : '//=' ;
DOT :			'.' ;
AT :			'@' ;
AND :			'and' ;
OR :			'or' ;
NOT :			'not' ;

FLOAT 
	:	'.' DIGITS (Exponent)?
	|	DIGITS '.' Exponent
	|	DIGITS ('.' (DIGITS (Exponent)?)? | Exponent);

LONGINT
	:	INT ('l' | 'L') ;

fragment
Exponent
	:	('e' | 'E') ('+' | '-')? DIGITS ;

INT :	'0' ('x' | 'X') ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
	|	'0' DIGITS*
	|	'1' .. '9' DIGITS* ;

COMPLEX
	:	INT ('j'|'J')
	|	FLOAT ('j'|'J') ;

fragment
DIGITS
	:	( '0' .. '9' )+ ;

STRING
	:	('r' | 'u' | 'ur')?
		(	'"' (ESC|~('\\'|'\n'|'"'))* '"'
		|	'\'' (ESC|~('\\'|'\n'|'\''))* '\''
		) ;

fragment
ESC	:	'\\' . ;

NEWLINE :       (('\u000C')?('\r')? '\n' ) {if self.nested > 0: $channel=HIDDEN} ;
WS 	:			(' '|'\t')+ {$channel=HIDDEN} ;

/*
 * End Python rules
 */

identifier
	:	WNAME | NAME ;

NONE
	:   'None' ;

WNAME
	:	( 'A' .. 'Z' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* ;

CANVAS 
	:	'canvas' | 'canvas.before' | 'canvas.after' ;

NAME 
	:	( 'a' .. 'z' | '_' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* ;

DIRECTIVETEXT
	:	HASH COLON (~'\n')* ;

COMMENTTEXT
	:	HASH (~'\n')* ;

fragment
HASH :          '#' ;

