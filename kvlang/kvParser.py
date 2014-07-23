# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 kv.g 2014-07-23 13:58:59

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

                 
from kvTree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INSTRUCTION=18
BACKQUOTE=74
SLASHEQUAL=42
STAR=34
CIRCUMFLEXEQUAL=46
GREATEREQUAL=58
COMPLEX=79
WIDGET=9
NOT=54
EOF=-1
CANVAS=30
NOTEQUAL=61
T__93=93
T__94=94
MINUSEQUAL=40
VBAR=62
T__91=91
RPAREN=38
T__92=92
NAME=31
GREATER=56
T__90=90
DOUBLESTAREQUAL=49
LESS=55
TEMPLATERULE=13
COMMENT=7
T__99=99
T__98=98
T__97=97
T__96=96
T__95=95
RBRACK=71
LCURLY=72
INT=76
RIGHTSHIFT=51
T__87=87
T__86=86
T__89=89
T__88=88
DOUBLESLASHEQUAL=50
WS=32
PROPERTY=10
NONE=75
VBAREQUAL=45
OR=52
RESETRULE=19
CLASSRULE=12
LONGINT=77
MULTICLASSRULE=15
PERCENTEQUAL=43
LESSEQUAL=59
DOUBLESLASH=68
LBRACK=70
DOUBLESTAR=35
ESC=84
DIGITS=82
Exponent=83
FLOAT=78
DEDENT=5
WNAME=24
RIGHTSHIFTEQUAL=48
AND=53
DIRECTIVE=8
BLANKLINE=6
INDENT=4
LPAREN=37
PLUSEQUAL=39
COMMENTTEXT=23
AT=26
MULTITEMPLATERULE=14
SLASH=66
DIRECTIVETEXT=22
T__107=107
COMMA=27
AMPER=64
PYTHON=17
T__103=103
T__104=104
EQUAL=57
T__105=105
T__106=106
TILDE=69
LEFTSHIFTEQUAL=47
PLUS=28
LEFTSHIFT=65
DOT=81
PERCENT=67
CLASSLIST=16
HASH=85
T__102=102
T__101=101
T__100=100
MINUS=29
SEMI=33
COLON=25
CANVASRULE=11
NEWLINE=21
AMPEREQUAL=44
RCURLY=73
ASSIGN=36
STAREQUAL=41
CIRCUMFLEX=63
STRING=80
AUTOCLASS=20
ALT_NOTEQUAL=60

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INDENT", "DEDENT", "BLANKLINE", "COMMENT", "DIRECTIVE", "WIDGET", "PROPERTY", 
    "CANVASRULE", "CLASSRULE", "TEMPLATERULE", "MULTITEMPLATERULE", "MULTICLASSRULE", 
    "CLASSLIST", "PYTHON", "INSTRUCTION", "RESETRULE", "AUTOCLASS", "NEWLINE", 
    "DIRECTIVETEXT", "COMMENTTEXT", "WNAME", "COLON", "AT", "COMMA", "PLUS", 
    "MINUS", "CANVAS", "NAME", "WS", "SEMI", "STAR", "DOUBLESTAR", "ASSIGN", 
    "LPAREN", "RPAREN", "PLUSEQUAL", "MINUSEQUAL", "STAREQUAL", "SLASHEQUAL", 
    "PERCENTEQUAL", "AMPEREQUAL", "VBAREQUAL", "CIRCUMFLEXEQUAL", "LEFTSHIFTEQUAL", 
    "RIGHTSHIFTEQUAL", "DOUBLESTAREQUAL", "DOUBLESLASHEQUAL", "RIGHTSHIFT", 
    "OR", "AND", "NOT", "LESS", "GREATER", "EQUAL", "GREATEREQUAL", "LESSEQUAL", 
    "ALT_NOTEQUAL", "NOTEQUAL", "VBAR", "CIRCUMFLEX", "AMPER", "LEFTSHIFT", 
    "SLASH", "PERCENT", "DOUBLESLASH", "TILDE", "LBRACK", "RBRACK", "LCURLY", 
    "RCURLY", "BACKQUOTE", "NONE", "INT", "LONGINT", "FLOAT", "COMPLEX", 
    "STRING", "DOT", "DIGITS", "Exponent", "ESC", "HASH", "'print'", "'del'", 
    "'pass'", "'break'", "'continue'", "'raise'", "'exec'", "'in'", "'assert'", 
    "'if'", "'else'", "'elif'", "'while'", "'for'", "'try'", "'finally'", 
    "'with'", "'as'", "'except'", "'is'", "'lambda'", "'yield'"
]




class kvParser(Parser):
    grammarFileName = "kv.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(kvParser, self).__init__(input, state, *args, **kwargs)

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
            )

        self.dfa51 = self.DFA51(
            self, 51,
            eot = self.DFA51_eot,
            eof = self.DFA51_eof,
            min = self.DFA51_min,
            max = self.DFA51_max,
            accept = self.DFA51_accept,
            special = self.DFA51_special,
            transition = self.DFA51_transition
            )

        self.dfa75 = self.DFA75(
            self, 75,
            eot = self.DFA75_eot,
            eof = self.DFA75_eof,
            min = self.DFA75_min,
            max = self.DFA75_max,
            accept = self.DFA75_accept,
            special = self.DFA75_special,
            transition = self.DFA75_transition
            )

        self.dfa81 = self.DFA81(
            self, 81,
            eot = self.DFA81_eot,
            eof = self.DFA81_eof,
            min = self.DFA81_min,
            max = self.DFA81_max,
            accept = self.DFA81_accept,
            special = self.DFA81_special,
            transition = self.DFA81_transition
            )

        self.dfa99 = self.DFA99(
            self, 99,
            eot = self.DFA99_eot,
            eof = self.DFA99_eof,
            min = self.DFA99_min,
            max = self.DFA99_max,
            accept = self.DFA99_accept,
            special = self.DFA99_special,
            transition = self.DFA99_transition
            )

        self.dfa114 = self.DFA114(
            self, 114,
            eot = self.DFA114_eot,
            eof = self.DFA114_eof,
            min = self.DFA114_min,
            max = self.DFA114_max,
            accept = self.DFA114_accept,
            special = self.DFA114_special,
            transition = self.DFA114_transition
            )

        self.dfa116 = self.DFA116(
            self, 116,
            eot = self.DFA116_eot,
            eof = self.DFA116_eof,
            min = self.DFA116_min,
            max = self.DFA116_max,
            accept = self.DFA116_accept,
            special = self.DFA116_special,
            transition = self.DFA116_transition
            )

        self.dfa118 = self.DFA118(
            self, 118,
            eot = self.DFA118_eot,
            eof = self.DFA118_eof,
            min = self.DFA118_min,
            max = self.DFA118_max,
            accept = self.DFA118_accept,
            special = self.DFA118_special,
            transition = self.DFA118_transition
            )



                       	
        self.root_node = None
        def found_root(node):
        	if self.root_node:
        		raise DuplicateRootError(self.input)
        	self.root_node = node
        self.found_root = found_root




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class kvfile_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.kvfile_return, self).__init__()

            self.tree = None




    # $ANTLR start "kvfile"
    # kv.g:113:1: kvfile : ( blank | line )* ;
    def kvfile(self, ):

        retval = self.kvfile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        blank1 = None

        line2 = None



        try:
            try:
                # kv.g:114:5: ( ( blank | line )* )
                # kv.g:114:7: ( blank | line )*
                pass 
                root_0 = self._adaptor.nil()

                # kv.g:114:7: ( blank | line )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1
                    elif ((DIRECTIVETEXT <= LA1_0 <= WNAME) or LA1_0 == LESS or LA1_0 == LBRACK) :
                        alt1 = 2


                    if alt1 == 1:
                        # kv.g:114:8: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_kvfile202)
                        blank1 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank1.tree)


                    elif alt1 == 2:
                        # kv.g:114:16: line
                        pass 
                        self._state.following.append(self.FOLLOW_line_in_kvfile206)
                        line2 = self.line()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, line2.tree)


                    else:
                        break #loop1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "kvfile"

    class blank_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.blank_return, self).__init__()

            self.tree = None




    # $ANTLR start "blank"
    # kv.g:116:1: blank : NEWLINE -> ^( BLANKLINE ) ;
    def blank(self, ):

        retval = self.blank_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE3 = None

        NEWLINE3_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")

        try:
            try:
                # kv.g:116:7: ( NEWLINE -> ^( BLANKLINE ) )
                # kv.g:116:9: NEWLINE
                pass 
                NEWLINE3=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_blank216) 
                if self._state.backtracking == 0:
                    stream_NEWLINE.add(NEWLINE3)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 116:17: -> ^( BLANKLINE )
                    # kv.g:116:20: ^( BLANKLINE )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(BlankNode(BLANKLINE), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "blank"

    class line_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.line_return, self).__init__()

            self.tree = None




    # $ANTLR start "line"
    # kv.g:118:1: line : ( directive | root_rule | class_rule | template_rule | comment );
    def line(self, ):

        retval = self.line_return()
        retval.start = self.input.LT(1)

        root_0 = None

        directive4 = None

        root_rule5 = None

        class_rule6 = None

        template_rule7 = None

        comment8 = None



        try:
            try:
                # kv.g:119:2: ( directive | root_rule | class_rule | template_rule | comment )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 == DIRECTIVETEXT:
                    alt2 = 1
                elif LA2 == WNAME:
                    alt2 = 2
                elif LA2 == LESS:
                    alt2 = 3
                elif LA2 == LBRACK:
                    alt2 = 4
                elif LA2 == COMMENTTEXT:
                    alt2 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # kv.g:119:4: directive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directive_in_line235)
                    directive4 = self.directive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, directive4.tree)


                elif alt2 == 2:
                    # kv.g:120:4: root_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_root_rule_in_line240)
                    root_rule5 = self.root_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, root_rule5.tree)


                elif alt2 == 3:
                    # kv.g:121:4: class_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_class_rule_in_line245)
                    class_rule6 = self.class_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, class_rule6.tree)


                elif alt2 == 4:
                    # kv.g:122:4: template_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_template_rule_in_line250)
                    template_rule7 = self.template_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, template_rule7.tree)


                elif alt2 == 5:
                    # kv.g:123:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_line255)
                    comment8 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment8.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "line"

    class directive_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.directive_return, self).__init__()

            self.tree = None




    # $ANTLR start "directive"
    # kv.g:125:1: directive : DIRECTIVETEXT NEWLINE -> ^( DIRECTIVE[$DIRECTIVETEXT] ) ;
    def directive(self, ):

        retval = self.directive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DIRECTIVETEXT9 = None
        NEWLINE10 = None

        DIRECTIVETEXT9_tree = None
        NEWLINE10_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_DIRECTIVETEXT = RewriteRuleTokenStream(self._adaptor, "token DIRECTIVETEXT")

        try:
            try:
                # kv.g:126:2: ( DIRECTIVETEXT NEWLINE -> ^( DIRECTIVE[$DIRECTIVETEXT] ) )
                # kv.g:126:4: DIRECTIVETEXT NEWLINE
                pass 
                DIRECTIVETEXT9=self.match(self.input, DIRECTIVETEXT, self.FOLLOW_DIRECTIVETEXT_in_directive265) 
                if self._state.backtracking == 0:
                    stream_DIRECTIVETEXT.add(DIRECTIVETEXT9)
                NEWLINE10=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive267) 
                if self._state.backtracking == 0:
                    stream_NEWLINE.add(NEWLINE10)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 126:26: -> ^( DIRECTIVE[$DIRECTIVETEXT] )
                    # kv.g:126:29: ^( DIRECTIVE[$DIRECTIVETEXT] )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(DirectiveNode(DIRECTIVE, DIRECTIVETEXT9), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "directive"

    class comment_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.comment_return, self).__init__()

            self.tree = None




    # $ANTLR start "comment"
    # kv.g:128:1: comment : COMMENTTEXT NEWLINE -> ^( COMMENT[$COMMENTTEXT] ) ;
    def comment(self, ):

        retval = self.comment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMENTTEXT11 = None
        NEWLINE12 = None

        COMMENTTEXT11_tree = None
        NEWLINE12_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_COMMENTTEXT = RewriteRuleTokenStream(self._adaptor, "token COMMENTTEXT")

        try:
            try:
                # kv.g:129:5: ( COMMENTTEXT NEWLINE -> ^( COMMENT[$COMMENTTEXT] ) )
                # kv.g:129:7: COMMENTTEXT NEWLINE
                pass 
                COMMENTTEXT11=self.match(self.input, COMMENTTEXT, self.FOLLOW_COMMENTTEXT_in_comment290) 
                if self._state.backtracking == 0:
                    stream_COMMENTTEXT.add(COMMENTTEXT11)
                NEWLINE12=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_comment292) 
                if self._state.backtracking == 0:
                    stream_NEWLINE.add(NEWLINE12)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 129:27: -> ^( COMMENT[$COMMENTTEXT] )
                    # kv.g:129:30: ^( COMMENT[$COMMENTTEXT] )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(CommentNode(COMMENT, COMMENTTEXT11), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "comment"

    class root_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.root_rule_return, self).__init__()

            self.tree = None




    # $ANTLR start "root_rule"
    # kv.g:131:1: root_rule : w= widget ;
    def root_rule(self, ):

        retval = self.root_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        w = None



        try:
            try:
                # kv.g:132:2: (w= widget )
                # kv.g:132:4: w= widget
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_widget_in_root_rule314)
                w = self.widget()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, w.tree)
                if self._state.backtracking == 0:
                    self.found_root(w.tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "root_rule"

    class widget_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget"
    # kv.g:134:1: widget : ( WNAME ( COLON )? NEWLINE -> ^( WIDGET[$WNAME] ) | WNAME ( COLON )? widget_body -> ^( WIDGET[$WNAME] widget_body ) );
    def widget(self, ):

        retval = self.widget_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME13 = None
        COLON14 = None
        NEWLINE15 = None
        WNAME16 = None
        COLON17 = None
        widget_body18 = None


        WNAME13_tree = None
        COLON14_tree = None
        NEWLINE15_tree = None
        WNAME16_tree = None
        COLON17_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:135:2: ( WNAME ( COLON )? NEWLINE -> ^( WIDGET[$WNAME] ) | WNAME ( COLON )? widget_body -> ^( WIDGET[$WNAME] widget_body ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == WNAME) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == COLON) :
                        LA5_2 = self.input.LA(3)

                        if (LA5_2 == NEWLINE) :
                            LA5_3 = self.input.LA(4)

                            if (LA5_3 == INDENT) :
                                alt5 = 2
                            elif (LA5_3 == EOF or LA5_3 == DEDENT or (NEWLINE <= LA5_3 <= WNAME) or (CANVAS <= LA5_3 <= NAME) or LA5_3 == LESS or LA5_3 == LBRACK) :
                                alt5 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 5, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 5, 2, self.input)

                            raise nvae

                    elif (LA5_1 == NEWLINE) :
                        LA5_3 = self.input.LA(3)

                        if (LA5_3 == INDENT) :
                            alt5 = 2
                        elif (LA5_3 == EOF or LA5_3 == DEDENT or (NEWLINE <= LA5_3 <= WNAME) or (CANVAS <= LA5_3 <= NAME) or LA5_3 == LESS or LA5_3 == LBRACK) :
                            alt5 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 5, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # kv.g:135:4: WNAME ( COLON )? NEWLINE
                    pass 
                    WNAME13=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget326) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME13)
                    # kv.g:135:10: ( COLON )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COLON) :
                        alt3 = 1
                    if alt3 == 1:
                        # kv.g:135:10: COLON
                        pass 
                        COLON14=self.match(self.input, COLON, self.FOLLOW_COLON_in_widget328) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON14)



                    NEWLINE15=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_widget331) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE15)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 135:25: -> ^( WIDGET[$WNAME] )
                        # kv.g:135:28: ^( WIDGET[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(WidgetNode(WIDGET, WNAME13), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 2:
                    # kv.g:136:4: WNAME ( COLON )? widget_body
                    pass 
                    WNAME16=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget346) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME16)
                    # kv.g:136:10: ( COLON )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COLON) :
                        alt4 = 1
                    if alt4 == 1:
                        # kv.g:136:10: COLON
                        pass 
                        COLON17=self.match(self.input, COLON, self.FOLLOW_COLON_in_widget348) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON17)



                    self._state.following.append(self.FOLLOW_widget_body_in_widget351)
                    widget_body18 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body18.tree)

                    # AST Rewrite
                    # elements: widget_body
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 136:29: -> ^( WIDGET[$WNAME] widget_body )
                        # kv.g:136:32: ^( WIDGET[$WNAME] widget_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(WidgetNode(WIDGET, WNAME16), root_1)

                        self._adaptor.addChild(root_1, stream_widget_body.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget"

    class class_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.class_rule_return, self).__init__()

            self.tree = None




    # $ANTLR start "class_rule"
    # kv.g:138:1: class_rule : ( '<' a= class_widget '>' ( COLON )? NEWLINE -> ^( CLASSRULE[$a.tree] ) | '<' a= class_widget '>' ( COLON )? widget_body -> ^( CLASSRULE[$a.tree] widget_body ) );
    def class_rule(self, ):

        retval = self.class_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal19 = None
        char_literal20 = None
        COLON21 = None
        NEWLINE22 = None
        char_literal23 = None
        char_literal24 = None
        COLON25 = None
        a = None

        widget_body26 = None


        char_literal19_tree = None
        char_literal20_tree = None
        COLON21_tree = None
        NEWLINE22_tree = None
        char_literal23_tree = None
        char_literal24_tree = None
        COLON25_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_GREATER = RewriteRuleTokenStream(self._adaptor, "token GREATER")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_LESS = RewriteRuleTokenStream(self._adaptor, "token LESS")
        stream_class_widget = RewriteRuleSubtreeStream(self._adaptor, "rule class_widget")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:139:2: ( '<' a= class_widget '>' ( COLON )? NEWLINE -> ^( CLASSRULE[$a.tree] ) | '<' a= class_widget '>' ( COLON )? widget_body -> ^( CLASSRULE[$a.tree] widget_body ) )
                alt8 = 2
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # kv.g:139:4: '<' a= class_widget '>' ( COLON )? NEWLINE
                    pass 
                    char_literal19=self.match(self.input, LESS, self.FOLLOW_LESS_in_class_rule373) 
                    if self._state.backtracking == 0:
                        stream_LESS.add(char_literal19)
                    self._state.following.append(self.FOLLOW_class_widget_in_class_rule377)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal20=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_class_rule379) 
                    if self._state.backtracking == 0:
                        stream_GREATER.add(char_literal20)
                    # kv.g:139:27: ( COLON )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COLON) :
                        alt6 = 1
                    if alt6 == 1:
                        # kv.g:139:27: COLON
                        pass 
                        COLON21=self.match(self.input, COLON, self.FOLLOW_COLON_in_class_rule381) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON21)



                    NEWLINE22=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_class_rule384) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE22)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 139:42: -> ^( CLASSRULE[$a.tree] )
                        # kv.g:139:45: ^( CLASSRULE[$a.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassRuleNode(CLASSRULE, a.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt8 == 2:
                    # kv.g:140:4: '<' a= class_widget '>' ( COLON )? widget_body
                    pass 
                    char_literal23=self.match(self.input, LESS, self.FOLLOW_LESS_in_class_rule399) 
                    if self._state.backtracking == 0:
                        stream_LESS.add(char_literal23)
                    self._state.following.append(self.FOLLOW_class_widget_in_class_rule403)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal24=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_class_rule405) 
                    if self._state.backtracking == 0:
                        stream_GREATER.add(char_literal24)
                    # kv.g:140:27: ( COLON )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COLON) :
                        alt7 = 1
                    if alt7 == 1:
                        # kv.g:140:27: COLON
                        pass 
                        COLON25=self.match(self.input, COLON, self.FOLLOW_COLON_in_class_rule407) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON25)



                    self._state.following.append(self.FOLLOW_widget_body_in_class_rule410)
                    widget_body26 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body26.tree)

                    # AST Rewrite
                    # elements: widget_body
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 140:46: -> ^( CLASSRULE[$a.tree] widget_body )
                        # kv.g:140:49: ^( CLASSRULE[$a.tree] widget_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassRuleNode(CLASSRULE, a.tree), root_1)

                        self._adaptor.addChild(root_1, stream_widget_body.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "class_rule"

    class class_widget_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.class_widget_return, self).__init__()

            self.tree = None




    # $ANTLR start "class_widget"
    # kv.g:142:1: class_widget : widget_comp ;
    def class_widget(self, ):

        retval = self.class_widget_return()
        retval.start = self.input.LT(1)

        root_0 = None

        widget_comp27 = None



        try:
            try:
                # kv.g:143:2: ( widget_comp )
                # kv.g:143:4: widget_comp
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_widget_comp_in_class_widget432)
                widget_comp27 = self.widget_comp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, widget_comp27.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "class_widget"

    class widget_comp_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_comp_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget_comp"
    # kv.g:145:1: widget_comp : ( widget_list -> widget_list | a= widget_list AT b= widget_base -> ^( AUTOCLASS[$a.tree,$b.tree] ) );
    def widget_comp(self, ):

        retval = self.widget_comp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AT29 = None
        a = None

        b = None

        widget_list28 = None


        AT29_tree = None
        stream_AT = RewriteRuleTokenStream(self._adaptor, "token AT")
        stream_widget_list = RewriteRuleSubtreeStream(self._adaptor, "rule widget_list")
        stream_widget_base = RewriteRuleSubtreeStream(self._adaptor, "rule widget_base")
        try:
            try:
                # kv.g:146:2: ( widget_list -> widget_list | a= widget_list AT b= widget_base -> ^( AUTOCLASS[$a.tree,$b.tree] ) )
                alt9 = 2
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # kv.g:146:6: widget_list
                    pass 
                    self._state.following.append(self.FOLLOW_widget_list_in_widget_comp444)
                    widget_list28 = self.widget_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_list.add(widget_list28.tree)

                    # AST Rewrite
                    # elements: widget_list
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 146:18: -> widget_list
                        self._adaptor.addChild(root_0, stream_widget_list.nextTree())



                        retval.tree = root_0


                elif alt9 == 2:
                    # kv.g:147:6: a= widget_list AT b= widget_base
                    pass 
                    self._state.following.append(self.FOLLOW_widget_list_in_widget_comp457)
                    a = self.widget_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_list.add(a.tree)
                    AT29=self.match(self.input, AT, self.FOLLOW_AT_in_widget_comp459) 
                    if self._state.backtracking == 0:
                        stream_AT.add(AT29)
                    self._state.following.append(self.FOLLOW_widget_base_in_widget_comp463)
                    b = self.widget_base()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_base.add(b.tree)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 147:37: -> ^( AUTOCLASS[$a.tree,$b.tree] )
                        # kv.g:147:40: ^( AUTOCLASS[$a.tree,$b.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(AutoClassNode(AUTOCLASS, a.tree, b.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget_comp"

    class widget_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget_list"
    # kv.g:149:1: widget_list : ( widget_name -> widget_name | widget_name (m= COMMA widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) );
    def widget_list(self, ):

        retval = self.widget_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        m = None
        widget_name30 = None

        widget_name31 = None

        widget_name32 = None


        m_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_widget_name = RewriteRuleSubtreeStream(self._adaptor, "rule widget_name")
        try:
            try:
                # kv.g:150:2: ( widget_name -> widget_name | widget_name (m= COMMA widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == WNAME) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == AT or LA11_1 == GREATER or LA11_1 == RBRACK) :
                        alt11 = 1
                    elif (LA11_1 == COMMA) :
                        alt11 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 11, 1, self.input)

                        raise nvae

                elif (LA11_0 == MINUS) :
                    LA11_2 = self.input.LA(2)

                    if (LA11_2 == WNAME) :
                        LA11_5 = self.input.LA(3)

                        if (LA11_5 == COMMA) :
                            alt11 = 2
                        elif (LA11_5 == AT or LA11_5 == GREATER or LA11_5 == RBRACK) :
                            alt11 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 11, 5, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 11, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # kv.g:150:6: widget_name
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_list485)
                    widget_name30 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name30.tree)

                    # AST Rewrite
                    # elements: widget_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 150:18: -> widget_name
                        self._adaptor.addChild(root_0, stream_widget_name.nextTree())



                        retval.tree = root_0


                elif alt11 == 2:
                    # kv.g:151:6: widget_name (m= COMMA widget_name )+
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_list496)
                    widget_name31 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name31.tree)
                    # kv.g:151:18: (m= COMMA widget_name )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == COMMA) :
                            alt10 = 1


                        if alt10 == 1:
                            # kv.g:151:19: m= COMMA widget_name
                            pass 
                            m=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_widget_list501) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(m)
                            self._state.following.append(self.FOLLOW_widget_name_in_widget_list503)
                            widget_name32 = self.widget_name()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_widget_name.add(widget_name32.tree)


                        else:
                            if cnt10 >= 1:
                                break #loop10

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1

                    # AST Rewrite
                    # elements: widget_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 151:41: -> ^( CLASSLIST[$m] ( widget_name )* )
                        # kv.g:151:44: ^( CLASSLIST[$m] ( widget_name )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassListNode(CLASSLIST, m), root_1)

                        # kv.g:151:75: ( widget_name )*
                        while stream_widget_name.hasNext():
                            self._adaptor.addChild(root_1, stream_widget_name.nextTree())


                        stream_widget_name.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget_list"

    class widget_base_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_base_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget_base"
    # kv.g:153:1: widget_base : ( widget_name -> widget_name | widget_name (m= PLUS widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) );
    def widget_base(self, ):

        retval = self.widget_base_return()
        retval.start = self.input.LT(1)

        root_0 = None

        m = None
        widget_name33 = None

        widget_name34 = None

        widget_name35 = None


        m_tree = None
        stream_PLUS = RewriteRuleTokenStream(self._adaptor, "token PLUS")
        stream_widget_name = RewriteRuleSubtreeStream(self._adaptor, "rule widget_name")
        try:
            try:
                # kv.g:154:2: ( widget_name -> widget_name | widget_name (m= PLUS widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == WNAME) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == GREATER or LA13_1 == RBRACK) :
                        alt13 = 1
                    elif (LA13_1 == PLUS) :
                        alt13 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae

                elif (LA13_0 == MINUS) :
                    LA13_2 = self.input.LA(2)

                    if (LA13_2 == WNAME) :
                        LA13_5 = self.input.LA(3)

                        if (LA13_5 == PLUS) :
                            alt13 = 2
                        elif (LA13_5 == GREATER or LA13_5 == RBRACK) :
                            alt13 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 13, 5, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 13, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # kv.g:154:6: widget_name
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_base530)
                    widget_name33 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name33.tree)

                    # AST Rewrite
                    # elements: widget_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 154:18: -> widget_name
                        self._adaptor.addChild(root_0, stream_widget_name.nextTree())



                        retval.tree = root_0


                elif alt13 == 2:
                    # kv.g:155:6: widget_name (m= PLUS widget_name )+
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_base541)
                    widget_name34 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name34.tree)
                    # kv.g:155:18: (m= PLUS widget_name )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == PLUS) :
                            alt12 = 1


                        if alt12 == 1:
                            # kv.g:155:19: m= PLUS widget_name
                            pass 
                            m=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_widget_base546) 
                            if self._state.backtracking == 0:
                                stream_PLUS.add(m)
                            self._state.following.append(self.FOLLOW_widget_name_in_widget_base548)
                            widget_name35 = self.widget_name()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_widget_name.add(widget_name35.tree)


                        else:
                            if cnt12 >= 1:
                                break #loop12

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1

                    # AST Rewrite
                    # elements: widget_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 155:40: -> ^( CLASSLIST[$m] ( widget_name )* )
                        # kv.g:155:43: ^( CLASSLIST[$m] ( widget_name )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassListNode(CLASSLIST, m), root_1)

                        # kv.g:155:74: ( widget_name )*
                        while stream_widget_name.hasNext():
                            self._adaptor.addChild(root_1, stream_widget_name.nextTree())


                        stream_widget_name.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget_base"

    class widget_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget_name"
    # kv.g:157:1: widget_name : ( WNAME -> WNAME | MINUS WNAME -> ^( RESETRULE[$WNAME] ) );
    def widget_name(self, ):

        retval = self.widget_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME36 = None
        MINUS37 = None
        WNAME38 = None

        WNAME36_tree = None
        MINUS37_tree = None
        WNAME38_tree = None
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")

        try:
            try:
                # kv.g:158:2: ( WNAME -> WNAME | MINUS WNAME -> ^( RESETRULE[$WNAME] ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == WNAME) :
                    alt14 = 1
                elif (LA14_0 == MINUS) :
                    alt14 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # kv.g:158:6: WNAME
                    pass 
                    WNAME36=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget_name575) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME36)

                    # AST Rewrite
                    # elements: WNAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 158:12: -> WNAME
                        self._adaptor.addChild(root_0, stream_WNAME.nextNode())



                        retval.tree = root_0


                elif alt14 == 2:
                    # kv.g:159:6: MINUS WNAME
                    pass 
                    MINUS37=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_widget_name586) 
                    if self._state.backtracking == 0:
                        stream_MINUS.add(MINUS37)
                    WNAME38=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget_name588) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME38)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 159:18: -> ^( RESETRULE[$WNAME] )
                        # kv.g:159:21: ^( RESETRULE[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ResetRuleNode(RESETRULE, WNAME38), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget_name"

    class class_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.class_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "class_list"
    # kv.g:161:1: class_list : WNAME ( PLUS WNAME )* ;
    def class_list(self, ):

        retval = self.class_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME39 = None
        PLUS40 = None
        WNAME41 = None

        WNAME39_tree = None
        PLUS40_tree = None
        WNAME41_tree = None

        try:
            try:
                # kv.g:162:2: ( WNAME ( PLUS WNAME )* )
                # kv.g:162:4: WNAME ( PLUS WNAME )*
                pass 
                root_0 = self._adaptor.nil()

                WNAME39=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_class_list608)
                if self._state.backtracking == 0:

                    WNAME39_tree = self._adaptor.createWithPayload(WNAME39)
                    self._adaptor.addChild(root_0, WNAME39_tree)

                # kv.g:162:10: ( PLUS WNAME )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == PLUS) :
                        alt15 = 1


                    if alt15 == 1:
                        # kv.g:162:11: PLUS WNAME
                        pass 
                        PLUS40=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_class_list611)
                        if self._state.backtracking == 0:

                            PLUS40_tree = self._adaptor.createWithPayload(PLUS40)
                            self._adaptor.addChild(root_0, PLUS40_tree)

                        WNAME41=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_class_list613)
                        if self._state.backtracking == 0:

                            WNAME41_tree = self._adaptor.createWithPayload(WNAME41)
                            self._adaptor.addChild(root_0, WNAME41_tree)



                    else:
                        break #loop15



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "class_list"

    class template_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.template_rule_return, self).__init__()

            self.tree = None




    # $ANTLR start "template_rule"
    # kv.g:164:1: template_rule : ( '[' a= class_widget ']' ( COLON )? NEWLINE -> ^( TEMPLATERULE[$a.tree] ) | '[' a= class_widget ']' ( COLON )? widget_body -> ^( TEMPLATERULE[$a.tree] widget_body ) );
    def template_rule(self, ):

        retval = self.template_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal42 = None
        char_literal43 = None
        COLON44 = None
        NEWLINE45 = None
        char_literal46 = None
        char_literal47 = None
        COLON48 = None
        a = None

        widget_body49 = None


        char_literal42_tree = None
        char_literal43_tree = None
        COLON44_tree = None
        NEWLINE45_tree = None
        char_literal46_tree = None
        char_literal47_tree = None
        COLON48_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_class_widget = RewriteRuleSubtreeStream(self._adaptor, "rule class_widget")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:165:2: ( '[' a= class_widget ']' ( COLON )? NEWLINE -> ^( TEMPLATERULE[$a.tree] ) | '[' a= class_widget ']' ( COLON )? widget_body -> ^( TEMPLATERULE[$a.tree] widget_body ) )
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # kv.g:165:4: '[' a= class_widget ']' ( COLON )? NEWLINE
                    pass 
                    char_literal42=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_template_rule625) 
                    if self._state.backtracking == 0:
                        stream_LBRACK.add(char_literal42)
                    self._state.following.append(self.FOLLOW_class_widget_in_template_rule629)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal43=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_template_rule631) 
                    if self._state.backtracking == 0:
                        stream_RBRACK.add(char_literal43)
                    # kv.g:165:27: ( COLON )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == COLON) :
                        alt16 = 1
                    if alt16 == 1:
                        # kv.g:165:27: COLON
                        pass 
                        COLON44=self.match(self.input, COLON, self.FOLLOW_COLON_in_template_rule633) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON44)



                    NEWLINE45=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_template_rule636) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE45)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 165:42: -> ^( TEMPLATERULE[$a.tree] )
                        # kv.g:165:45: ^( TEMPLATERULE[$a.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(TemplateRuleNode(TEMPLATERULE, a.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt18 == 2:
                    # kv.g:166:4: '[' a= class_widget ']' ( COLON )? widget_body
                    pass 
                    char_literal46=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_template_rule651) 
                    if self._state.backtracking == 0:
                        stream_LBRACK.add(char_literal46)
                    self._state.following.append(self.FOLLOW_class_widget_in_template_rule655)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal47=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_template_rule657) 
                    if self._state.backtracking == 0:
                        stream_RBRACK.add(char_literal47)
                    # kv.g:166:27: ( COLON )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == COLON) :
                        alt17 = 1
                    if alt17 == 1:
                        # kv.g:166:27: COLON
                        pass 
                        COLON48=self.match(self.input, COLON, self.FOLLOW_COLON_in_template_rule659) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON48)



                    self._state.following.append(self.FOLLOW_widget_body_in_template_rule662)
                    widget_body49 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body49.tree)

                    # AST Rewrite
                    # elements: widget_body
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 166:46: -> ^( TEMPLATERULE[$a.tree] widget_body )
                        # kv.g:166:49: ^( TEMPLATERULE[$a.tree] widget_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(TemplateRuleNode(TEMPLATERULE, a.tree), root_1)

                        self._adaptor.addChild(root_1, stream_widget_body.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "template_rule"

    class widget_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.widget_body_return, self).__init__()

            self.tree = None




    # $ANTLR start "widget_body"
    # kv.g:168:1: widget_body : NEWLINE INDENT ( stmt )+ DEDENT ;
    def widget_body(self, ):

        retval = self.widget_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE50 = None
        INDENT51 = None
        DEDENT53 = None
        stmt52 = None


        NEWLINE50_tree = None
        INDENT51_tree = None
        DEDENT53_tree = None

        try:
            try:
                # kv.g:169:5: ( NEWLINE INDENT ( stmt )+ DEDENT )
                # kv.g:169:7: NEWLINE INDENT ( stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE50=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_widget_body687)
                INDENT51=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_widget_body690)
                # kv.g:169:24: ( stmt )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == NEWLINE or (COMMENTTEXT <= LA19_0 <= WNAME) or (CANVAS <= LA19_0 <= NAME)) :
                        alt19 = 1


                    if alt19 == 1:
                        # kv.g:169:25: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_widget_body694)
                        stmt52 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stmt52.tree)


                    else:
                        if cnt19 >= 1:
                            break #loop19

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1
                DEDENT53=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_widget_body698)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "widget_body"

    class canvas_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.canvas_body_return, self).__init__()

            self.tree = None




    # $ANTLR start "canvas_body"
    # kv.g:171:1: canvas_body : NEWLINE INDENT ( canvas_stmt )+ DEDENT ;
    def canvas_body(self, ):

        retval = self.canvas_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE54 = None
        INDENT55 = None
        DEDENT57 = None
        canvas_stmt56 = None


        NEWLINE54_tree = None
        INDENT55_tree = None
        DEDENT57_tree = None

        try:
            try:
                # kv.g:172:2: ( NEWLINE INDENT ( canvas_stmt )+ DEDENT )
                # kv.g:172:4: NEWLINE INDENT ( canvas_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE54=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_canvas_body709)
                INDENT55=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_canvas_body712)
                # kv.g:172:21: ( canvas_stmt )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == NEWLINE or (COMMENTTEXT <= LA20_0 <= WNAME)) :
                        alt20 = 1


                    if alt20 == 1:
                        # kv.g:172:22: canvas_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_canvas_stmt_in_canvas_body716)
                        canvas_stmt56 = self.canvas_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, canvas_stmt56.tree)


                    else:
                        if cnt20 >= 1:
                            break #loop20

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1
                DEDENT57=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_canvas_body720)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "canvas_body"

    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "stmt"
    # kv.g:174:1: stmt : ( widget | canvas | prop | comment | blank );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        widget58 = None

        canvas59 = None

        prop60 = None

        comment61 = None

        blank62 = None



        try:
            try:
                # kv.g:175:2: ( widget | canvas | prop | comment | blank )
                alt21 = 5
                LA21 = self.input.LA(1)
                if LA21 == WNAME:
                    alt21 = 1
                elif LA21 == CANVAS:
                    alt21 = 2
                elif LA21 == NAME:
                    alt21 = 3
                elif LA21 == COMMENTTEXT:
                    alt21 = 4
                elif LA21 == NEWLINE:
                    alt21 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # kv.g:175:4: widget
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_widget_in_stmt731)
                    widget58 = self.widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, widget58.tree)


                elif alt21 == 2:
                    # kv.g:176:4: canvas
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_canvas_in_stmt736)
                    canvas59 = self.canvas()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, canvas59.tree)


                elif alt21 == 3:
                    # kv.g:177:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_stmt741)
                    prop60 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop60.tree)


                elif alt21 == 4:
                    # kv.g:178:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_stmt746)
                    comment61 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment61.tree)


                elif alt21 == 5:
                    # kv.g:179:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_stmt751)
                    blank62 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank62.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "stmt"

    class canvas_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.canvas_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "canvas_stmt"
    # kv.g:181:1: canvas_stmt : ( instruction | comment | blank );
    def canvas_stmt(self, ):

        retval = self.canvas_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        instruction63 = None

        comment64 = None

        blank65 = None



        try:
            try:
                # kv.g:182:2: ( instruction | comment | blank )
                alt22 = 3
                LA22 = self.input.LA(1)
                if LA22 == WNAME:
                    alt22 = 1
                elif LA22 == COMMENTTEXT:
                    alt22 = 2
                elif LA22 == NEWLINE:
                    alt22 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # kv.g:182:4: instruction
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_instruction_in_canvas_stmt762)
                    instruction63 = self.instruction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, instruction63.tree)


                elif alt22 == 2:
                    # kv.g:183:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_canvas_stmt767)
                    comment64 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment64.tree)


                elif alt22 == 3:
                    # kv.g:184:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_canvas_stmt772)
                    blank65 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank65.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "canvas_stmt"

    class instruction_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.instruction_return, self).__init__()

            self.tree = None




    # $ANTLR start "instruction"
    # kv.g:186:1: instruction : ( WNAME ( COLON )? NEWLINE -> ^( INSTRUCTION[$WNAME] ) | WNAME ( COLON )? instruction_body -> ^( INSTRUCTION[$WNAME] instruction_body ) );
    def instruction(self, ):

        retval = self.instruction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME66 = None
        COLON67 = None
        NEWLINE68 = None
        WNAME69 = None
        COLON70 = None
        instruction_body71 = None


        WNAME66_tree = None
        COLON67_tree = None
        NEWLINE68_tree = None
        WNAME69_tree = None
        COLON70_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_instruction_body = RewriteRuleSubtreeStream(self._adaptor, "rule instruction_body")
        try:
            try:
                # kv.g:187:2: ( WNAME ( COLON )? NEWLINE -> ^( INSTRUCTION[$WNAME] ) | WNAME ( COLON )? instruction_body -> ^( INSTRUCTION[$WNAME] instruction_body ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == WNAME) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == COLON) :
                        LA25_2 = self.input.LA(3)

                        if (LA25_2 == NEWLINE) :
                            LA25_3 = self.input.LA(4)

                            if (LA25_3 == INDENT) :
                                alt25 = 2
                            elif (LA25_3 == DEDENT or LA25_3 == NEWLINE or (COMMENTTEXT <= LA25_3 <= WNAME)) :
                                alt25 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 25, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 25, 2, self.input)

                            raise nvae

                    elif (LA25_1 == NEWLINE) :
                        LA25_3 = self.input.LA(3)

                        if (LA25_3 == INDENT) :
                            alt25 = 2
                        elif (LA25_3 == DEDENT or LA25_3 == NEWLINE or (COMMENTTEXT <= LA25_3 <= WNAME)) :
                            alt25 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 25, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # kv.g:187:4: WNAME ( COLON )? NEWLINE
                    pass 
                    WNAME66=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction783) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME66)
                    # kv.g:187:10: ( COLON )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == COLON) :
                        alt23 = 1
                    if alt23 == 1:
                        # kv.g:187:10: COLON
                        pass 
                        COLON67=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction785) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON67)



                    NEWLINE68=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction788) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE68)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 187:25: -> ^( INSTRUCTION[$WNAME] )
                        # kv.g:187:28: ^( INSTRUCTION[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME66), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt25 == 2:
                    # kv.g:188:4: WNAME ( COLON )? instruction_body
                    pass 
                    WNAME69=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction803) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME69)
                    # kv.g:188:10: ( COLON )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COLON) :
                        alt24 = 1
                    if alt24 == 1:
                        # kv.g:188:10: COLON
                        pass 
                        COLON70=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction805) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON70)



                    self._state.following.append(self.FOLLOW_instruction_body_in_instruction808)
                    instruction_body71 = self.instruction_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_instruction_body.add(instruction_body71.tree)

                    # AST Rewrite
                    # elements: instruction_body
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 188:34: -> ^( INSTRUCTION[$WNAME] instruction_body )
                        # kv.g:188:37: ^( INSTRUCTION[$WNAME] instruction_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME69), root_1)

                        self._adaptor.addChild(root_1, stream_instruction_body.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "instruction"

    class instruction_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.instruction_body_return, self).__init__()

            self.tree = None




    # $ANTLR start "instruction_body"
    # kv.g:190:1: instruction_body : NEWLINE INDENT ( instruction_stmt )+ DEDENT ;
    def instruction_body(self, ):

        retval = self.instruction_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE72 = None
        INDENT73 = None
        DEDENT75 = None
        instruction_stmt74 = None


        NEWLINE72_tree = None
        INDENT73_tree = None
        DEDENT75_tree = None

        try:
            try:
                # kv.g:191:2: ( NEWLINE INDENT ( instruction_stmt )+ DEDENT )
                # kv.g:191:4: NEWLINE INDENT ( instruction_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE72=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction_body831)
                INDENT73=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_instruction_body834)
                # kv.g:191:21: ( instruction_stmt )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == NEWLINE or LA26_0 == COMMENTTEXT or LA26_0 == NAME) :
                        alt26 = 1


                    if alt26 == 1:
                        # kv.g:191:22: instruction_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_instruction_stmt_in_instruction_body838)
                        instruction_stmt74 = self.instruction_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instruction_stmt74.tree)


                    else:
                        if cnt26 >= 1:
                            break #loop26

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1
                DEDENT75=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_instruction_body842)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "instruction_body"

    class instruction_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.instruction_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "instruction_stmt"
    # kv.g:193:1: instruction_stmt : ( prop | comment | blank );
    def instruction_stmt(self, ):

        retval = self.instruction_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prop76 = None

        comment77 = None

        blank78 = None



        try:
            try:
                # kv.g:194:2: ( prop | comment | blank )
                alt27 = 3
                LA27 = self.input.LA(1)
                if LA27 == NAME:
                    alt27 = 1
                elif LA27 == COMMENTTEXT:
                    alt27 = 2
                elif LA27 == NEWLINE:
                    alt27 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # kv.g:194:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_instruction_stmt854)
                    prop76 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop76.tree)


                elif alt27 == 2:
                    # kv.g:195:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_instruction_stmt859)
                    comment77 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment77.tree)


                elif alt27 == 3:
                    # kv.g:196:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_instruction_stmt864)
                    blank78 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank78.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "instruction_stmt"

    class canvas_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.canvas_return, self).__init__()

            self.tree = None




    # $ANTLR start "canvas"
    # kv.g:198:1: canvas : CANVAS COLON canvas_body -> ^( CANVASRULE[$CANVAS] canvas_body ) ;
    def canvas(self, ):

        retval = self.canvas_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CANVAS79 = None
        COLON80 = None
        canvas_body81 = None


        CANVAS79_tree = None
        COLON80_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_CANVAS = RewriteRuleTokenStream(self._adaptor, "token CANVAS")
        stream_canvas_body = RewriteRuleSubtreeStream(self._adaptor, "rule canvas_body")
        try:
            try:
                # kv.g:199:2: ( CANVAS COLON canvas_body -> ^( CANVASRULE[$CANVAS] canvas_body ) )
                # kv.g:199:4: CANVAS COLON canvas_body
                pass 
                CANVAS79=self.match(self.input, CANVAS, self.FOLLOW_CANVAS_in_canvas875) 
                if self._state.backtracking == 0:
                    stream_CANVAS.add(CANVAS79)
                COLON80=self.match(self.input, COLON, self.FOLLOW_COLON_in_canvas877) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON80)
                self._state.following.append(self.FOLLOW_canvas_body_in_canvas879)
                canvas_body81 = self.canvas_body()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_canvas_body.add(canvas_body81.tree)

                # AST Rewrite
                # elements: canvas_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 199:29: -> ^( CANVASRULE[$CANVAS] canvas_body )
                    # kv.g:199:32: ^( CANVASRULE[$CANVAS] canvas_body )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(CanvasNode(CANVASRULE, CANVAS79), root_1)

                    self._adaptor.addChild(root_1, stream_canvas_body.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "canvas"

    class prop_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.prop_return, self).__init__()

            self.tree = None




    # $ANTLR start "prop"
    # kv.g:201:1: prop : ( NAME COLON ( WS )* p= property_body -> ^( PROPERTY[$NAME,$p.tree] ) | NAME COLON ( WS )* p= prop_value NEWLINE -> ^( PROPERTY[$NAME,$p.tree] ) );
    def prop(self, ):

        retval = self.prop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME82 = None
        COLON83 = None
        WS84 = None
        NAME85 = None
        COLON86 = None
        WS87 = None
        NEWLINE88 = None
        p = None


        NAME82_tree = None
        COLON83_tree = None
        WS84_tree = None
        NAME85_tree = None
        COLON86_tree = None
        WS87_tree = None
        NEWLINE88_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_prop_value = RewriteRuleSubtreeStream(self._adaptor, "rule prop_value")
        stream_property_body = RewriteRuleSubtreeStream(self._adaptor, "rule property_body")
        try:
            try:
                # kv.g:202:2: ( NAME COLON ( WS )* p= property_body -> ^( PROPERTY[$NAME,$p.tree] ) | NAME COLON ( WS )* p= prop_value NEWLINE -> ^( PROPERTY[$NAME,$p.tree] ) )
                alt30 = 2
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # kv.g:202:4: NAME COLON ( WS )* p= property_body
                    pass 
                    NAME82=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop900) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME82)
                    COLON83=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop902) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON83)
                    # kv.g:202:15: ( WS )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == WS) :
                            alt28 = 1


                        if alt28 == 1:
                            # kv.g:202:15: WS
                            pass 
                            WS84=self.match(self.input, WS, self.FOLLOW_WS_in_prop904) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS84)


                        else:
                            break #loop28
                    self._state.following.append(self.FOLLOW_property_body_in_prop909)
                    p = self.property_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property_body.add(p.tree)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 202:35: -> ^( PROPERTY[$NAME,$p.tree] )
                        # kv.g:202:38: ^( PROPERTY[$NAME,$p.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME82, p.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt30 == 2:
                    # kv.g:203:4: NAME COLON ( WS )* p= prop_value NEWLINE
                    pass 
                    NAME85=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop924) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME85)
                    COLON86=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop926) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON86)
                    # kv.g:203:15: ( WS )*
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == WS) :
                            alt29 = 1


                        if alt29 == 1:
                            # kv.g:203:15: WS
                            pass 
                            WS87=self.match(self.input, WS, self.FOLLOW_WS_in_prop928) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS87)


                        else:
                            break #loop29
                    self._state.following.append(self.FOLLOW_prop_value_in_prop933)
                    p = self.prop_value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prop_value.add(p.tree)
                    NEWLINE88=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_prop935) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE88)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 203:40: -> ^( PROPERTY[$NAME,$p.tree] )
                        # kv.g:203:43: ^( PROPERTY[$NAME,$p.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME85, p.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prop"

    class property_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.property_body_return, self).__init__()

            self.tree = None




    # $ANTLR start "property_body"
    # kv.g:205:1: property_body : NEWLINE INDENT prop_value ( NEWLINE prop_value )* DEDENT ;
    def property_body(self, ):

        retval = self.property_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE89 = None
        INDENT90 = None
        NEWLINE92 = None
        DEDENT94 = None
        prop_value91 = None

        prop_value93 = None


        NEWLINE89_tree = None
        INDENT90_tree = None
        NEWLINE92_tree = None
        DEDENT94_tree = None

        try:
            try:
                # kv.g:206:2: ( NEWLINE INDENT prop_value ( NEWLINE prop_value )* DEDENT )
                # kv.g:206:4: NEWLINE INDENT prop_value ( NEWLINE prop_value )* DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE89=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_property_body955)
                INDENT90=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_property_body958)
                self._state.following.append(self.FOLLOW_prop_value_in_property_body961)
                prop_value91 = self.prop_value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, prop_value91.tree)
                # kv.g:206:32: ( NEWLINE prop_value )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == NEWLINE) :
                        alt31 = 1


                    if alt31 == 1:
                        # kv.g:206:33: NEWLINE prop_value
                        pass 
                        NEWLINE92=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_property_body964)
                        self._state.following.append(self.FOLLOW_prop_value_in_property_body967)
                        prop_value93 = self.prop_value()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, prop_value93.tree)


                    else:
                        break #loop31
                DEDENT94=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_property_body971)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "property_body"

    class prop_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.prop_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "prop_value"
    # kv.g:208:1: prop_value : p= python -> ^( PYTHON[$p.tree] ) ;
    def prop_value(self, ):

        retval = self.prop_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        p = None


        stream_python = RewriteRuleSubtreeStream(self._adaptor, "rule python")
        try:
            try:
                # kv.g:209:2: (p= python -> ^( PYTHON[$p.tree] ) )
                # kv.g:209:4: p= python
                pass 
                self._state.following.append(self.FOLLOW_python_in_prop_value984)
                p = self.python()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_python.add(p.tree)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 209:13: -> ^( PYTHON[$p.tree] )
                    # kv.g:209:16: ^( PYTHON[$p.tree] )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(PythonNode(PYTHON, p.tree), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prop_value"

    class python_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.python_return, self).__init__()

            self.tree = None




    # $ANTLR start "python"
    # kv.g:214:1: python : ( simple_stmt | compound_stmt );
    def python(self, ):

        retval = self.python_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simple_stmt95 = None

        compound_stmt96 = None



        try:
            try:
                # kv.g:215:2: ( simple_stmt | compound_stmt )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == WNAME or (PLUS <= LA32_0 <= MINUS) or LA32_0 == NAME or LA32_0 == LPAREN or LA32_0 == NOT or (TILDE <= LA32_0 <= LBRACK) or LA32_0 == LCURLY or (BACKQUOTE <= LA32_0 <= STRING) or (86 <= LA32_0 <= 92) or LA32_0 == 94 or (106 <= LA32_0 <= 107)) :
                    alt32 = 1
                elif (LA32_0 == 95 or (98 <= LA32_0 <= 100) or LA32_0 == 102) :
                    alt32 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # kv.g:215:6: simple_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_stmt_in_python1007)
                    simple_stmt95 = self.simple_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_stmt95.tree)


                elif alt32 == 2:
                    # kv.g:216:6: compound_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_compound_stmt_in_python1014)
                    compound_stmt96 = self.compound_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, compound_stmt96.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "python"

    class simple_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.simple_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "simple_stmt"
    # kv.g:218:1: simple_stmt : small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )? ;
    def simple_stmt(self, ):

        retval = self.simple_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI98 = None
        SEMI100 = None
        small_stmt97 = None

        small_stmt99 = None


        SEMI98_tree = None
        SEMI100_tree = None

        try:
            try:
                # kv.g:219:2: ( small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )? )
                # kv.g:219:4: small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_small_stmt_in_simple_stmt1024)
                small_stmt97 = self.small_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, small_stmt97.tree)
                # kv.g:219:15: ( options {greedy=true; } : SEMI small_stmt )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == SEMI) :
                        LA33_1 = self.input.LA(2)

                        if (LA33_1 == WNAME or (PLUS <= LA33_1 <= MINUS) or LA33_1 == NAME or LA33_1 == LPAREN or LA33_1 == NOT or (TILDE <= LA33_1 <= LBRACK) or LA33_1 == LCURLY or (BACKQUOTE <= LA33_1 <= STRING) or (86 <= LA33_1 <= 92) or LA33_1 == 94 or (106 <= LA33_1 <= 107)) :
                            alt33 = 1




                    if alt33 == 1:
                        # kv.g:219:39: SEMI small_stmt
                        pass 
                        SEMI98=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_simple_stmt1034)
                        if self._state.backtracking == 0:

                            SEMI98_tree = self._adaptor.createWithPayload(SEMI98)
                            self._adaptor.addChild(root_0, SEMI98_tree)

                        self._state.following.append(self.FOLLOW_small_stmt_in_simple_stmt1036)
                        small_stmt99 = self.small_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, small_stmt99.tree)


                    else:
                        break #loop33
                # kv.g:219:57: ( SEMI )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == SEMI) :
                    alt34 = 1
                if alt34 == 1:
                    # kv.g:219:58: SEMI
                    pass 
                    SEMI100=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_simple_stmt1041)
                    if self._state.backtracking == 0:

                        SEMI100_tree = self._adaptor.createWithPayload(SEMI100)
                        self._adaptor.addChild(root_0, SEMI100_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simple_stmt"

    class small_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.small_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "small_stmt"
    # kv.g:221:1: small_stmt : ( expr_stmt | print_stmt | del_stmt | pass_stmt | flow_stmt | exec_stmt | assert_stmt );
    def small_stmt(self, ):

        retval = self.small_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        expr_stmt101 = None

        print_stmt102 = None

        del_stmt103 = None

        pass_stmt104 = None

        flow_stmt105 = None

        exec_stmt106 = None

        assert_stmt107 = None



        try:
            try:
                # kv.g:222:2: ( expr_stmt | print_stmt | del_stmt | pass_stmt | flow_stmt | exec_stmt | assert_stmt )
                alt35 = 7
                LA35 = self.input.LA(1)
                if LA35 == WNAME or LA35 == PLUS or LA35 == MINUS or LA35 == NAME or LA35 == LPAREN or LA35 == NOT or LA35 == TILDE or LA35 == LBRACK or LA35 == LCURLY or LA35 == BACKQUOTE or LA35 == NONE or LA35 == INT or LA35 == LONGINT or LA35 == FLOAT or LA35 == COMPLEX or LA35 == STRING or LA35 == 106:
                    alt35 = 1
                elif LA35 == 86:
                    alt35 = 2
                elif LA35 == 87:
                    alt35 = 3
                elif LA35 == 88:
                    alt35 = 4
                elif LA35 == 89 or LA35 == 90 or LA35 == 91 or LA35 == 107:
                    alt35 = 5
                elif LA35 == 92:
                    alt35 = 6
                elif LA35 == 94:
                    alt35 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # kv.g:222:4: expr_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_stmt_in_small_stmt1054)
                    expr_stmt101 = self.expr_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr_stmt101.tree)


                elif alt35 == 2:
                    # kv.g:223:6: print_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_print_stmt_in_small_stmt1061)
                    print_stmt102 = self.print_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, print_stmt102.tree)


                elif alt35 == 3:
                    # kv.g:224:6: del_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_del_stmt_in_small_stmt1068)
                    del_stmt103 = self.del_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, del_stmt103.tree)


                elif alt35 == 4:
                    # kv.g:225:6: pass_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pass_stmt_in_small_stmt1075)
                    pass_stmt104 = self.pass_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pass_stmt104.tree)


                elif alt35 == 5:
                    # kv.g:226:6: flow_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flow_stmt_in_small_stmt1082)
                    flow_stmt105 = self.flow_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, flow_stmt105.tree)


                elif alt35 == 6:
                    # kv.g:227:6: exec_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_exec_stmt_in_small_stmt1089)
                    exec_stmt106 = self.exec_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, exec_stmt106.tree)


                elif alt35 == 7:
                    # kv.g:228:6: assert_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assert_stmt_in_small_stmt1096)
                    assert_stmt107 = self.assert_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assert_stmt107.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "small_stmt"

    class varargslist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.varargslist_return, self).__init__()

            self.tree = None




    # $ANTLR start "varargslist"
    # kv.g:230:1: varargslist : ( defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )? | STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier );
    def varargslist(self, ):

        retval = self.varargslist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA109 = None
        COMMA111 = None
        STAR112 = None
        COMMA114 = None
        DOUBLESTAR115 = None
        DOUBLESTAR117 = None
        STAR119 = None
        COMMA121 = None
        DOUBLESTAR122 = None
        DOUBLESTAR124 = None
        defparameter108 = None

        defparameter110 = None

        identifier113 = None

        identifier116 = None

        identifier118 = None

        identifier120 = None

        identifier123 = None

        identifier125 = None


        COMMA109_tree = None
        COMMA111_tree = None
        STAR112_tree = None
        COMMA114_tree = None
        DOUBLESTAR115_tree = None
        DOUBLESTAR117_tree = None
        STAR119_tree = None
        COMMA121_tree = None
        DOUBLESTAR122_tree = None
        DOUBLESTAR124_tree = None

        try:
            try:
                # kv.g:231:2: ( defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )? | STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )
                alt41 = 3
                LA41 = self.input.LA(1)
                if LA41 == WNAME or LA41 == NAME or LA41 == LPAREN:
                    alt41 = 1
                elif LA41 == STAR:
                    alt41 = 2
                elif LA41 == DOUBLESTAR:
                    alt41 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # kv.g:231:4: defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_defparameter_in_varargslist1106)
                    defparameter108 = self.defparameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, defparameter108.tree)
                    # kv.g:231:17: ( options {greedy=true; } : COMMA defparameter )*
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == COMMA) :
                            LA36_1 = self.input.LA(2)

                            if (LA36_1 == WNAME or LA36_1 == NAME or LA36_1 == LPAREN) :
                                alt36 = 1




                        if alt36 == 1:
                            # kv.g:231:41: COMMA defparameter
                            pass 
                            COMMA109=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1116)
                            if self._state.backtracking == 0:

                                COMMA109_tree = self._adaptor.createWithPayload(COMMA109)
                                self._adaptor.addChild(root_0, COMMA109_tree)

                            self._state.following.append(self.FOLLOW_defparameter_in_varargslist1118)
                            defparameter110 = self.defparameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, defparameter110.tree)


                        else:
                            break #loop36
                    # kv.g:231:62: ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == COMMA) :
                        alt39 = 1
                    if alt39 == 1:
                        # kv.g:231:63: COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        pass 
                        COMMA111=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1123)
                        if self._state.backtracking == 0:

                            COMMA111_tree = self._adaptor.createWithPayload(COMMA111)
                            self._adaptor.addChild(root_0, COMMA111_tree)

                        # kv.g:231:69: ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        alt38 = 3
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == STAR) :
                            alt38 = 1
                        elif (LA38_0 == DOUBLESTAR) :
                            alt38 = 2
                        if alt38 == 1:
                            # kv.g:231:71: STAR identifier ( COMMA DOUBLESTAR identifier )?
                            pass 
                            STAR112=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1127)
                            if self._state.backtracking == 0:

                                STAR112_tree = self._adaptor.createWithPayload(STAR112)
                                self._adaptor.addChild(root_0, STAR112_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1129)
                            identifier113 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier113.tree)
                            # kv.g:231:87: ( COMMA DOUBLESTAR identifier )?
                            alt37 = 2
                            LA37_0 = self.input.LA(1)

                            if (LA37_0 == COMMA) :
                                alt37 = 1
                            if alt37 == 1:
                                # kv.g:231:88: COMMA DOUBLESTAR identifier
                                pass 
                                COMMA114=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1132)
                                if self._state.backtracking == 0:

                                    COMMA114_tree = self._adaptor.createWithPayload(COMMA114)
                                    self._adaptor.addChild(root_0, COMMA114_tree)

                                DOUBLESTAR115=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1134)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR115_tree = self._adaptor.createWithPayload(DOUBLESTAR115)
                                    self._adaptor.addChild(root_0, DOUBLESTAR115_tree)

                                self._state.following.append(self.FOLLOW_identifier_in_varargslist1136)
                                identifier116 = self.identifier()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, identifier116.tree)





                        elif alt38 == 2:
                            # kv.g:231:120: DOUBLESTAR identifier
                            pass 
                            DOUBLESTAR117=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1142)
                            if self._state.backtracking == 0:

                                DOUBLESTAR117_tree = self._adaptor.createWithPayload(DOUBLESTAR117)
                                self._adaptor.addChild(root_0, DOUBLESTAR117_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1144)
                            identifier118 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier118.tree)








                elif alt41 == 2:
                    # kv.g:232:4: STAR identifier ( COMMA DOUBLESTAR identifier )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR119=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1155)
                    if self._state.backtracking == 0:

                        STAR119_tree = self._adaptor.createWithPayload(STAR119)
                        self._adaptor.addChild(root_0, STAR119_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1157)
                    identifier120 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier120.tree)
                    # kv.g:232:20: ( COMMA DOUBLESTAR identifier )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == COMMA) :
                        alt40 = 1
                    if alt40 == 1:
                        # kv.g:232:21: COMMA DOUBLESTAR identifier
                        pass 
                        COMMA121=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1160)
                        if self._state.backtracking == 0:

                            COMMA121_tree = self._adaptor.createWithPayload(COMMA121)
                            self._adaptor.addChild(root_0, COMMA121_tree)

                        DOUBLESTAR122=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1162)
                        if self._state.backtracking == 0:

                            DOUBLESTAR122_tree = self._adaptor.createWithPayload(DOUBLESTAR122)
                            self._adaptor.addChild(root_0, DOUBLESTAR122_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_varargslist1164)
                        identifier123 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier123.tree)





                elif alt41 == 3:
                    # kv.g:233:4: DOUBLESTAR identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR124=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1171)
                    if self._state.backtracking == 0:

                        DOUBLESTAR124_tree = self._adaptor.createWithPayload(DOUBLESTAR124)
                        self._adaptor.addChild(root_0, DOUBLESTAR124_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1173)
                    identifier125 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier125.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "varargslist"

    class defparameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.defparameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "defparameter"
    # kv.g:235:1: defparameter : fpdef ( ASSIGN test )? ;
    def defparameter(self, ):

        retval = self.defparameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN127 = None
        fpdef126 = None

        test128 = None


        ASSIGN127_tree = None

        try:
            try:
                # kv.g:236:2: ( fpdef ( ASSIGN test )? )
                # kv.g:236:4: fpdef ( ASSIGN test )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_defparameter1183)
                fpdef126 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef126.tree)
                # kv.g:236:10: ( ASSIGN test )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == ASSIGN) :
                    alt42 = 1
                if alt42 == 1:
                    # kv.g:236:11: ASSIGN test
                    pass 
                    ASSIGN127=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_defparameter1186)
                    if self._state.backtracking == 0:

                        ASSIGN127_tree = self._adaptor.createWithPayload(ASSIGN127)
                        self._adaptor.addChild(root_0, ASSIGN127_tree)

                    self._state.following.append(self.FOLLOW_test_in_defparameter1188)
                    test128 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test128.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "defparameter"

    class fpdef_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.fpdef_return, self).__init__()

            self.tree = None




    # $ANTLR start "fpdef"
    # kv.g:238:1: fpdef : ( identifier | LPAREN fplist RPAREN );
    def fpdef(self, ):

        retval = self.fpdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN130 = None
        RPAREN132 = None
        identifier129 = None

        fplist131 = None


        LPAREN130_tree = None
        RPAREN132_tree = None

        try:
            try:
                # kv.g:239:2: ( identifier | LPAREN fplist RPAREN )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == WNAME or LA43_0 == NAME) :
                    alt43 = 1
                elif (LA43_0 == LPAREN) :
                    alt43 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # kv.g:239:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_fpdef1200)
                    identifier129 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier129.tree)


                elif alt43 == 2:
                    # kv.g:240:4: LPAREN fplist RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN130=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_fpdef1205)
                    if self._state.backtracking == 0:

                        LPAREN130_tree = self._adaptor.createWithPayload(LPAREN130)
                        self._adaptor.addChild(root_0, LPAREN130_tree)

                    self._state.following.append(self.FOLLOW_fplist_in_fpdef1207)
                    fplist131 = self.fplist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fplist131.tree)
                    RPAREN132=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_fpdef1209)
                    if self._state.backtracking == 0:

                        RPAREN132_tree = self._adaptor.createWithPayload(RPAREN132)
                        self._adaptor.addChild(root_0, RPAREN132_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fpdef"

    class fplist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.fplist_return, self).__init__()

            self.tree = None




    # $ANTLR start "fplist"
    # kv.g:242:1: fplist : fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )? ;
    def fplist(self, ):

        retval = self.fplist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA134 = None
        COMMA136 = None
        fpdef133 = None

        fpdef135 = None


        COMMA134_tree = None
        COMMA136_tree = None

        try:
            try:
                # kv.g:243:2: ( fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )? )
                # kv.g:243:4: fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_fplist1219)
                fpdef133 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef133.tree)
                # kv.g:243:10: ( options {greedy=true; } : COMMA fpdef )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == COMMA) :
                        LA44_1 = self.input.LA(2)

                        if (LA44_1 == WNAME or LA44_1 == NAME or LA44_1 == LPAREN) :
                            alt44 = 1




                    if alt44 == 1:
                        # kv.g:243:34: COMMA fpdef
                        pass 
                        COMMA134=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1229)
                        if self._state.backtracking == 0:

                            COMMA134_tree = self._adaptor.createWithPayload(COMMA134)
                            self._adaptor.addChild(root_0, COMMA134_tree)

                        self._state.following.append(self.FOLLOW_fpdef_in_fplist1231)
                        fpdef135 = self.fpdef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fpdef135.tree)


                    else:
                        break #loop44
                # kv.g:243:48: ( COMMA )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == COMMA) :
                    alt45 = 1
                if alt45 == 1:
                    # kv.g:243:49: COMMA
                    pass 
                    COMMA136=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1236)
                    if self._state.backtracking == 0:

                        COMMA136_tree = self._adaptor.createWithPayload(COMMA136)
                        self._adaptor.addChild(root_0, COMMA136_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fplist"

    class expr_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.expr_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr_stmt"
    # kv.g:245:1: expr_stmt : testlist ( augassign yield_expr | augassign testlist | assigns )? ;
    def expr_stmt(self, ):

        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        testlist137 = None

        augassign138 = None

        yield_expr139 = None

        augassign140 = None

        testlist141 = None

        assigns142 = None



        try:
            try:
                # kv.g:246:2: ( testlist ( augassign yield_expr | augassign testlist | assigns )? )
                # kv.g:246:4: testlist ( augassign yield_expr | augassign testlist | assigns )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1249)
                testlist137 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist137.tree)
                # kv.g:246:13: ( augassign yield_expr | augassign testlist | assigns )?
                alt46 = 4
                LA46_0 = self.input.LA(1)

                if ((PLUSEQUAL <= LA46_0 <= DOUBLESLASHEQUAL)) :
                    LA46_1 = self.input.LA(2)

                    if (LA46_1 == WNAME or (PLUS <= LA46_1 <= MINUS) or LA46_1 == NAME or LA46_1 == LPAREN or LA46_1 == NOT or (TILDE <= LA46_1 <= LBRACK) or LA46_1 == LCURLY or (BACKQUOTE <= LA46_1 <= STRING) or LA46_1 == 106) :
                        alt46 = 2
                    elif (LA46_1 == 107) :
                        alt46 = 1
                elif (LA46_0 == ASSIGN) :
                    alt46 = 3
                if alt46 == 1:
                    # kv.g:246:14: augassign yield_expr
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1252)
                    augassign138 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign138.tree)
                    self._state.following.append(self.FOLLOW_yield_expr_in_expr_stmt1254)
                    yield_expr139 = self.yield_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_expr139.tree)


                elif alt46 == 2:
                    # kv.g:246:37: augassign testlist
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1258)
                    augassign140 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign140.tree)
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1260)
                    testlist141 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist141.tree)


                elif alt46 == 3:
                    # kv.g:246:58: assigns
                    pass 
                    self._state.following.append(self.FOLLOW_assigns_in_expr_stmt1264)
                    assigns142 = self.assigns()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assigns142.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr_stmt"

    class assigns_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.assigns_return, self).__init__()

            self.tree = None




    # $ANTLR start "assigns"
    # kv.g:248:1: assigns : ( ( assign_testlist )+ | ( assign_yield )+ );
    def assigns(self, ):

        retval = self.assigns_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_testlist143 = None

        assign_yield144 = None



        try:
            try:
                # kv.g:249:2: ( ( assign_testlist )+ | ( assign_yield )+ )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == ASSIGN) :
                    LA49_1 = self.input.LA(2)

                    if (LA49_1 == 107) :
                        alt49 = 2
                    elif (LA49_1 == WNAME or (PLUS <= LA49_1 <= MINUS) or LA49_1 == NAME or LA49_1 == LPAREN or LA49_1 == NOT or (TILDE <= LA49_1 <= LBRACK) or LA49_1 == LCURLY or (BACKQUOTE <= LA49_1 <= STRING) or LA49_1 == 106) :
                        alt49 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 49, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # kv.g:249:4: ( assign_testlist )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:249:4: ( assign_testlist )+
                    cnt47 = 0
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == ASSIGN) :
                            alt47 = 1


                        if alt47 == 1:
                            # kv.g:249:4: assign_testlist
                            pass 
                            self._state.following.append(self.FOLLOW_assign_testlist_in_assigns1277)
                            assign_testlist143 = self.assign_testlist()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_testlist143.tree)


                        else:
                            if cnt47 >= 1:
                                break #loop47

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(47, self.input)
                            raise eee

                        cnt47 += 1


                elif alt49 == 2:
                    # kv.g:249:23: ( assign_yield )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:249:23: ( assign_yield )+
                    cnt48 = 0
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == ASSIGN) :
                            alt48 = 1


                        if alt48 == 1:
                            # kv.g:249:23: assign_yield
                            pass 
                            self._state.following.append(self.FOLLOW_assign_yield_in_assigns1282)
                            assign_yield144 = self.assign_yield()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_yield144.tree)


                        else:
                            if cnt48 >= 1:
                                break #loop48

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(48, self.input)
                            raise eee

                        cnt48 += 1


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assigns"

    class assign_testlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.assign_testlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "assign_testlist"
    # kv.g:251:1: assign_testlist : ASSIGN testlist ;
    def assign_testlist(self, ):

        retval = self.assign_testlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN145 = None
        testlist146 = None


        ASSIGN145_tree = None

        try:
            try:
                # kv.g:252:2: ( ASSIGN testlist )
                # kv.g:252:4: ASSIGN testlist
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN145=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_testlist1294)
                if self._state.backtracking == 0:

                    ASSIGN145_tree = self._adaptor.createWithPayload(ASSIGN145)
                    self._adaptor.addChild(root_0, ASSIGN145_tree)

                self._state.following.append(self.FOLLOW_testlist_in_assign_testlist1296)
                testlist146 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist146.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assign_testlist"

    class assign_yield_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.assign_yield_return, self).__init__()

            self.tree = None




    # $ANTLR start "assign_yield"
    # kv.g:254:1: assign_yield : ASSIGN yield_expr ;
    def assign_yield(self, ):

        retval = self.assign_yield_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN147 = None
        yield_expr148 = None


        ASSIGN147_tree = None

        try:
            try:
                # kv.g:255:2: ( ASSIGN yield_expr )
                # kv.g:255:4: ASSIGN yield_expr
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN147=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_yield1307)
                if self._state.backtracking == 0:

                    ASSIGN147_tree = self._adaptor.createWithPayload(ASSIGN147)
                    self._adaptor.addChild(root_0, ASSIGN147_tree)

                self._state.following.append(self.FOLLOW_yield_expr_in_assign_yield1309)
                yield_expr148 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr148.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assign_yield"

    class augassign_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.augassign_return, self).__init__()

            self.tree = None




    # $ANTLR start "augassign"
    # kv.g:257:1: augassign : ( PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL );
    def augassign(self, ):

        retval = self.augassign_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set149 = None

        set149_tree = None

        try:
            try:
                # kv.g:258:2: ( PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set149 = self.input.LT(1)
                if (PLUSEQUAL <= self.input.LA(1) <= DOUBLESLASHEQUAL):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set149))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "augassign"

    class print_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.print_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "print_stmt"
    # kv.g:262:1: print_stmt : 'print' ( printlist | RIGHTSHIFT printlist )? ;
    def print_stmt(self, ):

        retval = self.print_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal150 = None
        RIGHTSHIFT152 = None
        printlist151 = None

        printlist153 = None


        string_literal150_tree = None
        RIGHTSHIFT152_tree = None

        try:
            try:
                # kv.g:263:2: ( 'print' ( printlist | RIGHTSHIFT printlist )? )
                # kv.g:263:6: 'print' ( printlist | RIGHTSHIFT printlist )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal150=self.match(self.input, 86, self.FOLLOW_86_in_print_stmt1379)
                if self._state.backtracking == 0:

                    string_literal150_tree = self._adaptor.createWithPayload(string_literal150)
                    self._adaptor.addChild(root_0, string_literal150_tree)

                # kv.g:263:14: ( printlist | RIGHTSHIFT printlist )?
                alt50 = 3
                LA50_0 = self.input.LA(1)

                if (LA50_0 == WNAME or (PLUS <= LA50_0 <= MINUS) or LA50_0 == NAME or LA50_0 == LPAREN or LA50_0 == NOT or (TILDE <= LA50_0 <= LBRACK) or LA50_0 == LCURLY or (BACKQUOTE <= LA50_0 <= STRING) or LA50_0 == 106) :
                    alt50 = 1
                elif (LA50_0 == RIGHTSHIFT) :
                    alt50 = 2
                if alt50 == 1:
                    # kv.g:263:15: printlist
                    pass 
                    self._state.following.append(self.FOLLOW_printlist_in_print_stmt1382)
                    printlist151 = self.printlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, printlist151.tree)


                elif alt50 == 2:
                    # kv.g:263:27: RIGHTSHIFT printlist
                    pass 
                    RIGHTSHIFT152=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_print_stmt1386)
                    if self._state.backtracking == 0:

                        RIGHTSHIFT152_tree = self._adaptor.createWithPayload(RIGHTSHIFT152)
                        self._adaptor.addChild(root_0, RIGHTSHIFT152_tree)

                    self._state.following.append(self.FOLLOW_printlist_in_print_stmt1388)
                    printlist153 = self.printlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, printlist153.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "print_stmt"

    class printlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.printlist_return, self).__init__()

            self.newline = None
            self.tree = None




    # $ANTLR start "printlist"
    # kv.g:265:1: printlist returns [newline] : test ( options {k=2; } : COMMA test )* ( COMMA )? ;
    def printlist(self, ):

        retval = self.printlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA155 = None
        COMMA157 = None
        test154 = None

        test156 = None


        COMMA155_tree = None
        COMMA157_tree = None

        try:
            try:
                # kv.g:266:2: ( test ( options {k=2; } : COMMA test )* ( COMMA )? )
                # kv.g:266:6: test ( options {k=2; } : COMMA test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_printlist1406)
                test154 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test154.tree)
                # kv.g:266:11: ( options {k=2; } : COMMA test )*
                while True: #loop51
                    alt51 = 2
                    alt51 = self.dfa51.predict(self.input)
                    if alt51 == 1:
                        # kv.g:266:28: COMMA test
                        pass 
                        COMMA155=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_printlist1417)
                        if self._state.backtracking == 0:

                            COMMA155_tree = self._adaptor.createWithPayload(COMMA155)
                            self._adaptor.addChild(root_0, COMMA155_tree)

                        self._state.following.append(self.FOLLOW_test_in_printlist1419)
                        test156 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test156.tree)


                    else:
                        break #loop51
                # kv.g:266:41: ( COMMA )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == COMMA) :
                    alt52 = 1
                if alt52 == 1:
                    # kv.g:266:42: COMMA
                    pass 
                    COMMA157=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_printlist1424)
                    if self._state.backtracking == 0:

                        COMMA157_tree = self._adaptor.createWithPayload(COMMA157)
                        self._adaptor.addChild(root_0, COMMA157_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "printlist"

    class del_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.del_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "del_stmt"
    # kv.g:268:1: del_stmt : 'del' exprlist ;
    def del_stmt(self, ):

        retval = self.del_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal158 = None
        exprlist159 = None


        string_literal158_tree = None

        try:
            try:
                # kv.g:269:2: ( 'del' exprlist )
                # kv.g:269:6: 'del' exprlist
                pass 
                root_0 = self._adaptor.nil()

                string_literal158=self.match(self.input, 87, self.FOLLOW_87_in_del_stmt1438)
                if self._state.backtracking == 0:

                    string_literal158_tree = self._adaptor.createWithPayload(string_literal158)
                    self._adaptor.addChild(root_0, string_literal158_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_del_stmt1440)
                exprlist159 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist159.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "del_stmt"

    class pass_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.pass_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "pass_stmt"
    # kv.g:271:1: pass_stmt : 'pass' ;
    def pass_stmt(self, ):

        retval = self.pass_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal160 = None

        string_literal160_tree = None

        try:
            try:
                # kv.g:272:2: ( 'pass' )
                # kv.g:272:6: 'pass'
                pass 
                root_0 = self._adaptor.nil()

                string_literal160=self.match(self.input, 88, self.FOLLOW_88_in_pass_stmt1452)
                if self._state.backtracking == 0:

                    string_literal160_tree = self._adaptor.createWithPayload(string_literal160)
                    self._adaptor.addChild(root_0, string_literal160_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pass_stmt"

    class flow_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.flow_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "flow_stmt"
    # kv.g:274:1: flow_stmt : ( break_stmt | continue_stmt | raise_stmt | yield_stmt );
    def flow_stmt(self, ):

        retval = self.flow_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        break_stmt161 = None

        continue_stmt162 = None

        raise_stmt163 = None

        yield_stmt164 = None



        try:
            try:
                # kv.g:275:2: ( break_stmt | continue_stmt | raise_stmt | yield_stmt )
                alt53 = 4
                LA53 = self.input.LA(1)
                if LA53 == 89:
                    alt53 = 1
                elif LA53 == 90:
                    alt53 = 2
                elif LA53 == 91:
                    alt53 = 3
                elif LA53 == 107:
                    alt53 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # kv.g:275:6: break_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_break_stmt_in_flow_stmt1464)
                    break_stmt161 = self.break_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, break_stmt161.tree)


                elif alt53 == 2:
                    # kv.g:276:6: continue_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_continue_stmt_in_flow_stmt1471)
                    continue_stmt162 = self.continue_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, continue_stmt162.tree)


                elif alt53 == 3:
                    # kv.g:278:6: raise_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_raise_stmt_in_flow_stmt1480)
                    raise_stmt163 = self.raise_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, raise_stmt163.tree)


                elif alt53 == 4:
                    # kv.g:279:6: yield_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_yield_stmt_in_flow_stmt1487)
                    yield_stmt164 = self.yield_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_stmt164.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "flow_stmt"

    class break_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.break_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "break_stmt"
    # kv.g:281:1: break_stmt : 'break' ;
    def break_stmt(self, ):

        retval = self.break_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal165 = None

        string_literal165_tree = None

        try:
            try:
                # kv.g:282:2: ( 'break' )
                # kv.g:282:6: 'break'
                pass 
                root_0 = self._adaptor.nil()

                string_literal165=self.match(self.input, 89, self.FOLLOW_89_in_break_stmt1499)
                if self._state.backtracking == 0:

                    string_literal165_tree = self._adaptor.createWithPayload(string_literal165)
                    self._adaptor.addChild(root_0, string_literal165_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "break_stmt"

    class continue_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.continue_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "continue_stmt"
    # kv.g:284:1: continue_stmt : 'continue' ;
    def continue_stmt(self, ):

        retval = self.continue_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal166 = None

        string_literal166_tree = None

        try:
            try:
                # kv.g:285:2: ( 'continue' )
                # kv.g:285:6: 'continue'
                pass 
                root_0 = self._adaptor.nil()

                string_literal166=self.match(self.input, 90, self.FOLLOW_90_in_continue_stmt1511)
                if self._state.backtracking == 0:

                    string_literal166_tree = self._adaptor.createWithPayload(string_literal166)
                    self._adaptor.addChild(root_0, string_literal166_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "continue_stmt"

    class yield_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.yield_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "yield_stmt"
    # kv.g:287:1: yield_stmt : yield_expr ;
    def yield_stmt(self, ):

        retval = self.yield_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        yield_expr167 = None



        try:
            try:
                # kv.g:288:2: ( yield_expr )
                # kv.g:288:4: yield_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_yield_expr_in_yield_stmt1521)
                yield_expr167 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr167.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "yield_stmt"

    class raise_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.raise_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "raise_stmt"
    # kv.g:290:1: raise_stmt : 'raise' ( test ( COMMA test ( COMMA test )? )? )? ;
    def raise_stmt(self, ):

        retval = self.raise_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal168 = None
        COMMA170 = None
        COMMA172 = None
        test169 = None

        test171 = None

        test173 = None


        string_literal168_tree = None
        COMMA170_tree = None
        COMMA172_tree = None

        try:
            try:
                # kv.g:291:2: ( 'raise' ( test ( COMMA test ( COMMA test )? )? )? )
                # kv.g:291:4: 'raise' ( test ( COMMA test ( COMMA test )? )? )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal168=self.match(self.input, 91, self.FOLLOW_91_in_raise_stmt1531)
                if self._state.backtracking == 0:

                    string_literal168_tree = self._adaptor.createWithPayload(string_literal168)
                    self._adaptor.addChild(root_0, string_literal168_tree)

                # kv.g:291:12: ( test ( COMMA test ( COMMA test )? )? )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == WNAME or (PLUS <= LA56_0 <= MINUS) or LA56_0 == NAME or LA56_0 == LPAREN or LA56_0 == NOT or (TILDE <= LA56_0 <= LBRACK) or LA56_0 == LCURLY or (BACKQUOTE <= LA56_0 <= STRING) or LA56_0 == 106) :
                    alt56 = 1
                if alt56 == 1:
                    # kv.g:291:13: test ( COMMA test ( COMMA test )? )?
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_raise_stmt1534)
                    test169 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test169.tree)
                    # kv.g:291:18: ( COMMA test ( COMMA test )? )?
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == COMMA) :
                        alt55 = 1
                    if alt55 == 1:
                        # kv.g:291:19: COMMA test ( COMMA test )?
                        pass 
                        COMMA170=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1537)
                        if self._state.backtracking == 0:

                            COMMA170_tree = self._adaptor.createWithPayload(COMMA170)
                            self._adaptor.addChild(root_0, COMMA170_tree)

                        self._state.following.append(self.FOLLOW_test_in_raise_stmt1539)
                        test171 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test171.tree)
                        # kv.g:291:30: ( COMMA test )?
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == COMMA) :
                            alt54 = 1
                        if alt54 == 1:
                            # kv.g:291:31: COMMA test
                            pass 
                            COMMA172=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1542)
                            if self._state.backtracking == 0:

                                COMMA172_tree = self._adaptor.createWithPayload(COMMA172)
                                self._adaptor.addChild(root_0, COMMA172_tree)

                            self._state.following.append(self.FOLLOW_test_in_raise_stmt1544)
                            test173 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test173.tree)












                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "raise_stmt"

    class exec_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.exec_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "exec_stmt"
    # kv.g:293:1: exec_stmt : 'exec' expr ( 'in' test ( COMMA test )? )? ;
    def exec_stmt(self, ):

        retval = self.exec_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal174 = None
        string_literal176 = None
        COMMA178 = None
        expr175 = None

        test177 = None

        test179 = None


        string_literal174_tree = None
        string_literal176_tree = None
        COMMA178_tree = None

        try:
            try:
                # kv.g:294:2: ( 'exec' expr ( 'in' test ( COMMA test )? )? )
                # kv.g:294:6: 'exec' expr ( 'in' test ( COMMA test )? )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal174=self.match(self.input, 92, self.FOLLOW_92_in_exec_stmt1562)
                if self._state.backtracking == 0:

                    string_literal174_tree = self._adaptor.createWithPayload(string_literal174)
                    self._adaptor.addChild(root_0, string_literal174_tree)

                self._state.following.append(self.FOLLOW_expr_in_exec_stmt1564)
                expr175 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr175.tree)
                # kv.g:294:18: ( 'in' test ( COMMA test )? )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == 93) :
                    alt58 = 1
                if alt58 == 1:
                    # kv.g:294:19: 'in' test ( COMMA test )?
                    pass 
                    string_literal176=self.match(self.input, 93, self.FOLLOW_93_in_exec_stmt1567)
                    if self._state.backtracking == 0:

                        string_literal176_tree = self._adaptor.createWithPayload(string_literal176)
                        self._adaptor.addChild(root_0, string_literal176_tree)

                    self._state.following.append(self.FOLLOW_test_in_exec_stmt1569)
                    test177 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test177.tree)
                    # kv.g:294:29: ( COMMA test )?
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == COMMA) :
                        alt57 = 1
                    if alt57 == 1:
                        # kv.g:294:30: COMMA test
                        pass 
                        COMMA178=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exec_stmt1572)
                        if self._state.backtracking == 0:

                            COMMA178_tree = self._adaptor.createWithPayload(COMMA178)
                            self._adaptor.addChild(root_0, COMMA178_tree)

                        self._state.following.append(self.FOLLOW_test_in_exec_stmt1574)
                        test179 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test179.tree)









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "exec_stmt"

    class assert_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.assert_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "assert_stmt"
    # kv.g:296:1: assert_stmt : 'assert' test ( COMMA test )? ;
    def assert_stmt(self, ):

        retval = self.assert_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal180 = None
        COMMA182 = None
        test181 = None

        test183 = None


        string_literal180_tree = None
        COMMA182_tree = None

        try:
            try:
                # kv.g:297:2: ( 'assert' test ( COMMA test )? )
                # kv.g:297:6: 'assert' test ( COMMA test )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal180=self.match(self.input, 94, self.FOLLOW_94_in_assert_stmt1590)
                if self._state.backtracking == 0:

                    string_literal180_tree = self._adaptor.createWithPayload(string_literal180)
                    self._adaptor.addChild(root_0, string_literal180_tree)

                self._state.following.append(self.FOLLOW_test_in_assert_stmt1592)
                test181 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test181.tree)
                # kv.g:297:20: ( COMMA test )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == COMMA) :
                    alt59 = 1
                if alt59 == 1:
                    # kv.g:297:21: COMMA test
                    pass 
                    COMMA182=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_assert_stmt1595)
                    if self._state.backtracking == 0:

                        COMMA182_tree = self._adaptor.createWithPayload(COMMA182)
                        self._adaptor.addChild(root_0, COMMA182_tree)

                    self._state.following.append(self.FOLLOW_test_in_assert_stmt1597)
                    test183 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test183.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assert_stmt"

    class compound_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.compound_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compound_stmt"
    # kv.g:299:1: compound_stmt : ( if_stmt | while_stmt | for_stmt | try_stmt | with_stmt );
    def compound_stmt(self, ):

        retval = self.compound_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        if_stmt184 = None

        while_stmt185 = None

        for_stmt186 = None

        try_stmt187 = None

        with_stmt188 = None



        try:
            try:
                # kv.g:300:2: ( if_stmt | while_stmt | for_stmt | try_stmt | with_stmt )
                alt60 = 5
                LA60 = self.input.LA(1)
                if LA60 == 95:
                    alt60 = 1
                elif LA60 == 98:
                    alt60 = 2
                elif LA60 == 99:
                    alt60 = 3
                elif LA60 == 100:
                    alt60 = 4
                elif LA60 == 102:
                    alt60 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 60, 0, self.input)

                    raise nvae

                if alt60 == 1:
                    # kv.g:300:6: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_stmt_in_compound_stmt1611)
                    if_stmt184 = self.if_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_stmt184.tree)


                elif alt60 == 2:
                    # kv.g:301:6: while_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_while_stmt_in_compound_stmt1618)
                    while_stmt185 = self.while_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, while_stmt185.tree)


                elif alt60 == 3:
                    # kv.g:302:6: for_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_for_stmt_in_compound_stmt1625)
                    for_stmt186 = self.for_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, for_stmt186.tree)


                elif alt60 == 4:
                    # kv.g:303:6: try_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_try_stmt_in_compound_stmt1632)
                    try_stmt187 = self.try_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, try_stmt187.tree)


                elif alt60 == 5:
                    # kv.g:304:6: with_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_with_stmt_in_compound_stmt1639)
                    with_stmt188 = self.with_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, with_stmt188.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compound_stmt"

    class if_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.if_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "if_stmt"
    # kv.g:309:1: if_stmt : 'if' test COLON suite ( elif_clause )* ( 'else' COLON suite )? ;
    def if_stmt(self, ):

        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal189 = None
        COLON191 = None
        string_literal194 = None
        COLON195 = None
        test190 = None

        suite192 = None

        elif_clause193 = None

        suite196 = None


        string_literal189_tree = None
        COLON191_tree = None
        string_literal194_tree = None
        COLON195_tree = None

        try:
            try:
                # kv.g:310:2: ( 'if' test COLON suite ( elif_clause )* ( 'else' COLON suite )? )
                # kv.g:310:6: 'if' test COLON suite ( elif_clause )* ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal189=self.match(self.input, 95, self.FOLLOW_95_in_if_stmt1656)
                if self._state.backtracking == 0:

                    string_literal189_tree = self._adaptor.createWithPayload(string_literal189)
                    self._adaptor.addChild(root_0, string_literal189_tree)

                self._state.following.append(self.FOLLOW_test_in_if_stmt1658)
                test190 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test190.tree)
                COLON191=self.match(self.input, COLON, self.FOLLOW_COLON_in_if_stmt1660)
                if self._state.backtracking == 0:

                    COLON191_tree = self._adaptor.createWithPayload(COLON191)
                    self._adaptor.addChild(root_0, COLON191_tree)

                self._state.following.append(self.FOLLOW_suite_in_if_stmt1662)
                suite192 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite192.tree)
                # kv.g:310:28: ( elif_clause )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == 97) :
                        alt61 = 1


                    if alt61 == 1:
                        # kv.g:310:28: elif_clause
                        pass 
                        self._state.following.append(self.FOLLOW_elif_clause_in_if_stmt1664)
                        elif_clause193 = self.elif_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, elif_clause193.tree)


                    else:
                        break #loop61
                # kv.g:310:41: ( 'else' COLON suite )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == 96) :
                    alt62 = 1
                if alt62 == 1:
                    # kv.g:310:42: 'else' COLON suite
                    pass 
                    string_literal194=self.match(self.input, 96, self.FOLLOW_96_in_if_stmt1668)
                    if self._state.backtracking == 0:

                        string_literal194_tree = self._adaptor.createWithPayload(string_literal194)
                        self._adaptor.addChild(root_0, string_literal194_tree)

                    COLON195=self.match(self.input, COLON, self.FOLLOW_COLON_in_if_stmt1670)
                    if self._state.backtracking == 0:

                        COLON195_tree = self._adaptor.createWithPayload(COLON195)
                        self._adaptor.addChild(root_0, COLON195_tree)

                    self._state.following.append(self.FOLLOW_suite_in_if_stmt1672)
                    suite196 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite196.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "if_stmt"

    class elif_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.elif_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "elif_clause"
    # kv.g:312:1: elif_clause : 'elif' test COLON suite ;
    def elif_clause(self, ):

        retval = self.elif_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal197 = None
        COLON199 = None
        test198 = None

        suite200 = None


        string_literal197_tree = None
        COLON199_tree = None

        try:
            try:
                # kv.g:313:2: ( 'elif' test COLON suite )
                # kv.g:313:6: 'elif' test COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal197=self.match(self.input, 97, self.FOLLOW_97_in_elif_clause1686)
                if self._state.backtracking == 0:

                    string_literal197_tree = self._adaptor.createWithPayload(string_literal197)
                    self._adaptor.addChild(root_0, string_literal197_tree)

                self._state.following.append(self.FOLLOW_test_in_elif_clause1688)
                test198 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test198.tree)
                COLON199=self.match(self.input, COLON, self.FOLLOW_COLON_in_elif_clause1690)
                if self._state.backtracking == 0:

                    COLON199_tree = self._adaptor.createWithPayload(COLON199)
                    self._adaptor.addChild(root_0, COLON199_tree)

                self._state.following.append(self.FOLLOW_suite_in_elif_clause1692)
                suite200 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite200.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elif_clause"

    class while_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.while_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "while_stmt"
    # kv.g:315:1: while_stmt : 'while' test COLON suite ( 'else' COLON suite )? ;
    def while_stmt(self, ):

        retval = self.while_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal201 = None
        COLON203 = None
        string_literal205 = None
        COLON206 = None
        test202 = None

        suite204 = None

        suite207 = None


        string_literal201_tree = None
        COLON203_tree = None
        string_literal205_tree = None
        COLON206_tree = None

        try:
            try:
                # kv.g:316:2: ( 'while' test COLON suite ( 'else' COLON suite )? )
                # kv.g:316:6: 'while' test COLON suite ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal201=self.match(self.input, 98, self.FOLLOW_98_in_while_stmt1704)
                if self._state.backtracking == 0:

                    string_literal201_tree = self._adaptor.createWithPayload(string_literal201)
                    self._adaptor.addChild(root_0, string_literal201_tree)

                self._state.following.append(self.FOLLOW_test_in_while_stmt1706)
                test202 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test202.tree)
                COLON203=self.match(self.input, COLON, self.FOLLOW_COLON_in_while_stmt1708)
                if self._state.backtracking == 0:

                    COLON203_tree = self._adaptor.createWithPayload(COLON203)
                    self._adaptor.addChild(root_0, COLON203_tree)

                self._state.following.append(self.FOLLOW_suite_in_while_stmt1710)
                suite204 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite204.tree)
                # kv.g:316:31: ( 'else' COLON suite )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == 96) :
                    alt63 = 1
                if alt63 == 1:
                    # kv.g:316:32: 'else' COLON suite
                    pass 
                    string_literal205=self.match(self.input, 96, self.FOLLOW_96_in_while_stmt1713)
                    if self._state.backtracking == 0:

                        string_literal205_tree = self._adaptor.createWithPayload(string_literal205)
                        self._adaptor.addChild(root_0, string_literal205_tree)

                    COLON206=self.match(self.input, COLON, self.FOLLOW_COLON_in_while_stmt1715)
                    if self._state.backtracking == 0:

                        COLON206_tree = self._adaptor.createWithPayload(COLON206)
                        self._adaptor.addChild(root_0, COLON206_tree)

                    self._state.following.append(self.FOLLOW_suite_in_while_stmt1717)
                    suite207 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite207.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "while_stmt"

    class for_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.for_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "for_stmt"
    # kv.g:318:1: for_stmt : 'for' exprlist 'in' testlist COLON suite ( 'else' COLON suite )? ;
    def for_stmt(self, ):

        retval = self.for_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal208 = None
        string_literal210 = None
        COLON212 = None
        string_literal214 = None
        COLON215 = None
        exprlist209 = None

        testlist211 = None

        suite213 = None

        suite216 = None


        string_literal208_tree = None
        string_literal210_tree = None
        COLON212_tree = None
        string_literal214_tree = None
        COLON215_tree = None

        try:
            try:
                # kv.g:319:2: ( 'for' exprlist 'in' testlist COLON suite ( 'else' COLON suite )? )
                # kv.g:319:6: 'for' exprlist 'in' testlist COLON suite ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal208=self.match(self.input, 99, self.FOLLOW_99_in_for_stmt1731)
                if self._state.backtracking == 0:

                    string_literal208_tree = self._adaptor.createWithPayload(string_literal208)
                    self._adaptor.addChild(root_0, string_literal208_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_for_stmt1733)
                exprlist209 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist209.tree)
                string_literal210=self.match(self.input, 93, self.FOLLOW_93_in_for_stmt1735)
                if self._state.backtracking == 0:

                    string_literal210_tree = self._adaptor.createWithPayload(string_literal210)
                    self._adaptor.addChild(root_0, string_literal210_tree)

                self._state.following.append(self.FOLLOW_testlist_in_for_stmt1737)
                testlist211 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist211.tree)
                COLON212=self.match(self.input, COLON, self.FOLLOW_COLON_in_for_stmt1739)
                if self._state.backtracking == 0:

                    COLON212_tree = self._adaptor.createWithPayload(COLON212)
                    self._adaptor.addChild(root_0, COLON212_tree)

                self._state.following.append(self.FOLLOW_suite_in_for_stmt1741)
                suite213 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite213.tree)
                # kv.g:319:47: ( 'else' COLON suite )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == 96) :
                    alt64 = 1
                if alt64 == 1:
                    # kv.g:319:48: 'else' COLON suite
                    pass 
                    string_literal214=self.match(self.input, 96, self.FOLLOW_96_in_for_stmt1744)
                    if self._state.backtracking == 0:

                        string_literal214_tree = self._adaptor.createWithPayload(string_literal214)
                        self._adaptor.addChild(root_0, string_literal214_tree)

                    COLON215=self.match(self.input, COLON, self.FOLLOW_COLON_in_for_stmt1746)
                    if self._state.backtracking == 0:

                        COLON215_tree = self._adaptor.createWithPayload(COLON215)
                        self._adaptor.addChild(root_0, COLON215_tree)

                    self._state.following.append(self.FOLLOW_suite_in_for_stmt1748)
                    suite216 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite216.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "for_stmt"

    class try_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.try_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "try_stmt"
    # kv.g:321:1: try_stmt : 'try' COLON suite ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite ) ;
    def try_stmt(self, ):

        retval = self.try_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal217 = None
        COLON218 = None
        string_literal221 = None
        COLON222 = None
        string_literal224 = None
        COLON225 = None
        string_literal227 = None
        COLON228 = None
        suite219 = None

        except_clause220 = None

        suite223 = None

        suite226 = None

        suite229 = None


        string_literal217_tree = None
        COLON218_tree = None
        string_literal221_tree = None
        COLON222_tree = None
        string_literal224_tree = None
        COLON225_tree = None
        string_literal227_tree = None
        COLON228_tree = None

        try:
            try:
                # kv.g:322:2: ( 'try' COLON suite ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite ) )
                # kv.g:322:6: 'try' COLON suite ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite )
                pass 
                root_0 = self._adaptor.nil()

                string_literal217=self.match(self.input, 100, self.FOLLOW_100_in_try_stmt1762)
                if self._state.backtracking == 0:

                    string_literal217_tree = self._adaptor.createWithPayload(string_literal217)
                    self._adaptor.addChild(root_0, string_literal217_tree)

                COLON218=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1764)
                if self._state.backtracking == 0:

                    COLON218_tree = self._adaptor.createWithPayload(COLON218)
                    self._adaptor.addChild(root_0, COLON218_tree)

                self._state.following.append(self.FOLLOW_suite_in_try_stmt1766)
                suite219 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite219.tree)
                # kv.g:323:4: ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite )
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == 104) :
                    alt68 = 1
                elif (LA68_0 == 101) :
                    alt68 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # kv.g:323:6: ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )?
                    pass 
                    # kv.g:323:6: ( except_clause )+
                    cnt65 = 0
                    while True: #loop65
                        alt65 = 2
                        LA65_0 = self.input.LA(1)

                        if (LA65_0 == 104) :
                            alt65 = 1


                        if alt65 == 1:
                            # kv.g:323:6: except_clause
                            pass 
                            self._state.following.append(self.FOLLOW_except_clause_in_try_stmt1773)
                            except_clause220 = self.except_clause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, except_clause220.tree)


                        else:
                            if cnt65 >= 1:
                                break #loop65

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(65, self.input)
                            raise eee

                        cnt65 += 1
                    # kv.g:323:21: ( 'else' COLON suite )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == 96) :
                        alt66 = 1
                    if alt66 == 1:
                        # kv.g:323:22: 'else' COLON suite
                        pass 
                        string_literal221=self.match(self.input, 96, self.FOLLOW_96_in_try_stmt1777)
                        if self._state.backtracking == 0:

                            string_literal221_tree = self._adaptor.createWithPayload(string_literal221)
                            self._adaptor.addChild(root_0, string_literal221_tree)

                        COLON222=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1779)
                        if self._state.backtracking == 0:

                            COLON222_tree = self._adaptor.createWithPayload(COLON222)
                            self._adaptor.addChild(root_0, COLON222_tree)

                        self._state.following.append(self.FOLLOW_suite_in_try_stmt1781)
                        suite223 = self.suite()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, suite223.tree)



                    # kv.g:323:43: ( 'finally' COLON suite )?
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == 101) :
                        alt67 = 1
                    if alt67 == 1:
                        # kv.g:323:44: 'finally' COLON suite
                        pass 
                        string_literal224=self.match(self.input, 101, self.FOLLOW_101_in_try_stmt1786)
                        if self._state.backtracking == 0:

                            string_literal224_tree = self._adaptor.createWithPayload(string_literal224)
                            self._adaptor.addChild(root_0, string_literal224_tree)

                        COLON225=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1788)
                        if self._state.backtracking == 0:

                            COLON225_tree = self._adaptor.createWithPayload(COLON225)
                            self._adaptor.addChild(root_0, COLON225_tree)

                        self._state.following.append(self.FOLLOW_suite_in_try_stmt1790)
                        suite226 = self.suite()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, suite226.tree)





                elif alt68 == 2:
                    # kv.g:324:6: 'finally' COLON suite
                    pass 
                    string_literal227=self.match(self.input, 101, self.FOLLOW_101_in_try_stmt1799)
                    if self._state.backtracking == 0:

                        string_literal227_tree = self._adaptor.createWithPayload(string_literal227)
                        self._adaptor.addChild(root_0, string_literal227_tree)

                    COLON228=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1801)
                    if self._state.backtracking == 0:

                        COLON228_tree = self._adaptor.createWithPayload(COLON228)
                        self._adaptor.addChild(root_0, COLON228_tree)

                    self._state.following.append(self.FOLLOW_suite_in_try_stmt1803)
                    suite229 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite229.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "try_stmt"

    class with_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.with_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "with_stmt"
    # kv.g:326:1: with_stmt : 'with' test ( with_var )? COLON suite ;
    def with_stmt(self, ):

        retval = self.with_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal230 = None
        COLON233 = None
        test231 = None

        with_var232 = None

        suite234 = None


        string_literal230_tree = None
        COLON233_tree = None

        try:
            try:
                # kv.g:327:2: ( 'with' test ( with_var )? COLON suite )
                # kv.g:327:6: 'with' test ( with_var )? COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal230=self.match(self.input, 102, self.FOLLOW_102_in_with_stmt1817)
                if self._state.backtracking == 0:

                    string_literal230_tree = self._adaptor.createWithPayload(string_literal230)
                    self._adaptor.addChild(root_0, string_literal230_tree)

                self._state.following.append(self.FOLLOW_test_in_with_stmt1819)
                test231 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test231.tree)
                # kv.g:327:18: ( with_var )?
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if (LA69_0 == WNAME or LA69_0 == NAME or LA69_0 == 103) :
                    alt69 = 1
                if alt69 == 1:
                    # kv.g:327:19: with_var
                    pass 
                    self._state.following.append(self.FOLLOW_with_var_in_with_stmt1822)
                    with_var232 = self.with_var()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, with_var232.tree)



                COLON233=self.match(self.input, COLON, self.FOLLOW_COLON_in_with_stmt1826)
                if self._state.backtracking == 0:

                    COLON233_tree = self._adaptor.createWithPayload(COLON233)
                    self._adaptor.addChild(root_0, COLON233_tree)

                self._state.following.append(self.FOLLOW_suite_in_with_stmt1828)
                suite234 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite234.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "with_stmt"

    class with_var_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.with_var_return, self).__init__()

            self.tree = None




    # $ANTLR start "with_var"
    # kv.g:329:1: with_var : ( 'as' | identifier ) expr ;
    def with_var(self, ):

        retval = self.with_var_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal235 = None
        identifier236 = None

        expr237 = None


        string_literal235_tree = None

        try:
            try:
                # kv.g:330:2: ( ( 'as' | identifier ) expr )
                # kv.g:330:6: ( 'as' | identifier ) expr
                pass 
                root_0 = self._adaptor.nil()

                # kv.g:330:6: ( 'as' | identifier )
                alt70 = 2
                LA70_0 = self.input.LA(1)

                if (LA70_0 == 103) :
                    alt70 = 1
                elif (LA70_0 == WNAME or LA70_0 == NAME) :
                    alt70 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # kv.g:330:7: 'as'
                    pass 
                    string_literal235=self.match(self.input, 103, self.FOLLOW_103_in_with_var1841)
                    if self._state.backtracking == 0:

                        string_literal235_tree = self._adaptor.createWithPayload(string_literal235)
                        self._adaptor.addChild(root_0, string_literal235_tree)



                elif alt70 == 2:
                    # kv.g:330:14: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_with_var1845)
                    identifier236 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier236.tree)



                self._state.following.append(self.FOLLOW_expr_in_with_var1848)
                expr237 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr237.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "with_var"

    class except_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.except_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "except_clause"
    # kv.g:332:1: except_clause : 'except' ( test ( COMMA test )? )? COLON suite ;
    def except_clause(self, ):

        retval = self.except_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal238 = None
        COMMA240 = None
        COLON242 = None
        test239 = None

        test241 = None

        suite243 = None


        string_literal238_tree = None
        COMMA240_tree = None
        COLON242_tree = None

        try:
            try:
                # kv.g:333:2: ( 'except' ( test ( COMMA test )? )? COLON suite )
                # kv.g:333:6: 'except' ( test ( COMMA test )? )? COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal238=self.match(self.input, 104, self.FOLLOW_104_in_except_clause1860)
                if self._state.backtracking == 0:

                    string_literal238_tree = self._adaptor.createWithPayload(string_literal238)
                    self._adaptor.addChild(root_0, string_literal238_tree)

                # kv.g:333:15: ( test ( COMMA test )? )?
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if (LA72_0 == WNAME or (PLUS <= LA72_0 <= MINUS) or LA72_0 == NAME or LA72_0 == LPAREN or LA72_0 == NOT or (TILDE <= LA72_0 <= LBRACK) or LA72_0 == LCURLY or (BACKQUOTE <= LA72_0 <= STRING) or LA72_0 == 106) :
                    alt72 = 1
                if alt72 == 1:
                    # kv.g:333:16: test ( COMMA test )?
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_except_clause1863)
                    test239 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test239.tree)
                    # kv.g:333:21: ( COMMA test )?
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == COMMA) :
                        alt71 = 1
                    if alt71 == 1:
                        # kv.g:333:22: COMMA test
                        pass 
                        COMMA240=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_except_clause1866)
                        if self._state.backtracking == 0:

                            COMMA240_tree = self._adaptor.createWithPayload(COMMA240)
                            self._adaptor.addChild(root_0, COMMA240_tree)

                        self._state.following.append(self.FOLLOW_test_in_except_clause1868)
                        test241 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test241.tree)






                COLON242=self.match(self.input, COLON, self.FOLLOW_COLON_in_except_clause1874)
                if self._state.backtracking == 0:

                    COLON242_tree = self._adaptor.createWithPayload(COLON242)
                    self._adaptor.addChild(root_0, COLON242_tree)

                self._state.following.append(self.FOLLOW_suite_in_except_clause1876)
                suite243 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite243.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "except_clause"

    class suite_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.suite_return, self).__init__()

            self.tree = None




    # $ANTLR start "suite"
    # kv.g:335:1: suite : ( simple_stmt | NEWLINE INDENT ( stmt )+ DEDENT );
    def suite(self, ):

        retval = self.suite_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE245 = None
        INDENT246 = None
        DEDENT248 = None
        simple_stmt244 = None

        stmt247 = None


        NEWLINE245_tree = None
        INDENT246_tree = None
        DEDENT248_tree = None

        try:
            try:
                # kv.g:336:2: ( simple_stmt | NEWLINE INDENT ( stmt )+ DEDENT )
                alt74 = 2
                LA74_0 = self.input.LA(1)

                if (LA74_0 == WNAME or (PLUS <= LA74_0 <= MINUS) or LA74_0 == NAME or LA74_0 == LPAREN or LA74_0 == NOT or (TILDE <= LA74_0 <= LBRACK) or LA74_0 == LCURLY or (BACKQUOTE <= LA74_0 <= STRING) or (86 <= LA74_0 <= 92) or LA74_0 == 94 or (106 <= LA74_0 <= 107)) :
                    alt74 = 1
                elif (LA74_0 == NEWLINE) :
                    alt74 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 74, 0, self.input)

                    raise nvae

                if alt74 == 1:
                    # kv.g:336:6: simple_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_stmt_in_suite1888)
                    simple_stmt244 = self.simple_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_stmt244.tree)


                elif alt74 == 2:
                    # kv.g:337:6: NEWLINE INDENT ( stmt )+ DEDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    NEWLINE245=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_suite1895)
                    if self._state.backtracking == 0:

                        NEWLINE245_tree = self._adaptor.createWithPayload(NEWLINE245)
                        self._adaptor.addChild(root_0, NEWLINE245_tree)

                    INDENT246=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_suite1897)
                    if self._state.backtracking == 0:

                        INDENT246_tree = self._adaptor.createWithPayload(INDENT246)
                        self._adaptor.addChild(root_0, INDENT246_tree)

                    # kv.g:337:21: ( stmt )+
                    cnt73 = 0
                    while True: #loop73
                        alt73 = 2
                        LA73_0 = self.input.LA(1)

                        if (LA73_0 == NEWLINE or (COMMENTTEXT <= LA73_0 <= WNAME) or (CANVAS <= LA73_0 <= NAME)) :
                            alt73 = 1


                        if alt73 == 1:
                            # kv.g:337:22: stmt
                            pass 
                            self._state.following.append(self.FOLLOW_stmt_in_suite1900)
                            stmt247 = self.stmt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, stmt247.tree)


                        else:
                            if cnt73 >= 1:
                                break #loop73

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(73, self.input)
                            raise eee

                        cnt73 += 1
                    DEDENT248=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_suite1904)
                    if self._state.backtracking == 0:

                        DEDENT248_tree = self._adaptor.createWithPayload(DEDENT248)
                        self._adaptor.addChild(root_0, DEDENT248_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "suite"

    class test_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.test_return, self).__init__()

            self.tree = None




    # $ANTLR start "test"
    # kv.g:340:1: test : ( or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )? | lambdef );
    def test(self, ):

        retval = self.test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal250 = None
        string_literal252 = None
        or_test249 = None

        or_test251 = None

        test253 = None

        lambdef254 = None


        string_literal250_tree = None
        string_literal252_tree = None

        try:
            try:
                # kv.g:341:2: ( or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )? | lambdef )
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if (LA76_0 == WNAME or (PLUS <= LA76_0 <= MINUS) or LA76_0 == NAME or LA76_0 == LPAREN or LA76_0 == NOT or (TILDE <= LA76_0 <= LBRACK) or LA76_0 == LCURLY or (BACKQUOTE <= LA76_0 <= STRING)) :
                    alt76 = 1
                elif (LA76_0 == 106) :
                    alt76 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 76, 0, self.input)

                    raise nvae

                if alt76 == 1:
                    # kv.g:341:4: or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_or_test_in_test1915)
                    or_test249 = self.or_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, or_test249.tree)
                    # kv.g:342:3: ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    alt75 = 2
                    alt75 = self.dfa75.predict(self.input)
                    if alt75 == 1:
                        # kv.g:342:5: ( 'if' or_test 'else' )=> 'if' or_test 'else' test
                        pass 
                        string_literal250=self.match(self.input, 95, self.FOLLOW_95_in_test1933)
                        if self._state.backtracking == 0:

                            string_literal250_tree = self._adaptor.createWithPayload(string_literal250)
                            self._adaptor.addChild(root_0, string_literal250_tree)

                        self._state.following.append(self.FOLLOW_or_test_in_test1935)
                        or_test251 = self.or_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, or_test251.tree)
                        string_literal252=self.match(self.input, 96, self.FOLLOW_96_in_test1937)
                        if self._state.backtracking == 0:

                            string_literal252_tree = self._adaptor.createWithPayload(string_literal252)
                            self._adaptor.addChild(root_0, string_literal252_tree)

                        self._state.following.append(self.FOLLOW_test_in_test1939)
                        test253 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test253.tree)





                elif alt76 == 2:
                    # kv.g:343:4: lambdef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_lambdef_in_test1947)
                    lambdef254 = self.lambdef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, lambdef254.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "test"

    class or_test_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.or_test_return, self).__init__()

            self.tree = None




    # $ANTLR start "or_test"
    # kv.g:345:1: or_test : and_test ( OR and_test )* ;
    def or_test(self, ):

        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR256 = None
        and_test255 = None

        and_test257 = None


        OR256_tree = None

        try:
            try:
                # kv.g:346:2: ( and_test ( OR and_test )* )
                # kv.g:346:4: and_test ( OR and_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_test_in_or_test1957)
                and_test255 = self.and_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_test255.tree)
                # kv.g:346:13: ( OR and_test )*
                while True: #loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == OR) :
                        alt77 = 1


                    if alt77 == 1:
                        # kv.g:346:14: OR and_test
                        pass 
                        OR256=self.match(self.input, OR, self.FOLLOW_OR_in_or_test1960)
                        if self._state.backtracking == 0:

                            OR256_tree = self._adaptor.createWithPayload(OR256)
                            self._adaptor.addChild(root_0, OR256_tree)

                        self._state.following.append(self.FOLLOW_and_test_in_or_test1962)
                        and_test257 = self.and_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_test257.tree)


                    else:
                        break #loop77



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "or_test"

    class and_test_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.and_test_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_test"
    # kv.g:348:1: and_test : not_test ( AND not_test )* ;
    def and_test(self, ):

        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND259 = None
        not_test258 = None

        not_test260 = None


        AND259_tree = None

        try:
            try:
                # kv.g:349:2: ( not_test ( AND not_test )* )
                # kv.g:349:4: not_test ( AND not_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_not_test_in_and_test1974)
                not_test258 = self.not_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, not_test258.tree)
                # kv.g:349:13: ( AND not_test )*
                while True: #loop78
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if (LA78_0 == AND) :
                        alt78 = 1


                    if alt78 == 1:
                        # kv.g:349:14: AND not_test
                        pass 
                        AND259=self.match(self.input, AND, self.FOLLOW_AND_in_and_test1977)
                        if self._state.backtracking == 0:

                            AND259_tree = self._adaptor.createWithPayload(AND259)
                            self._adaptor.addChild(root_0, AND259_tree)

                        self._state.following.append(self.FOLLOW_not_test_in_and_test1979)
                        not_test260 = self.not_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, not_test260.tree)


                    else:
                        break #loop78



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "and_test"

    class not_test_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.not_test_return, self).__init__()

            self.tree = None




    # $ANTLR start "not_test"
    # kv.g:351:1: not_test : ( NOT not_test | comparison );
    def not_test(self, ):

        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT261 = None
        not_test262 = None

        comparison263 = None


        NOT261_tree = None

        try:
            try:
                # kv.g:352:2: ( NOT not_test | comparison )
                alt79 = 2
                LA79_0 = self.input.LA(1)

                if (LA79_0 == NOT) :
                    alt79 = 1
                elif (LA79_0 == WNAME or (PLUS <= LA79_0 <= MINUS) or LA79_0 == NAME or LA79_0 == LPAREN or (TILDE <= LA79_0 <= LBRACK) or LA79_0 == LCURLY or (BACKQUOTE <= LA79_0 <= STRING)) :
                    alt79 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 79, 0, self.input)

                    raise nvae

                if alt79 == 1:
                    # kv.g:352:4: NOT not_test
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT261=self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1991)
                    if self._state.backtracking == 0:

                        NOT261_tree = self._adaptor.createWithPayload(NOT261)
                        self._adaptor.addChild(root_0, NOT261_tree)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1993)
                    not_test262 = self.not_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, not_test262.tree)


                elif alt79 == 2:
                    # kv.g:353:4: comparison
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comparison_in_not_test1998)
                    comparison263 = self.comparison()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comparison263.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "not_test"

    class comparison_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.comparison_return, self).__init__()

            self.tree = None




    # $ANTLR start "comparison"
    # kv.g:355:1: comparison : expr ( comp_op expr )* ;
    def comparison(self, ):

        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        root_0 = None

        expr264 = None

        comp_op265 = None

        expr266 = None



        try:
            try:
                # kv.g:356:2: ( expr ( comp_op expr )* )
                # kv.g:356:4: expr ( comp_op expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_comparison2008)
                expr264 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr264.tree)
                # kv.g:356:9: ( comp_op expr )*
                while True: #loop80
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if ((NOT <= LA80_0 <= NOTEQUAL) or LA80_0 == 93 or LA80_0 == 105) :
                        alt80 = 1


                    if alt80 == 1:
                        # kv.g:356:10: comp_op expr
                        pass 
                        self._state.following.append(self.FOLLOW_comp_op_in_comparison2011)
                        comp_op265 = self.comp_op()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, comp_op265.tree)
                        self._state.following.append(self.FOLLOW_expr_in_comparison2013)
                        expr266 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr266.tree)


                    else:
                        break #loop80



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "comparison"

    class comp_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.comp_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "comp_op"
    # kv.g:358:1: comp_op : ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | NOT 'in' | 'is' | NOT 'is' );
    def comp_op(self, ):

        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LESS267 = None
        GREATER268 = None
        EQUAL269 = None
        GREATEREQUAL270 = None
        LESSEQUAL271 = None
        ALT_NOTEQUAL272 = None
        NOTEQUAL273 = None
        string_literal274 = None
        NOT275 = None
        string_literal276 = None
        string_literal277 = None
        NOT278 = None
        string_literal279 = None

        LESS267_tree = None
        GREATER268_tree = None
        EQUAL269_tree = None
        GREATEREQUAL270_tree = None
        LESSEQUAL271_tree = None
        ALT_NOTEQUAL272_tree = None
        NOTEQUAL273_tree = None
        string_literal274_tree = None
        NOT275_tree = None
        string_literal276_tree = None
        string_literal277_tree = None
        NOT278_tree = None
        string_literal279_tree = None

        try:
            try:
                # kv.g:359:2: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | NOT 'in' | 'is' | NOT 'is' )
                alt81 = 11
                alt81 = self.dfa81.predict(self.input)
                if alt81 == 1:
                    # kv.g:359:4: LESS
                    pass 
                    root_0 = self._adaptor.nil()

                    LESS267=self.match(self.input, LESS, self.FOLLOW_LESS_in_comp_op2025)
                    if self._state.backtracking == 0:

                        LESS267_tree = self._adaptor.createWithPayload(LESS267)
                        self._adaptor.addChild(root_0, LESS267_tree)



                elif alt81 == 2:
                    # kv.g:359:11: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER268=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comp_op2029)
                    if self._state.backtracking == 0:

                        GREATER268_tree = self._adaptor.createWithPayload(GREATER268)
                        self._adaptor.addChild(root_0, GREATER268_tree)



                elif alt81 == 3:
                    # kv.g:359:21: EQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    EQUAL269=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comp_op2033)
                    if self._state.backtracking == 0:

                        EQUAL269_tree = self._adaptor.createWithPayload(EQUAL269)
                        self._adaptor.addChild(root_0, EQUAL269_tree)



                elif alt81 == 4:
                    # kv.g:359:29: GREATEREQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATEREQUAL270=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comp_op2037)
                    if self._state.backtracking == 0:

                        GREATEREQUAL270_tree = self._adaptor.createWithPayload(GREATEREQUAL270)
                        self._adaptor.addChild(root_0, GREATEREQUAL270_tree)



                elif alt81 == 5:
                    # kv.g:359:44: LESSEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    LESSEQUAL271=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comp_op2041)
                    if self._state.backtracking == 0:

                        LESSEQUAL271_tree = self._adaptor.createWithPayload(LESSEQUAL271)
                        self._adaptor.addChild(root_0, LESSEQUAL271_tree)



                elif alt81 == 6:
                    # kv.g:359:56: ALT_NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    ALT_NOTEQUAL272=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comp_op2045)
                    if self._state.backtracking == 0:

                        ALT_NOTEQUAL272_tree = self._adaptor.createWithPayload(ALT_NOTEQUAL272)
                        self._adaptor.addChild(root_0, ALT_NOTEQUAL272_tree)



                elif alt81 == 7:
                    # kv.g:359:71: NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    NOTEQUAL273=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comp_op2049)
                    if self._state.backtracking == 0:

                        NOTEQUAL273_tree = self._adaptor.createWithPayload(NOTEQUAL273)
                        self._adaptor.addChild(root_0, NOTEQUAL273_tree)



                elif alt81 == 8:
                    # kv.g:360:4: 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal274=self.match(self.input, 93, self.FOLLOW_93_in_comp_op2054)
                    if self._state.backtracking == 0:

                        string_literal274_tree = self._adaptor.createWithPayload(string_literal274)
                        self._adaptor.addChild(root_0, string_literal274_tree)



                elif alt81 == 9:
                    # kv.g:360:11: NOT 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT275=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2058)
                    if self._state.backtracking == 0:

                        NOT275_tree = self._adaptor.createWithPayload(NOT275)
                        self._adaptor.addChild(root_0, NOT275_tree)

                    string_literal276=self.match(self.input, 93, self.FOLLOW_93_in_comp_op2060)
                    if self._state.backtracking == 0:

                        string_literal276_tree = self._adaptor.createWithPayload(string_literal276)
                        self._adaptor.addChild(root_0, string_literal276_tree)



                elif alt81 == 10:
                    # kv.g:360:22: 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal277=self.match(self.input, 105, self.FOLLOW_105_in_comp_op2064)
                    if self._state.backtracking == 0:

                        string_literal277_tree = self._adaptor.createWithPayload(string_literal277)
                        self._adaptor.addChild(root_0, string_literal277_tree)



                elif alt81 == 11:
                    # kv.g:360:29: NOT 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT278=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2068)
                    if self._state.backtracking == 0:

                        NOT278_tree = self._adaptor.createWithPayload(NOT278)
                        self._adaptor.addChild(root_0, NOT278_tree)

                    string_literal279=self.match(self.input, 105, self.FOLLOW_105_in_comp_op2070)
                    if self._state.backtracking == 0:

                        string_literal279_tree = self._adaptor.createWithPayload(string_literal279)
                        self._adaptor.addChild(root_0, string_literal279_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "comp_op"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # kv.g:362:1: expr : xor_expr ( VBAR xor_expr )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VBAR281 = None
        xor_expr280 = None

        xor_expr282 = None


        VBAR281_tree = None

        try:
            try:
                # kv.g:363:2: ( xor_expr ( VBAR xor_expr )* )
                # kv.g:363:4: xor_expr ( VBAR xor_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_xor_expr_in_expr2080)
                xor_expr280 = self.xor_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, xor_expr280.tree)
                # kv.g:363:13: ( VBAR xor_expr )*
                while True: #loop82
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if (LA82_0 == VBAR) :
                        alt82 = 1


                    if alt82 == 1:
                        # kv.g:363:14: VBAR xor_expr
                        pass 
                        VBAR281=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_expr2083)
                        if self._state.backtracking == 0:

                            VBAR281_tree = self._adaptor.createWithPayload(VBAR281)
                            self._adaptor.addChild(root_0, VBAR281_tree)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr2085)
                        xor_expr282 = self.xor_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, xor_expr282.tree)


                    else:
                        break #loop82



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class xor_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.xor_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "xor_expr"
    # kv.g:365:1: xor_expr : and_expr ( CIRCUMFLEX and_expr )* ;
    def xor_expr(self, ):

        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CIRCUMFLEX284 = None
        and_expr283 = None

        and_expr285 = None


        CIRCUMFLEX284_tree = None

        try:
            try:
                # kv.g:366:2: ( and_expr ( CIRCUMFLEX and_expr )* )
                # kv.g:366:4: and_expr ( CIRCUMFLEX and_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr2097)
                and_expr283 = self.and_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expr283.tree)
                # kv.g:366:13: ( CIRCUMFLEX and_expr )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == CIRCUMFLEX) :
                        alt83 = 1


                    if alt83 == 1:
                        # kv.g:366:14: CIRCUMFLEX and_expr
                        pass 
                        CIRCUMFLEX284=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_xor_expr2100)
                        if self._state.backtracking == 0:

                            CIRCUMFLEX284_tree = self._adaptor.createWithPayload(CIRCUMFLEX284)
                            self._adaptor.addChild(root_0, CIRCUMFLEX284_tree)

                        self._state.following.append(self.FOLLOW_and_expr_in_xor_expr2102)
                        and_expr285 = self.and_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_expr285.tree)


                    else:
                        break #loop83



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "xor_expr"

    class and_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.and_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_expr"
    # kv.g:368:1: and_expr : shift_expr ( AMPER shift_expr )* ;
    def and_expr(self, ):

        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AMPER287 = None
        shift_expr286 = None

        shift_expr288 = None


        AMPER287_tree = None

        try:
            try:
                # kv.g:369:2: ( shift_expr ( AMPER shift_expr )* )
                # kv.g:369:4: shift_expr ( AMPER shift_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr2114)
                shift_expr286 = self.shift_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, shift_expr286.tree)
                # kv.g:369:15: ( AMPER shift_expr )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == AMPER) :
                        alt84 = 1


                    if alt84 == 1:
                        # kv.g:369:16: AMPER shift_expr
                        pass 
                        AMPER287=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_and_expr2117)
                        if self._state.backtracking == 0:

                            AMPER287_tree = self._adaptor.createWithPayload(AMPER287)
                            self._adaptor.addChild(root_0, AMPER287_tree)

                        self._state.following.append(self.FOLLOW_shift_expr_in_and_expr2119)
                        shift_expr288 = self.shift_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, shift_expr288.tree)


                    else:
                        break #loop84



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "and_expr"

    class shift_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.shift_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "shift_expr"
    # kv.g:371:1: shift_expr : arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )* ;
    def shift_expr(self, ):

        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set290 = None
        arith_expr289 = None

        arith_expr291 = None


        set290_tree = None

        try:
            try:
                # kv.g:372:2: ( arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )* )
                # kv.g:372:4: arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr2131)
                arith_expr289 = self.arith_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arith_expr289.tree)
                # kv.g:372:15: ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == RIGHTSHIFT or LA85_0 == LEFTSHIFT) :
                        alt85 = 1


                    if alt85 == 1:
                        # kv.g:372:16: ( LEFTSHIFT | RIGHTSHIFT ) arith_expr
                        pass 
                        set290 = self.input.LT(1)
                        if self.input.LA(1) == RIGHTSHIFT or self.input.LA(1) == LEFTSHIFT:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set290))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr2140)
                        arith_expr291 = self.arith_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arith_expr291.tree)


                    else:
                        break #loop85



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "shift_expr"

    class arith_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.arith_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arith_expr"
    # kv.g:374:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(self, ):

        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set293 = None
        term292 = None

        term294 = None


        set293_tree = None

        try:
            try:
                # kv.g:375:2: ( term ( ( PLUS | MINUS ) term )* )
                # kv.g:375:4: term ( ( PLUS | MINUS ) term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_arith_expr2152)
                term292 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term292.tree)
                # kv.g:375:9: ( ( PLUS | MINUS ) term )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if ((PLUS <= LA86_0 <= MINUS)) :
                        alt86 = 1


                    if alt86 == 1:
                        # kv.g:375:10: ( PLUS | MINUS ) term
                        pass 
                        set293 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set293))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_arith_expr2161)
                        term294 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term294.tree)


                    else:
                        break #loop86



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arith_expr"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # kv.g:377:1: term : factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )* ;
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set296 = None
        factor295 = None

        factor297 = None


        set296_tree = None

        try:
            try:
                # kv.g:378:2: ( factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )* )
                # kv.g:378:4: factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_factor_in_term2173)
                factor295 = self.factor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, factor295.tree)
                # kv.g:378:11: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == STAR or (SLASH <= LA87_0 <= DOUBLESLASH)) :
                        alt87 = 1


                    if alt87 == 1:
                        # kv.g:378:12: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor
                        pass 
                        set296 = self.input.LT(1)
                        if self.input.LA(1) == STAR or (SLASH <= self.input.LA(1) <= DOUBLESLASH):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set296))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term2193)
                        factor297 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, factor297.tree)


                    else:
                        break #loop87



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class factor_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.factor_return, self).__init__()

            self.tree = None




    # $ANTLR start "factor"
    # kv.g:380:1: factor : ( PLUS factor | MINUS factor | TILDE factor | power );
    def factor(self, ):

        retval = self.factor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS298 = None
        MINUS300 = None
        TILDE302 = None
        factor299 = None

        factor301 = None

        factor303 = None

        power304 = None


        PLUS298_tree = None
        MINUS300_tree = None
        TILDE302_tree = None

        try:
            try:
                # kv.g:381:2: ( PLUS factor | MINUS factor | TILDE factor | power )
                alt88 = 4
                LA88 = self.input.LA(1)
                if LA88 == PLUS:
                    alt88 = 1
                elif LA88 == MINUS:
                    alt88 = 2
                elif LA88 == TILDE:
                    alt88 = 3
                elif LA88 == WNAME or LA88 == NAME or LA88 == LPAREN or LA88 == LBRACK or LA88 == LCURLY or LA88 == BACKQUOTE or LA88 == NONE or LA88 == INT or LA88 == LONGINT or LA88 == FLOAT or LA88 == COMPLEX or LA88 == STRING:
                    alt88 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae

                if alt88 == 1:
                    # kv.g:381:4: PLUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS298=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor2205)
                    if self._state.backtracking == 0:

                        PLUS298_tree = self._adaptor.createWithPayload(PLUS298)
                        self._adaptor.addChild(root_0, PLUS298_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2207)
                    factor299 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor299.tree)


                elif alt88 == 2:
                    # kv.g:381:18: MINUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    MINUS300=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor2211)
                    if self._state.backtracking == 0:

                        MINUS300_tree = self._adaptor.createWithPayload(MINUS300)
                        self._adaptor.addChild(root_0, MINUS300_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2213)
                    factor301 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor301.tree)


                elif alt88 == 3:
                    # kv.g:381:33: TILDE factor
                    pass 
                    root_0 = self._adaptor.nil()

                    TILDE302=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor2217)
                    if self._state.backtracking == 0:

                        TILDE302_tree = self._adaptor.createWithPayload(TILDE302)
                        self._adaptor.addChild(root_0, TILDE302_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2219)
                    factor303 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor303.tree)


                elif alt88 == 4:
                    # kv.g:381:48: power
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_power_in_factor2223)
                    power304 = self.power()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, power304.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "factor"

    class power_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.power_return, self).__init__()

            self.tree = None




    # $ANTLR start "power"
    # kv.g:383:1: power : atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? ;
    def power(self, ):

        retval = self.power_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOUBLESTAR307 = None
        atom305 = None

        trailer306 = None

        factor308 = None


        DOUBLESTAR307_tree = None

        try:
            try:
                # kv.g:384:2: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # kv.g:384:4: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_in_power2233)
                atom305 = self.atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, atom305.tree)
                # kv.g:384:9: ( trailer )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LPAREN or LA89_0 == LBRACK or LA89_0 == DOT) :
                        alt89 = 1


                    if alt89 == 1:
                        # kv.g:384:10: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power2236)
                        trailer306 = self.trailer()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, trailer306.tree)


                    else:
                        break #loop89
                # kv.g:384:20: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt90 = 2
                LA90_0 = self.input.LA(1)

                if (LA90_0 == DOUBLESTAR) :
                    alt90 = 1
                if alt90 == 1:
                    # kv.g:384:44: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR307=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power2248)
                    if self._state.backtracking == 0:

                        DOUBLESTAR307_tree = self._adaptor.createWithPayload(DOUBLESTAR307)
                        self._adaptor.addChild(root_0, DOUBLESTAR307_tree)

                    self._state.following.append(self.FOLLOW_factor_in_power2250)
                    factor308 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor308.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "power"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "atom"
    # kv.g:386:1: atom : ( LPAREN ( yield_expr | testlist_gexp )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | BACKQUOTE testlist BACKQUOTE | identifier | NONE | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN309 = None
        RPAREN312 = None
        LBRACK313 = None
        RBRACK315 = None
        LCURLY316 = None
        RCURLY318 = None
        BACKQUOTE319 = None
        BACKQUOTE321 = None
        NONE323 = None
        INT324 = None
        LONGINT325 = None
        FLOAT326 = None
        COMPLEX327 = None
        STRING328 = None
        yield_expr310 = None

        testlist_gexp311 = None

        listmaker314 = None

        dictmaker317 = None

        testlist320 = None

        identifier322 = None


        LPAREN309_tree = None
        RPAREN312_tree = None
        LBRACK313_tree = None
        RBRACK315_tree = None
        LCURLY316_tree = None
        RCURLY318_tree = None
        BACKQUOTE319_tree = None
        BACKQUOTE321_tree = None
        NONE323_tree = None
        INT324_tree = None
        LONGINT325_tree = None
        FLOAT326_tree = None
        COMPLEX327_tree = None
        STRING328_tree = None

        try:
            try:
                # kv.g:387:2: ( LPAREN ( yield_expr | testlist_gexp )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | BACKQUOTE testlist BACKQUOTE | identifier | NONE | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
                alt95 = 11
                LA95 = self.input.LA(1)
                if LA95 == LPAREN:
                    alt95 = 1
                elif LA95 == LBRACK:
                    alt95 = 2
                elif LA95 == LCURLY:
                    alt95 = 3
                elif LA95 == BACKQUOTE:
                    alt95 = 4
                elif LA95 == WNAME or LA95 == NAME:
                    alt95 = 5
                elif LA95 == NONE:
                    alt95 = 6
                elif LA95 == INT:
                    alt95 = 7
                elif LA95 == LONGINT:
                    alt95 = 8
                elif LA95 == FLOAT:
                    alt95 = 9
                elif LA95 == COMPLEX:
                    alt95 = 10
                elif LA95 == STRING:
                    alt95 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 95, 0, self.input)

                    raise nvae

                if alt95 == 1:
                    # kv.g:387:4: LPAREN ( yield_expr | testlist_gexp )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN309=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2262)
                    if self._state.backtracking == 0:

                        LPAREN309_tree = self._adaptor.createWithPayload(LPAREN309)
                        self._adaptor.addChild(root_0, LPAREN309_tree)

                    # kv.g:387:11: ( yield_expr | testlist_gexp )?
                    alt91 = 3
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == 107) :
                        alt91 = 1
                    elif (LA91_0 == WNAME or (PLUS <= LA91_0 <= MINUS) or LA91_0 == NAME or LA91_0 == LPAREN or LA91_0 == NOT or (TILDE <= LA91_0 <= LBRACK) or LA91_0 == LCURLY or (BACKQUOTE <= LA91_0 <= STRING) or LA91_0 == 106) :
                        alt91 = 2
                    if alt91 == 1:
                        # kv.g:387:13: yield_expr
                        pass 
                        self._state.following.append(self.FOLLOW_yield_expr_in_atom2266)
                        yield_expr310 = self.yield_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, yield_expr310.tree)


                    elif alt91 == 2:
                        # kv.g:387:26: testlist_gexp
                        pass 
                        self._state.following.append(self.FOLLOW_testlist_gexp_in_atom2270)
                        testlist_gexp311 = self.testlist_gexp()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, testlist_gexp311.tree)



                    RPAREN312=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2275)
                    if self._state.backtracking == 0:

                        RPAREN312_tree = self._adaptor.createWithPayload(RPAREN312)
                        self._adaptor.addChild(root_0, RPAREN312_tree)



                elif alt95 == 2:
                    # kv.g:388:4: LBRACK ( listmaker )? RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK313=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom2280)
                    if self._state.backtracking == 0:

                        LBRACK313_tree = self._adaptor.createWithPayload(LBRACK313)
                        self._adaptor.addChild(root_0, LBRACK313_tree)

                    # kv.g:388:11: ( listmaker )?
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == WNAME or (PLUS <= LA92_0 <= MINUS) or LA92_0 == NAME or LA92_0 == LPAREN or LA92_0 == NOT or (TILDE <= LA92_0 <= LBRACK) or LA92_0 == LCURLY or (BACKQUOTE <= LA92_0 <= STRING) or LA92_0 == 106) :
                        alt92 = 1
                    if alt92 == 1:
                        # kv.g:388:12: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom2283)
                        listmaker314 = self.listmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, listmaker314.tree)



                    RBRACK315=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom2287)
                    if self._state.backtracking == 0:

                        RBRACK315_tree = self._adaptor.createWithPayload(RBRACK315)
                        self._adaptor.addChild(root_0, RBRACK315_tree)



                elif alt95 == 3:
                    # kv.g:389:4: LCURLY ( dictmaker )? RCURLY
                    pass 
                    root_0 = self._adaptor.nil()

                    LCURLY316=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom2292)
                    if self._state.backtracking == 0:

                        LCURLY316_tree = self._adaptor.createWithPayload(LCURLY316)
                        self._adaptor.addChild(root_0, LCURLY316_tree)

                    # kv.g:389:11: ( dictmaker )?
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == WNAME or (PLUS <= LA93_0 <= MINUS) or LA93_0 == NAME or LA93_0 == LPAREN or LA93_0 == NOT or (TILDE <= LA93_0 <= LBRACK) or LA93_0 == LCURLY or (BACKQUOTE <= LA93_0 <= STRING) or LA93_0 == 106) :
                        alt93 = 1
                    if alt93 == 1:
                        # kv.g:389:12: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom2295)
                        dictmaker317 = self.dictmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, dictmaker317.tree)



                    RCURLY318=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom2299)
                    if self._state.backtracking == 0:

                        RCURLY318_tree = self._adaptor.createWithPayload(RCURLY318)
                        self._adaptor.addChild(root_0, RCURLY318_tree)



                elif alt95 == 4:
                    # kv.g:390:4: BACKQUOTE testlist BACKQUOTE
                    pass 
                    root_0 = self._adaptor.nil()

                    BACKQUOTE319=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom2304)
                    if self._state.backtracking == 0:

                        BACKQUOTE319_tree = self._adaptor.createWithPayload(BACKQUOTE319)
                        self._adaptor.addChild(root_0, BACKQUOTE319_tree)

                    self._state.following.append(self.FOLLOW_testlist_in_atom2306)
                    testlist320 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist320.tree)
                    BACKQUOTE321=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom2308)
                    if self._state.backtracking == 0:

                        BACKQUOTE321_tree = self._adaptor.createWithPayload(BACKQUOTE321)
                        self._adaptor.addChild(root_0, BACKQUOTE321_tree)



                elif alt95 == 5:
                    # kv.g:391:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_atom2313)
                    identifier322 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier322.tree)


                elif alt95 == 6:
                    # kv.g:392:6: NONE
                    pass 
                    root_0 = self._adaptor.nil()

                    NONE323=self.match(self.input, NONE, self.FOLLOW_NONE_in_atom2320)
                    if self._state.backtracking == 0:

                        NONE323_tree = self._adaptor.createWithPayload(NONE323)
                        self._adaptor.addChild(root_0, NONE323_tree)



                elif alt95 == 7:
                    # kv.g:393:4: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT324=self.match(self.input, INT, self.FOLLOW_INT_in_atom2325)
                    if self._state.backtracking == 0:

                        INT324_tree = self._adaptor.createWithPayload(INT324)
                        self._adaptor.addChild(root_0, INT324_tree)



                elif alt95 == 8:
                    # kv.g:394:4: LONGINT
                    pass 
                    root_0 = self._adaptor.nil()

                    LONGINT325=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom2330)
                    if self._state.backtracking == 0:

                        LONGINT325_tree = self._adaptor.createWithPayload(LONGINT325)
                        self._adaptor.addChild(root_0, LONGINT325_tree)



                elif alt95 == 9:
                    # kv.g:395:4: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()

                    FLOAT326=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom2335)
                    if self._state.backtracking == 0:

                        FLOAT326_tree = self._adaptor.createWithPayload(FLOAT326)
                        self._adaptor.addChild(root_0, FLOAT326_tree)



                elif alt95 == 10:
                    # kv.g:396:4: COMPLEX
                    pass 
                    root_0 = self._adaptor.nil()

                    COMPLEX327=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom2340)
                    if self._state.backtracking == 0:

                        COMPLEX327_tree = self._adaptor.createWithPayload(COMPLEX327)
                        self._adaptor.addChild(root_0, COMPLEX327_tree)



                elif alt95 == 11:
                    # kv.g:397:4: ( STRING )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:397:4: ( STRING )+
                    cnt94 = 0
                    while True: #loop94
                        alt94 = 2
                        LA94_0 = self.input.LA(1)

                        if (LA94_0 == STRING) :
                            alt94 = 1


                        if alt94 == 1:
                            # kv.g:397:5: STRING
                            pass 
                            STRING328=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom2346)
                            if self._state.backtracking == 0:

                                STRING328_tree = self._adaptor.createWithPayload(STRING328)
                                self._adaptor.addChild(root_0, STRING328_tree)



                        else:
                            if cnt94 >= 1:
                                break #loop94

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(94, self.input)
                            raise eee

                        cnt94 += 1


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atom"

    class listmaker_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.listmaker_return, self).__init__()

            self.tree = None




    # $ANTLR start "listmaker"
    # kv.g:399:1: listmaker : test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )? ;
    def listmaker(self, ):

        retval = self.listmaker_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA331 = None
        COMMA333 = None
        test329 = None

        list_for330 = None

        test332 = None


        COMMA331_tree = None
        COMMA333_tree = None

        try:
            try:
                # kv.g:400:2: ( test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )? )
                # kv.g:400:4: test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_listmaker2358)
                test329 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test329.tree)
                # kv.g:400:9: ( list_for | ( options {greedy=true; } : COMMA test )* )
                alt97 = 2
                LA97_0 = self.input.LA(1)

                if (LA97_0 == 99) :
                    alt97 = 1
                elif (LA97_0 == COMMA or LA97_0 == RBRACK) :
                    alt97 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 97, 0, self.input)

                    raise nvae

                if alt97 == 1:
                    # kv.g:400:10: list_for
                    pass 
                    self._state.following.append(self.FOLLOW_list_for_in_listmaker2361)
                    list_for330 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for330.tree)


                elif alt97 == 2:
                    # kv.g:400:21: ( options {greedy=true; } : COMMA test )*
                    pass 
                    # kv.g:400:21: ( options {greedy=true; } : COMMA test )*
                    while True: #loop96
                        alt96 = 2
                        LA96_0 = self.input.LA(1)

                        if (LA96_0 == COMMA) :
                            LA96_1 = self.input.LA(2)

                            if (LA96_1 == WNAME or (PLUS <= LA96_1 <= MINUS) or LA96_1 == NAME or LA96_1 == LPAREN or LA96_1 == NOT or (TILDE <= LA96_1 <= LBRACK) or LA96_1 == LCURLY or (BACKQUOTE <= LA96_1 <= STRING) or LA96_1 == 106) :
                                alt96 = 1




                        if alt96 == 1:
                            # kv.g:400:45: COMMA test
                            pass 
                            COMMA331=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2373)
                            if self._state.backtracking == 0:

                                COMMA331_tree = self._adaptor.createWithPayload(COMMA331)
                                self._adaptor.addChild(root_0, COMMA331_tree)

                            self._state.following.append(self.FOLLOW_test_in_listmaker2375)
                            test332 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test332.tree)


                        else:
                            break #loop96



                # kv.g:400:60: ( COMMA )?
                alt98 = 2
                LA98_0 = self.input.LA(1)

                if (LA98_0 == COMMA) :
                    alt98 = 1
                if alt98 == 1:
                    # kv.g:400:61: COMMA
                    pass 
                    COMMA333=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2382)
                    if self._state.backtracking == 0:

                        COMMA333_tree = self._adaptor.createWithPayload(COMMA333)
                        self._adaptor.addChild(root_0, COMMA333_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "listmaker"

    class testlist_gexp_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.testlist_gexp_return, self).__init__()

            self.tree = None




    # $ANTLR start "testlist_gexp"
    # kv.g:402:1: testlist_gexp : test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for ) ;
    def testlist_gexp(self, ):

        retval = self.testlist_gexp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA335 = None
        COMMA337 = None
        test334 = None

        test336 = None

        gen_for338 = None


        COMMA335_tree = None
        COMMA337_tree = None

        try:
            try:
                # kv.g:403:2: ( test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for ) )
                # kv.g:403:4: test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist_gexp2394)
                test334 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test334.tree)
                # kv.g:403:9: ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                alt101 = 2
                LA101_0 = self.input.LA(1)

                if (LA101_0 == COMMA or LA101_0 == RPAREN) :
                    alt101 = 1
                elif (LA101_0 == 99) :
                    alt101 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 101, 0, self.input)

                    raise nvae

                if alt101 == 1:
                    # kv.g:403:11: ( options {k=2; } : COMMA test )* ( COMMA )?
                    pass 
                    # kv.g:403:11: ( options {k=2; } : COMMA test )*
                    while True: #loop99
                        alt99 = 2
                        alt99 = self.dfa99.predict(self.input)
                        if alt99 == 1:
                            # kv.g:403:28: COMMA test
                            pass 
                            COMMA335=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp2407)
                            if self._state.backtracking == 0:

                                COMMA335_tree = self._adaptor.createWithPayload(COMMA335)
                                self._adaptor.addChild(root_0, COMMA335_tree)

                            self._state.following.append(self.FOLLOW_test_in_testlist_gexp2409)
                            test336 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test336.tree)


                        else:
                            break #loop99
                    # kv.g:403:41: ( COMMA )?
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == COMMA) :
                        alt100 = 1
                    if alt100 == 1:
                        # kv.g:403:42: COMMA
                        pass 
                        COMMA337=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp2414)
                        if self._state.backtracking == 0:

                            COMMA337_tree = self._adaptor.createWithPayload(COMMA337)
                            self._adaptor.addChild(root_0, COMMA337_tree)






                elif alt101 == 2:
                    # kv.g:403:52: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_testlist_gexp2420)
                    gen_for338 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for338.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "testlist_gexp"

    class lambdef_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.lambdef_return, self).__init__()

            self.tree = None




    # $ANTLR start "lambdef"
    # kv.g:405:1: lambdef : 'lambda' ( varargslist )? COLON test ;
    def lambdef(self, ):

        retval = self.lambdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal339 = None
        COLON341 = None
        varargslist340 = None

        test342 = None


        string_literal339_tree = None
        COLON341_tree = None

        try:
            try:
                # kv.g:406:2: ( 'lambda' ( varargslist )? COLON test )
                # kv.g:406:4: 'lambda' ( varargslist )? COLON test
                pass 
                root_0 = self._adaptor.nil()

                string_literal339=self.match(self.input, 106, self.FOLLOW_106_in_lambdef2432)
                if self._state.backtracking == 0:

                    string_literal339_tree = self._adaptor.createWithPayload(string_literal339)
                    self._adaptor.addChild(root_0, string_literal339_tree)

                # kv.g:406:13: ( varargslist )?
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if (LA102_0 == WNAME or LA102_0 == NAME or (STAR <= LA102_0 <= DOUBLESTAR) or LA102_0 == LPAREN) :
                    alt102 = 1
                if alt102 == 1:
                    # kv.g:406:14: varargslist
                    pass 
                    self._state.following.append(self.FOLLOW_varargslist_in_lambdef2435)
                    varargslist340 = self.varargslist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, varargslist340.tree)



                COLON341=self.match(self.input, COLON, self.FOLLOW_COLON_in_lambdef2439)
                if self._state.backtracking == 0:

                    COLON341_tree = self._adaptor.createWithPayload(COLON341)
                    self._adaptor.addChild(root_0, COLON341_tree)

                self._state.following.append(self.FOLLOW_test_in_lambdef2441)
                test342 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test342.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "lambdef"

    class trailer_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.trailer_return, self).__init__()

            self.tree = None




    # $ANTLR start "trailer"
    # kv.g:408:1: trailer : ( LPAREN ( arglist )? RPAREN | LBRACK subscriptlist RBRACK | DOT identifier );
    def trailer(self, ):

        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN343 = None
        RPAREN345 = None
        LBRACK346 = None
        RBRACK348 = None
        DOT349 = None
        arglist344 = None

        subscriptlist347 = None

        identifier350 = None


        LPAREN343_tree = None
        RPAREN345_tree = None
        LBRACK346_tree = None
        RBRACK348_tree = None
        DOT349_tree = None

        try:
            try:
                # kv.g:409:2: ( LPAREN ( arglist )? RPAREN | LBRACK subscriptlist RBRACK | DOT identifier )
                alt104 = 3
                LA104 = self.input.LA(1)
                if LA104 == LPAREN:
                    alt104 = 1
                elif LA104 == LBRACK:
                    alt104 = 2
                elif LA104 == DOT:
                    alt104 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 104, 0, self.input)

                    raise nvae

                if alt104 == 1:
                    # kv.g:409:4: LPAREN ( arglist )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN343=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer2451)
                    if self._state.backtracking == 0:

                        LPAREN343_tree = self._adaptor.createWithPayload(LPAREN343)
                        self._adaptor.addChild(root_0, LPAREN343_tree)

                    # kv.g:409:11: ( arglist )?
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == WNAME or (PLUS <= LA103_0 <= MINUS) or LA103_0 == NAME or (STAR <= LA103_0 <= DOUBLESTAR) or LA103_0 == LPAREN or LA103_0 == NOT or (TILDE <= LA103_0 <= LBRACK) or LA103_0 == LCURLY or (BACKQUOTE <= LA103_0 <= STRING) or LA103_0 == 106) :
                        alt103 = 1
                    if alt103 == 1:
                        # kv.g:409:12: arglist
                        pass 
                        self._state.following.append(self.FOLLOW_arglist_in_trailer2454)
                        arglist344 = self.arglist()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arglist344.tree)



                    RPAREN345=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer2458)
                    if self._state.backtracking == 0:

                        RPAREN345_tree = self._adaptor.createWithPayload(RPAREN345)
                        self._adaptor.addChild(root_0, RPAREN345_tree)



                elif alt104 == 2:
                    # kv.g:410:4: LBRACK subscriptlist RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK346=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer2463)
                    if self._state.backtracking == 0:

                        LBRACK346_tree = self._adaptor.createWithPayload(LBRACK346)
                        self._adaptor.addChild(root_0, LBRACK346_tree)

                    self._state.following.append(self.FOLLOW_subscriptlist_in_trailer2465)
                    subscriptlist347 = self.subscriptlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, subscriptlist347.tree)
                    RBRACK348=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer2467)
                    if self._state.backtracking == 0:

                        RBRACK348_tree = self._adaptor.createWithPayload(RBRACK348)
                        self._adaptor.addChild(root_0, RBRACK348_tree)



                elif alt104 == 3:
                    # kv.g:411:4: DOT identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT349=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2472)
                    if self._state.backtracking == 0:

                        DOT349_tree = self._adaptor.createWithPayload(DOT349)
                        self._adaptor.addChild(root_0, DOT349_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_trailer2474)
                    identifier350 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier350.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "trailer"

    class subscriptlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.subscriptlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "subscriptlist"
    # kv.g:413:1: subscriptlist : subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )? ;
    def subscriptlist(self, ):

        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA352 = None
        COMMA354 = None
        subscript351 = None

        subscript353 = None


        COMMA352_tree = None
        COMMA354_tree = None

        try:
            try:
                # kv.g:414:2: ( subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )? )
                # kv.g:414:4: subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_subscript_in_subscriptlist2484)
                subscript351 = self.subscript()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, subscript351.tree)
                # kv.g:414:14: ( options {greedy=true; } : COMMA subscript )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == COMMA) :
                        LA105_1 = self.input.LA(2)

                        if ((WNAME <= LA105_1 <= COLON) or (PLUS <= LA105_1 <= MINUS) or LA105_1 == NAME or LA105_1 == LPAREN or LA105_1 == NOT or (TILDE <= LA105_1 <= LBRACK) or LA105_1 == LCURLY or (BACKQUOTE <= LA105_1 <= DOT) or LA105_1 == 106) :
                            alt105 = 1




                    if alt105 == 1:
                        # kv.g:414:38: COMMA subscript
                        pass 
                        COMMA352=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2494)
                        if self._state.backtracking == 0:

                            COMMA352_tree = self._adaptor.createWithPayload(COMMA352)
                            self._adaptor.addChild(root_0, COMMA352_tree)

                        self._state.following.append(self.FOLLOW_subscript_in_subscriptlist2496)
                        subscript353 = self.subscript()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, subscript353.tree)


                    else:
                        break #loop105
                # kv.g:414:56: ( COMMA )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == COMMA) :
                    alt106 = 1
                if alt106 == 1:
                    # kv.g:414:57: COMMA
                    pass 
                    COMMA354=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2501)
                    if self._state.backtracking == 0:

                        COMMA354_tree = self._adaptor.createWithPayload(COMMA354)
                        self._adaptor.addChild(root_0, COMMA354_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "subscriptlist"

    class subscript_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.subscript_return, self).__init__()

            self.tree = None




    # $ANTLR start "subscript"
    # kv.g:416:1: subscript : ( DOT DOT DOT | test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript(self, ):

        retval = self.subscript_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT355 = None
        DOT356 = None
        DOT357 = None
        COLON359 = None
        COLON362 = None
        test358 = None

        test360 = None

        sliceop361 = None

        test363 = None

        sliceop364 = None


        DOT355_tree = None
        DOT356_tree = None
        DOT357_tree = None
        COLON359_tree = None
        COLON362_tree = None

        try:
            try:
                # kv.g:417:2: ( DOT DOT DOT | test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt112 = 3
                LA112 = self.input.LA(1)
                if LA112 == DOT:
                    alt112 = 1
                elif LA112 == WNAME or LA112 == PLUS or LA112 == MINUS or LA112 == NAME or LA112 == LPAREN or LA112 == NOT or LA112 == TILDE or LA112 == LBRACK or LA112 == LCURLY or LA112 == BACKQUOTE or LA112 == NONE or LA112 == INT or LA112 == LONGINT or LA112 == FLOAT or LA112 == COMPLEX or LA112 == STRING or LA112 == 106:
                    alt112 = 2
                elif LA112 == COLON:
                    alt112 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 112, 0, self.input)

                    raise nvae

                if alt112 == 1:
                    # kv.g:417:4: DOT DOT DOT
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT355=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2513)
                    if self._state.backtracking == 0:

                        DOT355_tree = self._adaptor.createWithPayload(DOT355)
                        self._adaptor.addChild(root_0, DOT355_tree)

                    DOT356=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2515)
                    if self._state.backtracking == 0:

                        DOT356_tree = self._adaptor.createWithPayload(DOT356)
                        self._adaptor.addChild(root_0, DOT356_tree)

                    DOT357=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2517)
                    if self._state.backtracking == 0:

                        DOT357_tree = self._adaptor.createWithPayload(DOT357)
                        self._adaptor.addChild(root_0, DOT357_tree)



                elif alt112 == 2:
                    # kv.g:418:4: test ( COLON ( test )? ( sliceop )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_test_in_subscript2522)
                    test358 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test358.tree)
                    # kv.g:418:9: ( COLON ( test )? ( sliceop )? )?
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == COLON) :
                        alt109 = 1
                    if alt109 == 1:
                        # kv.g:418:10: COLON ( test )? ( sliceop )?
                        pass 
                        COLON359=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript2525)
                        if self._state.backtracking == 0:

                            COLON359_tree = self._adaptor.createWithPayload(COLON359)
                            self._adaptor.addChild(root_0, COLON359_tree)

                        # kv.g:418:16: ( test )?
                        alt107 = 2
                        LA107_0 = self.input.LA(1)

                        if (LA107_0 == WNAME or (PLUS <= LA107_0 <= MINUS) or LA107_0 == NAME or LA107_0 == LPAREN or LA107_0 == NOT or (TILDE <= LA107_0 <= LBRACK) or LA107_0 == LCURLY or (BACKQUOTE <= LA107_0 <= STRING) or LA107_0 == 106) :
                            alt107 = 1
                        if alt107 == 1:
                            # kv.g:418:17: test
                            pass 
                            self._state.following.append(self.FOLLOW_test_in_subscript2528)
                            test360 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test360.tree)



                        # kv.g:418:24: ( sliceop )?
                        alt108 = 2
                        LA108_0 = self.input.LA(1)

                        if (LA108_0 == COLON) :
                            alt108 = 1
                        if alt108 == 1:
                            # kv.g:418:25: sliceop
                            pass 
                            self._state.following.append(self.FOLLOW_sliceop_in_subscript2533)
                            sliceop361 = self.sliceop()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, sliceop361.tree)








                elif alt112 == 3:
                    # kv.g:419:4: COLON ( test )? ( sliceop )?
                    pass 
                    root_0 = self._adaptor.nil()

                    COLON362=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript2542)
                    if self._state.backtracking == 0:

                        COLON362_tree = self._adaptor.createWithPayload(COLON362)
                        self._adaptor.addChild(root_0, COLON362_tree)

                    # kv.g:419:10: ( test )?
                    alt110 = 2
                    LA110_0 = self.input.LA(1)

                    if (LA110_0 == WNAME or (PLUS <= LA110_0 <= MINUS) or LA110_0 == NAME or LA110_0 == LPAREN or LA110_0 == NOT or (TILDE <= LA110_0 <= LBRACK) or LA110_0 == LCURLY or (BACKQUOTE <= LA110_0 <= STRING) or LA110_0 == 106) :
                        alt110 = 1
                    if alt110 == 1:
                        # kv.g:419:11: test
                        pass 
                        self._state.following.append(self.FOLLOW_test_in_subscript2545)
                        test363 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test363.tree)



                    # kv.g:419:18: ( sliceop )?
                    alt111 = 2
                    LA111_0 = self.input.LA(1)

                    if (LA111_0 == COLON) :
                        alt111 = 1
                    if alt111 == 1:
                        # kv.g:419:19: sliceop
                        pass 
                        self._state.following.append(self.FOLLOW_sliceop_in_subscript2550)
                        sliceop364 = self.sliceop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sliceop364.tree)





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "subscript"

    class sliceop_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.sliceop_return, self).__init__()

            self.tree = None




    # $ANTLR start "sliceop"
    # kv.g:421:1: sliceop : COLON ( test )? ;
    def sliceop(self, ):

        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON365 = None
        test366 = None


        COLON365_tree = None

        try:
            try:
                # kv.g:422:2: ( COLON ( test )? )
                # kv.g:422:4: COLON ( test )?
                pass 
                root_0 = self._adaptor.nil()

                COLON365=self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop2562)
                if self._state.backtracking == 0:

                    COLON365_tree = self._adaptor.createWithPayload(COLON365)
                    self._adaptor.addChild(root_0, COLON365_tree)

                # kv.g:422:10: ( test )?
                alt113 = 2
                LA113_0 = self.input.LA(1)

                if (LA113_0 == WNAME or (PLUS <= LA113_0 <= MINUS) or LA113_0 == NAME or LA113_0 == LPAREN or LA113_0 == NOT or (TILDE <= LA113_0 <= LBRACK) or LA113_0 == LCURLY or (BACKQUOTE <= LA113_0 <= STRING) or LA113_0 == 106) :
                    alt113 = 1
                if alt113 == 1:
                    # kv.g:422:11: test
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_sliceop2565)
                    test366 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test366.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sliceop"

    class exprlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.exprlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "exprlist"
    # kv.g:424:1: exprlist : expr ( options {k=2; } : COMMA expr )* ( COMMA )? ;
    def exprlist(self, ):

        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA368 = None
        COMMA370 = None
        expr367 = None

        expr369 = None


        COMMA368_tree = None
        COMMA370_tree = None

        try:
            try:
                # kv.g:425:2: ( expr ( options {k=2; } : COMMA expr )* ( COMMA )? )
                # kv.g:425:4: expr ( options {k=2; } : COMMA expr )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_exprlist2577)
                expr367 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr367.tree)
                # kv.g:425:9: ( options {k=2; } : COMMA expr )*
                while True: #loop114
                    alt114 = 2
                    alt114 = self.dfa114.predict(self.input)
                    if alt114 == 1:
                        # kv.g:425:26: COMMA expr
                        pass 
                        COMMA368=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2588)
                        if self._state.backtracking == 0:

                            COMMA368_tree = self._adaptor.createWithPayload(COMMA368)
                            self._adaptor.addChild(root_0, COMMA368_tree)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist2590)
                        expr369 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr369.tree)


                    else:
                        break #loop114
                # kv.g:425:39: ( COMMA )?
                alt115 = 2
                LA115_0 = self.input.LA(1)

                if (LA115_0 == COMMA) :
                    alt115 = 1
                if alt115 == 1:
                    # kv.g:425:40: COMMA
                    pass 
                    COMMA370=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2595)
                    if self._state.backtracking == 0:

                        COMMA370_tree = self._adaptor.createWithPayload(COMMA370)
                        self._adaptor.addChild(root_0, COMMA370_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "exprlist"

    class testlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.testlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "testlist"
    # kv.g:427:1: testlist : test ( options {k=2; } : COMMA test )* ( COMMA )? ;
    def testlist(self, ):

        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA372 = None
        COMMA374 = None
        test371 = None

        test373 = None


        COMMA372_tree = None
        COMMA374_tree = None

        try:
            try:
                # kv.g:428:2: ( test ( options {k=2; } : COMMA test )* ( COMMA )? )
                # kv.g:428:4: test ( options {k=2; } : COMMA test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist2607)
                test371 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test371.tree)
                # kv.g:428:9: ( options {k=2; } : COMMA test )*
                while True: #loop116
                    alt116 = 2
                    alt116 = self.dfa116.predict(self.input)
                    if alt116 == 1:
                        # kv.g:428:26: COMMA test
                        pass 
                        COMMA372=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2618)
                        if self._state.backtracking == 0:

                            COMMA372_tree = self._adaptor.createWithPayload(COMMA372)
                            self._adaptor.addChild(root_0, COMMA372_tree)

                        self._state.following.append(self.FOLLOW_test_in_testlist2620)
                        test373 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test373.tree)


                    else:
                        break #loop116
                # kv.g:428:39: ( COMMA )?
                alt117 = 2
                LA117_0 = self.input.LA(1)

                if (LA117_0 == COMMA) :
                    alt117 = 1
                if alt117 == 1:
                    # kv.g:428:40: COMMA
                    pass 
                    COMMA374=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2625)
                    if self._state.backtracking == 0:

                        COMMA374_tree = self._adaptor.createWithPayload(COMMA374)
                        self._adaptor.addChild(root_0, COMMA374_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "testlist"

    class dictmaker_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.dictmaker_return, self).__init__()

            self.tree = None




    # $ANTLR start "dictmaker"
    # kv.g:430:1: dictmaker : test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )? ;
    def dictmaker(self, ):

        retval = self.dictmaker_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON376 = None
        COMMA378 = None
        COLON380 = None
        COMMA382 = None
        test375 = None

        test377 = None

        test379 = None

        test381 = None


        COLON376_tree = None
        COMMA378_tree = None
        COLON380_tree = None
        COMMA382_tree = None

        try:
            try:
                # kv.g:431:2: ( test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )? )
                # kv.g:431:4: test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_dictmaker2637)
                test375 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test375.tree)
                COLON376=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2639)
                if self._state.backtracking == 0:

                    COLON376_tree = self._adaptor.createWithPayload(COLON376)
                    self._adaptor.addChild(root_0, COLON376_tree)

                self._state.following.append(self.FOLLOW_test_in_dictmaker2641)
                test377 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test377.tree)
                # kv.g:431:20: ( options {k=2; } : COMMA test COLON test )*
                while True: #loop118
                    alt118 = 2
                    alt118 = self.dfa118.predict(self.input)
                    if alt118 == 1:
                        # kv.g:431:37: COMMA test COLON test
                        pass 
                        COMMA378=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2652)
                        if self._state.backtracking == 0:

                            COMMA378_tree = self._adaptor.createWithPayload(COMMA378)
                            self._adaptor.addChild(root_0, COMMA378_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2654)
                        test379 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test379.tree)
                        COLON380=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2656)
                        if self._state.backtracking == 0:

                            COLON380_tree = self._adaptor.createWithPayload(COLON380)
                            self._adaptor.addChild(root_0, COLON380_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2658)
                        test381 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test381.tree)


                    else:
                        break #loop118
                # kv.g:431:61: ( COMMA )?
                alt119 = 2
                LA119_0 = self.input.LA(1)

                if (LA119_0 == COMMA) :
                    alt119 = 1
                if alt119 == 1:
                    # kv.g:431:62: COMMA
                    pass 
                    COMMA382=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2663)
                    if self._state.backtracking == 0:

                        COMMA382_tree = self._adaptor.createWithPayload(COMMA382)
                        self._adaptor.addChild(root_0, COMMA382_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "dictmaker"

    class arglist_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.arglist_return, self).__init__()

            self.tree = None




    # $ANTLR start "arglist"
    # kv.g:433:1: arglist : ( argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )? | STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test );
    def arglist(self, ):

        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA384 = None
        COMMA386 = None
        STAR387 = None
        COMMA389 = None
        DOUBLESTAR390 = None
        DOUBLESTAR392 = None
        STAR394 = None
        COMMA396 = None
        DOUBLESTAR397 = None
        DOUBLESTAR399 = None
        argument383 = None

        argument385 = None

        test388 = None

        test391 = None

        test393 = None

        test395 = None

        test398 = None

        test400 = None


        COMMA384_tree = None
        COMMA386_tree = None
        STAR387_tree = None
        COMMA389_tree = None
        DOUBLESTAR390_tree = None
        DOUBLESTAR392_tree = None
        STAR394_tree = None
        COMMA396_tree = None
        DOUBLESTAR397_tree = None
        DOUBLESTAR399_tree = None

        try:
            try:
                # kv.g:434:2: ( argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )? | STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )
                alt125 = 3
                LA125 = self.input.LA(1)
                if LA125 == WNAME or LA125 == PLUS or LA125 == MINUS or LA125 == NAME or LA125 == LPAREN or LA125 == NOT or LA125 == TILDE or LA125 == LBRACK or LA125 == LCURLY or LA125 == BACKQUOTE or LA125 == NONE or LA125 == INT or LA125 == LONGINT or LA125 == FLOAT or LA125 == COMPLEX or LA125 == STRING or LA125 == 106:
                    alt125 = 1
                elif LA125 == STAR:
                    alt125 = 2
                elif LA125 == DOUBLESTAR:
                    alt125 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 125, 0, self.input)

                    raise nvae

                if alt125 == 1:
                    # kv.g:434:4: argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_argument_in_arglist2675)
                    argument383 = self.argument()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, argument383.tree)
                    # kv.g:434:13: ( COMMA argument )*
                    while True: #loop120
                        alt120 = 2
                        LA120_0 = self.input.LA(1)

                        if (LA120_0 == COMMA) :
                            LA120_1 = self.input.LA(2)

                            if (LA120_1 == WNAME or (PLUS <= LA120_1 <= MINUS) or LA120_1 == NAME or LA120_1 == LPAREN or LA120_1 == NOT or (TILDE <= LA120_1 <= LBRACK) or LA120_1 == LCURLY or (BACKQUOTE <= LA120_1 <= STRING) or LA120_1 == 106) :
                                alt120 = 1




                        if alt120 == 1:
                            # kv.g:434:14: COMMA argument
                            pass 
                            COMMA384=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2678)
                            if self._state.backtracking == 0:

                                COMMA384_tree = self._adaptor.createWithPayload(COMMA384)
                                self._adaptor.addChild(root_0, COMMA384_tree)

                            self._state.following.append(self.FOLLOW_argument_in_arglist2680)
                            argument385 = self.argument()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, argument385.tree)


                        else:
                            break #loop120
                    # kv.g:434:31: ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    alt123 = 2
                    LA123_0 = self.input.LA(1)

                    if (LA123_0 == COMMA) :
                        alt123 = 1
                    if alt123 == 1:
                        # kv.g:434:33: COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        pass 
                        COMMA386=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2686)
                        if self._state.backtracking == 0:

                            COMMA386_tree = self._adaptor.createWithPayload(COMMA386)
                            self._adaptor.addChild(root_0, COMMA386_tree)

                        # kv.g:434:39: ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        alt122 = 3
                        LA122_0 = self.input.LA(1)

                        if (LA122_0 == STAR) :
                            alt122 = 1
                        elif (LA122_0 == DOUBLESTAR) :
                            alt122 = 2
                        if alt122 == 1:
                            # kv.g:434:41: STAR test ( COMMA DOUBLESTAR test )?
                            pass 
                            STAR387=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2690)
                            if self._state.backtracking == 0:

                                STAR387_tree = self._adaptor.createWithPayload(STAR387)
                                self._adaptor.addChild(root_0, STAR387_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2692)
                            test388 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test388.tree)
                            # kv.g:434:51: ( COMMA DOUBLESTAR test )?
                            alt121 = 2
                            LA121_0 = self.input.LA(1)

                            if (LA121_0 == COMMA) :
                                alt121 = 1
                            if alt121 == 1:
                                # kv.g:434:52: COMMA DOUBLESTAR test
                                pass 
                                COMMA389=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2695)
                                if self._state.backtracking == 0:

                                    COMMA389_tree = self._adaptor.createWithPayload(COMMA389)
                                    self._adaptor.addChild(root_0, COMMA389_tree)

                                DOUBLESTAR390=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2697)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR390_tree = self._adaptor.createWithPayload(DOUBLESTAR390)
                                    self._adaptor.addChild(root_0, DOUBLESTAR390_tree)

                                self._state.following.append(self.FOLLOW_test_in_arglist2699)
                                test391 = self.test()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, test391.tree)





                        elif alt122 == 2:
                            # kv.g:434:78: DOUBLESTAR test
                            pass 
                            DOUBLESTAR392=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2705)
                            if self._state.backtracking == 0:

                                DOUBLESTAR392_tree = self._adaptor.createWithPayload(DOUBLESTAR392)
                                self._adaptor.addChild(root_0, DOUBLESTAR392_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2707)
                            test393 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test393.tree)








                elif alt125 == 2:
                    # kv.g:435:4: STAR test ( COMMA DOUBLESTAR test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR394=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2718)
                    if self._state.backtracking == 0:

                        STAR394_tree = self._adaptor.createWithPayload(STAR394)
                        self._adaptor.addChild(root_0, STAR394_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2720)
                    test395 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test395.tree)
                    # kv.g:435:14: ( COMMA DOUBLESTAR test )?
                    alt124 = 2
                    LA124_0 = self.input.LA(1)

                    if (LA124_0 == COMMA) :
                        alt124 = 1
                    if alt124 == 1:
                        # kv.g:435:15: COMMA DOUBLESTAR test
                        pass 
                        COMMA396=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2723)
                        if self._state.backtracking == 0:

                            COMMA396_tree = self._adaptor.createWithPayload(COMMA396)
                            self._adaptor.addChild(root_0, COMMA396_tree)

                        DOUBLESTAR397=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2725)
                        if self._state.backtracking == 0:

                            DOUBLESTAR397_tree = self._adaptor.createWithPayload(DOUBLESTAR397)
                            self._adaptor.addChild(root_0, DOUBLESTAR397_tree)

                        self._state.following.append(self.FOLLOW_test_in_arglist2727)
                        test398 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test398.tree)





                elif alt125 == 3:
                    # kv.g:436:4: DOUBLESTAR test
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR399=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2734)
                    if self._state.backtracking == 0:

                        DOUBLESTAR399_tree = self._adaptor.createWithPayload(DOUBLESTAR399)
                        self._adaptor.addChild(root_0, DOUBLESTAR399_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2736)
                    test400 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test400.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arglist"

    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.argument_return, self).__init__()

            self.tree = None




    # $ANTLR start "argument"
    # kv.g:438:1: argument : test ( ( ASSIGN test ) | gen_for )? ;
    def argument(self, ):

        retval = self.argument_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN402 = None
        test401 = None

        test403 = None

        gen_for404 = None


        ASSIGN402_tree = None

        try:
            try:
                # kv.g:439:2: ( test ( ( ASSIGN test ) | gen_for )? )
                # kv.g:439:4: test ( ( ASSIGN test ) | gen_for )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_argument2746)
                test401 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test401.tree)
                # kv.g:439:9: ( ( ASSIGN test ) | gen_for )?
                alt126 = 3
                LA126_0 = self.input.LA(1)

                if (LA126_0 == ASSIGN) :
                    alt126 = 1
                elif (LA126_0 == 99) :
                    alt126 = 2
                if alt126 == 1:
                    # kv.g:439:11: ( ASSIGN test )
                    pass 
                    # kv.g:439:11: ( ASSIGN test )
                    # kv.g:439:13: ASSIGN test
                    pass 
                    ASSIGN402=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument2752)
                    if self._state.backtracking == 0:

                        ASSIGN402_tree = self._adaptor.createWithPayload(ASSIGN402)
                        self._adaptor.addChild(root_0, ASSIGN402_tree)

                    self._state.following.append(self.FOLLOW_test_in_argument2754)
                    test403 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test403.tree)





                elif alt126 == 2:
                    # kv.g:439:29: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_argument2760)
                    gen_for404 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for404.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "argument"

    class list_iter_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.list_iter_return, self).__init__()

            self.tree = None




    # $ANTLR start "list_iter"
    # kv.g:441:1: list_iter : ( list_for | list_if );
    def list_iter(self, ):

        retval = self.list_iter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        list_for405 = None

        list_if406 = None



        try:
            try:
                # kv.g:442:2: ( list_for | list_if )
                alt127 = 2
                LA127_0 = self.input.LA(1)

                if (LA127_0 == 99) :
                    alt127 = 1
                elif (LA127_0 == 95) :
                    alt127 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 127, 0, self.input)

                    raise nvae

                if alt127 == 1:
                    # kv.g:442:4: list_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_for_in_list_iter2773)
                    list_for405 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for405.tree)


                elif alt127 == 2:
                    # kv.g:442:15: list_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_if_in_list_iter2777)
                    list_if406 = self.list_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_if406.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "list_iter"

    class list_for_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.list_for_return, self).__init__()

            self.tree = None




    # $ANTLR start "list_for"
    # kv.g:444:1: list_for : 'for' exprlist 'in' testlist ( list_iter )? ;
    def list_for(self, ):

        retval = self.list_for_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal407 = None
        string_literal409 = None
        exprlist408 = None

        testlist410 = None

        list_iter411 = None


        string_literal407_tree = None
        string_literal409_tree = None

        try:
            try:
                # kv.g:445:2: ( 'for' exprlist 'in' testlist ( list_iter )? )
                # kv.g:445:4: 'for' exprlist 'in' testlist ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal407=self.match(self.input, 99, self.FOLLOW_99_in_list_for2787)
                if self._state.backtracking == 0:

                    string_literal407_tree = self._adaptor.createWithPayload(string_literal407)
                    self._adaptor.addChild(root_0, string_literal407_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_list_for2789)
                exprlist408 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist408.tree)
                string_literal409=self.match(self.input, 93, self.FOLLOW_93_in_list_for2791)
                if self._state.backtracking == 0:

                    string_literal409_tree = self._adaptor.createWithPayload(string_literal409)
                    self._adaptor.addChild(root_0, string_literal409_tree)

                self._state.following.append(self.FOLLOW_testlist_in_list_for2793)
                testlist410 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist410.tree)
                # kv.g:445:33: ( list_iter )?
                alt128 = 2
                LA128_0 = self.input.LA(1)

                if (LA128_0 == 95 or LA128_0 == 99) :
                    alt128 = 1
                if alt128 == 1:
                    # kv.g:445:34: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_for2796)
                    list_iter411 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter411.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "list_for"

    class list_if_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.list_if_return, self).__init__()

            self.tree = None




    # $ANTLR start "list_if"
    # kv.g:447:1: list_if : 'if' test ( list_iter )? ;
    def list_if(self, ):

        retval = self.list_if_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal412 = None
        test413 = None

        list_iter414 = None


        string_literal412_tree = None

        try:
            try:
                # kv.g:448:2: ( 'if' test ( list_iter )? )
                # kv.g:448:4: 'if' test ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal412=self.match(self.input, 95, self.FOLLOW_95_in_list_if2808)
                if self._state.backtracking == 0:

                    string_literal412_tree = self._adaptor.createWithPayload(string_literal412)
                    self._adaptor.addChild(root_0, string_literal412_tree)

                self._state.following.append(self.FOLLOW_test_in_list_if2810)
                test413 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test413.tree)
                # kv.g:448:14: ( list_iter )?
                alt129 = 2
                LA129_0 = self.input.LA(1)

                if (LA129_0 == 95 or LA129_0 == 99) :
                    alt129 = 1
                if alt129 == 1:
                    # kv.g:448:15: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_if2813)
                    list_iter414 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter414.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "list_if"

    class gen_iter_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.gen_iter_return, self).__init__()

            self.tree = None




    # $ANTLR start "gen_iter"
    # kv.g:450:1: gen_iter : ( gen_for | gen_if );
    def gen_iter(self, ):

        retval = self.gen_iter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        gen_for415 = None

        gen_if416 = None



        try:
            try:
                # kv.g:451:2: ( gen_for | gen_if )
                alt130 = 2
                LA130_0 = self.input.LA(1)

                if (LA130_0 == 99) :
                    alt130 = 1
                elif (LA130_0 == 95) :
                    alt130 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 130, 0, self.input)

                    raise nvae

                if alt130 == 1:
                    # kv.g:451:4: gen_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_for_in_gen_iter2825)
                    gen_for415 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for415.tree)


                elif alt130 == 2:
                    # kv.g:451:14: gen_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_if_in_gen_iter2829)
                    gen_if416 = self.gen_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_if416.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "gen_iter"

    class gen_for_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.gen_for_return, self).__init__()

            self.tree = None




    # $ANTLR start "gen_for"
    # kv.g:453:1: gen_for : 'for' exprlist 'in' or_test ( gen_iter )? ;
    def gen_for(self, ):

        retval = self.gen_for_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal417 = None
        string_literal419 = None
        exprlist418 = None

        or_test420 = None

        gen_iter421 = None


        string_literal417_tree = None
        string_literal419_tree = None

        try:
            try:
                # kv.g:454:2: ( 'for' exprlist 'in' or_test ( gen_iter )? )
                # kv.g:454:4: 'for' exprlist 'in' or_test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal417=self.match(self.input, 99, self.FOLLOW_99_in_gen_for2839)
                if self._state.backtracking == 0:

                    string_literal417_tree = self._adaptor.createWithPayload(string_literal417)
                    self._adaptor.addChild(root_0, string_literal417_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_gen_for2841)
                exprlist418 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist418.tree)
                string_literal419=self.match(self.input, 93, self.FOLLOW_93_in_gen_for2843)
                if self._state.backtracking == 0:

                    string_literal419_tree = self._adaptor.createWithPayload(string_literal419)
                    self._adaptor.addChild(root_0, string_literal419_tree)

                self._state.following.append(self.FOLLOW_or_test_in_gen_for2845)
                or_test420 = self.or_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_test420.tree)
                # kv.g:454:32: ( gen_iter )?
                alt131 = 2
                LA131_0 = self.input.LA(1)

                if (LA131_0 == 95 or LA131_0 == 99) :
                    alt131 = 1
                if alt131 == 1:
                    # kv.g:454:32: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_for2847)
                    gen_iter421 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter421.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "gen_for"

    class gen_if_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.gen_if_return, self).__init__()

            self.tree = None




    # $ANTLR start "gen_if"
    # kv.g:456:1: gen_if : 'if' test ( gen_iter )? ;
    def gen_if(self, ):

        retval = self.gen_if_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal422 = None
        test423 = None

        gen_iter424 = None


        string_literal422_tree = None

        try:
            try:
                # kv.g:457:2: ( 'if' test ( gen_iter )? )
                # kv.g:457:4: 'if' test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal422=self.match(self.input, 95, self.FOLLOW_95_in_gen_if2858)
                if self._state.backtracking == 0:

                    string_literal422_tree = self._adaptor.createWithPayload(string_literal422)
                    self._adaptor.addChild(root_0, string_literal422_tree)

                self._state.following.append(self.FOLLOW_test_in_gen_if2860)
                test423 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test423.tree)
                # kv.g:457:14: ( gen_iter )?
                alt132 = 2
                LA132_0 = self.input.LA(1)

                if (LA132_0 == 95 or LA132_0 == 99) :
                    alt132 = 1
                if alt132 == 1:
                    # kv.g:457:14: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_if2862)
                    gen_iter424 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter424.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "gen_if"

    class yield_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.yield_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "yield_expr"
    # kv.g:459:1: yield_expr : 'yield' ( testlist )? ;
    def yield_expr(self, ):

        retval = self.yield_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal425 = None
        testlist426 = None


        string_literal425_tree = None

        try:
            try:
                # kv.g:460:2: ( 'yield' ( testlist )? )
                # kv.g:460:4: 'yield' ( testlist )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal425=self.match(self.input, 107, self.FOLLOW_107_in_yield_expr2873)
                if self._state.backtracking == 0:

                    string_literal425_tree = self._adaptor.createWithPayload(string_literal425)
                    self._adaptor.addChild(root_0, string_literal425_tree)

                # kv.g:460:12: ( testlist )?
                alt133 = 2
                LA133_0 = self.input.LA(1)

                if (LA133_0 == WNAME or (PLUS <= LA133_0 <= MINUS) or LA133_0 == NAME or LA133_0 == LPAREN or LA133_0 == NOT or (TILDE <= LA133_0 <= LBRACK) or LA133_0 == LCURLY or (BACKQUOTE <= LA133_0 <= STRING) or LA133_0 == 106) :
                    alt133 = 1
                if alt133 == 1:
                    # kv.g:460:12: testlist
                    pass 
                    self._state.following.append(self.FOLLOW_testlist_in_yield_expr2875)
                    testlist426 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist426.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "yield_expr"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.identifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "identifier"
    # kv.g:551:1: identifier : ( WNAME | NAME );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set427 = None

        set427_tree = None

        try:
            try:
                # kv.g:552:2: ( WNAME | NAME )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set427 = self.input.LT(1)
                if self.input.LA(1) == WNAME or self.input.LA(1) == NAME:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set427))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "identifier"

    # $ANTLR start "synpred1_kv"
    def synpred1_kv_fragment(self, ):
        # kv.g:342:5: ( 'if' or_test 'else' )
        # kv.g:342:7: 'if' or_test 'else'
        pass 
        self.match(self.input, 95, self.FOLLOW_95_in_synpred1_kv1923)
        self._state.following.append(self.FOLLOW_or_test_in_synpred1_kv1925)
        self.or_test()

        self._state.following.pop()
        self.match(self.input, 96, self.FOLLOW_96_in_synpred1_kv1927)


    # $ANTLR end "synpred1_kv"




    # Delegated rules

    def synpred1_kv(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_kv_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\15\uffff\1\22\10\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\67\1\30\1\32\3\30\1\25\2\32\1\30\1\34\1\30\1\25\1\4\1\32\1\30"
        u"\1\34\2\uffff\1\34\1\30\1\34"
        )

    DFA8_max = DFA.unpack(
        u"\1\67\1\35\1\70\1\30\2\35\1\31\2\70\1\30\1\70\1\30\1\25\1\106\1"
        u"\70\1\35\1\70\2\uffff\1\70\1\30\1\70"
        )

    DFA8_accept = DFA.unpack(
        u"\21\uffff\1\2\1\1\3\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\4\uffff\1\3"),
        DFA.unpack(u"\1\5\1\4\34\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\11"),
        DFA.unpack(u"\1\12\4\uffff\1\13"),
        DFA.unpack(u"\1\15\3\uffff\1\14"),
        DFA.unpack(u"\1\5\1\4\34\uffff\1\6"),
        DFA.unpack(u"\1\5\1\4\34\uffff\1\6"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17\33\uffff\1\6"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\21\20\uffff\4\22\36\uffff\1\22\16\uffff\1\22"),
        DFA.unpack(u"\1\5\1\4\34\uffff\1\6"),
        DFA.unpack(u"\1\23\4\uffff\1\24"),
        DFA.unpack(u"\1\17\33\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\33\uffff\1\6"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\17\33\uffff\1\6")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\30\1\32\1\30\1\uffff\1\30\1\uffff\2\32\1\30\1\32"
        )

    DFA9_max = DFA.unpack(
        u"\1\35\1\107\1\30\1\uffff\1\35\1\uffff\2\107\1\30\1\107"
        )

    DFA9_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1\4\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\1\4\uffff\1\2"),
        DFA.unpack(u"\1\3\1\4\34\uffff\1\5\16\uffff\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\4\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\4\34\uffff\1\5\16\uffff\1\5"),
        DFA.unpack(u"\1\3\1\4\34\uffff\1\5\16\uffff\1\5"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\3\1\4\34\uffff\1\5\16\uffff\1\5")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\15\uffff\1\22\10\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\106\1\30\1\32\3\30\1\25\2\32\1\30\1\34\1\30\1\25\1\4\1\32\1"
        u"\30\1\34\2\uffff\1\34\1\30\1\34"
        )

    DFA18_max = DFA.unpack(
        u"\1\106\1\35\1\107\1\30\2\35\1\31\2\107\1\30\1\107\1\30\1\25\1\106"
        u"\1\107\1\35\1\107\2\uffff\1\107\1\30\1\107"
        )

    DFA18_accept = DFA.unpack(
        u"\21\uffff\1\2\1\1\3\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\4\uffff\1\3"),
        DFA.unpack(u"\1\5\1\4\53\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\11"),
        DFA.unpack(u"\1\12\4\uffff\1\13"),
        DFA.unpack(u"\1\15\3\uffff\1\14"),
        DFA.unpack(u"\1\5\1\4\53\uffff\1\6"),
        DFA.unpack(u"\1\5\1\4\53\uffff\1\6"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17\52\uffff\1\6"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\21\20\uffff\4\22\36\uffff\1\22\16\uffff\1\22"),
        DFA.unpack(u"\1\5\1\4\53\uffff\1\6"),
        DFA.unpack(u"\1\23\4\uffff\1\24"),
        DFA.unpack(u"\1\17\52\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\52\uffff\1\6"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\17\52\uffff\1\6")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\37\1\31\2\25\2\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\1\37\1\31\2\153\2\uffff"
        )

    DFA30_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1"
        )

    DFA30_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA30_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\5\2\uffff\1\4\3\uffff\2\4\1\uffff\1\4\1\3\4\uffff"
        u"\1\4\20\uffff\1\4\16\uffff\2\4\1\uffff\1\4\1\uffff\7\4\5\uffff"
        u"\7\4\1\uffff\2\4\2\uffff\3\4\1\uffff\1\4\3\uffff\2\4"),
        DFA.unpack(u"\1\5\2\uffff\1\4\3\uffff\2\4\1\uffff\1\4\1\3\4\uffff"
        u"\1\4\20\uffff\1\4\16\uffff\2\4\1\uffff\1\4\1\uffff\7\4\5\uffff"
        u"\7\4\1\uffff\2\4\2\uffff\3\4\1\uffff\1\4\3\uffff\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA51_min = DFA.unpack(
        u"\2\5\36\uffff"
        )

    DFA51_max = DFA.unpack(
        u"\1\150\1\152\36\uffff"
        )

    DFA51_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1\26\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA51_transition = [
        DFA.unpack(u"\1\2\17\uffff\1\2\5\uffff\1\1\5\uffff\1\2\76\uffff\2"
        u"\2\3\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u"\1\2\17\uffff\1\2\2\uffff\1\11\3\uffff\2\11\1\uffff"
        u"\1\11\1\uffff\1\2\3\uffff\1\11\20\uffff\1\11\16\uffff\2\11\1\uffff"
        u"\1\11\1\uffff\7\11\17\uffff\2\2\3\uffff\1\2\2\uffff\1\2\1\uffff"
        u"\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #51

    class DFA51(DFA):
        pass


    # lookup tables for DFA #75

    DFA75_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA75_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA75_min = DFA.unpack(
        u"\1\5\1\0\23\uffff"
        )

    DFA75_max = DFA.unpack(
        u"\1\150\1\0\23\uffff"
        )

    DFA75_accept = DFA.unpack(
        u"\2\uffff\1\2\21\uffff\1\1"
        )

    DFA75_special = DFA.unpack(
        u"\1\uffff\1\0\23\uffff"
        )

            
    DFA75_transition = [
        DFA.unpack(u"\1\2\17\uffff\1\2\2\uffff\2\2\1\uffff\1\2\3\uffff\1"
        u"\2\1\uffff\1\2\2\uffff\1\2\1\uffff\15\2\24\uffff\1\2\1\uffff\2"
        u"\2\24\uffff\1\1\2\2\1\uffff\1\2\1\uffff\1\2\1\uffff\2\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #75

    class DFA75(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA75_1 = input.LA(1)

                 
                index75_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_kv()):
                    s = 20

                elif (True):
                    s = 2

                 
                input.seek(index75_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 75, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #81

    DFA81_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA81_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA81_min = DFA.unpack(
        u"\1\66\10\uffff\1\135\3\uffff"
        )

    DFA81_max = DFA.unpack(
        u"\1\151\10\uffff\1\151\3\uffff"
        )

    DFA81_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\uffff\1\12\1\11\1\13"
        )

    DFA81_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA81_transition = [
        DFA.unpack(u"\1\11\1\1\1\2\1\3\1\4\1\5\1\6\1\7\37\uffff\1\10\13\uffff"
        u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13\13\uffff\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #81

    class DFA81(DFA):
        pass


    # lookup tables for DFA #99

    DFA99_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA99_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA99_min = DFA.unpack(
        u"\1\33\1\30\22\uffff"
        )

    DFA99_max = DFA.unpack(
        u"\1\46\1\152\22\uffff"
        )

    DFA99_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\20\uffff"
        )

    DFA99_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA99_transition = [
        DFA.unpack(u"\1\1\12\uffff\1\2"),
        DFA.unpack(u"\1\3\3\uffff\2\3\1\uffff\1\3\5\uffff\1\3\1\2\17\uffff"
        u"\1\3\16\uffff\2\3\1\uffff\1\3\1\uffff\7\3\31\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #99

    class DFA99(DFA):
        pass


    # lookup tables for DFA #114

    DFA114_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA114_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA114_min = DFA.unpack(
        u"\2\5\36\uffff"
        )

    DFA114_max = DFA.unpack(
        u"\2\150\36\uffff"
        )

    DFA114_accept = DFA.unpack(
        u"\2\uffff\1\2\7\uffff\1\1\25\uffff"
        )

    DFA114_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA114_transition = [
        DFA.unpack(u"\1\2\17\uffff\1\2\5\uffff\1\1\5\uffff\1\2\73\uffff\1"
        u"\2\2\uffff\2\2\3\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u"\1\2\17\uffff\1\2\2\uffff\1\12\3\uffff\2\12\1\uffff"
        u"\1\12\1\uffff\1\2\3\uffff\1\12\37\uffff\2\12\1\uffff\1\12\1\uffff"
        u"\7\12\14\uffff\1\2\2\uffff\2\2\3\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #114

    class DFA114(DFA):
        pass


    # lookup tables for DFA #116

    DFA116_eot = DFA.unpack(
        u"\60\uffff"
        )

    DFA116_eof = DFA.unpack(
        u"\60\uffff"
        )

    DFA116_min = DFA.unpack(
        u"\2\5\56\uffff"
        )

    DFA116_max = DFA.unpack(
        u"\1\150\1\152\56\uffff"
        )

    DFA116_accept = DFA.unpack(
        u"\2\uffff\1\2\30\uffff\1\1\5\uffff\1\1\16\uffff"
        )

    DFA116_special = DFA.unpack(
        u"\60\uffff"
        )

            
    DFA116_transition = [
        DFA.unpack(u"\1\2\17\uffff\1\2\3\uffff\1\2\1\uffff\1\1\5\uffff\1"
        u"\2\2\uffff\1\2\1\uffff\15\2\24\uffff\1\2\2\uffff\1\2\24\uffff\3"
        u"\2\1\uffff\1\2\1\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u"\1\2\17\uffff\1\2\2\uffff\1\41\1\2\1\uffff\1\2\2\41"
        u"\1\uffff\1\41\1\uffff\1\2\2\uffff\1\2\1\41\15\2\3\uffff\1\41\16"
        u"\uffff\2\41\1\2\1\41\1\uffff\1\33\6\41\16\uffff\3\2\1\uffff\1\2"
        u"\1\uffff\1\2\2\uffff\1\2\1\uffff\1\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #116

    class DFA116(DFA):
        pass


    # lookup tables for DFA #118

    DFA118_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA118_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA118_min = DFA.unpack(
        u"\1\33\1\30\22\uffff"
        )

    DFA118_max = DFA.unpack(
        u"\1\111\1\152\22\uffff"
        )

    DFA118_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\20\uffff"
        )

    DFA118_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA118_transition = [
        DFA.unpack(u"\1\1\55\uffff\1\2"),
        DFA.unpack(u"\1\3\3\uffff\2\3\1\uffff\1\3\5\uffff\1\3\20\uffff\1"
        u"\3\16\uffff\2\3\1\uffff\1\3\1\2\7\3\31\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #118

    class DFA118(DFA):
        pass


 

    FOLLOW_blank_in_kvfile202 = frozenset([1, 21, 22, 23, 24, 55, 70])
    FOLLOW_line_in_kvfile206 = frozenset([1, 21, 22, 23, 24, 55, 70])
    FOLLOW_NEWLINE_in_blank216 = frozenset([1])
    FOLLOW_directive_in_line235 = frozenset([1])
    FOLLOW_root_rule_in_line240 = frozenset([1])
    FOLLOW_class_rule_in_line245 = frozenset([1])
    FOLLOW_template_rule_in_line250 = frozenset([1])
    FOLLOW_comment_in_line255 = frozenset([1])
    FOLLOW_DIRECTIVETEXT_in_directive265 = frozenset([21])
    FOLLOW_NEWLINE_in_directive267 = frozenset([1])
    FOLLOW_COMMENTTEXT_in_comment290 = frozenset([21])
    FOLLOW_NEWLINE_in_comment292 = frozenset([1])
    FOLLOW_widget_in_root_rule314 = frozenset([1])
    FOLLOW_WNAME_in_widget326 = frozenset([21, 25])
    FOLLOW_COLON_in_widget328 = frozenset([21])
    FOLLOW_NEWLINE_in_widget331 = frozenset([1])
    FOLLOW_WNAME_in_widget346 = frozenset([21, 25])
    FOLLOW_COLON_in_widget348 = frozenset([21, 25])
    FOLLOW_widget_body_in_widget351 = frozenset([1])
    FOLLOW_LESS_in_class_rule373 = frozenset([24, 29])
    FOLLOW_class_widget_in_class_rule377 = frozenset([56])
    FOLLOW_GREATER_in_class_rule379 = frozenset([21, 25])
    FOLLOW_COLON_in_class_rule381 = frozenset([21])
    FOLLOW_NEWLINE_in_class_rule384 = frozenset([1])
    FOLLOW_LESS_in_class_rule399 = frozenset([24, 29])
    FOLLOW_class_widget_in_class_rule403 = frozenset([56])
    FOLLOW_GREATER_in_class_rule405 = frozenset([21, 25])
    FOLLOW_COLON_in_class_rule407 = frozenset([21, 25])
    FOLLOW_widget_body_in_class_rule410 = frozenset([1])
    FOLLOW_widget_comp_in_class_widget432 = frozenset([1])
    FOLLOW_widget_list_in_widget_comp444 = frozenset([1])
    FOLLOW_widget_list_in_widget_comp457 = frozenset([26])
    FOLLOW_AT_in_widget_comp459 = frozenset([24, 29])
    FOLLOW_widget_base_in_widget_comp463 = frozenset([1])
    FOLLOW_widget_name_in_widget_list485 = frozenset([1])
    FOLLOW_widget_name_in_widget_list496 = frozenset([27])
    FOLLOW_COMMA_in_widget_list501 = frozenset([24, 29])
    FOLLOW_widget_name_in_widget_list503 = frozenset([1, 27])
    FOLLOW_widget_name_in_widget_base530 = frozenset([1])
    FOLLOW_widget_name_in_widget_base541 = frozenset([28])
    FOLLOW_PLUS_in_widget_base546 = frozenset([24, 29])
    FOLLOW_widget_name_in_widget_base548 = frozenset([1, 28])
    FOLLOW_WNAME_in_widget_name575 = frozenset([1])
    FOLLOW_MINUS_in_widget_name586 = frozenset([24])
    FOLLOW_WNAME_in_widget_name588 = frozenset([1])
    FOLLOW_WNAME_in_class_list608 = frozenset([1, 28])
    FOLLOW_PLUS_in_class_list611 = frozenset([24])
    FOLLOW_WNAME_in_class_list613 = frozenset([1, 28])
    FOLLOW_LBRACK_in_template_rule625 = frozenset([24, 29])
    FOLLOW_class_widget_in_template_rule629 = frozenset([71])
    FOLLOW_RBRACK_in_template_rule631 = frozenset([21, 25])
    FOLLOW_COLON_in_template_rule633 = frozenset([21])
    FOLLOW_NEWLINE_in_template_rule636 = frozenset([1])
    FOLLOW_LBRACK_in_template_rule651 = frozenset([24, 29])
    FOLLOW_class_widget_in_template_rule655 = frozenset([71])
    FOLLOW_RBRACK_in_template_rule657 = frozenset([21, 25])
    FOLLOW_COLON_in_template_rule659 = frozenset([21, 25])
    FOLLOW_widget_body_in_template_rule662 = frozenset([1])
    FOLLOW_NEWLINE_in_widget_body687 = frozenset([4])
    FOLLOW_INDENT_in_widget_body690 = frozenset([21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_stmt_in_widget_body694 = frozenset([5, 21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_DEDENT_in_widget_body698 = frozenset([1])
    FOLLOW_NEWLINE_in_canvas_body709 = frozenset([4])
    FOLLOW_INDENT_in_canvas_body712 = frozenset([21, 22, 23, 24, 55, 70])
    FOLLOW_canvas_stmt_in_canvas_body716 = frozenset([5, 21, 22, 23, 24, 55, 70])
    FOLLOW_DEDENT_in_canvas_body720 = frozenset([1])
    FOLLOW_widget_in_stmt731 = frozenset([1])
    FOLLOW_canvas_in_stmt736 = frozenset([1])
    FOLLOW_prop_in_stmt741 = frozenset([1])
    FOLLOW_comment_in_stmt746 = frozenset([1])
    FOLLOW_blank_in_stmt751 = frozenset([1])
    FOLLOW_instruction_in_canvas_stmt762 = frozenset([1])
    FOLLOW_comment_in_canvas_stmt767 = frozenset([1])
    FOLLOW_blank_in_canvas_stmt772 = frozenset([1])
    FOLLOW_WNAME_in_instruction783 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction785 = frozenset([21])
    FOLLOW_NEWLINE_in_instruction788 = frozenset([1])
    FOLLOW_WNAME_in_instruction803 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction805 = frozenset([21, 25])
    FOLLOW_instruction_body_in_instruction808 = frozenset([1])
    FOLLOW_NEWLINE_in_instruction_body831 = frozenset([4])
    FOLLOW_INDENT_in_instruction_body834 = frozenset([21, 22, 23, 24, 31, 55, 70])
    FOLLOW_instruction_stmt_in_instruction_body838 = frozenset([5, 21, 22, 23, 24, 31, 55, 70])
    FOLLOW_DEDENT_in_instruction_body842 = frozenset([1])
    FOLLOW_prop_in_instruction_stmt854 = frozenset([1])
    FOLLOW_comment_in_instruction_stmt859 = frozenset([1])
    FOLLOW_blank_in_instruction_stmt864 = frozenset([1])
    FOLLOW_CANVAS_in_canvas875 = frozenset([25])
    FOLLOW_COLON_in_canvas877 = frozenset([21])
    FOLLOW_canvas_body_in_canvas879 = frozenset([1])
    FOLLOW_NAME_in_prop900 = frozenset([25])
    FOLLOW_COLON_in_prop902 = frozenset([21, 32])
    FOLLOW_WS_in_prop904 = frozenset([21, 32])
    FOLLOW_property_body_in_prop909 = frozenset([1])
    FOLLOW_NAME_in_prop924 = frozenset([25])
    FOLLOW_COLON_in_prop926 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_WS_in_prop928 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_prop933 = frozenset([21])
    FOLLOW_NEWLINE_in_prop935 = frozenset([1])
    FOLLOW_NEWLINE_in_property_body955 = frozenset([4])
    FOLLOW_INDENT_in_property_body958 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_property_body961 = frozenset([5, 21])
    FOLLOW_NEWLINE_in_property_body964 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_property_body967 = frozenset([5, 21])
    FOLLOW_DEDENT_in_property_body971 = frozenset([1])
    FOLLOW_python_in_prop_value984 = frozenset([1])
    FOLLOW_simple_stmt_in_python1007 = frozenset([1])
    FOLLOW_compound_stmt_in_python1014 = frozenset([1])
    FOLLOW_small_stmt_in_simple_stmt1024 = frozenset([1, 33])
    FOLLOW_SEMI_in_simple_stmt1034 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_small_stmt_in_simple_stmt1036 = frozenset([1, 33])
    FOLLOW_SEMI_in_simple_stmt1041 = frozenset([1])
    FOLLOW_expr_stmt_in_small_stmt1054 = frozenset([1])
    FOLLOW_print_stmt_in_small_stmt1061 = frozenset([1])
    FOLLOW_del_stmt_in_small_stmt1068 = frozenset([1])
    FOLLOW_pass_stmt_in_small_stmt1075 = frozenset([1])
    FOLLOW_flow_stmt_in_small_stmt1082 = frozenset([1])
    FOLLOW_exec_stmt_in_small_stmt1089 = frozenset([1])
    FOLLOW_assert_stmt_in_small_stmt1096 = frozenset([1])
    FOLLOW_defparameter_in_varargslist1106 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1116 = frozenset([24, 31, 37])
    FOLLOW_defparameter_in_varargslist1118 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1123 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_varargslist1127 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1129 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1132 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1134 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1136 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1142 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1144 = frozenset([1])
    FOLLOW_STAR_in_varargslist1155 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1157 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1160 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1162 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1164 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1171 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1173 = frozenset([1])
    FOLLOW_fpdef_in_defparameter1183 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_defparameter1186 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_defparameter1188 = frozenset([1])
    FOLLOW_identifier_in_fpdef1200 = frozenset([1])
    FOLLOW_LPAREN_in_fpdef1205 = frozenset([24, 31, 37])
    FOLLOW_fplist_in_fpdef1207 = frozenset([38])
    FOLLOW_RPAREN_in_fpdef1209 = frozenset([1])
    FOLLOW_fpdef_in_fplist1219 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1229 = frozenset([24, 31, 37])
    FOLLOW_fpdef_in_fplist1231 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1236 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt1249 = frozenset([1, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    FOLLOW_augassign_in_expr_stmt1252 = frozenset([89, 90, 91, 107])
    FOLLOW_yield_expr_in_expr_stmt1254 = frozenset([1])
    FOLLOW_augassign_in_expr_stmt1258 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_expr_stmt1260 = frozenset([1])
    FOLLOW_assigns_in_expr_stmt1264 = frozenset([1])
    FOLLOW_assign_testlist_in_assigns1277 = frozenset([1, 36])
    FOLLOW_assign_yield_in_assigns1282 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_assign_testlist1294 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_assign_testlist1296 = frozenset([1])
    FOLLOW_ASSIGN_in_assign_yield1307 = frozenset([89, 90, 91, 107])
    FOLLOW_yield_expr_in_assign_yield1309 = frozenset([1])
    FOLLOW_set_in_augassign0 = frozenset([1])
    FOLLOW_86_in_print_stmt1379 = frozenset([1, 24, 28, 29, 31, 37, 51, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_printlist_in_print_stmt1382 = frozenset([1])
    FOLLOW_RIGHTSHIFT_in_print_stmt1386 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_printlist_in_print_stmt1388 = frozenset([1])
    FOLLOW_test_in_printlist1406 = frozenset([1, 27])
    FOLLOW_COMMA_in_printlist1417 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_printlist1419 = frozenset([1, 27])
    FOLLOW_COMMA_in_printlist1424 = frozenset([1])
    FOLLOW_87_in_del_stmt1438 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_del_stmt1440 = frozenset([1])
    FOLLOW_88_in_pass_stmt1452 = frozenset([1])
    FOLLOW_break_stmt_in_flow_stmt1464 = frozenset([1])
    FOLLOW_continue_stmt_in_flow_stmt1471 = frozenset([1])
    FOLLOW_raise_stmt_in_flow_stmt1480 = frozenset([1])
    FOLLOW_yield_stmt_in_flow_stmt1487 = frozenset([1])
    FOLLOW_89_in_break_stmt1499 = frozenset([1])
    FOLLOW_90_in_continue_stmt1511 = frozenset([1])
    FOLLOW_yield_expr_in_yield_stmt1521 = frozenset([1])
    FOLLOW_91_in_raise_stmt1531 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1534 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1537 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1539 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1542 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1544 = frozenset([1])
    FOLLOW_92_in_exec_stmt1562 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_exec_stmt1564 = frozenset([1, 93])
    FOLLOW_93_in_exec_stmt1567 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_exec_stmt1569 = frozenset([1, 27])
    FOLLOW_COMMA_in_exec_stmt1572 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_exec_stmt1574 = frozenset([1])
    FOLLOW_94_in_assert_stmt1590 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_assert_stmt1592 = frozenset([1, 27])
    FOLLOW_COMMA_in_assert_stmt1595 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_assert_stmt1597 = frozenset([1])
    FOLLOW_if_stmt_in_compound_stmt1611 = frozenset([1])
    FOLLOW_while_stmt_in_compound_stmt1618 = frozenset([1])
    FOLLOW_for_stmt_in_compound_stmt1625 = frozenset([1])
    FOLLOW_try_stmt_in_compound_stmt1632 = frozenset([1])
    FOLLOW_with_stmt_in_compound_stmt1639 = frozenset([1])
    FOLLOW_95_in_if_stmt1656 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_if_stmt1658 = frozenset([25])
    FOLLOW_COLON_in_if_stmt1660 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_if_stmt1662 = frozenset([1, 96, 97])
    FOLLOW_elif_clause_in_if_stmt1664 = frozenset([1, 96, 97])
    FOLLOW_96_in_if_stmt1668 = frozenset([25])
    FOLLOW_COLON_in_if_stmt1670 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_if_stmt1672 = frozenset([1])
    FOLLOW_97_in_elif_clause1686 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_elif_clause1688 = frozenset([25])
    FOLLOW_COLON_in_elif_clause1690 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_elif_clause1692 = frozenset([1])
    FOLLOW_98_in_while_stmt1704 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_while_stmt1706 = frozenset([25])
    FOLLOW_COLON_in_while_stmt1708 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_while_stmt1710 = frozenset([1, 96])
    FOLLOW_96_in_while_stmt1713 = frozenset([25])
    FOLLOW_COLON_in_while_stmt1715 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_while_stmt1717 = frozenset([1])
    FOLLOW_99_in_for_stmt1731 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_for_stmt1733 = frozenset([93])
    FOLLOW_93_in_for_stmt1735 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_for_stmt1737 = frozenset([25])
    FOLLOW_COLON_in_for_stmt1739 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_for_stmt1741 = frozenset([1, 96])
    FOLLOW_96_in_for_stmt1744 = frozenset([25])
    FOLLOW_COLON_in_for_stmt1746 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_for_stmt1748 = frozenset([1])
    FOLLOW_100_in_try_stmt1762 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1764 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1766 = frozenset([101, 104])
    FOLLOW_except_clause_in_try_stmt1773 = frozenset([1, 96, 101, 104])
    FOLLOW_96_in_try_stmt1777 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1779 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1781 = frozenset([1, 101])
    FOLLOW_101_in_try_stmt1786 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1788 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1790 = frozenset([1])
    FOLLOW_101_in_try_stmt1799 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1801 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1803 = frozenset([1])
    FOLLOW_102_in_with_stmt1817 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_with_stmt1819 = frozenset([24, 25, 31, 103])
    FOLLOW_with_var_in_with_stmt1822 = frozenset([25])
    FOLLOW_COLON_in_with_stmt1826 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_with_stmt1828 = frozenset([1])
    FOLLOW_103_in_with_var1841 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_identifier_in_with_var1845 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_with_var1848 = frozenset([1])
    FOLLOW_104_in_except_clause1860 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_except_clause1863 = frozenset([25, 27])
    FOLLOW_COMMA_in_except_clause1866 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_except_clause1868 = frozenset([25])
    FOLLOW_COLON_in_except_clause1874 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_except_clause1876 = frozenset([1])
    FOLLOW_simple_stmt_in_suite1888 = frozenset([1])
    FOLLOW_NEWLINE_in_suite1895 = frozenset([4])
    FOLLOW_INDENT_in_suite1897 = frozenset([21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_stmt_in_suite1900 = frozenset([5, 21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_DEDENT_in_suite1904 = frozenset([1])
    FOLLOW_or_test_in_test1915 = frozenset([1, 95])
    FOLLOW_95_in_test1933 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_test1935 = frozenset([96])
    FOLLOW_96_in_test1937 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_test1939 = frozenset([1])
    FOLLOW_lambdef_in_test1947 = frozenset([1])
    FOLLOW_and_test_in_or_test1957 = frozenset([1, 52])
    FOLLOW_OR_in_or_test1960 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_and_test_in_or_test1962 = frozenset([1, 52])
    FOLLOW_not_test_in_and_test1974 = frozenset([1, 53])
    FOLLOW_AND_in_and_test1977 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_not_test_in_and_test1979 = frozenset([1, 53])
    FOLLOW_NOT_in_not_test1991 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_not_test_in_not_test1993 = frozenset([1])
    FOLLOW_comparison_in_not_test1998 = frozenset([1])
    FOLLOW_expr_in_comparison2008 = frozenset([1, 54, 55, 56, 57, 58, 59, 60, 61, 93, 105])
    FOLLOW_comp_op_in_comparison2011 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_comparison2013 = frozenset([1, 54, 55, 56, 57, 58, 59, 60, 61, 93, 105])
    FOLLOW_LESS_in_comp_op2025 = frozenset([1])
    FOLLOW_GREATER_in_comp_op2029 = frozenset([1])
    FOLLOW_EQUAL_in_comp_op2033 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comp_op2037 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comp_op2041 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comp_op2045 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comp_op2049 = frozenset([1])
    FOLLOW_93_in_comp_op2054 = frozenset([1])
    FOLLOW_NOT_in_comp_op2058 = frozenset([93])
    FOLLOW_93_in_comp_op2060 = frozenset([1])
    FOLLOW_105_in_comp_op2064 = frozenset([1])
    FOLLOW_NOT_in_comp_op2068 = frozenset([105])
    FOLLOW_105_in_comp_op2070 = frozenset([1])
    FOLLOW_xor_expr_in_expr2080 = frozenset([1, 62])
    FOLLOW_VBAR_in_expr2083 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_xor_expr_in_expr2085 = frozenset([1, 62])
    FOLLOW_and_expr_in_xor_expr2097 = frozenset([1, 63])
    FOLLOW_CIRCUMFLEX_in_xor_expr2100 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_and_expr_in_xor_expr2102 = frozenset([1, 63])
    FOLLOW_shift_expr_in_and_expr2114 = frozenset([1, 64])
    FOLLOW_AMPER_in_and_expr2117 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_shift_expr_in_and_expr2119 = frozenset([1, 64])
    FOLLOW_arith_expr_in_shift_expr2131 = frozenset([1, 51, 65])
    FOLLOW_set_in_shift_expr2134 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_arith_expr_in_shift_expr2140 = frozenset([1, 51, 65])
    FOLLOW_term_in_arith_expr2152 = frozenset([1, 28, 29])
    FOLLOW_set_in_arith_expr2155 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_term_in_arith_expr2161 = frozenset([1, 28, 29])
    FOLLOW_factor_in_term2173 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_set_in_term2176 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_term2193 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_PLUS_in_factor2205 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2207 = frozenset([1])
    FOLLOW_MINUS_in_factor2211 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2213 = frozenset([1])
    FOLLOW_TILDE_in_factor2217 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2219 = frozenset([1])
    FOLLOW_power_in_factor2223 = frozenset([1])
    FOLLOW_atom_in_power2233 = frozenset([1, 35, 37, 70, 81])
    FOLLOW_trailer_in_power2236 = frozenset([1, 35, 37, 70, 81])
    FOLLOW_DOUBLESTAR_in_power2248 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_power2250 = frozenset([1])
    FOLLOW_LPAREN_in_atom2262 = frozenset([24, 28, 29, 31, 37, 38, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 89, 90, 91, 106, 107])
    FOLLOW_yield_expr_in_atom2266 = frozenset([38])
    FOLLOW_testlist_gexp_in_atom2270 = frozenset([38])
    FOLLOW_RPAREN_in_atom2275 = frozenset([1])
    FOLLOW_LBRACK_in_atom2280 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_listmaker_in_atom2283 = frozenset([71])
    FOLLOW_RBRACK_in_atom2287 = frozenset([1])
    FOLLOW_LCURLY_in_atom2292 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_dictmaker_in_atom2295 = frozenset([73])
    FOLLOW_RCURLY_in_atom2299 = frozenset([1])
    FOLLOW_BACKQUOTE_in_atom2304 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_atom2306 = frozenset([74])
    FOLLOW_BACKQUOTE_in_atom2308 = frozenset([1])
    FOLLOW_identifier_in_atom2313 = frozenset([1])
    FOLLOW_NONE_in_atom2320 = frozenset([1])
    FOLLOW_INT_in_atom2325 = frozenset([1])
    FOLLOW_LONGINT_in_atom2330 = frozenset([1])
    FOLLOW_FLOAT_in_atom2335 = frozenset([1])
    FOLLOW_COMPLEX_in_atom2340 = frozenset([1])
    FOLLOW_STRING_in_atom2346 = frozenset([1, 80])
    FOLLOW_test_in_listmaker2358 = frozenset([1, 27, 99])
    FOLLOW_list_for_in_listmaker2361 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker2373 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_listmaker2375 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker2382 = frozenset([1])
    FOLLOW_test_in_testlist_gexp2394 = frozenset([1, 27, 99])
    FOLLOW_COMMA_in_testlist_gexp2407 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_testlist_gexp2409 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist_gexp2414 = frozenset([1])
    FOLLOW_gen_for_in_testlist_gexp2420 = frozenset([1])
    FOLLOW_106_in_lambdef2432 = frozenset([24, 25, 31, 34, 35, 37])
    FOLLOW_varargslist_in_lambdef2435 = frozenset([25])
    FOLLOW_COLON_in_lambdef2439 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_lambdef2441 = frozenset([1])
    FOLLOW_LPAREN_in_trailer2451 = frozenset([24, 28, 29, 31, 34, 35, 37, 38, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_arglist_in_trailer2454 = frozenset([38])
    FOLLOW_RPAREN_in_trailer2458 = frozenset([1])
    FOLLOW_LBRACK_in_trailer2463 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 106])
    FOLLOW_subscriptlist_in_trailer2465 = frozenset([71])
    FOLLOW_RBRACK_in_trailer2467 = frozenset([1])
    FOLLOW_DOT_in_trailer2472 = frozenset([24, 31])
    FOLLOW_identifier_in_trailer2474 = frozenset([1])
    FOLLOW_subscript_in_subscriptlist2484 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist2494 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 106])
    FOLLOW_subscript_in_subscriptlist2496 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist2501 = frozenset([1])
    FOLLOW_DOT_in_subscript2513 = frozenset([81])
    FOLLOW_DOT_in_subscript2515 = frozenset([81])
    FOLLOW_DOT_in_subscript2517 = frozenset([1])
    FOLLOW_test_in_subscript2522 = frozenset([1, 25])
    FOLLOW_COLON_in_subscript2525 = frozenset([1, 24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_subscript2528 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript2533 = frozenset([1])
    FOLLOW_COLON_in_subscript2542 = frozenset([1, 24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_subscript2545 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript2550 = frozenset([1])
    FOLLOW_COLON_in_sliceop2562 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_sliceop2565 = frozenset([1])
    FOLLOW_expr_in_exprlist2577 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2588 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_exprlist2590 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2595 = frozenset([1])
    FOLLOW_test_in_testlist2607 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2618 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_testlist2620 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2625 = frozenset([1])
    FOLLOW_test_in_dictmaker2637 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2639 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2641 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2652 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2654 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2656 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2658 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2663 = frozenset([1])
    FOLLOW_argument_in_arglist2675 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2678 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_argument_in_arglist2680 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2686 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_arglist2690 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2692 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2695 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2697 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2699 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2705 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2707 = frozenset([1])
    FOLLOW_STAR_in_arglist2718 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2720 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2723 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2725 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2727 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2734 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2736 = frozenset([1])
    FOLLOW_test_in_argument2746 = frozenset([27, 36, 99])
    FOLLOW_ASSIGN_in_argument2752 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_argument2754 = frozenset([1])
    FOLLOW_gen_for_in_argument2760 = frozenset([1])
    FOLLOW_list_for_in_list_iter2773 = frozenset([1])
    FOLLOW_list_if_in_list_iter2777 = frozenset([1])
    FOLLOW_99_in_list_for2787 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_list_for2789 = frozenset([93])
    FOLLOW_93_in_list_for2791 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_list_for2793 = frozenset([1, 95, 99])
    FOLLOW_list_iter_in_list_for2796 = frozenset([1])
    FOLLOW_95_in_list_if2808 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_list_if2810 = frozenset([1, 95, 99])
    FOLLOW_list_iter_in_list_if2813 = frozenset([1])
    FOLLOW_gen_for_in_gen_iter2825 = frozenset([1])
    FOLLOW_gen_if_in_gen_iter2829 = frozenset([1])
    FOLLOW_99_in_gen_for2839 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_gen_for2841 = frozenset([93])
    FOLLOW_93_in_gen_for2843 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_gen_for2845 = frozenset([1, 27, 95, 99])
    FOLLOW_gen_iter_in_gen_for2847 = frozenset([1])
    FOLLOW_95_in_gen_if2858 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_gen_if2860 = frozenset([1, 27, 95, 99])
    FOLLOW_gen_iter_in_gen_if2862 = frozenset([1])
    FOLLOW_107_in_yield_expr2873 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_yield_expr2875 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_95_in_synpred1_kv1923 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_synpred1_kv1925 = frozenset([96])
    FOLLOW_96_in_synpred1_kv1927 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("kvLexer", kvParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
