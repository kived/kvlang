# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 kv.g 2015-05-23 22:28:38

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

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

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

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )

        self.dfa55 = self.DFA55(
            self, 55,
            eot = self.DFA55_eot,
            eof = self.DFA55_eof,
            min = self.DFA55_min,
            max = self.DFA55_max,
            accept = self.DFA55_accept,
            special = self.DFA55_special,
            transition = self.DFA55_transition
            )

        self.dfa79 = self.DFA79(
            self, 79,
            eot = self.DFA79_eot,
            eof = self.DFA79_eof,
            min = self.DFA79_min,
            max = self.DFA79_max,
            accept = self.DFA79_accept,
            special = self.DFA79_special,
            transition = self.DFA79_transition
            )

        self.dfa85 = self.DFA85(
            self, 85,
            eot = self.DFA85_eot,
            eof = self.DFA85_eof,
            min = self.DFA85_min,
            max = self.DFA85_max,
            accept = self.DFA85_accept,
            special = self.DFA85_special,
            transition = self.DFA85_transition
            )

        self.dfa103 = self.DFA103(
            self, 103,
            eot = self.DFA103_eot,
            eof = self.DFA103_eof,
            min = self.DFA103_min,
            max = self.DFA103_max,
            accept = self.DFA103_accept,
            special = self.DFA103_special,
            transition = self.DFA103_transition
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

        self.dfa120 = self.DFA120(
            self, 120,
            eot = self.DFA120_eot,
            eof = self.DFA120_eof,
            min = self.DFA120_min,
            max = self.DFA120_max,
            accept = self.DFA120_accept,
            special = self.DFA120_special,
            transition = self.DFA120_transition
            )

        self.dfa122 = self.DFA122(
            self, 122,
            eot = self.DFA122_eot,
            eof = self.DFA122_eof,
            min = self.DFA122_min,
            max = self.DFA122_max,
            accept = self.DFA122_accept,
            special = self.DFA122_special,
            transition = self.DFA122_transition
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
                alt5 = self.dfa5.predict(self.input)
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
    # kv.g:168:1: widget_body : NEWLINE ( blank )* INDENT ( stmt )+ DEDENT ;
    def widget_body(self, ):

        retval = self.widget_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE50 = None
        INDENT52 = None
        DEDENT54 = None
        blank51 = None

        stmt53 = None


        NEWLINE50_tree = None
        INDENT52_tree = None
        DEDENT54_tree = None

        try:
            try:
                # kv.g:169:5: ( NEWLINE ( blank )* INDENT ( stmt )+ DEDENT )
                # kv.g:169:7: NEWLINE ( blank )* INDENT ( stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE50=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_widget_body687)
                # kv.g:169:16: ( blank )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == NEWLINE) :
                        alt19 = 1


                    if alt19 == 1:
                        # kv.g:169:16: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_widget_body690)
                        blank51 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank51.tree)


                    else:
                        break #loop19
                INDENT52=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_widget_body693)
                # kv.g:169:31: ( stmt )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == NEWLINE or (COMMENTTEXT <= LA20_0 <= WNAME) or (CANVAS <= LA20_0 <= NAME)) :
                        alt20 = 1


                    if alt20 == 1:
                        # kv.g:169:32: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_widget_body697)
                        stmt53 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stmt53.tree)


                    else:
                        if cnt20 >= 1:
                            break #loop20

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1
                DEDENT54=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_widget_body701)



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
    # kv.g:171:1: canvas_body : NEWLINE ( blank )* INDENT ( canvas_stmt )+ DEDENT ;
    def canvas_body(self, ):

        retval = self.canvas_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE55 = None
        INDENT57 = None
        DEDENT59 = None
        blank56 = None

        canvas_stmt58 = None


        NEWLINE55_tree = None
        INDENT57_tree = None
        DEDENT59_tree = None

        try:
            try:
                # kv.g:172:2: ( NEWLINE ( blank )* INDENT ( canvas_stmt )+ DEDENT )
                # kv.g:172:4: NEWLINE ( blank )* INDENT ( canvas_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE55=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_canvas_body712)
                # kv.g:172:13: ( blank )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == NEWLINE) :
                        alt21 = 1


                    if alt21 == 1:
                        # kv.g:172:13: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_canvas_body715)
                        blank56 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank56.tree)


                    else:
                        break #loop21
                INDENT57=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_canvas_body718)
                # kv.g:172:28: ( canvas_stmt )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == NEWLINE or (COMMENTTEXT <= LA22_0 <= WNAME)) :
                        alt22 = 1


                    if alt22 == 1:
                        # kv.g:172:29: canvas_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_canvas_stmt_in_canvas_body722)
                        canvas_stmt58 = self.canvas_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, canvas_stmt58.tree)


                    else:
                        if cnt22 >= 1:
                            break #loop22

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1
                DEDENT59=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_canvas_body726)



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

        widget60 = None

        canvas61 = None

        prop62 = None

        comment63 = None

        blank64 = None



        try:
            try:
                # kv.g:175:2: ( widget | canvas | prop | comment | blank )
                alt23 = 5
                LA23 = self.input.LA(1)
                if LA23 == WNAME:
                    alt23 = 1
                elif LA23 == CANVAS:
                    alt23 = 2
                elif LA23 == NAME:
                    alt23 = 3
                elif LA23 == COMMENTTEXT:
                    alt23 = 4
                elif LA23 == NEWLINE:
                    alt23 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # kv.g:175:4: widget
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_widget_in_stmt737)
                    widget60 = self.widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, widget60.tree)


                elif alt23 == 2:
                    # kv.g:176:4: canvas
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_canvas_in_stmt742)
                    canvas61 = self.canvas()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, canvas61.tree)


                elif alt23 == 3:
                    # kv.g:177:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_stmt747)
                    prop62 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop62.tree)


                elif alt23 == 4:
                    # kv.g:178:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_stmt752)
                    comment63 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment63.tree)


                elif alt23 == 5:
                    # kv.g:179:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_stmt757)
                    blank64 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank64.tree)


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

        instruction65 = None

        comment66 = None

        blank67 = None



        try:
            try:
                # kv.g:182:2: ( instruction | comment | blank )
                alt24 = 3
                LA24 = self.input.LA(1)
                if LA24 == WNAME:
                    alt24 = 1
                elif LA24 == COMMENTTEXT:
                    alt24 = 2
                elif LA24 == NEWLINE:
                    alt24 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # kv.g:182:4: instruction
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_instruction_in_canvas_stmt768)
                    instruction65 = self.instruction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, instruction65.tree)


                elif alt24 == 2:
                    # kv.g:183:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_canvas_stmt773)
                    comment66 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment66.tree)


                elif alt24 == 3:
                    # kv.g:184:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_canvas_stmt778)
                    blank67 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank67.tree)


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

        WNAME68 = None
        COLON69 = None
        NEWLINE70 = None
        WNAME71 = None
        COLON72 = None
        instruction_body73 = None


        WNAME68_tree = None
        COLON69_tree = None
        NEWLINE70_tree = None
        WNAME71_tree = None
        COLON72_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_instruction_body = RewriteRuleSubtreeStream(self._adaptor, "rule instruction_body")
        try:
            try:
                # kv.g:187:2: ( WNAME ( COLON )? NEWLINE -> ^( INSTRUCTION[$WNAME] ) | WNAME ( COLON )? instruction_body -> ^( INSTRUCTION[$WNAME] instruction_body ) )
                alt27 = 2
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # kv.g:187:4: WNAME ( COLON )? NEWLINE
                    pass 
                    WNAME68=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction789) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME68)
                    # kv.g:187:10: ( COLON )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == COLON) :
                        alt25 = 1
                    if alt25 == 1:
                        # kv.g:187:10: COLON
                        pass 
                        COLON69=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction791) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON69)



                    NEWLINE70=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction794) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE70)

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
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME68), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 2:
                    # kv.g:188:4: WNAME ( COLON )? instruction_body
                    pass 
                    WNAME71=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction809) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME71)
                    # kv.g:188:10: ( COLON )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COLON) :
                        alt26 = 1
                    if alt26 == 1:
                        # kv.g:188:10: COLON
                        pass 
                        COLON72=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction811) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON72)



                    self._state.following.append(self.FOLLOW_instruction_body_in_instruction814)
                    instruction_body73 = self.instruction_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_instruction_body.add(instruction_body73.tree)

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
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME71), root_1)

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
    # kv.g:190:1: instruction_body : NEWLINE ( blank )* INDENT ( instruction_stmt )+ DEDENT ;
    def instruction_body(self, ):

        retval = self.instruction_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE74 = None
        INDENT76 = None
        DEDENT78 = None
        blank75 = None

        instruction_stmt77 = None


        NEWLINE74_tree = None
        INDENT76_tree = None
        DEDENT78_tree = None

        try:
            try:
                # kv.g:191:2: ( NEWLINE ( blank )* INDENT ( instruction_stmt )+ DEDENT )
                # kv.g:191:4: NEWLINE ( blank )* INDENT ( instruction_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE74=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction_body837)
                # kv.g:191:13: ( blank )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == NEWLINE) :
                        alt28 = 1


                    if alt28 == 1:
                        # kv.g:191:13: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_instruction_body840)
                        blank75 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank75.tree)


                    else:
                        break #loop28
                INDENT76=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_instruction_body843)
                # kv.g:191:28: ( instruction_stmt )+
                cnt29 = 0
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == NEWLINE or LA29_0 == COMMENTTEXT or LA29_0 == NAME) :
                        alt29 = 1


                    if alt29 == 1:
                        # kv.g:191:29: instruction_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_instruction_stmt_in_instruction_body847)
                        instruction_stmt77 = self.instruction_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instruction_stmt77.tree)


                    else:
                        if cnt29 >= 1:
                            break #loop29

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(29, self.input)
                        raise eee

                    cnt29 += 1
                DEDENT78=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_instruction_body851)



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

        prop79 = None

        comment80 = None

        blank81 = None



        try:
            try:
                # kv.g:194:2: ( prop | comment | blank )
                alt30 = 3
                LA30 = self.input.LA(1)
                if LA30 == NAME:
                    alt30 = 1
                elif LA30 == COMMENTTEXT:
                    alt30 = 2
                elif LA30 == NEWLINE:
                    alt30 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # kv.g:194:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_instruction_stmt863)
                    prop79 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop79.tree)


                elif alt30 == 2:
                    # kv.g:195:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_instruction_stmt868)
                    comment80 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment80.tree)


                elif alt30 == 3:
                    # kv.g:196:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_instruction_stmt873)
                    blank81 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank81.tree)


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

        CANVAS82 = None
        COLON83 = None
        canvas_body84 = None


        CANVAS82_tree = None
        COLON83_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_CANVAS = RewriteRuleTokenStream(self._adaptor, "token CANVAS")
        stream_canvas_body = RewriteRuleSubtreeStream(self._adaptor, "rule canvas_body")
        try:
            try:
                # kv.g:199:2: ( CANVAS COLON canvas_body -> ^( CANVASRULE[$CANVAS] canvas_body ) )
                # kv.g:199:4: CANVAS COLON canvas_body
                pass 
                CANVAS82=self.match(self.input, CANVAS, self.FOLLOW_CANVAS_in_canvas884) 
                if self._state.backtracking == 0:
                    stream_CANVAS.add(CANVAS82)
                COLON83=self.match(self.input, COLON, self.FOLLOW_COLON_in_canvas886) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON83)
                self._state.following.append(self.FOLLOW_canvas_body_in_canvas888)
                canvas_body84 = self.canvas_body()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_canvas_body.add(canvas_body84.tree)

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
                    root_1 = self._adaptor.becomeRoot(CanvasNode(CANVASRULE, CANVAS82), root_1)

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

        NAME85 = None
        COLON86 = None
        WS87 = None
        NAME88 = None
        COLON89 = None
        WS90 = None
        NEWLINE91 = None
        p = None


        NAME85_tree = None
        COLON86_tree = None
        WS87_tree = None
        NAME88_tree = None
        COLON89_tree = None
        WS90_tree = None
        NEWLINE91_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_prop_value = RewriteRuleSubtreeStream(self._adaptor, "rule prop_value")
        stream_property_body = RewriteRuleSubtreeStream(self._adaptor, "rule property_body")
        try:
            try:
                # kv.g:202:2: ( NAME COLON ( WS )* p= property_body -> ^( PROPERTY[$NAME,$p.tree] ) | NAME COLON ( WS )* p= prop_value NEWLINE -> ^( PROPERTY[$NAME,$p.tree] ) )
                alt33 = 2
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # kv.g:202:4: NAME COLON ( WS )* p= property_body
                    pass 
                    NAME85=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop909) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME85)
                    COLON86=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop911) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON86)
                    # kv.g:202:15: ( WS )*
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == WS) :
                            alt31 = 1


                        if alt31 == 1:
                            # kv.g:202:15: WS
                            pass 
                            WS87=self.match(self.input, WS, self.FOLLOW_WS_in_prop913) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS87)


                        else:
                            break #loop31
                    self._state.following.append(self.FOLLOW_property_body_in_prop918)
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
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME85, p.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt33 == 2:
                    # kv.g:203:4: NAME COLON ( WS )* p= prop_value NEWLINE
                    pass 
                    NAME88=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop933) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME88)
                    COLON89=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop935) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON89)
                    # kv.g:203:15: ( WS )*
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == WS) :
                            alt32 = 1


                        if alt32 == 1:
                            # kv.g:203:15: WS
                            pass 
                            WS90=self.match(self.input, WS, self.FOLLOW_WS_in_prop937) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS90)


                        else:
                            break #loop32
                    self._state.following.append(self.FOLLOW_prop_value_in_prop942)
                    p = self.prop_value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prop_value.add(p.tree)
                    NEWLINE91=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_prop944) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE91)

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
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME88, p.tree), root_1)

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
    # kv.g:205:1: property_body : NEWLINE ( blank )* INDENT prop_value ( NEWLINE prop_value )* DEDENT ;
    def property_body(self, ):

        retval = self.property_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE92 = None
        INDENT94 = None
        NEWLINE96 = None
        DEDENT98 = None
        blank93 = None

        prop_value95 = None

        prop_value97 = None


        NEWLINE92_tree = None
        INDENT94_tree = None
        NEWLINE96_tree = None
        DEDENT98_tree = None

        try:
            try:
                # kv.g:206:2: ( NEWLINE ( blank )* INDENT prop_value ( NEWLINE prop_value )* DEDENT )
                # kv.g:206:4: NEWLINE ( blank )* INDENT prop_value ( NEWLINE prop_value )* DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE92=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_property_body964)
                # kv.g:206:13: ( blank )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == NEWLINE) :
                        alt34 = 1


                    if alt34 == 1:
                        # kv.g:206:13: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_property_body967)
                        blank93 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank93.tree)


                    else:
                        break #loop34
                INDENT94=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_property_body970)
                self._state.following.append(self.FOLLOW_prop_value_in_property_body973)
                prop_value95 = self.prop_value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, prop_value95.tree)
                # kv.g:206:39: ( NEWLINE prop_value )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == NEWLINE) :
                        alt35 = 1


                    if alt35 == 1:
                        # kv.g:206:40: NEWLINE prop_value
                        pass 
                        NEWLINE96=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_property_body976)
                        self._state.following.append(self.FOLLOW_prop_value_in_property_body979)
                        prop_value97 = self.prop_value()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, prop_value97.tree)


                    else:
                        break #loop35
                DEDENT98=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_property_body983)



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
                self._state.following.append(self.FOLLOW_python_in_prop_value996)
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

        simple_stmt99 = None

        compound_stmt100 = None



        try:
            try:
                # kv.g:215:2: ( simple_stmt | compound_stmt )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == WNAME or (PLUS <= LA36_0 <= MINUS) or LA36_0 == NAME or LA36_0 == LPAREN or LA36_0 == NOT or (TILDE <= LA36_0 <= LBRACK) or LA36_0 == LCURLY or (BACKQUOTE <= LA36_0 <= STRING) or (86 <= LA36_0 <= 92) or LA36_0 == 94 or (106 <= LA36_0 <= 107)) :
                    alt36 = 1
                elif (LA36_0 == 95 or (98 <= LA36_0 <= 100) or LA36_0 == 102) :
                    alt36 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # kv.g:215:6: simple_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_stmt_in_python1019)
                    simple_stmt99 = self.simple_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_stmt99.tree)


                elif alt36 == 2:
                    # kv.g:216:6: compound_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_compound_stmt_in_python1026)
                    compound_stmt100 = self.compound_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, compound_stmt100.tree)


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

        SEMI102 = None
        SEMI104 = None
        small_stmt101 = None

        small_stmt103 = None


        SEMI102_tree = None
        SEMI104_tree = None

        try:
            try:
                # kv.g:219:2: ( small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )? )
                # kv.g:219:4: small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_small_stmt_in_simple_stmt1036)
                small_stmt101 = self.small_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, small_stmt101.tree)
                # kv.g:219:15: ( options {greedy=true; } : SEMI small_stmt )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == SEMI) :
                        LA37_1 = self.input.LA(2)

                        if (LA37_1 == WNAME or (PLUS <= LA37_1 <= MINUS) or LA37_1 == NAME or LA37_1 == LPAREN or LA37_1 == NOT or (TILDE <= LA37_1 <= LBRACK) or LA37_1 == LCURLY or (BACKQUOTE <= LA37_1 <= STRING) or (86 <= LA37_1 <= 92) or LA37_1 == 94 or (106 <= LA37_1 <= 107)) :
                            alt37 = 1




                    if alt37 == 1:
                        # kv.g:219:39: SEMI small_stmt
                        pass 
                        SEMI102=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_simple_stmt1046)
                        if self._state.backtracking == 0:

                            SEMI102_tree = self._adaptor.createWithPayload(SEMI102)
                            self._adaptor.addChild(root_0, SEMI102_tree)

                        self._state.following.append(self.FOLLOW_small_stmt_in_simple_stmt1048)
                        small_stmt103 = self.small_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, small_stmt103.tree)


                    else:
                        break #loop37
                # kv.g:219:57: ( SEMI )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == SEMI) :
                    alt38 = 1
                if alt38 == 1:
                    # kv.g:219:58: SEMI
                    pass 
                    SEMI104=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_simple_stmt1053)
                    if self._state.backtracking == 0:

                        SEMI104_tree = self._adaptor.createWithPayload(SEMI104)
                        self._adaptor.addChild(root_0, SEMI104_tree)







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

        expr_stmt105 = None

        print_stmt106 = None

        del_stmt107 = None

        pass_stmt108 = None

        flow_stmt109 = None

        exec_stmt110 = None

        assert_stmt111 = None



        try:
            try:
                # kv.g:222:2: ( expr_stmt | print_stmt | del_stmt | pass_stmt | flow_stmt | exec_stmt | assert_stmt )
                alt39 = 7
                LA39 = self.input.LA(1)
                if LA39 == WNAME or LA39 == PLUS or LA39 == MINUS or LA39 == NAME or LA39 == LPAREN or LA39 == NOT or LA39 == TILDE or LA39 == LBRACK or LA39 == LCURLY or LA39 == BACKQUOTE or LA39 == NONE or LA39 == INT or LA39 == LONGINT or LA39 == FLOAT or LA39 == COMPLEX or LA39 == STRING or LA39 == 106:
                    alt39 = 1
                elif LA39 == 86:
                    alt39 = 2
                elif LA39 == 87:
                    alt39 = 3
                elif LA39 == 88:
                    alt39 = 4
                elif LA39 == 89 or LA39 == 90 or LA39 == 91 or LA39 == 107:
                    alt39 = 5
                elif LA39 == 92:
                    alt39 = 6
                elif LA39 == 94:
                    alt39 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # kv.g:222:4: expr_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_stmt_in_small_stmt1066)
                    expr_stmt105 = self.expr_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr_stmt105.tree)


                elif alt39 == 2:
                    # kv.g:223:6: print_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_print_stmt_in_small_stmt1073)
                    print_stmt106 = self.print_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, print_stmt106.tree)


                elif alt39 == 3:
                    # kv.g:224:6: del_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_del_stmt_in_small_stmt1080)
                    del_stmt107 = self.del_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, del_stmt107.tree)


                elif alt39 == 4:
                    # kv.g:225:6: pass_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pass_stmt_in_small_stmt1087)
                    pass_stmt108 = self.pass_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pass_stmt108.tree)


                elif alt39 == 5:
                    # kv.g:226:6: flow_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flow_stmt_in_small_stmt1094)
                    flow_stmt109 = self.flow_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, flow_stmt109.tree)


                elif alt39 == 6:
                    # kv.g:227:6: exec_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_exec_stmt_in_small_stmt1101)
                    exec_stmt110 = self.exec_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, exec_stmt110.tree)


                elif alt39 == 7:
                    # kv.g:228:6: assert_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assert_stmt_in_small_stmt1108)
                    assert_stmt111 = self.assert_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assert_stmt111.tree)


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

        COMMA113 = None
        COMMA115 = None
        STAR116 = None
        COMMA118 = None
        DOUBLESTAR119 = None
        DOUBLESTAR121 = None
        STAR123 = None
        COMMA125 = None
        DOUBLESTAR126 = None
        DOUBLESTAR128 = None
        defparameter112 = None

        defparameter114 = None

        identifier117 = None

        identifier120 = None

        identifier122 = None

        identifier124 = None

        identifier127 = None

        identifier129 = None


        COMMA113_tree = None
        COMMA115_tree = None
        STAR116_tree = None
        COMMA118_tree = None
        DOUBLESTAR119_tree = None
        DOUBLESTAR121_tree = None
        STAR123_tree = None
        COMMA125_tree = None
        DOUBLESTAR126_tree = None
        DOUBLESTAR128_tree = None

        try:
            try:
                # kv.g:231:2: ( defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )? | STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )
                alt45 = 3
                LA45 = self.input.LA(1)
                if LA45 == WNAME or LA45 == NAME or LA45 == LPAREN:
                    alt45 = 1
                elif LA45 == STAR:
                    alt45 = 2
                elif LA45 == DOUBLESTAR:
                    alt45 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # kv.g:231:4: defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_defparameter_in_varargslist1118)
                    defparameter112 = self.defparameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, defparameter112.tree)
                    # kv.g:231:17: ( options {greedy=true; } : COMMA defparameter )*
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == COMMA) :
                            LA40_1 = self.input.LA(2)

                            if (LA40_1 == WNAME or LA40_1 == NAME or LA40_1 == LPAREN) :
                                alt40 = 1




                        if alt40 == 1:
                            # kv.g:231:41: COMMA defparameter
                            pass 
                            COMMA113=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1128)
                            if self._state.backtracking == 0:

                                COMMA113_tree = self._adaptor.createWithPayload(COMMA113)
                                self._adaptor.addChild(root_0, COMMA113_tree)

                            self._state.following.append(self.FOLLOW_defparameter_in_varargslist1130)
                            defparameter114 = self.defparameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, defparameter114.tree)


                        else:
                            break #loop40
                    # kv.g:231:62: ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == COMMA) :
                        alt43 = 1
                    if alt43 == 1:
                        # kv.g:231:63: COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        pass 
                        COMMA115=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1135)
                        if self._state.backtracking == 0:

                            COMMA115_tree = self._adaptor.createWithPayload(COMMA115)
                            self._adaptor.addChild(root_0, COMMA115_tree)

                        # kv.g:231:69: ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        alt42 = 3
                        LA42_0 = self.input.LA(1)

                        if (LA42_0 == STAR) :
                            alt42 = 1
                        elif (LA42_0 == DOUBLESTAR) :
                            alt42 = 2
                        if alt42 == 1:
                            # kv.g:231:71: STAR identifier ( COMMA DOUBLESTAR identifier )?
                            pass 
                            STAR116=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1139)
                            if self._state.backtracking == 0:

                                STAR116_tree = self._adaptor.createWithPayload(STAR116)
                                self._adaptor.addChild(root_0, STAR116_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1141)
                            identifier117 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier117.tree)
                            # kv.g:231:87: ( COMMA DOUBLESTAR identifier )?
                            alt41 = 2
                            LA41_0 = self.input.LA(1)

                            if (LA41_0 == COMMA) :
                                alt41 = 1
                            if alt41 == 1:
                                # kv.g:231:88: COMMA DOUBLESTAR identifier
                                pass 
                                COMMA118=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1144)
                                if self._state.backtracking == 0:

                                    COMMA118_tree = self._adaptor.createWithPayload(COMMA118)
                                    self._adaptor.addChild(root_0, COMMA118_tree)

                                DOUBLESTAR119=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1146)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR119_tree = self._adaptor.createWithPayload(DOUBLESTAR119)
                                    self._adaptor.addChild(root_0, DOUBLESTAR119_tree)

                                self._state.following.append(self.FOLLOW_identifier_in_varargslist1148)
                                identifier120 = self.identifier()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, identifier120.tree)





                        elif alt42 == 2:
                            # kv.g:231:120: DOUBLESTAR identifier
                            pass 
                            DOUBLESTAR121=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1154)
                            if self._state.backtracking == 0:

                                DOUBLESTAR121_tree = self._adaptor.createWithPayload(DOUBLESTAR121)
                                self._adaptor.addChild(root_0, DOUBLESTAR121_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1156)
                            identifier122 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier122.tree)








                elif alt45 == 2:
                    # kv.g:232:4: STAR identifier ( COMMA DOUBLESTAR identifier )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR123=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1167)
                    if self._state.backtracking == 0:

                        STAR123_tree = self._adaptor.createWithPayload(STAR123)
                        self._adaptor.addChild(root_0, STAR123_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1169)
                    identifier124 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier124.tree)
                    # kv.g:232:20: ( COMMA DOUBLESTAR identifier )?
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == COMMA) :
                        alt44 = 1
                    if alt44 == 1:
                        # kv.g:232:21: COMMA DOUBLESTAR identifier
                        pass 
                        COMMA125=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1172)
                        if self._state.backtracking == 0:

                            COMMA125_tree = self._adaptor.createWithPayload(COMMA125)
                            self._adaptor.addChild(root_0, COMMA125_tree)

                        DOUBLESTAR126=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1174)
                        if self._state.backtracking == 0:

                            DOUBLESTAR126_tree = self._adaptor.createWithPayload(DOUBLESTAR126)
                            self._adaptor.addChild(root_0, DOUBLESTAR126_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_varargslist1176)
                        identifier127 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier127.tree)





                elif alt45 == 3:
                    # kv.g:233:4: DOUBLESTAR identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR128=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1183)
                    if self._state.backtracking == 0:

                        DOUBLESTAR128_tree = self._adaptor.createWithPayload(DOUBLESTAR128)
                        self._adaptor.addChild(root_0, DOUBLESTAR128_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1185)
                    identifier129 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier129.tree)


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

        ASSIGN131 = None
        fpdef130 = None

        test132 = None


        ASSIGN131_tree = None

        try:
            try:
                # kv.g:236:2: ( fpdef ( ASSIGN test )? )
                # kv.g:236:4: fpdef ( ASSIGN test )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_defparameter1195)
                fpdef130 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef130.tree)
                # kv.g:236:10: ( ASSIGN test )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == ASSIGN) :
                    alt46 = 1
                if alt46 == 1:
                    # kv.g:236:11: ASSIGN test
                    pass 
                    ASSIGN131=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_defparameter1198)
                    if self._state.backtracking == 0:

                        ASSIGN131_tree = self._adaptor.createWithPayload(ASSIGN131)
                        self._adaptor.addChild(root_0, ASSIGN131_tree)

                    self._state.following.append(self.FOLLOW_test_in_defparameter1200)
                    test132 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test132.tree)






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

        LPAREN134 = None
        RPAREN136 = None
        identifier133 = None

        fplist135 = None


        LPAREN134_tree = None
        RPAREN136_tree = None

        try:
            try:
                # kv.g:239:2: ( identifier | LPAREN fplist RPAREN )
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == WNAME or LA47_0 == NAME) :
                    alt47 = 1
                elif (LA47_0 == LPAREN) :
                    alt47 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # kv.g:239:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_fpdef1212)
                    identifier133 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier133.tree)


                elif alt47 == 2:
                    # kv.g:240:4: LPAREN fplist RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN134=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_fpdef1217)
                    if self._state.backtracking == 0:

                        LPAREN134_tree = self._adaptor.createWithPayload(LPAREN134)
                        self._adaptor.addChild(root_0, LPAREN134_tree)

                    self._state.following.append(self.FOLLOW_fplist_in_fpdef1219)
                    fplist135 = self.fplist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fplist135.tree)
                    RPAREN136=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_fpdef1221)
                    if self._state.backtracking == 0:

                        RPAREN136_tree = self._adaptor.createWithPayload(RPAREN136)
                        self._adaptor.addChild(root_0, RPAREN136_tree)



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

        COMMA138 = None
        COMMA140 = None
        fpdef137 = None

        fpdef139 = None


        COMMA138_tree = None
        COMMA140_tree = None

        try:
            try:
                # kv.g:243:2: ( fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )? )
                # kv.g:243:4: fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_fplist1231)
                fpdef137 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef137.tree)
                # kv.g:243:10: ( options {greedy=true; } : COMMA fpdef )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == COMMA) :
                        LA48_1 = self.input.LA(2)

                        if (LA48_1 == WNAME or LA48_1 == NAME or LA48_1 == LPAREN) :
                            alt48 = 1




                    if alt48 == 1:
                        # kv.g:243:34: COMMA fpdef
                        pass 
                        COMMA138=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1241)
                        if self._state.backtracking == 0:

                            COMMA138_tree = self._adaptor.createWithPayload(COMMA138)
                            self._adaptor.addChild(root_0, COMMA138_tree)

                        self._state.following.append(self.FOLLOW_fpdef_in_fplist1243)
                        fpdef139 = self.fpdef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fpdef139.tree)


                    else:
                        break #loop48
                # kv.g:243:48: ( COMMA )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == COMMA) :
                    alt49 = 1
                if alt49 == 1:
                    # kv.g:243:49: COMMA
                    pass 
                    COMMA140=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1248)
                    if self._state.backtracking == 0:

                        COMMA140_tree = self._adaptor.createWithPayload(COMMA140)
                        self._adaptor.addChild(root_0, COMMA140_tree)







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

        testlist141 = None

        augassign142 = None

        yield_expr143 = None

        augassign144 = None

        testlist145 = None

        assigns146 = None



        try:
            try:
                # kv.g:246:2: ( testlist ( augassign yield_expr | augassign testlist | assigns )? )
                # kv.g:246:4: testlist ( augassign yield_expr | augassign testlist | assigns )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1261)
                testlist141 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist141.tree)
                # kv.g:246:13: ( augassign yield_expr | augassign testlist | assigns )?
                alt50 = 4
                LA50_0 = self.input.LA(1)

                if ((PLUSEQUAL <= LA50_0 <= DOUBLESLASHEQUAL)) :
                    LA50_1 = self.input.LA(2)

                    if (LA50_1 == 107) :
                        alt50 = 1
                    elif (LA50_1 == WNAME or (PLUS <= LA50_1 <= MINUS) or LA50_1 == NAME or LA50_1 == LPAREN or LA50_1 == NOT or (TILDE <= LA50_1 <= LBRACK) or LA50_1 == LCURLY or (BACKQUOTE <= LA50_1 <= STRING) or LA50_1 == 106) :
                        alt50 = 2
                elif (LA50_0 == ASSIGN) :
                    alt50 = 3
                if alt50 == 1:
                    # kv.g:246:14: augassign yield_expr
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1264)
                    augassign142 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign142.tree)
                    self._state.following.append(self.FOLLOW_yield_expr_in_expr_stmt1266)
                    yield_expr143 = self.yield_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_expr143.tree)


                elif alt50 == 2:
                    # kv.g:246:37: augassign testlist
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1270)
                    augassign144 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign144.tree)
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1272)
                    testlist145 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist145.tree)


                elif alt50 == 3:
                    # kv.g:246:58: assigns
                    pass 
                    self._state.following.append(self.FOLLOW_assigns_in_expr_stmt1276)
                    assigns146 = self.assigns()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assigns146.tree)






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

        assign_testlist147 = None

        assign_yield148 = None



        try:
            try:
                # kv.g:249:2: ( ( assign_testlist )+ | ( assign_yield )+ )
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == ASSIGN) :
                    LA53_1 = self.input.LA(2)

                    if (LA53_1 == WNAME or (PLUS <= LA53_1 <= MINUS) or LA53_1 == NAME or LA53_1 == LPAREN or LA53_1 == NOT or (TILDE <= LA53_1 <= LBRACK) or LA53_1 == LCURLY or (BACKQUOTE <= LA53_1 <= STRING) or LA53_1 == 106) :
                        alt53 = 1
                    elif (LA53_1 == 107) :
                        alt53 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 53, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # kv.g:249:4: ( assign_testlist )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:249:4: ( assign_testlist )+
                    cnt51 = 0
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == ASSIGN) :
                            alt51 = 1


                        if alt51 == 1:
                            # kv.g:249:4: assign_testlist
                            pass 
                            self._state.following.append(self.FOLLOW_assign_testlist_in_assigns1289)
                            assign_testlist147 = self.assign_testlist()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_testlist147.tree)


                        else:
                            if cnt51 >= 1:
                                break #loop51

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(51, self.input)
                            raise eee

                        cnt51 += 1


                elif alt53 == 2:
                    # kv.g:249:23: ( assign_yield )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:249:23: ( assign_yield )+
                    cnt52 = 0
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == ASSIGN) :
                            alt52 = 1


                        if alt52 == 1:
                            # kv.g:249:23: assign_yield
                            pass 
                            self._state.following.append(self.FOLLOW_assign_yield_in_assigns1294)
                            assign_yield148 = self.assign_yield()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_yield148.tree)


                        else:
                            if cnt52 >= 1:
                                break #loop52

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(52, self.input)
                            raise eee

                        cnt52 += 1


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

        ASSIGN149 = None
        testlist150 = None


        ASSIGN149_tree = None

        try:
            try:
                # kv.g:252:2: ( ASSIGN testlist )
                # kv.g:252:4: ASSIGN testlist
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN149=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_testlist1306)
                if self._state.backtracking == 0:

                    ASSIGN149_tree = self._adaptor.createWithPayload(ASSIGN149)
                    self._adaptor.addChild(root_0, ASSIGN149_tree)

                self._state.following.append(self.FOLLOW_testlist_in_assign_testlist1308)
                testlist150 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist150.tree)



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

        ASSIGN151 = None
        yield_expr152 = None


        ASSIGN151_tree = None

        try:
            try:
                # kv.g:255:2: ( ASSIGN yield_expr )
                # kv.g:255:4: ASSIGN yield_expr
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN151=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_yield1319)
                if self._state.backtracking == 0:

                    ASSIGN151_tree = self._adaptor.createWithPayload(ASSIGN151)
                    self._adaptor.addChild(root_0, ASSIGN151_tree)

                self._state.following.append(self.FOLLOW_yield_expr_in_assign_yield1321)
                yield_expr152 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr152.tree)



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

        set153 = None

        set153_tree = None

        try:
            try:
                # kv.g:258:2: ( PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set153 = self.input.LT(1)
                if (PLUSEQUAL <= self.input.LA(1) <= DOUBLESLASHEQUAL):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set153))
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

        string_literal154 = None
        RIGHTSHIFT156 = None
        printlist155 = None

        printlist157 = None


        string_literal154_tree = None
        RIGHTSHIFT156_tree = None

        try:
            try:
                # kv.g:263:2: ( 'print' ( printlist | RIGHTSHIFT printlist )? )
                # kv.g:263:6: 'print' ( printlist | RIGHTSHIFT printlist )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal154=self.match(self.input, 86, self.FOLLOW_86_in_print_stmt1391)
                if self._state.backtracking == 0:

                    string_literal154_tree = self._adaptor.createWithPayload(string_literal154)
                    self._adaptor.addChild(root_0, string_literal154_tree)

                # kv.g:263:14: ( printlist | RIGHTSHIFT printlist )?
                alt54 = 3
                LA54_0 = self.input.LA(1)

                if (LA54_0 == WNAME or (PLUS <= LA54_0 <= MINUS) or LA54_0 == NAME or LA54_0 == LPAREN or LA54_0 == NOT or (TILDE <= LA54_0 <= LBRACK) or LA54_0 == LCURLY or (BACKQUOTE <= LA54_0 <= STRING) or LA54_0 == 106) :
                    alt54 = 1
                elif (LA54_0 == RIGHTSHIFT) :
                    alt54 = 2
                if alt54 == 1:
                    # kv.g:263:15: printlist
                    pass 
                    self._state.following.append(self.FOLLOW_printlist_in_print_stmt1394)
                    printlist155 = self.printlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, printlist155.tree)


                elif alt54 == 2:
                    # kv.g:263:27: RIGHTSHIFT printlist
                    pass 
                    RIGHTSHIFT156=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_print_stmt1398)
                    if self._state.backtracking == 0:

                        RIGHTSHIFT156_tree = self._adaptor.createWithPayload(RIGHTSHIFT156)
                        self._adaptor.addChild(root_0, RIGHTSHIFT156_tree)

                    self._state.following.append(self.FOLLOW_printlist_in_print_stmt1400)
                    printlist157 = self.printlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, printlist157.tree)






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

        COMMA159 = None
        COMMA161 = None
        test158 = None

        test160 = None


        COMMA159_tree = None
        COMMA161_tree = None

        try:
            try:
                # kv.g:266:2: ( test ( options {k=2; } : COMMA test )* ( COMMA )? )
                # kv.g:266:6: test ( options {k=2; } : COMMA test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_printlist1418)
                test158 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test158.tree)
                # kv.g:266:11: ( options {k=2; } : COMMA test )*
                while True: #loop55
                    alt55 = 2
                    alt55 = self.dfa55.predict(self.input)
                    if alt55 == 1:
                        # kv.g:266:28: COMMA test
                        pass 
                        COMMA159=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_printlist1429)
                        if self._state.backtracking == 0:

                            COMMA159_tree = self._adaptor.createWithPayload(COMMA159)
                            self._adaptor.addChild(root_0, COMMA159_tree)

                        self._state.following.append(self.FOLLOW_test_in_printlist1431)
                        test160 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test160.tree)


                    else:
                        break #loop55
                # kv.g:266:41: ( COMMA )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == COMMA) :
                    alt56 = 1
                if alt56 == 1:
                    # kv.g:266:42: COMMA
                    pass 
                    COMMA161=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_printlist1436)
                    if self._state.backtracking == 0:

                        COMMA161_tree = self._adaptor.createWithPayload(COMMA161)
                        self._adaptor.addChild(root_0, COMMA161_tree)







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

        string_literal162 = None
        exprlist163 = None


        string_literal162_tree = None

        try:
            try:
                # kv.g:269:2: ( 'del' exprlist )
                # kv.g:269:6: 'del' exprlist
                pass 
                root_0 = self._adaptor.nil()

                string_literal162=self.match(self.input, 87, self.FOLLOW_87_in_del_stmt1450)
                if self._state.backtracking == 0:

                    string_literal162_tree = self._adaptor.createWithPayload(string_literal162)
                    self._adaptor.addChild(root_0, string_literal162_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_del_stmt1452)
                exprlist163 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist163.tree)



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

        string_literal164 = None

        string_literal164_tree = None

        try:
            try:
                # kv.g:272:2: ( 'pass' )
                # kv.g:272:6: 'pass'
                pass 
                root_0 = self._adaptor.nil()

                string_literal164=self.match(self.input, 88, self.FOLLOW_88_in_pass_stmt1464)
                if self._state.backtracking == 0:

                    string_literal164_tree = self._adaptor.createWithPayload(string_literal164)
                    self._adaptor.addChild(root_0, string_literal164_tree)




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

        break_stmt165 = None

        continue_stmt166 = None

        raise_stmt167 = None

        yield_stmt168 = None



        try:
            try:
                # kv.g:275:2: ( break_stmt | continue_stmt | raise_stmt | yield_stmt )
                alt57 = 4
                LA57 = self.input.LA(1)
                if LA57 == 89:
                    alt57 = 1
                elif LA57 == 90:
                    alt57 = 2
                elif LA57 == 91:
                    alt57 = 3
                elif LA57 == 107:
                    alt57 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # kv.g:275:6: break_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_break_stmt_in_flow_stmt1476)
                    break_stmt165 = self.break_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, break_stmt165.tree)


                elif alt57 == 2:
                    # kv.g:276:6: continue_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_continue_stmt_in_flow_stmt1483)
                    continue_stmt166 = self.continue_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, continue_stmt166.tree)


                elif alt57 == 3:
                    # kv.g:278:6: raise_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_raise_stmt_in_flow_stmt1492)
                    raise_stmt167 = self.raise_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, raise_stmt167.tree)


                elif alt57 == 4:
                    # kv.g:279:6: yield_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_yield_stmt_in_flow_stmt1499)
                    yield_stmt168 = self.yield_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_stmt168.tree)


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

        string_literal169 = None

        string_literal169_tree = None

        try:
            try:
                # kv.g:282:2: ( 'break' )
                # kv.g:282:6: 'break'
                pass 
                root_0 = self._adaptor.nil()

                string_literal169=self.match(self.input, 89, self.FOLLOW_89_in_break_stmt1511)
                if self._state.backtracking == 0:

                    string_literal169_tree = self._adaptor.createWithPayload(string_literal169)
                    self._adaptor.addChild(root_0, string_literal169_tree)




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

        string_literal170 = None

        string_literal170_tree = None

        try:
            try:
                # kv.g:285:2: ( 'continue' )
                # kv.g:285:6: 'continue'
                pass 
                root_0 = self._adaptor.nil()

                string_literal170=self.match(self.input, 90, self.FOLLOW_90_in_continue_stmt1523)
                if self._state.backtracking == 0:

                    string_literal170_tree = self._adaptor.createWithPayload(string_literal170)
                    self._adaptor.addChild(root_0, string_literal170_tree)




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

        yield_expr171 = None



        try:
            try:
                # kv.g:288:2: ( yield_expr )
                # kv.g:288:4: yield_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_yield_expr_in_yield_stmt1533)
                yield_expr171 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr171.tree)



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

        string_literal172 = None
        COMMA174 = None
        COMMA176 = None
        test173 = None

        test175 = None

        test177 = None


        string_literal172_tree = None
        COMMA174_tree = None
        COMMA176_tree = None

        try:
            try:
                # kv.g:291:2: ( 'raise' ( test ( COMMA test ( COMMA test )? )? )? )
                # kv.g:291:4: 'raise' ( test ( COMMA test ( COMMA test )? )? )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal172=self.match(self.input, 91, self.FOLLOW_91_in_raise_stmt1543)
                if self._state.backtracking == 0:

                    string_literal172_tree = self._adaptor.createWithPayload(string_literal172)
                    self._adaptor.addChild(root_0, string_literal172_tree)

                # kv.g:291:12: ( test ( COMMA test ( COMMA test )? )? )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == WNAME or (PLUS <= LA60_0 <= MINUS) or LA60_0 == NAME or LA60_0 == LPAREN or LA60_0 == NOT or (TILDE <= LA60_0 <= LBRACK) or LA60_0 == LCURLY or (BACKQUOTE <= LA60_0 <= STRING) or LA60_0 == 106) :
                    alt60 = 1
                if alt60 == 1:
                    # kv.g:291:13: test ( COMMA test ( COMMA test )? )?
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_raise_stmt1546)
                    test173 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test173.tree)
                    # kv.g:291:18: ( COMMA test ( COMMA test )? )?
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == COMMA) :
                        alt59 = 1
                    if alt59 == 1:
                        # kv.g:291:19: COMMA test ( COMMA test )?
                        pass 
                        COMMA174=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1549)
                        if self._state.backtracking == 0:

                            COMMA174_tree = self._adaptor.createWithPayload(COMMA174)
                            self._adaptor.addChild(root_0, COMMA174_tree)

                        self._state.following.append(self.FOLLOW_test_in_raise_stmt1551)
                        test175 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test175.tree)
                        # kv.g:291:30: ( COMMA test )?
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if (LA58_0 == COMMA) :
                            alt58 = 1
                        if alt58 == 1:
                            # kv.g:291:31: COMMA test
                            pass 
                            COMMA176=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1554)
                            if self._state.backtracking == 0:

                                COMMA176_tree = self._adaptor.createWithPayload(COMMA176)
                                self._adaptor.addChild(root_0, COMMA176_tree)

                            self._state.following.append(self.FOLLOW_test_in_raise_stmt1556)
                            test177 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test177.tree)












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

        string_literal178 = None
        string_literal180 = None
        COMMA182 = None
        expr179 = None

        test181 = None

        test183 = None


        string_literal178_tree = None
        string_literal180_tree = None
        COMMA182_tree = None

        try:
            try:
                # kv.g:294:2: ( 'exec' expr ( 'in' test ( COMMA test )? )? )
                # kv.g:294:6: 'exec' expr ( 'in' test ( COMMA test )? )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal178=self.match(self.input, 92, self.FOLLOW_92_in_exec_stmt1574)
                if self._state.backtracking == 0:

                    string_literal178_tree = self._adaptor.createWithPayload(string_literal178)
                    self._adaptor.addChild(root_0, string_literal178_tree)

                self._state.following.append(self.FOLLOW_expr_in_exec_stmt1576)
                expr179 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr179.tree)
                # kv.g:294:18: ( 'in' test ( COMMA test )? )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == 93) :
                    alt62 = 1
                if alt62 == 1:
                    # kv.g:294:19: 'in' test ( COMMA test )?
                    pass 
                    string_literal180=self.match(self.input, 93, self.FOLLOW_93_in_exec_stmt1579)
                    if self._state.backtracking == 0:

                        string_literal180_tree = self._adaptor.createWithPayload(string_literal180)
                        self._adaptor.addChild(root_0, string_literal180_tree)

                    self._state.following.append(self.FOLLOW_test_in_exec_stmt1581)
                    test181 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test181.tree)
                    # kv.g:294:29: ( COMMA test )?
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == COMMA) :
                        alt61 = 1
                    if alt61 == 1:
                        # kv.g:294:30: COMMA test
                        pass 
                        COMMA182=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exec_stmt1584)
                        if self._state.backtracking == 0:

                            COMMA182_tree = self._adaptor.createWithPayload(COMMA182)
                            self._adaptor.addChild(root_0, COMMA182_tree)

                        self._state.following.append(self.FOLLOW_test_in_exec_stmt1586)
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

        string_literal184 = None
        COMMA186 = None
        test185 = None

        test187 = None


        string_literal184_tree = None
        COMMA186_tree = None

        try:
            try:
                # kv.g:297:2: ( 'assert' test ( COMMA test )? )
                # kv.g:297:6: 'assert' test ( COMMA test )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal184=self.match(self.input, 94, self.FOLLOW_94_in_assert_stmt1602)
                if self._state.backtracking == 0:

                    string_literal184_tree = self._adaptor.createWithPayload(string_literal184)
                    self._adaptor.addChild(root_0, string_literal184_tree)

                self._state.following.append(self.FOLLOW_test_in_assert_stmt1604)
                test185 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test185.tree)
                # kv.g:297:20: ( COMMA test )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == COMMA) :
                    alt63 = 1
                if alt63 == 1:
                    # kv.g:297:21: COMMA test
                    pass 
                    COMMA186=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_assert_stmt1607)
                    if self._state.backtracking == 0:

                        COMMA186_tree = self._adaptor.createWithPayload(COMMA186)
                        self._adaptor.addChild(root_0, COMMA186_tree)

                    self._state.following.append(self.FOLLOW_test_in_assert_stmt1609)
                    test187 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test187.tree)






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

        if_stmt188 = None

        while_stmt189 = None

        for_stmt190 = None

        try_stmt191 = None

        with_stmt192 = None



        try:
            try:
                # kv.g:300:2: ( if_stmt | while_stmt | for_stmt | try_stmt | with_stmt )
                alt64 = 5
                LA64 = self.input.LA(1)
                if LA64 == 95:
                    alt64 = 1
                elif LA64 == 98:
                    alt64 = 2
                elif LA64 == 99:
                    alt64 = 3
                elif LA64 == 100:
                    alt64 = 4
                elif LA64 == 102:
                    alt64 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 64, 0, self.input)

                    raise nvae

                if alt64 == 1:
                    # kv.g:300:6: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_stmt_in_compound_stmt1623)
                    if_stmt188 = self.if_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_stmt188.tree)


                elif alt64 == 2:
                    # kv.g:301:6: while_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_while_stmt_in_compound_stmt1630)
                    while_stmt189 = self.while_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, while_stmt189.tree)


                elif alt64 == 3:
                    # kv.g:302:6: for_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_for_stmt_in_compound_stmt1637)
                    for_stmt190 = self.for_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, for_stmt190.tree)


                elif alt64 == 4:
                    # kv.g:303:6: try_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_try_stmt_in_compound_stmt1644)
                    try_stmt191 = self.try_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, try_stmt191.tree)


                elif alt64 == 5:
                    # kv.g:304:6: with_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_with_stmt_in_compound_stmt1651)
                    with_stmt192 = self.with_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, with_stmt192.tree)


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

        string_literal193 = None
        COLON195 = None
        string_literal198 = None
        COLON199 = None
        test194 = None

        suite196 = None

        elif_clause197 = None

        suite200 = None


        string_literal193_tree = None
        COLON195_tree = None
        string_literal198_tree = None
        COLON199_tree = None

        try:
            try:
                # kv.g:310:2: ( 'if' test COLON suite ( elif_clause )* ( 'else' COLON suite )? )
                # kv.g:310:6: 'if' test COLON suite ( elif_clause )* ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal193=self.match(self.input, 95, self.FOLLOW_95_in_if_stmt1668)
                if self._state.backtracking == 0:

                    string_literal193_tree = self._adaptor.createWithPayload(string_literal193)
                    self._adaptor.addChild(root_0, string_literal193_tree)

                self._state.following.append(self.FOLLOW_test_in_if_stmt1670)
                test194 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test194.tree)
                COLON195=self.match(self.input, COLON, self.FOLLOW_COLON_in_if_stmt1672)
                if self._state.backtracking == 0:

                    COLON195_tree = self._adaptor.createWithPayload(COLON195)
                    self._adaptor.addChild(root_0, COLON195_tree)

                self._state.following.append(self.FOLLOW_suite_in_if_stmt1674)
                suite196 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite196.tree)
                # kv.g:310:28: ( elif_clause )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == 97) :
                        alt65 = 1


                    if alt65 == 1:
                        # kv.g:310:28: elif_clause
                        pass 
                        self._state.following.append(self.FOLLOW_elif_clause_in_if_stmt1676)
                        elif_clause197 = self.elif_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, elif_clause197.tree)


                    else:
                        break #loop65
                # kv.g:310:41: ( 'else' COLON suite )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == 96) :
                    alt66 = 1
                if alt66 == 1:
                    # kv.g:310:42: 'else' COLON suite
                    pass 
                    string_literal198=self.match(self.input, 96, self.FOLLOW_96_in_if_stmt1680)
                    if self._state.backtracking == 0:

                        string_literal198_tree = self._adaptor.createWithPayload(string_literal198)
                        self._adaptor.addChild(root_0, string_literal198_tree)

                    COLON199=self.match(self.input, COLON, self.FOLLOW_COLON_in_if_stmt1682)
                    if self._state.backtracking == 0:

                        COLON199_tree = self._adaptor.createWithPayload(COLON199)
                        self._adaptor.addChild(root_0, COLON199_tree)

                    self._state.following.append(self.FOLLOW_suite_in_if_stmt1684)
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

        string_literal201 = None
        COLON203 = None
        test202 = None

        suite204 = None


        string_literal201_tree = None
        COLON203_tree = None

        try:
            try:
                # kv.g:313:2: ( 'elif' test COLON suite )
                # kv.g:313:6: 'elif' test COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal201=self.match(self.input, 97, self.FOLLOW_97_in_elif_clause1698)
                if self._state.backtracking == 0:

                    string_literal201_tree = self._adaptor.createWithPayload(string_literal201)
                    self._adaptor.addChild(root_0, string_literal201_tree)

                self._state.following.append(self.FOLLOW_test_in_elif_clause1700)
                test202 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test202.tree)
                COLON203=self.match(self.input, COLON, self.FOLLOW_COLON_in_elif_clause1702)
                if self._state.backtracking == 0:

                    COLON203_tree = self._adaptor.createWithPayload(COLON203)
                    self._adaptor.addChild(root_0, COLON203_tree)

                self._state.following.append(self.FOLLOW_suite_in_elif_clause1704)
                suite204 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite204.tree)



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

        string_literal205 = None
        COLON207 = None
        string_literal209 = None
        COLON210 = None
        test206 = None

        suite208 = None

        suite211 = None


        string_literal205_tree = None
        COLON207_tree = None
        string_literal209_tree = None
        COLON210_tree = None

        try:
            try:
                # kv.g:316:2: ( 'while' test COLON suite ( 'else' COLON suite )? )
                # kv.g:316:6: 'while' test COLON suite ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal205=self.match(self.input, 98, self.FOLLOW_98_in_while_stmt1716)
                if self._state.backtracking == 0:

                    string_literal205_tree = self._adaptor.createWithPayload(string_literal205)
                    self._adaptor.addChild(root_0, string_literal205_tree)

                self._state.following.append(self.FOLLOW_test_in_while_stmt1718)
                test206 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test206.tree)
                COLON207=self.match(self.input, COLON, self.FOLLOW_COLON_in_while_stmt1720)
                if self._state.backtracking == 0:

                    COLON207_tree = self._adaptor.createWithPayload(COLON207)
                    self._adaptor.addChild(root_0, COLON207_tree)

                self._state.following.append(self.FOLLOW_suite_in_while_stmt1722)
                suite208 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite208.tree)
                # kv.g:316:31: ( 'else' COLON suite )?
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == 96) :
                    alt67 = 1
                if alt67 == 1:
                    # kv.g:316:32: 'else' COLON suite
                    pass 
                    string_literal209=self.match(self.input, 96, self.FOLLOW_96_in_while_stmt1725)
                    if self._state.backtracking == 0:

                        string_literal209_tree = self._adaptor.createWithPayload(string_literal209)
                        self._adaptor.addChild(root_0, string_literal209_tree)

                    COLON210=self.match(self.input, COLON, self.FOLLOW_COLON_in_while_stmt1727)
                    if self._state.backtracking == 0:

                        COLON210_tree = self._adaptor.createWithPayload(COLON210)
                        self._adaptor.addChild(root_0, COLON210_tree)

                    self._state.following.append(self.FOLLOW_suite_in_while_stmt1729)
                    suite211 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite211.tree)






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

        string_literal212 = None
        string_literal214 = None
        COLON216 = None
        string_literal218 = None
        COLON219 = None
        exprlist213 = None

        testlist215 = None

        suite217 = None

        suite220 = None


        string_literal212_tree = None
        string_literal214_tree = None
        COLON216_tree = None
        string_literal218_tree = None
        COLON219_tree = None

        try:
            try:
                # kv.g:319:2: ( 'for' exprlist 'in' testlist COLON suite ( 'else' COLON suite )? )
                # kv.g:319:6: 'for' exprlist 'in' testlist COLON suite ( 'else' COLON suite )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal212=self.match(self.input, 99, self.FOLLOW_99_in_for_stmt1743)
                if self._state.backtracking == 0:

                    string_literal212_tree = self._adaptor.createWithPayload(string_literal212)
                    self._adaptor.addChild(root_0, string_literal212_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_for_stmt1745)
                exprlist213 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist213.tree)
                string_literal214=self.match(self.input, 93, self.FOLLOW_93_in_for_stmt1747)
                if self._state.backtracking == 0:

                    string_literal214_tree = self._adaptor.createWithPayload(string_literal214)
                    self._adaptor.addChild(root_0, string_literal214_tree)

                self._state.following.append(self.FOLLOW_testlist_in_for_stmt1749)
                testlist215 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist215.tree)
                COLON216=self.match(self.input, COLON, self.FOLLOW_COLON_in_for_stmt1751)
                if self._state.backtracking == 0:

                    COLON216_tree = self._adaptor.createWithPayload(COLON216)
                    self._adaptor.addChild(root_0, COLON216_tree)

                self._state.following.append(self.FOLLOW_suite_in_for_stmt1753)
                suite217 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite217.tree)
                # kv.g:319:47: ( 'else' COLON suite )?
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == 96) :
                    alt68 = 1
                if alt68 == 1:
                    # kv.g:319:48: 'else' COLON suite
                    pass 
                    string_literal218=self.match(self.input, 96, self.FOLLOW_96_in_for_stmt1756)
                    if self._state.backtracking == 0:

                        string_literal218_tree = self._adaptor.createWithPayload(string_literal218)
                        self._adaptor.addChild(root_0, string_literal218_tree)

                    COLON219=self.match(self.input, COLON, self.FOLLOW_COLON_in_for_stmt1758)
                    if self._state.backtracking == 0:

                        COLON219_tree = self._adaptor.createWithPayload(COLON219)
                        self._adaptor.addChild(root_0, COLON219_tree)

                    self._state.following.append(self.FOLLOW_suite_in_for_stmt1760)
                    suite220 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite220.tree)






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

        string_literal221 = None
        COLON222 = None
        string_literal225 = None
        COLON226 = None
        string_literal228 = None
        COLON229 = None
        string_literal231 = None
        COLON232 = None
        suite223 = None

        except_clause224 = None

        suite227 = None

        suite230 = None

        suite233 = None


        string_literal221_tree = None
        COLON222_tree = None
        string_literal225_tree = None
        COLON226_tree = None
        string_literal228_tree = None
        COLON229_tree = None
        string_literal231_tree = None
        COLON232_tree = None

        try:
            try:
                # kv.g:322:2: ( 'try' COLON suite ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite ) )
                # kv.g:322:6: 'try' COLON suite ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite )
                pass 
                root_0 = self._adaptor.nil()

                string_literal221=self.match(self.input, 100, self.FOLLOW_100_in_try_stmt1774)
                if self._state.backtracking == 0:

                    string_literal221_tree = self._adaptor.createWithPayload(string_literal221)
                    self._adaptor.addChild(root_0, string_literal221_tree)

                COLON222=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1776)
                if self._state.backtracking == 0:

                    COLON222_tree = self._adaptor.createWithPayload(COLON222)
                    self._adaptor.addChild(root_0, COLON222_tree)

                self._state.following.append(self.FOLLOW_suite_in_try_stmt1778)
                suite223 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite223.tree)
                # kv.g:323:4: ( ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )? | 'finally' COLON suite )
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if (LA72_0 == 104) :
                    alt72 = 1
                elif (LA72_0 == 101) :
                    alt72 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # kv.g:323:6: ( except_clause )+ ( 'else' COLON suite )? ( 'finally' COLON suite )?
                    pass 
                    # kv.g:323:6: ( except_clause )+
                    cnt69 = 0
                    while True: #loop69
                        alt69 = 2
                        LA69_0 = self.input.LA(1)

                        if (LA69_0 == 104) :
                            alt69 = 1


                        if alt69 == 1:
                            # kv.g:323:6: except_clause
                            pass 
                            self._state.following.append(self.FOLLOW_except_clause_in_try_stmt1785)
                            except_clause224 = self.except_clause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, except_clause224.tree)


                        else:
                            if cnt69 >= 1:
                                break #loop69

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(69, self.input)
                            raise eee

                        cnt69 += 1
                    # kv.g:323:21: ( 'else' COLON suite )?
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == 96) :
                        alt70 = 1
                    if alt70 == 1:
                        # kv.g:323:22: 'else' COLON suite
                        pass 
                        string_literal225=self.match(self.input, 96, self.FOLLOW_96_in_try_stmt1789)
                        if self._state.backtracking == 0:

                            string_literal225_tree = self._adaptor.createWithPayload(string_literal225)
                            self._adaptor.addChild(root_0, string_literal225_tree)

                        COLON226=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1791)
                        if self._state.backtracking == 0:

                            COLON226_tree = self._adaptor.createWithPayload(COLON226)
                            self._adaptor.addChild(root_0, COLON226_tree)

                        self._state.following.append(self.FOLLOW_suite_in_try_stmt1793)
                        suite227 = self.suite()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, suite227.tree)



                    # kv.g:323:43: ( 'finally' COLON suite )?
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == 101) :
                        alt71 = 1
                    if alt71 == 1:
                        # kv.g:323:44: 'finally' COLON suite
                        pass 
                        string_literal228=self.match(self.input, 101, self.FOLLOW_101_in_try_stmt1798)
                        if self._state.backtracking == 0:

                            string_literal228_tree = self._adaptor.createWithPayload(string_literal228)
                            self._adaptor.addChild(root_0, string_literal228_tree)

                        COLON229=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1800)
                        if self._state.backtracking == 0:

                            COLON229_tree = self._adaptor.createWithPayload(COLON229)
                            self._adaptor.addChild(root_0, COLON229_tree)

                        self._state.following.append(self.FOLLOW_suite_in_try_stmt1802)
                        suite230 = self.suite()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, suite230.tree)





                elif alt72 == 2:
                    # kv.g:324:6: 'finally' COLON suite
                    pass 
                    string_literal231=self.match(self.input, 101, self.FOLLOW_101_in_try_stmt1811)
                    if self._state.backtracking == 0:

                        string_literal231_tree = self._adaptor.createWithPayload(string_literal231)
                        self._adaptor.addChild(root_0, string_literal231_tree)

                    COLON232=self.match(self.input, COLON, self.FOLLOW_COLON_in_try_stmt1813)
                    if self._state.backtracking == 0:

                        COLON232_tree = self._adaptor.createWithPayload(COLON232)
                        self._adaptor.addChild(root_0, COLON232_tree)

                    self._state.following.append(self.FOLLOW_suite_in_try_stmt1815)
                    suite233 = self.suite()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, suite233.tree)






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

        string_literal234 = None
        COLON237 = None
        test235 = None

        with_var236 = None

        suite238 = None


        string_literal234_tree = None
        COLON237_tree = None

        try:
            try:
                # kv.g:327:2: ( 'with' test ( with_var )? COLON suite )
                # kv.g:327:6: 'with' test ( with_var )? COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal234=self.match(self.input, 102, self.FOLLOW_102_in_with_stmt1829)
                if self._state.backtracking == 0:

                    string_literal234_tree = self._adaptor.createWithPayload(string_literal234)
                    self._adaptor.addChild(root_0, string_literal234_tree)

                self._state.following.append(self.FOLLOW_test_in_with_stmt1831)
                test235 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test235.tree)
                # kv.g:327:18: ( with_var )?
                alt73 = 2
                LA73_0 = self.input.LA(1)

                if (LA73_0 == WNAME or LA73_0 == NAME or LA73_0 == 103) :
                    alt73 = 1
                if alt73 == 1:
                    # kv.g:327:19: with_var
                    pass 
                    self._state.following.append(self.FOLLOW_with_var_in_with_stmt1834)
                    with_var236 = self.with_var()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, with_var236.tree)



                COLON237=self.match(self.input, COLON, self.FOLLOW_COLON_in_with_stmt1838)
                if self._state.backtracking == 0:

                    COLON237_tree = self._adaptor.createWithPayload(COLON237)
                    self._adaptor.addChild(root_0, COLON237_tree)

                self._state.following.append(self.FOLLOW_suite_in_with_stmt1840)
                suite238 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite238.tree)



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

        string_literal239 = None
        identifier240 = None

        expr241 = None


        string_literal239_tree = None

        try:
            try:
                # kv.g:330:2: ( ( 'as' | identifier ) expr )
                # kv.g:330:6: ( 'as' | identifier ) expr
                pass 
                root_0 = self._adaptor.nil()

                # kv.g:330:6: ( 'as' | identifier )
                alt74 = 2
                LA74_0 = self.input.LA(1)

                if (LA74_0 == 103) :
                    alt74 = 1
                elif (LA74_0 == WNAME or LA74_0 == NAME) :
                    alt74 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 74, 0, self.input)

                    raise nvae

                if alt74 == 1:
                    # kv.g:330:7: 'as'
                    pass 
                    string_literal239=self.match(self.input, 103, self.FOLLOW_103_in_with_var1853)
                    if self._state.backtracking == 0:

                        string_literal239_tree = self._adaptor.createWithPayload(string_literal239)
                        self._adaptor.addChild(root_0, string_literal239_tree)



                elif alt74 == 2:
                    # kv.g:330:14: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_with_var1857)
                    identifier240 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier240.tree)



                self._state.following.append(self.FOLLOW_expr_in_with_var1860)
                expr241 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr241.tree)



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

        string_literal242 = None
        COMMA244 = None
        COLON246 = None
        test243 = None

        test245 = None

        suite247 = None


        string_literal242_tree = None
        COMMA244_tree = None
        COLON246_tree = None

        try:
            try:
                # kv.g:333:2: ( 'except' ( test ( COMMA test )? )? COLON suite )
                # kv.g:333:6: 'except' ( test ( COMMA test )? )? COLON suite
                pass 
                root_0 = self._adaptor.nil()

                string_literal242=self.match(self.input, 104, self.FOLLOW_104_in_except_clause1872)
                if self._state.backtracking == 0:

                    string_literal242_tree = self._adaptor.createWithPayload(string_literal242)
                    self._adaptor.addChild(root_0, string_literal242_tree)

                # kv.g:333:15: ( test ( COMMA test )? )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if (LA76_0 == WNAME or (PLUS <= LA76_0 <= MINUS) or LA76_0 == NAME or LA76_0 == LPAREN or LA76_0 == NOT or (TILDE <= LA76_0 <= LBRACK) or LA76_0 == LCURLY or (BACKQUOTE <= LA76_0 <= STRING) or LA76_0 == 106) :
                    alt76 = 1
                if alt76 == 1:
                    # kv.g:333:16: test ( COMMA test )?
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_except_clause1875)
                    test243 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test243.tree)
                    # kv.g:333:21: ( COMMA test )?
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == COMMA) :
                        alt75 = 1
                    if alt75 == 1:
                        # kv.g:333:22: COMMA test
                        pass 
                        COMMA244=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_except_clause1878)
                        if self._state.backtracking == 0:

                            COMMA244_tree = self._adaptor.createWithPayload(COMMA244)
                            self._adaptor.addChild(root_0, COMMA244_tree)

                        self._state.following.append(self.FOLLOW_test_in_except_clause1880)
                        test245 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test245.tree)






                COLON246=self.match(self.input, COLON, self.FOLLOW_COLON_in_except_clause1886)
                if self._state.backtracking == 0:

                    COLON246_tree = self._adaptor.createWithPayload(COLON246)
                    self._adaptor.addChild(root_0, COLON246_tree)

                self._state.following.append(self.FOLLOW_suite_in_except_clause1888)
                suite247 = self.suite()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, suite247.tree)



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

        NEWLINE249 = None
        INDENT250 = None
        DEDENT252 = None
        simple_stmt248 = None

        stmt251 = None


        NEWLINE249_tree = None
        INDENT250_tree = None
        DEDENT252_tree = None

        try:
            try:
                # kv.g:336:2: ( simple_stmt | NEWLINE INDENT ( stmt )+ DEDENT )
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if (LA78_0 == WNAME or (PLUS <= LA78_0 <= MINUS) or LA78_0 == NAME or LA78_0 == LPAREN or LA78_0 == NOT or (TILDE <= LA78_0 <= LBRACK) or LA78_0 == LCURLY or (BACKQUOTE <= LA78_0 <= STRING) or (86 <= LA78_0 <= 92) or LA78_0 == 94 or (106 <= LA78_0 <= 107)) :
                    alt78 = 1
                elif (LA78_0 == NEWLINE) :
                    alt78 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 78, 0, self.input)

                    raise nvae

                if alt78 == 1:
                    # kv.g:336:6: simple_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_stmt_in_suite1900)
                    simple_stmt248 = self.simple_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_stmt248.tree)


                elif alt78 == 2:
                    # kv.g:337:6: NEWLINE INDENT ( stmt )+ DEDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    NEWLINE249=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_suite1907)
                    if self._state.backtracking == 0:

                        NEWLINE249_tree = self._adaptor.createWithPayload(NEWLINE249)
                        self._adaptor.addChild(root_0, NEWLINE249_tree)

                    INDENT250=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_suite1909)
                    if self._state.backtracking == 0:

                        INDENT250_tree = self._adaptor.createWithPayload(INDENT250)
                        self._adaptor.addChild(root_0, INDENT250_tree)

                    # kv.g:337:21: ( stmt )+
                    cnt77 = 0
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == NEWLINE or (COMMENTTEXT <= LA77_0 <= WNAME) or (CANVAS <= LA77_0 <= NAME)) :
                            alt77 = 1


                        if alt77 == 1:
                            # kv.g:337:22: stmt
                            pass 
                            self._state.following.append(self.FOLLOW_stmt_in_suite1912)
                            stmt251 = self.stmt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, stmt251.tree)


                        else:
                            if cnt77 >= 1:
                                break #loop77

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(77, self.input)
                            raise eee

                        cnt77 += 1
                    DEDENT252=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_suite1916)
                    if self._state.backtracking == 0:

                        DEDENT252_tree = self._adaptor.createWithPayload(DEDENT252)
                        self._adaptor.addChild(root_0, DEDENT252_tree)



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

        string_literal254 = None
        string_literal256 = None
        or_test253 = None

        or_test255 = None

        test257 = None

        lambdef258 = None


        string_literal254_tree = None
        string_literal256_tree = None

        try:
            try:
                # kv.g:341:2: ( or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )? | lambdef )
                alt80 = 2
                LA80_0 = self.input.LA(1)

                if (LA80_0 == WNAME or (PLUS <= LA80_0 <= MINUS) or LA80_0 == NAME or LA80_0 == LPAREN or LA80_0 == NOT or (TILDE <= LA80_0 <= LBRACK) or LA80_0 == LCURLY or (BACKQUOTE <= LA80_0 <= STRING)) :
                    alt80 = 1
                elif (LA80_0 == 106) :
                    alt80 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # kv.g:341:4: or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_or_test_in_test1927)
                    or_test253 = self.or_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, or_test253.tree)
                    # kv.g:342:3: ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    alt79 = 2
                    alt79 = self.dfa79.predict(self.input)
                    if alt79 == 1:
                        # kv.g:342:5: ( 'if' or_test 'else' )=> 'if' or_test 'else' test
                        pass 
                        string_literal254=self.match(self.input, 95, self.FOLLOW_95_in_test1945)
                        if self._state.backtracking == 0:

                            string_literal254_tree = self._adaptor.createWithPayload(string_literal254)
                            self._adaptor.addChild(root_0, string_literal254_tree)

                        self._state.following.append(self.FOLLOW_or_test_in_test1947)
                        or_test255 = self.or_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, or_test255.tree)
                        string_literal256=self.match(self.input, 96, self.FOLLOW_96_in_test1949)
                        if self._state.backtracking == 0:

                            string_literal256_tree = self._adaptor.createWithPayload(string_literal256)
                            self._adaptor.addChild(root_0, string_literal256_tree)

                        self._state.following.append(self.FOLLOW_test_in_test1951)
                        test257 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test257.tree)





                elif alt80 == 2:
                    # kv.g:343:4: lambdef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_lambdef_in_test1959)
                    lambdef258 = self.lambdef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, lambdef258.tree)


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

        OR260 = None
        and_test259 = None

        and_test261 = None


        OR260_tree = None

        try:
            try:
                # kv.g:346:2: ( and_test ( OR and_test )* )
                # kv.g:346:4: and_test ( OR and_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_test_in_or_test1969)
                and_test259 = self.and_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_test259.tree)
                # kv.g:346:13: ( OR and_test )*
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == OR) :
                        alt81 = 1


                    if alt81 == 1:
                        # kv.g:346:14: OR and_test
                        pass 
                        OR260=self.match(self.input, OR, self.FOLLOW_OR_in_or_test1972)
                        if self._state.backtracking == 0:

                            OR260_tree = self._adaptor.createWithPayload(OR260)
                            self._adaptor.addChild(root_0, OR260_tree)

                        self._state.following.append(self.FOLLOW_and_test_in_or_test1974)
                        and_test261 = self.and_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_test261.tree)


                    else:
                        break #loop81



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

        AND263 = None
        not_test262 = None

        not_test264 = None


        AND263_tree = None

        try:
            try:
                # kv.g:349:2: ( not_test ( AND not_test )* )
                # kv.g:349:4: not_test ( AND not_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_not_test_in_and_test1986)
                not_test262 = self.not_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, not_test262.tree)
                # kv.g:349:13: ( AND not_test )*
                while True: #loop82
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if (LA82_0 == AND) :
                        alt82 = 1


                    if alt82 == 1:
                        # kv.g:349:14: AND not_test
                        pass 
                        AND263=self.match(self.input, AND, self.FOLLOW_AND_in_and_test1989)
                        if self._state.backtracking == 0:

                            AND263_tree = self._adaptor.createWithPayload(AND263)
                            self._adaptor.addChild(root_0, AND263_tree)

                        self._state.following.append(self.FOLLOW_not_test_in_and_test1991)
                        not_test264 = self.not_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, not_test264.tree)


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

        NOT265 = None
        not_test266 = None

        comparison267 = None


        NOT265_tree = None

        try:
            try:
                # kv.g:352:2: ( NOT not_test | comparison )
                alt83 = 2
                LA83_0 = self.input.LA(1)

                if (LA83_0 == NOT) :
                    alt83 = 1
                elif (LA83_0 == WNAME or (PLUS <= LA83_0 <= MINUS) or LA83_0 == NAME or LA83_0 == LPAREN or (TILDE <= LA83_0 <= LBRACK) or LA83_0 == LCURLY or (BACKQUOTE <= LA83_0 <= STRING)) :
                    alt83 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 83, 0, self.input)

                    raise nvae

                if alt83 == 1:
                    # kv.g:352:4: NOT not_test
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT265=self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test2003)
                    if self._state.backtracking == 0:

                        NOT265_tree = self._adaptor.createWithPayload(NOT265)
                        self._adaptor.addChild(root_0, NOT265_tree)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test2005)
                    not_test266 = self.not_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, not_test266.tree)


                elif alt83 == 2:
                    # kv.g:353:4: comparison
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comparison_in_not_test2010)
                    comparison267 = self.comparison()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comparison267.tree)


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

        expr268 = None

        comp_op269 = None

        expr270 = None



        try:
            try:
                # kv.g:356:2: ( expr ( comp_op expr )* )
                # kv.g:356:4: expr ( comp_op expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_comparison2020)
                expr268 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr268.tree)
                # kv.g:356:9: ( comp_op expr )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if ((NOT <= LA84_0 <= NOTEQUAL) or LA84_0 == 93 or LA84_0 == 105) :
                        alt84 = 1


                    if alt84 == 1:
                        # kv.g:356:10: comp_op expr
                        pass 
                        self._state.following.append(self.FOLLOW_comp_op_in_comparison2023)
                        comp_op269 = self.comp_op()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, comp_op269.tree)
                        self._state.following.append(self.FOLLOW_expr_in_comparison2025)
                        expr270 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr270.tree)


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

        LESS271 = None
        GREATER272 = None
        EQUAL273 = None
        GREATEREQUAL274 = None
        LESSEQUAL275 = None
        ALT_NOTEQUAL276 = None
        NOTEQUAL277 = None
        string_literal278 = None
        NOT279 = None
        string_literal280 = None
        string_literal281 = None
        NOT282 = None
        string_literal283 = None

        LESS271_tree = None
        GREATER272_tree = None
        EQUAL273_tree = None
        GREATEREQUAL274_tree = None
        LESSEQUAL275_tree = None
        ALT_NOTEQUAL276_tree = None
        NOTEQUAL277_tree = None
        string_literal278_tree = None
        NOT279_tree = None
        string_literal280_tree = None
        string_literal281_tree = None
        NOT282_tree = None
        string_literal283_tree = None

        try:
            try:
                # kv.g:359:2: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | NOT 'in' | 'is' | NOT 'is' )
                alt85 = 11
                alt85 = self.dfa85.predict(self.input)
                if alt85 == 1:
                    # kv.g:359:4: LESS
                    pass 
                    root_0 = self._adaptor.nil()

                    LESS271=self.match(self.input, LESS, self.FOLLOW_LESS_in_comp_op2037)
                    if self._state.backtracking == 0:

                        LESS271_tree = self._adaptor.createWithPayload(LESS271)
                        self._adaptor.addChild(root_0, LESS271_tree)



                elif alt85 == 2:
                    # kv.g:359:11: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER272=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comp_op2041)
                    if self._state.backtracking == 0:

                        GREATER272_tree = self._adaptor.createWithPayload(GREATER272)
                        self._adaptor.addChild(root_0, GREATER272_tree)



                elif alt85 == 3:
                    # kv.g:359:21: EQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    EQUAL273=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comp_op2045)
                    if self._state.backtracking == 0:

                        EQUAL273_tree = self._adaptor.createWithPayload(EQUAL273)
                        self._adaptor.addChild(root_0, EQUAL273_tree)



                elif alt85 == 4:
                    # kv.g:359:29: GREATEREQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATEREQUAL274=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comp_op2049)
                    if self._state.backtracking == 0:

                        GREATEREQUAL274_tree = self._adaptor.createWithPayload(GREATEREQUAL274)
                        self._adaptor.addChild(root_0, GREATEREQUAL274_tree)



                elif alt85 == 5:
                    # kv.g:359:44: LESSEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    LESSEQUAL275=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comp_op2053)
                    if self._state.backtracking == 0:

                        LESSEQUAL275_tree = self._adaptor.createWithPayload(LESSEQUAL275)
                        self._adaptor.addChild(root_0, LESSEQUAL275_tree)



                elif alt85 == 6:
                    # kv.g:359:56: ALT_NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    ALT_NOTEQUAL276=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comp_op2057)
                    if self._state.backtracking == 0:

                        ALT_NOTEQUAL276_tree = self._adaptor.createWithPayload(ALT_NOTEQUAL276)
                        self._adaptor.addChild(root_0, ALT_NOTEQUAL276_tree)



                elif alt85 == 7:
                    # kv.g:359:71: NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    NOTEQUAL277=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comp_op2061)
                    if self._state.backtracking == 0:

                        NOTEQUAL277_tree = self._adaptor.createWithPayload(NOTEQUAL277)
                        self._adaptor.addChild(root_0, NOTEQUAL277_tree)



                elif alt85 == 8:
                    # kv.g:360:4: 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal278=self.match(self.input, 93, self.FOLLOW_93_in_comp_op2066)
                    if self._state.backtracking == 0:

                        string_literal278_tree = self._adaptor.createWithPayload(string_literal278)
                        self._adaptor.addChild(root_0, string_literal278_tree)



                elif alt85 == 9:
                    # kv.g:360:11: NOT 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT279=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2070)
                    if self._state.backtracking == 0:

                        NOT279_tree = self._adaptor.createWithPayload(NOT279)
                        self._adaptor.addChild(root_0, NOT279_tree)

                    string_literal280=self.match(self.input, 93, self.FOLLOW_93_in_comp_op2072)
                    if self._state.backtracking == 0:

                        string_literal280_tree = self._adaptor.createWithPayload(string_literal280)
                        self._adaptor.addChild(root_0, string_literal280_tree)



                elif alt85 == 10:
                    # kv.g:360:22: 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal281=self.match(self.input, 105, self.FOLLOW_105_in_comp_op2076)
                    if self._state.backtracking == 0:

                        string_literal281_tree = self._adaptor.createWithPayload(string_literal281)
                        self._adaptor.addChild(root_0, string_literal281_tree)



                elif alt85 == 11:
                    # kv.g:360:29: NOT 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT282=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2080)
                    if self._state.backtracking == 0:

                        NOT282_tree = self._adaptor.createWithPayload(NOT282)
                        self._adaptor.addChild(root_0, NOT282_tree)

                    string_literal283=self.match(self.input, 105, self.FOLLOW_105_in_comp_op2082)
                    if self._state.backtracking == 0:

                        string_literal283_tree = self._adaptor.createWithPayload(string_literal283)
                        self._adaptor.addChild(root_0, string_literal283_tree)



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

        VBAR285 = None
        xor_expr284 = None

        xor_expr286 = None


        VBAR285_tree = None

        try:
            try:
                # kv.g:363:2: ( xor_expr ( VBAR xor_expr )* )
                # kv.g:363:4: xor_expr ( VBAR xor_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_xor_expr_in_expr2092)
                xor_expr284 = self.xor_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, xor_expr284.tree)
                # kv.g:363:13: ( VBAR xor_expr )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == VBAR) :
                        alt86 = 1


                    if alt86 == 1:
                        # kv.g:363:14: VBAR xor_expr
                        pass 
                        VBAR285=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_expr2095)
                        if self._state.backtracking == 0:

                            VBAR285_tree = self._adaptor.createWithPayload(VBAR285)
                            self._adaptor.addChild(root_0, VBAR285_tree)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr2097)
                        xor_expr286 = self.xor_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, xor_expr286.tree)


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

        CIRCUMFLEX288 = None
        and_expr287 = None

        and_expr289 = None


        CIRCUMFLEX288_tree = None

        try:
            try:
                # kv.g:366:2: ( and_expr ( CIRCUMFLEX and_expr )* )
                # kv.g:366:4: and_expr ( CIRCUMFLEX and_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr2109)
                and_expr287 = self.and_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expr287.tree)
                # kv.g:366:13: ( CIRCUMFLEX and_expr )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == CIRCUMFLEX) :
                        alt87 = 1


                    if alt87 == 1:
                        # kv.g:366:14: CIRCUMFLEX and_expr
                        pass 
                        CIRCUMFLEX288=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_xor_expr2112)
                        if self._state.backtracking == 0:

                            CIRCUMFLEX288_tree = self._adaptor.createWithPayload(CIRCUMFLEX288)
                            self._adaptor.addChild(root_0, CIRCUMFLEX288_tree)

                        self._state.following.append(self.FOLLOW_and_expr_in_xor_expr2114)
                        and_expr289 = self.and_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_expr289.tree)


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

        AMPER291 = None
        shift_expr290 = None

        shift_expr292 = None


        AMPER291_tree = None

        try:
            try:
                # kv.g:369:2: ( shift_expr ( AMPER shift_expr )* )
                # kv.g:369:4: shift_expr ( AMPER shift_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr2126)
                shift_expr290 = self.shift_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, shift_expr290.tree)
                # kv.g:369:15: ( AMPER shift_expr )*
                while True: #loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == AMPER) :
                        alt88 = 1


                    if alt88 == 1:
                        # kv.g:369:16: AMPER shift_expr
                        pass 
                        AMPER291=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_and_expr2129)
                        if self._state.backtracking == 0:

                            AMPER291_tree = self._adaptor.createWithPayload(AMPER291)
                            self._adaptor.addChild(root_0, AMPER291_tree)

                        self._state.following.append(self.FOLLOW_shift_expr_in_and_expr2131)
                        shift_expr292 = self.shift_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, shift_expr292.tree)


                    else:
                        break #loop88



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

        set294 = None
        arith_expr293 = None

        arith_expr295 = None


        set294_tree = None

        try:
            try:
                # kv.g:372:2: ( arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )* )
                # kv.g:372:4: arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr2143)
                arith_expr293 = self.arith_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arith_expr293.tree)
                # kv.g:372:15: ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == RIGHTSHIFT or LA89_0 == LEFTSHIFT) :
                        alt89 = 1


                    if alt89 == 1:
                        # kv.g:372:16: ( LEFTSHIFT | RIGHTSHIFT ) arith_expr
                        pass 
                        set294 = self.input.LT(1)
                        if self.input.LA(1) == RIGHTSHIFT or self.input.LA(1) == LEFTSHIFT:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set294))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr2152)
                        arith_expr295 = self.arith_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arith_expr295.tree)


                    else:
                        break #loop89



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

        set297 = None
        term296 = None

        term298 = None


        set297_tree = None

        try:
            try:
                # kv.g:375:2: ( term ( ( PLUS | MINUS ) term )* )
                # kv.g:375:4: term ( ( PLUS | MINUS ) term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_arith_expr2164)
                term296 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term296.tree)
                # kv.g:375:9: ( ( PLUS | MINUS ) term )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if ((PLUS <= LA90_0 <= MINUS)) :
                        alt90 = 1


                    if alt90 == 1:
                        # kv.g:375:10: ( PLUS | MINUS ) term
                        pass 
                        set297 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set297))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_arith_expr2173)
                        term298 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term298.tree)


                    else:
                        break #loop90



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

        set300 = None
        factor299 = None

        factor301 = None


        set300_tree = None

        try:
            try:
                # kv.g:378:2: ( factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )* )
                # kv.g:378:4: factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_factor_in_term2185)
                factor299 = self.factor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, factor299.tree)
                # kv.g:378:11: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == STAR or (SLASH <= LA91_0 <= DOUBLESLASH)) :
                        alt91 = 1


                    if alt91 == 1:
                        # kv.g:378:12: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor
                        pass 
                        set300 = self.input.LT(1)
                        if self.input.LA(1) == STAR or (SLASH <= self.input.LA(1) <= DOUBLESLASH):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set300))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term2205)
                        factor301 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, factor301.tree)


                    else:
                        break #loop91



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

        PLUS302 = None
        MINUS304 = None
        TILDE306 = None
        factor303 = None

        factor305 = None

        factor307 = None

        power308 = None


        PLUS302_tree = None
        MINUS304_tree = None
        TILDE306_tree = None

        try:
            try:
                # kv.g:381:2: ( PLUS factor | MINUS factor | TILDE factor | power )
                alt92 = 4
                LA92 = self.input.LA(1)
                if LA92 == PLUS:
                    alt92 = 1
                elif LA92 == MINUS:
                    alt92 = 2
                elif LA92 == TILDE:
                    alt92 = 3
                elif LA92 == WNAME or LA92 == NAME or LA92 == LPAREN or LA92 == LBRACK or LA92 == LCURLY or LA92 == BACKQUOTE or LA92 == NONE or LA92 == INT or LA92 == LONGINT or LA92 == FLOAT or LA92 == COMPLEX or LA92 == STRING:
                    alt92 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 92, 0, self.input)

                    raise nvae

                if alt92 == 1:
                    # kv.g:381:4: PLUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS302=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor2217)
                    if self._state.backtracking == 0:

                        PLUS302_tree = self._adaptor.createWithPayload(PLUS302)
                        self._adaptor.addChild(root_0, PLUS302_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2219)
                    factor303 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor303.tree)


                elif alt92 == 2:
                    # kv.g:381:18: MINUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    MINUS304=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor2223)
                    if self._state.backtracking == 0:

                        MINUS304_tree = self._adaptor.createWithPayload(MINUS304)
                        self._adaptor.addChild(root_0, MINUS304_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2225)
                    factor305 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor305.tree)


                elif alt92 == 3:
                    # kv.g:381:33: TILDE factor
                    pass 
                    root_0 = self._adaptor.nil()

                    TILDE306=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor2229)
                    if self._state.backtracking == 0:

                        TILDE306_tree = self._adaptor.createWithPayload(TILDE306)
                        self._adaptor.addChild(root_0, TILDE306_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor2231)
                    factor307 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor307.tree)


                elif alt92 == 4:
                    # kv.g:381:48: power
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_power_in_factor2235)
                    power308 = self.power()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, power308.tree)


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

        DOUBLESTAR311 = None
        atom309 = None

        trailer310 = None

        factor312 = None


        DOUBLESTAR311_tree = None

        try:
            try:
                # kv.g:384:2: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # kv.g:384:4: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_in_power2245)
                atom309 = self.atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, atom309.tree)
                # kv.g:384:9: ( trailer )*
                while True: #loop93
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == LPAREN or LA93_0 == LBRACK or LA93_0 == DOT) :
                        alt93 = 1


                    if alt93 == 1:
                        # kv.g:384:10: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power2248)
                        trailer310 = self.trailer()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, trailer310.tree)


                    else:
                        break #loop93
                # kv.g:384:20: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if (LA94_0 == DOUBLESTAR) :
                    alt94 = 1
                if alt94 == 1:
                    # kv.g:384:44: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR311=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power2260)
                    if self._state.backtracking == 0:

                        DOUBLESTAR311_tree = self._adaptor.createWithPayload(DOUBLESTAR311)
                        self._adaptor.addChild(root_0, DOUBLESTAR311_tree)

                    self._state.following.append(self.FOLLOW_factor_in_power2262)
                    factor312 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor312.tree)






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

        LPAREN313 = None
        RPAREN316 = None
        LBRACK317 = None
        RBRACK319 = None
        LCURLY320 = None
        RCURLY322 = None
        BACKQUOTE323 = None
        BACKQUOTE325 = None
        NONE327 = None
        INT328 = None
        LONGINT329 = None
        FLOAT330 = None
        COMPLEX331 = None
        STRING332 = None
        yield_expr314 = None

        testlist_gexp315 = None

        listmaker318 = None

        dictmaker321 = None

        testlist324 = None

        identifier326 = None


        LPAREN313_tree = None
        RPAREN316_tree = None
        LBRACK317_tree = None
        RBRACK319_tree = None
        LCURLY320_tree = None
        RCURLY322_tree = None
        BACKQUOTE323_tree = None
        BACKQUOTE325_tree = None
        NONE327_tree = None
        INT328_tree = None
        LONGINT329_tree = None
        FLOAT330_tree = None
        COMPLEX331_tree = None
        STRING332_tree = None

        try:
            try:
                # kv.g:387:2: ( LPAREN ( yield_expr | testlist_gexp )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | BACKQUOTE testlist BACKQUOTE | identifier | NONE | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
                alt99 = 11
                LA99 = self.input.LA(1)
                if LA99 == LPAREN:
                    alt99 = 1
                elif LA99 == LBRACK:
                    alt99 = 2
                elif LA99 == LCURLY:
                    alt99 = 3
                elif LA99 == BACKQUOTE:
                    alt99 = 4
                elif LA99 == WNAME or LA99 == NAME:
                    alt99 = 5
                elif LA99 == NONE:
                    alt99 = 6
                elif LA99 == INT:
                    alt99 = 7
                elif LA99 == LONGINT:
                    alt99 = 8
                elif LA99 == FLOAT:
                    alt99 = 9
                elif LA99 == COMPLEX:
                    alt99 = 10
                elif LA99 == STRING:
                    alt99 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 99, 0, self.input)

                    raise nvae

                if alt99 == 1:
                    # kv.g:387:4: LPAREN ( yield_expr | testlist_gexp )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN313=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2274)
                    if self._state.backtracking == 0:

                        LPAREN313_tree = self._adaptor.createWithPayload(LPAREN313)
                        self._adaptor.addChild(root_0, LPAREN313_tree)

                    # kv.g:387:11: ( yield_expr | testlist_gexp )?
                    alt95 = 3
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == 107) :
                        alt95 = 1
                    elif (LA95_0 == WNAME or (PLUS <= LA95_0 <= MINUS) or LA95_0 == NAME or LA95_0 == LPAREN or LA95_0 == NOT or (TILDE <= LA95_0 <= LBRACK) or LA95_0 == LCURLY or (BACKQUOTE <= LA95_0 <= STRING) or LA95_0 == 106) :
                        alt95 = 2
                    if alt95 == 1:
                        # kv.g:387:13: yield_expr
                        pass 
                        self._state.following.append(self.FOLLOW_yield_expr_in_atom2278)
                        yield_expr314 = self.yield_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, yield_expr314.tree)


                    elif alt95 == 2:
                        # kv.g:387:26: testlist_gexp
                        pass 
                        self._state.following.append(self.FOLLOW_testlist_gexp_in_atom2282)
                        testlist_gexp315 = self.testlist_gexp()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, testlist_gexp315.tree)



                    RPAREN316=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2287)
                    if self._state.backtracking == 0:

                        RPAREN316_tree = self._adaptor.createWithPayload(RPAREN316)
                        self._adaptor.addChild(root_0, RPAREN316_tree)



                elif alt99 == 2:
                    # kv.g:388:4: LBRACK ( listmaker )? RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK317=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom2292)
                    if self._state.backtracking == 0:

                        LBRACK317_tree = self._adaptor.createWithPayload(LBRACK317)
                        self._adaptor.addChild(root_0, LBRACK317_tree)

                    # kv.g:388:11: ( listmaker )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == WNAME or (PLUS <= LA96_0 <= MINUS) or LA96_0 == NAME or LA96_0 == LPAREN or LA96_0 == NOT or (TILDE <= LA96_0 <= LBRACK) or LA96_0 == LCURLY or (BACKQUOTE <= LA96_0 <= STRING) or LA96_0 == 106) :
                        alt96 = 1
                    if alt96 == 1:
                        # kv.g:388:12: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom2295)
                        listmaker318 = self.listmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, listmaker318.tree)



                    RBRACK319=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom2299)
                    if self._state.backtracking == 0:

                        RBRACK319_tree = self._adaptor.createWithPayload(RBRACK319)
                        self._adaptor.addChild(root_0, RBRACK319_tree)



                elif alt99 == 3:
                    # kv.g:389:4: LCURLY ( dictmaker )? RCURLY
                    pass 
                    root_0 = self._adaptor.nil()

                    LCURLY320=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom2304)
                    if self._state.backtracking == 0:

                        LCURLY320_tree = self._adaptor.createWithPayload(LCURLY320)
                        self._adaptor.addChild(root_0, LCURLY320_tree)

                    # kv.g:389:11: ( dictmaker )?
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == WNAME or (PLUS <= LA97_0 <= MINUS) or LA97_0 == NAME or LA97_0 == LPAREN or LA97_0 == NOT or (TILDE <= LA97_0 <= LBRACK) or LA97_0 == LCURLY or (BACKQUOTE <= LA97_0 <= STRING) or LA97_0 == 106) :
                        alt97 = 1
                    if alt97 == 1:
                        # kv.g:389:12: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom2307)
                        dictmaker321 = self.dictmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, dictmaker321.tree)



                    RCURLY322=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom2311)
                    if self._state.backtracking == 0:

                        RCURLY322_tree = self._adaptor.createWithPayload(RCURLY322)
                        self._adaptor.addChild(root_0, RCURLY322_tree)



                elif alt99 == 4:
                    # kv.g:390:4: BACKQUOTE testlist BACKQUOTE
                    pass 
                    root_0 = self._adaptor.nil()

                    BACKQUOTE323=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom2316)
                    if self._state.backtracking == 0:

                        BACKQUOTE323_tree = self._adaptor.createWithPayload(BACKQUOTE323)
                        self._adaptor.addChild(root_0, BACKQUOTE323_tree)

                    self._state.following.append(self.FOLLOW_testlist_in_atom2318)
                    testlist324 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist324.tree)
                    BACKQUOTE325=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom2320)
                    if self._state.backtracking == 0:

                        BACKQUOTE325_tree = self._adaptor.createWithPayload(BACKQUOTE325)
                        self._adaptor.addChild(root_0, BACKQUOTE325_tree)



                elif alt99 == 5:
                    # kv.g:391:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_atom2325)
                    identifier326 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier326.tree)


                elif alt99 == 6:
                    # kv.g:392:6: NONE
                    pass 
                    root_0 = self._adaptor.nil()

                    NONE327=self.match(self.input, NONE, self.FOLLOW_NONE_in_atom2332)
                    if self._state.backtracking == 0:

                        NONE327_tree = self._adaptor.createWithPayload(NONE327)
                        self._adaptor.addChild(root_0, NONE327_tree)



                elif alt99 == 7:
                    # kv.g:393:4: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT328=self.match(self.input, INT, self.FOLLOW_INT_in_atom2337)
                    if self._state.backtracking == 0:

                        INT328_tree = self._adaptor.createWithPayload(INT328)
                        self._adaptor.addChild(root_0, INT328_tree)



                elif alt99 == 8:
                    # kv.g:394:4: LONGINT
                    pass 
                    root_0 = self._adaptor.nil()

                    LONGINT329=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom2342)
                    if self._state.backtracking == 0:

                        LONGINT329_tree = self._adaptor.createWithPayload(LONGINT329)
                        self._adaptor.addChild(root_0, LONGINT329_tree)



                elif alt99 == 9:
                    # kv.g:395:4: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()

                    FLOAT330=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom2347)
                    if self._state.backtracking == 0:

                        FLOAT330_tree = self._adaptor.createWithPayload(FLOAT330)
                        self._adaptor.addChild(root_0, FLOAT330_tree)



                elif alt99 == 10:
                    # kv.g:396:4: COMPLEX
                    pass 
                    root_0 = self._adaptor.nil()

                    COMPLEX331=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom2352)
                    if self._state.backtracking == 0:

                        COMPLEX331_tree = self._adaptor.createWithPayload(COMPLEX331)
                        self._adaptor.addChild(root_0, COMPLEX331_tree)



                elif alt99 == 11:
                    # kv.g:397:4: ( STRING )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:397:4: ( STRING )+
                    cnt98 = 0
                    while True: #loop98
                        alt98 = 2
                        LA98_0 = self.input.LA(1)

                        if (LA98_0 == STRING) :
                            alt98 = 1


                        if alt98 == 1:
                            # kv.g:397:5: STRING
                            pass 
                            STRING332=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom2358)
                            if self._state.backtracking == 0:

                                STRING332_tree = self._adaptor.createWithPayload(STRING332)
                                self._adaptor.addChild(root_0, STRING332_tree)



                        else:
                            if cnt98 >= 1:
                                break #loop98

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(98, self.input)
                            raise eee

                        cnt98 += 1


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

        COMMA335 = None
        COMMA337 = None
        test333 = None

        list_for334 = None

        test336 = None


        COMMA335_tree = None
        COMMA337_tree = None

        try:
            try:
                # kv.g:400:2: ( test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )? )
                # kv.g:400:4: test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_listmaker2370)
                test333 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test333.tree)
                # kv.g:400:9: ( list_for | ( options {greedy=true; } : COMMA test )* )
                alt101 = 2
                LA101_0 = self.input.LA(1)

                if (LA101_0 == 99) :
                    alt101 = 1
                elif (LA101_0 == COMMA or LA101_0 == RBRACK) :
                    alt101 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 101, 0, self.input)

                    raise nvae

                if alt101 == 1:
                    # kv.g:400:10: list_for
                    pass 
                    self._state.following.append(self.FOLLOW_list_for_in_listmaker2373)
                    list_for334 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for334.tree)


                elif alt101 == 2:
                    # kv.g:400:21: ( options {greedy=true; } : COMMA test )*
                    pass 
                    # kv.g:400:21: ( options {greedy=true; } : COMMA test )*
                    while True: #loop100
                        alt100 = 2
                        LA100_0 = self.input.LA(1)

                        if (LA100_0 == COMMA) :
                            LA100_1 = self.input.LA(2)

                            if (LA100_1 == WNAME or (PLUS <= LA100_1 <= MINUS) or LA100_1 == NAME or LA100_1 == LPAREN or LA100_1 == NOT or (TILDE <= LA100_1 <= LBRACK) or LA100_1 == LCURLY or (BACKQUOTE <= LA100_1 <= STRING) or LA100_1 == 106) :
                                alt100 = 1




                        if alt100 == 1:
                            # kv.g:400:45: COMMA test
                            pass 
                            COMMA335=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2385)
                            if self._state.backtracking == 0:

                                COMMA335_tree = self._adaptor.createWithPayload(COMMA335)
                                self._adaptor.addChild(root_0, COMMA335_tree)

                            self._state.following.append(self.FOLLOW_test_in_listmaker2387)
                            test336 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test336.tree)


                        else:
                            break #loop100



                # kv.g:400:60: ( COMMA )?
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if (LA102_0 == COMMA) :
                    alt102 = 1
                if alt102 == 1:
                    # kv.g:400:61: COMMA
                    pass 
                    COMMA337=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2394)
                    if self._state.backtracking == 0:

                        COMMA337_tree = self._adaptor.createWithPayload(COMMA337)
                        self._adaptor.addChild(root_0, COMMA337_tree)







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

        COMMA339 = None
        COMMA341 = None
        test338 = None

        test340 = None

        gen_for342 = None


        COMMA339_tree = None
        COMMA341_tree = None

        try:
            try:
                # kv.g:403:2: ( test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for ) )
                # kv.g:403:4: test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist_gexp2406)
                test338 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test338.tree)
                # kv.g:403:9: ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == COMMA or LA105_0 == RPAREN) :
                    alt105 = 1
                elif (LA105_0 == 99) :
                    alt105 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 105, 0, self.input)

                    raise nvae

                if alt105 == 1:
                    # kv.g:403:11: ( options {k=2; } : COMMA test )* ( COMMA )?
                    pass 
                    # kv.g:403:11: ( options {k=2; } : COMMA test )*
                    while True: #loop103
                        alt103 = 2
                        alt103 = self.dfa103.predict(self.input)
                        if alt103 == 1:
                            # kv.g:403:28: COMMA test
                            pass 
                            COMMA339=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp2419)
                            if self._state.backtracking == 0:

                                COMMA339_tree = self._adaptor.createWithPayload(COMMA339)
                                self._adaptor.addChild(root_0, COMMA339_tree)

                            self._state.following.append(self.FOLLOW_test_in_testlist_gexp2421)
                            test340 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test340.tree)


                        else:
                            break #loop103
                    # kv.g:403:41: ( COMMA )?
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == COMMA) :
                        alt104 = 1
                    if alt104 == 1:
                        # kv.g:403:42: COMMA
                        pass 
                        COMMA341=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp2426)
                        if self._state.backtracking == 0:

                            COMMA341_tree = self._adaptor.createWithPayload(COMMA341)
                            self._adaptor.addChild(root_0, COMMA341_tree)






                elif alt105 == 2:
                    # kv.g:403:52: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_testlist_gexp2432)
                    gen_for342 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for342.tree)






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

        string_literal343 = None
        COLON345 = None
        varargslist344 = None

        test346 = None


        string_literal343_tree = None
        COLON345_tree = None

        try:
            try:
                # kv.g:406:2: ( 'lambda' ( varargslist )? COLON test )
                # kv.g:406:4: 'lambda' ( varargslist )? COLON test
                pass 
                root_0 = self._adaptor.nil()

                string_literal343=self.match(self.input, 106, self.FOLLOW_106_in_lambdef2444)
                if self._state.backtracking == 0:

                    string_literal343_tree = self._adaptor.createWithPayload(string_literal343)
                    self._adaptor.addChild(root_0, string_literal343_tree)

                # kv.g:406:13: ( varargslist )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == WNAME or LA106_0 == NAME or (STAR <= LA106_0 <= DOUBLESTAR) or LA106_0 == LPAREN) :
                    alt106 = 1
                if alt106 == 1:
                    # kv.g:406:14: varargslist
                    pass 
                    self._state.following.append(self.FOLLOW_varargslist_in_lambdef2447)
                    varargslist344 = self.varargslist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, varargslist344.tree)



                COLON345=self.match(self.input, COLON, self.FOLLOW_COLON_in_lambdef2451)
                if self._state.backtracking == 0:

                    COLON345_tree = self._adaptor.createWithPayload(COLON345)
                    self._adaptor.addChild(root_0, COLON345_tree)

                self._state.following.append(self.FOLLOW_test_in_lambdef2453)
                test346 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test346.tree)



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

        LPAREN347 = None
        RPAREN349 = None
        LBRACK350 = None
        RBRACK352 = None
        DOT353 = None
        arglist348 = None

        subscriptlist351 = None

        identifier354 = None


        LPAREN347_tree = None
        RPAREN349_tree = None
        LBRACK350_tree = None
        RBRACK352_tree = None
        DOT353_tree = None

        try:
            try:
                # kv.g:409:2: ( LPAREN ( arglist )? RPAREN | LBRACK subscriptlist RBRACK | DOT identifier )
                alt108 = 3
                LA108 = self.input.LA(1)
                if LA108 == LPAREN:
                    alt108 = 1
                elif LA108 == LBRACK:
                    alt108 = 2
                elif LA108 == DOT:
                    alt108 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 108, 0, self.input)

                    raise nvae

                if alt108 == 1:
                    # kv.g:409:4: LPAREN ( arglist )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN347=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer2463)
                    if self._state.backtracking == 0:

                        LPAREN347_tree = self._adaptor.createWithPayload(LPAREN347)
                        self._adaptor.addChild(root_0, LPAREN347_tree)

                    # kv.g:409:11: ( arglist )?
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if (LA107_0 == WNAME or (PLUS <= LA107_0 <= MINUS) or LA107_0 == NAME or (STAR <= LA107_0 <= DOUBLESTAR) or LA107_0 == LPAREN or LA107_0 == NOT or (TILDE <= LA107_0 <= LBRACK) or LA107_0 == LCURLY or (BACKQUOTE <= LA107_0 <= STRING) or LA107_0 == 106) :
                        alt107 = 1
                    if alt107 == 1:
                        # kv.g:409:12: arglist
                        pass 
                        self._state.following.append(self.FOLLOW_arglist_in_trailer2466)
                        arglist348 = self.arglist()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arglist348.tree)



                    RPAREN349=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer2470)
                    if self._state.backtracking == 0:

                        RPAREN349_tree = self._adaptor.createWithPayload(RPAREN349)
                        self._adaptor.addChild(root_0, RPAREN349_tree)



                elif alt108 == 2:
                    # kv.g:410:4: LBRACK subscriptlist RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK350=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer2475)
                    if self._state.backtracking == 0:

                        LBRACK350_tree = self._adaptor.createWithPayload(LBRACK350)
                        self._adaptor.addChild(root_0, LBRACK350_tree)

                    self._state.following.append(self.FOLLOW_subscriptlist_in_trailer2477)
                    subscriptlist351 = self.subscriptlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, subscriptlist351.tree)
                    RBRACK352=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer2479)
                    if self._state.backtracking == 0:

                        RBRACK352_tree = self._adaptor.createWithPayload(RBRACK352)
                        self._adaptor.addChild(root_0, RBRACK352_tree)



                elif alt108 == 3:
                    # kv.g:411:4: DOT identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT353=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2484)
                    if self._state.backtracking == 0:

                        DOT353_tree = self._adaptor.createWithPayload(DOT353)
                        self._adaptor.addChild(root_0, DOT353_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_trailer2486)
                    identifier354 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier354.tree)


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

        COMMA356 = None
        COMMA358 = None
        subscript355 = None

        subscript357 = None


        COMMA356_tree = None
        COMMA358_tree = None

        try:
            try:
                # kv.g:414:2: ( subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )? )
                # kv.g:414:4: subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_subscript_in_subscriptlist2496)
                subscript355 = self.subscript()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, subscript355.tree)
                # kv.g:414:14: ( options {greedy=true; } : COMMA subscript )*
                while True: #loop109
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == COMMA) :
                        LA109_1 = self.input.LA(2)

                        if ((WNAME <= LA109_1 <= COLON) or (PLUS <= LA109_1 <= MINUS) or LA109_1 == NAME or LA109_1 == LPAREN or LA109_1 == NOT or (TILDE <= LA109_1 <= LBRACK) or LA109_1 == LCURLY or (BACKQUOTE <= LA109_1 <= DOT) or LA109_1 == 106) :
                            alt109 = 1




                    if alt109 == 1:
                        # kv.g:414:38: COMMA subscript
                        pass 
                        COMMA356=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2506)
                        if self._state.backtracking == 0:

                            COMMA356_tree = self._adaptor.createWithPayload(COMMA356)
                            self._adaptor.addChild(root_0, COMMA356_tree)

                        self._state.following.append(self.FOLLOW_subscript_in_subscriptlist2508)
                        subscript357 = self.subscript()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, subscript357.tree)


                    else:
                        break #loop109
                # kv.g:414:56: ( COMMA )?
                alt110 = 2
                LA110_0 = self.input.LA(1)

                if (LA110_0 == COMMA) :
                    alt110 = 1
                if alt110 == 1:
                    # kv.g:414:57: COMMA
                    pass 
                    COMMA358=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2513)
                    if self._state.backtracking == 0:

                        COMMA358_tree = self._adaptor.createWithPayload(COMMA358)
                        self._adaptor.addChild(root_0, COMMA358_tree)







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

        DOT359 = None
        DOT360 = None
        DOT361 = None
        COLON363 = None
        COLON366 = None
        test362 = None

        test364 = None

        sliceop365 = None

        test367 = None

        sliceop368 = None


        DOT359_tree = None
        DOT360_tree = None
        DOT361_tree = None
        COLON363_tree = None
        COLON366_tree = None

        try:
            try:
                # kv.g:417:2: ( DOT DOT DOT | test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt116 = 3
                LA116 = self.input.LA(1)
                if LA116 == DOT:
                    alt116 = 1
                elif LA116 == WNAME or LA116 == PLUS or LA116 == MINUS or LA116 == NAME or LA116 == LPAREN or LA116 == NOT or LA116 == TILDE or LA116 == LBRACK or LA116 == LCURLY or LA116 == BACKQUOTE or LA116 == NONE or LA116 == INT or LA116 == LONGINT or LA116 == FLOAT or LA116 == COMPLEX or LA116 == STRING or LA116 == 106:
                    alt116 = 2
                elif LA116 == COLON:
                    alt116 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 116, 0, self.input)

                    raise nvae

                if alt116 == 1:
                    # kv.g:417:4: DOT DOT DOT
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT359=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2525)
                    if self._state.backtracking == 0:

                        DOT359_tree = self._adaptor.createWithPayload(DOT359)
                        self._adaptor.addChild(root_0, DOT359_tree)

                    DOT360=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2527)
                    if self._state.backtracking == 0:

                        DOT360_tree = self._adaptor.createWithPayload(DOT360)
                        self._adaptor.addChild(root_0, DOT360_tree)

                    DOT361=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript2529)
                    if self._state.backtracking == 0:

                        DOT361_tree = self._adaptor.createWithPayload(DOT361)
                        self._adaptor.addChild(root_0, DOT361_tree)



                elif alt116 == 2:
                    # kv.g:418:4: test ( COLON ( test )? ( sliceop )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_test_in_subscript2534)
                    test362 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test362.tree)
                    # kv.g:418:9: ( COLON ( test )? ( sliceop )? )?
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == COLON) :
                        alt113 = 1
                    if alt113 == 1:
                        # kv.g:418:10: COLON ( test )? ( sliceop )?
                        pass 
                        COLON363=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript2537)
                        if self._state.backtracking == 0:

                            COLON363_tree = self._adaptor.createWithPayload(COLON363)
                            self._adaptor.addChild(root_0, COLON363_tree)

                        # kv.g:418:16: ( test )?
                        alt111 = 2
                        LA111_0 = self.input.LA(1)

                        if (LA111_0 == WNAME or (PLUS <= LA111_0 <= MINUS) or LA111_0 == NAME or LA111_0 == LPAREN or LA111_0 == NOT or (TILDE <= LA111_0 <= LBRACK) or LA111_0 == LCURLY or (BACKQUOTE <= LA111_0 <= STRING) or LA111_0 == 106) :
                            alt111 = 1
                        if alt111 == 1:
                            # kv.g:418:17: test
                            pass 
                            self._state.following.append(self.FOLLOW_test_in_subscript2540)
                            test364 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test364.tree)



                        # kv.g:418:24: ( sliceop )?
                        alt112 = 2
                        LA112_0 = self.input.LA(1)

                        if (LA112_0 == COLON) :
                            alt112 = 1
                        if alt112 == 1:
                            # kv.g:418:25: sliceop
                            pass 
                            self._state.following.append(self.FOLLOW_sliceop_in_subscript2545)
                            sliceop365 = self.sliceop()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, sliceop365.tree)








                elif alt116 == 3:
                    # kv.g:419:4: COLON ( test )? ( sliceop )?
                    pass 
                    root_0 = self._adaptor.nil()

                    COLON366=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript2554)
                    if self._state.backtracking == 0:

                        COLON366_tree = self._adaptor.createWithPayload(COLON366)
                        self._adaptor.addChild(root_0, COLON366_tree)

                    # kv.g:419:10: ( test )?
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == WNAME or (PLUS <= LA114_0 <= MINUS) or LA114_0 == NAME or LA114_0 == LPAREN or LA114_0 == NOT or (TILDE <= LA114_0 <= LBRACK) or LA114_0 == LCURLY or (BACKQUOTE <= LA114_0 <= STRING) or LA114_0 == 106) :
                        alt114 = 1
                    if alt114 == 1:
                        # kv.g:419:11: test
                        pass 
                        self._state.following.append(self.FOLLOW_test_in_subscript2557)
                        test367 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test367.tree)



                    # kv.g:419:18: ( sliceop )?
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == COLON) :
                        alt115 = 1
                    if alt115 == 1:
                        # kv.g:419:19: sliceop
                        pass 
                        self._state.following.append(self.FOLLOW_sliceop_in_subscript2562)
                        sliceop368 = self.sliceop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sliceop368.tree)





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

        COLON369 = None
        test370 = None


        COLON369_tree = None

        try:
            try:
                # kv.g:422:2: ( COLON ( test )? )
                # kv.g:422:4: COLON ( test )?
                pass 
                root_0 = self._adaptor.nil()

                COLON369=self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop2574)
                if self._state.backtracking == 0:

                    COLON369_tree = self._adaptor.createWithPayload(COLON369)
                    self._adaptor.addChild(root_0, COLON369_tree)

                # kv.g:422:10: ( test )?
                alt117 = 2
                LA117_0 = self.input.LA(1)

                if (LA117_0 == WNAME or (PLUS <= LA117_0 <= MINUS) or LA117_0 == NAME or LA117_0 == LPAREN or LA117_0 == NOT or (TILDE <= LA117_0 <= LBRACK) or LA117_0 == LCURLY or (BACKQUOTE <= LA117_0 <= STRING) or LA117_0 == 106) :
                    alt117 = 1
                if alt117 == 1:
                    # kv.g:422:11: test
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_sliceop2577)
                    test370 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test370.tree)






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

        COMMA372 = None
        COMMA374 = None
        expr371 = None

        expr373 = None


        COMMA372_tree = None
        COMMA374_tree = None

        try:
            try:
                # kv.g:425:2: ( expr ( options {k=2; } : COMMA expr )* ( COMMA )? )
                # kv.g:425:4: expr ( options {k=2; } : COMMA expr )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_exprlist2589)
                expr371 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr371.tree)
                # kv.g:425:9: ( options {k=2; } : COMMA expr )*
                while True: #loop118
                    alt118 = 2
                    alt118 = self.dfa118.predict(self.input)
                    if alt118 == 1:
                        # kv.g:425:26: COMMA expr
                        pass 
                        COMMA372=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2600)
                        if self._state.backtracking == 0:

                            COMMA372_tree = self._adaptor.createWithPayload(COMMA372)
                            self._adaptor.addChild(root_0, COMMA372_tree)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist2602)
                        expr373 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr373.tree)


                    else:
                        break #loop118
                # kv.g:425:39: ( COMMA )?
                alt119 = 2
                LA119_0 = self.input.LA(1)

                if (LA119_0 == COMMA) :
                    alt119 = 1
                if alt119 == 1:
                    # kv.g:425:40: COMMA
                    pass 
                    COMMA374=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2607)
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

        COMMA376 = None
        COMMA378 = None
        test375 = None

        test377 = None


        COMMA376_tree = None
        COMMA378_tree = None

        try:
            try:
                # kv.g:428:2: ( test ( options {k=2; } : COMMA test )* ( COMMA )? )
                # kv.g:428:4: test ( options {k=2; } : COMMA test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist2619)
                test375 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test375.tree)
                # kv.g:428:9: ( options {k=2; } : COMMA test )*
                while True: #loop120
                    alt120 = 2
                    alt120 = self.dfa120.predict(self.input)
                    if alt120 == 1:
                        # kv.g:428:26: COMMA test
                        pass 
                        COMMA376=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2630)
                        if self._state.backtracking == 0:

                            COMMA376_tree = self._adaptor.createWithPayload(COMMA376)
                            self._adaptor.addChild(root_0, COMMA376_tree)

                        self._state.following.append(self.FOLLOW_test_in_testlist2632)
                        test377 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test377.tree)


                    else:
                        break #loop120
                # kv.g:428:39: ( COMMA )?
                alt121 = 2
                LA121_0 = self.input.LA(1)

                if (LA121_0 == COMMA) :
                    alt121 = 1
                if alt121 == 1:
                    # kv.g:428:40: COMMA
                    pass 
                    COMMA378=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2637)
                    if self._state.backtracking == 0:

                        COMMA378_tree = self._adaptor.createWithPayload(COMMA378)
                        self._adaptor.addChild(root_0, COMMA378_tree)







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

        COLON380 = None
        COMMA382 = None
        COLON384 = None
        COMMA386 = None
        test379 = None

        test381 = None

        test383 = None

        test385 = None


        COLON380_tree = None
        COMMA382_tree = None
        COLON384_tree = None
        COMMA386_tree = None

        try:
            try:
                # kv.g:431:2: ( test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )? )
                # kv.g:431:4: test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_dictmaker2649)
                test379 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test379.tree)
                COLON380=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2651)
                if self._state.backtracking == 0:

                    COLON380_tree = self._adaptor.createWithPayload(COLON380)
                    self._adaptor.addChild(root_0, COLON380_tree)

                self._state.following.append(self.FOLLOW_test_in_dictmaker2653)
                test381 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test381.tree)
                # kv.g:431:20: ( options {k=2; } : COMMA test COLON test )*
                while True: #loop122
                    alt122 = 2
                    alt122 = self.dfa122.predict(self.input)
                    if alt122 == 1:
                        # kv.g:431:37: COMMA test COLON test
                        pass 
                        COMMA382=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2664)
                        if self._state.backtracking == 0:

                            COMMA382_tree = self._adaptor.createWithPayload(COMMA382)
                            self._adaptor.addChild(root_0, COMMA382_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2666)
                        test383 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test383.tree)
                        COLON384=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2668)
                        if self._state.backtracking == 0:

                            COLON384_tree = self._adaptor.createWithPayload(COLON384)
                            self._adaptor.addChild(root_0, COLON384_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2670)
                        test385 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test385.tree)


                    else:
                        break #loop122
                # kv.g:431:61: ( COMMA )?
                alt123 = 2
                LA123_0 = self.input.LA(1)

                if (LA123_0 == COMMA) :
                    alt123 = 1
                if alt123 == 1:
                    # kv.g:431:62: COMMA
                    pass 
                    COMMA386=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2675)
                    if self._state.backtracking == 0:

                        COMMA386_tree = self._adaptor.createWithPayload(COMMA386)
                        self._adaptor.addChild(root_0, COMMA386_tree)







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

        COMMA388 = None
        COMMA390 = None
        STAR391 = None
        COMMA393 = None
        DOUBLESTAR394 = None
        DOUBLESTAR396 = None
        STAR398 = None
        COMMA400 = None
        DOUBLESTAR401 = None
        DOUBLESTAR403 = None
        argument387 = None

        argument389 = None

        test392 = None

        test395 = None

        test397 = None

        test399 = None

        test402 = None

        test404 = None


        COMMA388_tree = None
        COMMA390_tree = None
        STAR391_tree = None
        COMMA393_tree = None
        DOUBLESTAR394_tree = None
        DOUBLESTAR396_tree = None
        STAR398_tree = None
        COMMA400_tree = None
        DOUBLESTAR401_tree = None
        DOUBLESTAR403_tree = None

        try:
            try:
                # kv.g:434:2: ( argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )? | STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )
                alt129 = 3
                LA129 = self.input.LA(1)
                if LA129 == WNAME or LA129 == PLUS or LA129 == MINUS or LA129 == NAME or LA129 == LPAREN or LA129 == NOT or LA129 == TILDE or LA129 == LBRACK or LA129 == LCURLY or LA129 == BACKQUOTE or LA129 == NONE or LA129 == INT or LA129 == LONGINT or LA129 == FLOAT or LA129 == COMPLEX or LA129 == STRING or LA129 == 106:
                    alt129 = 1
                elif LA129 == STAR:
                    alt129 = 2
                elif LA129 == DOUBLESTAR:
                    alt129 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 129, 0, self.input)

                    raise nvae

                if alt129 == 1:
                    # kv.g:434:4: argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_argument_in_arglist2687)
                    argument387 = self.argument()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, argument387.tree)
                    # kv.g:434:13: ( COMMA argument )*
                    while True: #loop124
                        alt124 = 2
                        LA124_0 = self.input.LA(1)

                        if (LA124_0 == COMMA) :
                            LA124_1 = self.input.LA(2)

                            if (LA124_1 == WNAME or (PLUS <= LA124_1 <= MINUS) or LA124_1 == NAME or LA124_1 == LPAREN or LA124_1 == NOT or (TILDE <= LA124_1 <= LBRACK) or LA124_1 == LCURLY or (BACKQUOTE <= LA124_1 <= STRING) or LA124_1 == 106) :
                                alt124 = 1




                        if alt124 == 1:
                            # kv.g:434:14: COMMA argument
                            pass 
                            COMMA388=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2690)
                            if self._state.backtracking == 0:

                                COMMA388_tree = self._adaptor.createWithPayload(COMMA388)
                                self._adaptor.addChild(root_0, COMMA388_tree)

                            self._state.following.append(self.FOLLOW_argument_in_arglist2692)
                            argument389 = self.argument()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, argument389.tree)


                        else:
                            break #loop124
                    # kv.g:434:31: ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    alt127 = 2
                    LA127_0 = self.input.LA(1)

                    if (LA127_0 == COMMA) :
                        alt127 = 1
                    if alt127 == 1:
                        # kv.g:434:33: COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        pass 
                        COMMA390=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2698)
                        if self._state.backtracking == 0:

                            COMMA390_tree = self._adaptor.createWithPayload(COMMA390)
                            self._adaptor.addChild(root_0, COMMA390_tree)

                        # kv.g:434:39: ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        alt126 = 3
                        LA126_0 = self.input.LA(1)

                        if (LA126_0 == STAR) :
                            alt126 = 1
                        elif (LA126_0 == DOUBLESTAR) :
                            alt126 = 2
                        if alt126 == 1:
                            # kv.g:434:41: STAR test ( COMMA DOUBLESTAR test )?
                            pass 
                            STAR391=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2702)
                            if self._state.backtracking == 0:

                                STAR391_tree = self._adaptor.createWithPayload(STAR391)
                                self._adaptor.addChild(root_0, STAR391_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2704)
                            test392 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test392.tree)
                            # kv.g:434:51: ( COMMA DOUBLESTAR test )?
                            alt125 = 2
                            LA125_0 = self.input.LA(1)

                            if (LA125_0 == COMMA) :
                                alt125 = 1
                            if alt125 == 1:
                                # kv.g:434:52: COMMA DOUBLESTAR test
                                pass 
                                COMMA393=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2707)
                                if self._state.backtracking == 0:

                                    COMMA393_tree = self._adaptor.createWithPayload(COMMA393)
                                    self._adaptor.addChild(root_0, COMMA393_tree)

                                DOUBLESTAR394=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2709)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR394_tree = self._adaptor.createWithPayload(DOUBLESTAR394)
                                    self._adaptor.addChild(root_0, DOUBLESTAR394_tree)

                                self._state.following.append(self.FOLLOW_test_in_arglist2711)
                                test395 = self.test()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, test395.tree)





                        elif alt126 == 2:
                            # kv.g:434:78: DOUBLESTAR test
                            pass 
                            DOUBLESTAR396=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2717)
                            if self._state.backtracking == 0:

                                DOUBLESTAR396_tree = self._adaptor.createWithPayload(DOUBLESTAR396)
                                self._adaptor.addChild(root_0, DOUBLESTAR396_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2719)
                            test397 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test397.tree)








                elif alt129 == 2:
                    # kv.g:435:4: STAR test ( COMMA DOUBLESTAR test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR398=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2730)
                    if self._state.backtracking == 0:

                        STAR398_tree = self._adaptor.createWithPayload(STAR398)
                        self._adaptor.addChild(root_0, STAR398_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2732)
                    test399 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test399.tree)
                    # kv.g:435:14: ( COMMA DOUBLESTAR test )?
                    alt128 = 2
                    LA128_0 = self.input.LA(1)

                    if (LA128_0 == COMMA) :
                        alt128 = 1
                    if alt128 == 1:
                        # kv.g:435:15: COMMA DOUBLESTAR test
                        pass 
                        COMMA400=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2735)
                        if self._state.backtracking == 0:

                            COMMA400_tree = self._adaptor.createWithPayload(COMMA400)
                            self._adaptor.addChild(root_0, COMMA400_tree)

                        DOUBLESTAR401=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2737)
                        if self._state.backtracking == 0:

                            DOUBLESTAR401_tree = self._adaptor.createWithPayload(DOUBLESTAR401)
                            self._adaptor.addChild(root_0, DOUBLESTAR401_tree)

                        self._state.following.append(self.FOLLOW_test_in_arglist2739)
                        test402 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test402.tree)





                elif alt129 == 3:
                    # kv.g:436:4: DOUBLESTAR test
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR403=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2746)
                    if self._state.backtracking == 0:

                        DOUBLESTAR403_tree = self._adaptor.createWithPayload(DOUBLESTAR403)
                        self._adaptor.addChild(root_0, DOUBLESTAR403_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2748)
                    test404 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test404.tree)


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

        ASSIGN406 = None
        test405 = None

        test407 = None

        gen_for408 = None


        ASSIGN406_tree = None

        try:
            try:
                # kv.g:439:2: ( test ( ( ASSIGN test ) | gen_for )? )
                # kv.g:439:4: test ( ( ASSIGN test ) | gen_for )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_argument2758)
                test405 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test405.tree)
                # kv.g:439:9: ( ( ASSIGN test ) | gen_for )?
                alt130 = 3
                LA130_0 = self.input.LA(1)

                if (LA130_0 == ASSIGN) :
                    alt130 = 1
                elif (LA130_0 == 99) :
                    alt130 = 2
                if alt130 == 1:
                    # kv.g:439:11: ( ASSIGN test )
                    pass 
                    # kv.g:439:11: ( ASSIGN test )
                    # kv.g:439:13: ASSIGN test
                    pass 
                    ASSIGN406=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument2764)
                    if self._state.backtracking == 0:

                        ASSIGN406_tree = self._adaptor.createWithPayload(ASSIGN406)
                        self._adaptor.addChild(root_0, ASSIGN406_tree)

                    self._state.following.append(self.FOLLOW_test_in_argument2766)
                    test407 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test407.tree)





                elif alt130 == 2:
                    # kv.g:439:29: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_argument2772)
                    gen_for408 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for408.tree)






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

        list_for409 = None

        list_if410 = None



        try:
            try:
                # kv.g:442:2: ( list_for | list_if )
                alt131 = 2
                LA131_0 = self.input.LA(1)

                if (LA131_0 == 99) :
                    alt131 = 1
                elif (LA131_0 == 95) :
                    alt131 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 131, 0, self.input)

                    raise nvae

                if alt131 == 1:
                    # kv.g:442:4: list_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_for_in_list_iter2785)
                    list_for409 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for409.tree)


                elif alt131 == 2:
                    # kv.g:442:15: list_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_if_in_list_iter2789)
                    list_if410 = self.list_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_if410.tree)


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

        string_literal411 = None
        string_literal413 = None
        exprlist412 = None

        testlist414 = None

        list_iter415 = None


        string_literal411_tree = None
        string_literal413_tree = None

        try:
            try:
                # kv.g:445:2: ( 'for' exprlist 'in' testlist ( list_iter )? )
                # kv.g:445:4: 'for' exprlist 'in' testlist ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal411=self.match(self.input, 99, self.FOLLOW_99_in_list_for2799)
                if self._state.backtracking == 0:

                    string_literal411_tree = self._adaptor.createWithPayload(string_literal411)
                    self._adaptor.addChild(root_0, string_literal411_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_list_for2801)
                exprlist412 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist412.tree)
                string_literal413=self.match(self.input, 93, self.FOLLOW_93_in_list_for2803)
                if self._state.backtracking == 0:

                    string_literal413_tree = self._adaptor.createWithPayload(string_literal413)
                    self._adaptor.addChild(root_0, string_literal413_tree)

                self._state.following.append(self.FOLLOW_testlist_in_list_for2805)
                testlist414 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist414.tree)
                # kv.g:445:33: ( list_iter )?
                alt132 = 2
                LA132_0 = self.input.LA(1)

                if (LA132_0 == 95 or LA132_0 == 99) :
                    alt132 = 1
                if alt132 == 1:
                    # kv.g:445:34: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_for2808)
                    list_iter415 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter415.tree)






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

        string_literal416 = None
        test417 = None

        list_iter418 = None


        string_literal416_tree = None

        try:
            try:
                # kv.g:448:2: ( 'if' test ( list_iter )? )
                # kv.g:448:4: 'if' test ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal416=self.match(self.input, 95, self.FOLLOW_95_in_list_if2820)
                if self._state.backtracking == 0:

                    string_literal416_tree = self._adaptor.createWithPayload(string_literal416)
                    self._adaptor.addChild(root_0, string_literal416_tree)

                self._state.following.append(self.FOLLOW_test_in_list_if2822)
                test417 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test417.tree)
                # kv.g:448:14: ( list_iter )?
                alt133 = 2
                LA133_0 = self.input.LA(1)

                if (LA133_0 == 95 or LA133_0 == 99) :
                    alt133 = 1
                if alt133 == 1:
                    # kv.g:448:15: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_if2825)
                    list_iter418 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter418.tree)






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

        gen_for419 = None

        gen_if420 = None



        try:
            try:
                # kv.g:451:2: ( gen_for | gen_if )
                alt134 = 2
                LA134_0 = self.input.LA(1)

                if (LA134_0 == 99) :
                    alt134 = 1
                elif (LA134_0 == 95) :
                    alt134 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 134, 0, self.input)

                    raise nvae

                if alt134 == 1:
                    # kv.g:451:4: gen_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_for_in_gen_iter2837)
                    gen_for419 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for419.tree)


                elif alt134 == 2:
                    # kv.g:451:14: gen_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_if_in_gen_iter2841)
                    gen_if420 = self.gen_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_if420.tree)


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

        string_literal421 = None
        string_literal423 = None
        exprlist422 = None

        or_test424 = None

        gen_iter425 = None


        string_literal421_tree = None
        string_literal423_tree = None

        try:
            try:
                # kv.g:454:2: ( 'for' exprlist 'in' or_test ( gen_iter )? )
                # kv.g:454:4: 'for' exprlist 'in' or_test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal421=self.match(self.input, 99, self.FOLLOW_99_in_gen_for2851)
                if self._state.backtracking == 0:

                    string_literal421_tree = self._adaptor.createWithPayload(string_literal421)
                    self._adaptor.addChild(root_0, string_literal421_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_gen_for2853)
                exprlist422 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist422.tree)
                string_literal423=self.match(self.input, 93, self.FOLLOW_93_in_gen_for2855)
                if self._state.backtracking == 0:

                    string_literal423_tree = self._adaptor.createWithPayload(string_literal423)
                    self._adaptor.addChild(root_0, string_literal423_tree)

                self._state.following.append(self.FOLLOW_or_test_in_gen_for2857)
                or_test424 = self.or_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_test424.tree)
                # kv.g:454:32: ( gen_iter )?
                alt135 = 2
                LA135_0 = self.input.LA(1)

                if (LA135_0 == 95 or LA135_0 == 99) :
                    alt135 = 1
                if alt135 == 1:
                    # kv.g:454:32: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_for2859)
                    gen_iter425 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter425.tree)






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

        string_literal426 = None
        test427 = None

        gen_iter428 = None


        string_literal426_tree = None

        try:
            try:
                # kv.g:457:2: ( 'if' test ( gen_iter )? )
                # kv.g:457:4: 'if' test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal426=self.match(self.input, 95, self.FOLLOW_95_in_gen_if2870)
                if self._state.backtracking == 0:

                    string_literal426_tree = self._adaptor.createWithPayload(string_literal426)
                    self._adaptor.addChild(root_0, string_literal426_tree)

                self._state.following.append(self.FOLLOW_test_in_gen_if2872)
                test427 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test427.tree)
                # kv.g:457:14: ( gen_iter )?
                alt136 = 2
                LA136_0 = self.input.LA(1)

                if (LA136_0 == 95 or LA136_0 == 99) :
                    alt136 = 1
                if alt136 == 1:
                    # kv.g:457:14: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_if2874)
                    gen_iter428 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter428.tree)






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

        string_literal429 = None
        testlist430 = None


        string_literal429_tree = None

        try:
            try:
                # kv.g:460:2: ( 'yield' ( testlist )? )
                # kv.g:460:4: 'yield' ( testlist )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal429=self.match(self.input, 107, self.FOLLOW_107_in_yield_expr2885)
                if self._state.backtracking == 0:

                    string_literal429_tree = self._adaptor.createWithPayload(string_literal429)
                    self._adaptor.addChild(root_0, string_literal429_tree)

                # kv.g:460:12: ( testlist )?
                alt137 = 2
                LA137_0 = self.input.LA(1)

                if (LA137_0 == WNAME or (PLUS <= LA137_0 <= MINUS) or LA137_0 == NAME or LA137_0 == LPAREN or LA137_0 == NOT or (TILDE <= LA137_0 <= LBRACK) or LA137_0 == LCURLY or (BACKQUOTE <= LA137_0 <= STRING) or LA137_0 == 106) :
                    alt137 = 1
                if alt137 == 1:
                    # kv.g:460:12: testlist
                    pass 
                    self._state.following.append(self.FOLLOW_testlist_in_yield_expr2887)
                    testlist430 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist430.tree)






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

        set431 = None

        set431_tree = None

        try:
            try:
                # kv.g:552:2: ( WNAME | NAME )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set431 = self.input.LT(1)
                if self.input.LA(1) == WNAME or self.input.LA(1) == NAME:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set431))
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
        self.match(self.input, 95, self.FOLLOW_95_in_synpred1_kv1935)
        self._state.following.append(self.FOLLOW_or_test_in_synpred1_kv1937)
        self.or_test()

        self._state.following.pop()
        self.match(self.input, 96, self.FOLLOW_96_in_synpred1_kv1939)


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



    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\3\uffff\1\4\1\uffff\1\4\1\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\30\2\25\1\4\1\uffff\1\4\1\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\30\1\31\1\25\1\106\1\uffff\1\106\1\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\4\uffff\1\1\1\uffff\1\2"
        )

    DFA5_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\3\uffff\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\6\1\4\17\uffff\1\5\3\4\5\uffff\2\4\27\uffff\1\4"
        u"\16\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\4\17\uffff\1\5\3\4\5\uffff\2\4\27\uffff\1\4"
        u"\16\uffff\1\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\27\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\15\uffff\1\23\3\uffff\1\23\5\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\67\1\30\1\32\3\30\1\25\2\32\1\30\1\34\1\30\1\25\1\4\1\32\1\30"
        u"\1\34\1\4\2\uffff\1\34\1\30\1\34"
        )

    DFA8_max = DFA.unpack(
        u"\1\67\1\35\1\70\1\30\2\35\1\31\2\70\1\30\1\70\1\30\1\25\1\106\1"
        u"\70\1\35\1\70\1\106\2\uffff\1\70\1\30\1\70"
        )

    DFA8_accept = DFA.unpack(
        u"\22\uffff\1\2\1\1\3\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\27\uffff"
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
        DFA.unpack(u"\1\22\20\uffff\1\21\3\23\36\uffff\1\23\16\uffff\1\23"),
        DFA.unpack(u"\1\5\1\4\34\uffff\1\6"),
        DFA.unpack(u"\1\24\4\uffff\1\25"),
        DFA.unpack(u"\1\17\33\uffff\1\6"),
        DFA.unpack(u"\1\22\20\uffff\1\21\3\23\36\uffff\1\23\16\uffff\1\23"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\33\uffff\1\6"),
        DFA.unpack(u"\1\26"),
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
        u"\27\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\15\uffff\1\21\4\uffff\1\21\4\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\106\1\30\1\32\3\30\1\25\2\32\1\30\1\34\1\30\1\25\1\4\1\32\1"
        u"\30\1\34\1\uffff\1\4\1\uffff\1\34\1\30\1\34"
        )

    DFA18_max = DFA.unpack(
        u"\1\106\1\35\1\107\1\30\2\35\1\31\2\107\1\30\1\107\1\30\1\25\1\106"
        u"\1\107\1\35\1\107\1\uffff\1\106\1\uffff\1\107\1\30\1\107"
        )

    DFA18_accept = DFA.unpack(
        u"\21\uffff\1\1\1\uffff\1\2\3\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\27\uffff"
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
        DFA.unpack(u"\1\23\20\uffff\1\22\3\21\36\uffff\1\21\16\uffff\1\21"),
        DFA.unpack(u"\1\5\1\4\53\uffff\1\6"),
        DFA.unpack(u"\1\24\4\uffff\1\25"),
        DFA.unpack(u"\1\17\52\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\20\uffff\1\22\3\21\36\uffff\1\21\16\uffff\1\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\52\uffff\1\6"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\17\52\uffff\1\6")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\1\30\2\25\2\4\2\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\1\30\1\31\1\25\2\30\2\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA27_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\3\uffff\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\5\1\6\17\uffff\1\4\1\uffff\2\6"),
        DFA.unpack(u"\1\5\1\6\17\uffff\1\4\1\uffff\2\6"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\37\1\31\2\25\2\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\1\37\1\31\2\153\2\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1"
        )

    DFA33_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA33_transition = [
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

    # class definition for DFA #33

    class DFA33(DFA):
        pass


    # lookup tables for DFA #55

    DFA55_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA55_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA55_min = DFA.unpack(
        u"\2\5\36\uffff"
        )

    DFA55_max = DFA.unpack(
        u"\1\150\1\152\36\uffff"
        )

    DFA55_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1\26\uffff"
        )

    DFA55_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA55_transition = [
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

    # class definition for DFA #55

    class DFA55(DFA):
        pass


    # lookup tables for DFA #79

    DFA79_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA79_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA79_min = DFA.unpack(
        u"\1\5\1\0\23\uffff"
        )

    DFA79_max = DFA.unpack(
        u"\1\150\1\0\23\uffff"
        )

    DFA79_accept = DFA.unpack(
        u"\2\uffff\1\2\21\uffff\1\1"
        )

    DFA79_special = DFA.unpack(
        u"\1\uffff\1\0\23\uffff"
        )

            
    DFA79_transition = [
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

    # class definition for DFA #79

    class DFA79(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA79_1 = input.LA(1)

                 
                index79_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_kv()):
                    s = 20

                elif (True):
                    s = 2

                 
                input.seek(index79_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 79, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #85

    DFA85_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA85_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA85_min = DFA.unpack(
        u"\1\66\10\uffff\1\135\3\uffff"
        )

    DFA85_max = DFA.unpack(
        u"\1\151\10\uffff\1\151\3\uffff"
        )

    DFA85_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\uffff\1\12\1\11\1\13"
        )

    DFA85_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA85_transition = [
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

    # class definition for DFA #85

    class DFA85(DFA):
        pass


    # lookup tables for DFA #103

    DFA103_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA103_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA103_min = DFA.unpack(
        u"\1\33\1\30\22\uffff"
        )

    DFA103_max = DFA.unpack(
        u"\1\46\1\152\22\uffff"
        )

    DFA103_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\17\uffff"
        )

    DFA103_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA103_transition = [
        DFA.unpack(u"\1\1\12\uffff\1\2"),
        DFA.unpack(u"\1\4\3\uffff\2\4\1\uffff\1\4\5\uffff\1\4\1\2\17\uffff"
        u"\1\4\16\uffff\2\4\1\uffff\1\4\1\uffff\7\4\31\uffff\1\4"),
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

    # class definition for DFA #103

    class DFA103(DFA):
        pass


    # lookup tables for DFA #118

    DFA118_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA118_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA118_min = DFA.unpack(
        u"\2\5\36\uffff"
        )

    DFA118_max = DFA.unpack(
        u"\2\150\36\uffff"
        )

    DFA118_accept = DFA.unpack(
        u"\2\uffff\1\2\7\uffff\1\1\25\uffff"
        )

    DFA118_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA118_transition = [
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

    # class definition for DFA #118

    class DFA118(DFA):
        pass


    # lookup tables for DFA #120

    DFA120_eot = DFA.unpack(
        u"\60\uffff"
        )

    DFA120_eof = DFA.unpack(
        u"\60\uffff"
        )

    DFA120_min = DFA.unpack(
        u"\2\5\56\uffff"
        )

    DFA120_max = DFA.unpack(
        u"\1\150\1\152\56\uffff"
        )

    DFA120_accept = DFA.unpack(
        u"\2\uffff\1\2\17\uffff\1\1\6\uffff\1\1\26\uffff"
        )

    DFA120_special = DFA.unpack(
        u"\60\uffff"
        )

            
    DFA120_transition = [
        DFA.unpack(u"\1\2\17\uffff\1\2\3\uffff\1\2\1\uffff\1\1\5\uffff\1"
        u"\2\2\uffff\1\2\1\uffff\15\2\24\uffff\1\2\2\uffff\1\2\24\uffff\3"
        u"\2\1\uffff\1\2\1\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u"\1\2\17\uffff\1\2\2\uffff\1\22\1\2\1\uffff\1\2\2\22"
        u"\1\uffff\1\22\1\uffff\1\2\2\uffff\1\2\1\22\15\2\3\uffff\1\22\16"
        u"\uffff\2\22\1\2\1\22\1\uffff\1\31\6\22\16\uffff\3\2\1\uffff\1\2"
        u"\1\uffff\1\2\2\uffff\1\2\1\uffff\1\22"),
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

    # class definition for DFA #120

    class DFA120(DFA):
        pass


    # lookup tables for DFA #122

    DFA122_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA122_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA122_min = DFA.unpack(
        u"\1\33\1\30\22\uffff"
        )

    DFA122_max = DFA.unpack(
        u"\1\111\1\152\22\uffff"
        )

    DFA122_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\20\uffff"
        )

    DFA122_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA122_transition = [
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

    # class definition for DFA #122

    class DFA122(DFA):
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
    FOLLOW_NEWLINE_in_widget_body687 = frozenset([4, 21])
    FOLLOW_blank_in_widget_body690 = frozenset([4, 21])
    FOLLOW_INDENT_in_widget_body693 = frozenset([21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_stmt_in_widget_body697 = frozenset([5, 21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_DEDENT_in_widget_body701 = frozenset([1])
    FOLLOW_NEWLINE_in_canvas_body712 = frozenset([4, 21])
    FOLLOW_blank_in_canvas_body715 = frozenset([4, 21])
    FOLLOW_INDENT_in_canvas_body718 = frozenset([21, 22, 23, 24, 55, 70])
    FOLLOW_canvas_stmt_in_canvas_body722 = frozenset([5, 21, 22, 23, 24, 55, 70])
    FOLLOW_DEDENT_in_canvas_body726 = frozenset([1])
    FOLLOW_widget_in_stmt737 = frozenset([1])
    FOLLOW_canvas_in_stmt742 = frozenset([1])
    FOLLOW_prop_in_stmt747 = frozenset([1])
    FOLLOW_comment_in_stmt752 = frozenset([1])
    FOLLOW_blank_in_stmt757 = frozenset([1])
    FOLLOW_instruction_in_canvas_stmt768 = frozenset([1])
    FOLLOW_comment_in_canvas_stmt773 = frozenset([1])
    FOLLOW_blank_in_canvas_stmt778 = frozenset([1])
    FOLLOW_WNAME_in_instruction789 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction791 = frozenset([21])
    FOLLOW_NEWLINE_in_instruction794 = frozenset([1])
    FOLLOW_WNAME_in_instruction809 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction811 = frozenset([21, 25])
    FOLLOW_instruction_body_in_instruction814 = frozenset([1])
    FOLLOW_NEWLINE_in_instruction_body837 = frozenset([4, 21])
    FOLLOW_blank_in_instruction_body840 = frozenset([4, 21])
    FOLLOW_INDENT_in_instruction_body843 = frozenset([21, 22, 23, 24, 31, 55, 70])
    FOLLOW_instruction_stmt_in_instruction_body847 = frozenset([5, 21, 22, 23, 24, 31, 55, 70])
    FOLLOW_DEDENT_in_instruction_body851 = frozenset([1])
    FOLLOW_prop_in_instruction_stmt863 = frozenset([1])
    FOLLOW_comment_in_instruction_stmt868 = frozenset([1])
    FOLLOW_blank_in_instruction_stmt873 = frozenset([1])
    FOLLOW_CANVAS_in_canvas884 = frozenset([25])
    FOLLOW_COLON_in_canvas886 = frozenset([21])
    FOLLOW_canvas_body_in_canvas888 = frozenset([1])
    FOLLOW_NAME_in_prop909 = frozenset([25])
    FOLLOW_COLON_in_prop911 = frozenset([21, 32])
    FOLLOW_WS_in_prop913 = frozenset([21, 32])
    FOLLOW_property_body_in_prop918 = frozenset([1])
    FOLLOW_NAME_in_prop933 = frozenset([25])
    FOLLOW_COLON_in_prop935 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_WS_in_prop937 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_prop942 = frozenset([21])
    FOLLOW_NEWLINE_in_prop944 = frozenset([1])
    FOLLOW_NEWLINE_in_property_body964 = frozenset([4, 21])
    FOLLOW_blank_in_property_body967 = frozenset([4, 21])
    FOLLOW_INDENT_in_property_body970 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_property_body973 = frozenset([5, 21])
    FOLLOW_NEWLINE_in_property_body976 = frozenset([24, 28, 29, 31, 32, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 95, 98, 99, 100, 102, 106, 107])
    FOLLOW_prop_value_in_property_body979 = frozenset([5, 21])
    FOLLOW_DEDENT_in_property_body983 = frozenset([1])
    FOLLOW_python_in_prop_value996 = frozenset([1])
    FOLLOW_simple_stmt_in_python1019 = frozenset([1])
    FOLLOW_compound_stmt_in_python1026 = frozenset([1])
    FOLLOW_small_stmt_in_simple_stmt1036 = frozenset([1, 33])
    FOLLOW_SEMI_in_simple_stmt1046 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_small_stmt_in_simple_stmt1048 = frozenset([1, 33])
    FOLLOW_SEMI_in_simple_stmt1053 = frozenset([1])
    FOLLOW_expr_stmt_in_small_stmt1066 = frozenset([1])
    FOLLOW_print_stmt_in_small_stmt1073 = frozenset([1])
    FOLLOW_del_stmt_in_small_stmt1080 = frozenset([1])
    FOLLOW_pass_stmt_in_small_stmt1087 = frozenset([1])
    FOLLOW_flow_stmt_in_small_stmt1094 = frozenset([1])
    FOLLOW_exec_stmt_in_small_stmt1101 = frozenset([1])
    FOLLOW_assert_stmt_in_small_stmt1108 = frozenset([1])
    FOLLOW_defparameter_in_varargslist1118 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1128 = frozenset([24, 31, 37])
    FOLLOW_defparameter_in_varargslist1130 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1135 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_varargslist1139 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1141 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1144 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1146 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1148 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1154 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1156 = frozenset([1])
    FOLLOW_STAR_in_varargslist1167 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1169 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1172 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1174 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1176 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1183 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1185 = frozenset([1])
    FOLLOW_fpdef_in_defparameter1195 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_defparameter1198 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_defparameter1200 = frozenset([1])
    FOLLOW_identifier_in_fpdef1212 = frozenset([1])
    FOLLOW_LPAREN_in_fpdef1217 = frozenset([24, 31, 37])
    FOLLOW_fplist_in_fpdef1219 = frozenset([38])
    FOLLOW_RPAREN_in_fpdef1221 = frozenset([1])
    FOLLOW_fpdef_in_fplist1231 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1241 = frozenset([24, 31, 37])
    FOLLOW_fpdef_in_fplist1243 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1248 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt1261 = frozenset([1, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    FOLLOW_augassign_in_expr_stmt1264 = frozenset([89, 90, 91, 107])
    FOLLOW_yield_expr_in_expr_stmt1266 = frozenset([1])
    FOLLOW_augassign_in_expr_stmt1270 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_expr_stmt1272 = frozenset([1])
    FOLLOW_assigns_in_expr_stmt1276 = frozenset([1])
    FOLLOW_assign_testlist_in_assigns1289 = frozenset([1, 36])
    FOLLOW_assign_yield_in_assigns1294 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_assign_testlist1306 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_assign_testlist1308 = frozenset([1])
    FOLLOW_ASSIGN_in_assign_yield1319 = frozenset([89, 90, 91, 107])
    FOLLOW_yield_expr_in_assign_yield1321 = frozenset([1])
    FOLLOW_set_in_augassign0 = frozenset([1])
    FOLLOW_86_in_print_stmt1391 = frozenset([1, 24, 28, 29, 31, 37, 51, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_printlist_in_print_stmt1394 = frozenset([1])
    FOLLOW_RIGHTSHIFT_in_print_stmt1398 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_printlist_in_print_stmt1400 = frozenset([1])
    FOLLOW_test_in_printlist1418 = frozenset([1, 27])
    FOLLOW_COMMA_in_printlist1429 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_printlist1431 = frozenset([1, 27])
    FOLLOW_COMMA_in_printlist1436 = frozenset([1])
    FOLLOW_87_in_del_stmt1450 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_del_stmt1452 = frozenset([1])
    FOLLOW_88_in_pass_stmt1464 = frozenset([1])
    FOLLOW_break_stmt_in_flow_stmt1476 = frozenset([1])
    FOLLOW_continue_stmt_in_flow_stmt1483 = frozenset([1])
    FOLLOW_raise_stmt_in_flow_stmt1492 = frozenset([1])
    FOLLOW_yield_stmt_in_flow_stmt1499 = frozenset([1])
    FOLLOW_89_in_break_stmt1511 = frozenset([1])
    FOLLOW_90_in_continue_stmt1523 = frozenset([1])
    FOLLOW_yield_expr_in_yield_stmt1533 = frozenset([1])
    FOLLOW_91_in_raise_stmt1543 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1546 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1549 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1551 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1554 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_raise_stmt1556 = frozenset([1])
    FOLLOW_92_in_exec_stmt1574 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_exec_stmt1576 = frozenset([1, 93])
    FOLLOW_93_in_exec_stmt1579 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_exec_stmt1581 = frozenset([1, 27])
    FOLLOW_COMMA_in_exec_stmt1584 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_exec_stmt1586 = frozenset([1])
    FOLLOW_94_in_assert_stmt1602 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_assert_stmt1604 = frozenset([1, 27])
    FOLLOW_COMMA_in_assert_stmt1607 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_assert_stmt1609 = frozenset([1])
    FOLLOW_if_stmt_in_compound_stmt1623 = frozenset([1])
    FOLLOW_while_stmt_in_compound_stmt1630 = frozenset([1])
    FOLLOW_for_stmt_in_compound_stmt1637 = frozenset([1])
    FOLLOW_try_stmt_in_compound_stmt1644 = frozenset([1])
    FOLLOW_with_stmt_in_compound_stmt1651 = frozenset([1])
    FOLLOW_95_in_if_stmt1668 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_if_stmt1670 = frozenset([25])
    FOLLOW_COLON_in_if_stmt1672 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_if_stmt1674 = frozenset([1, 96, 97])
    FOLLOW_elif_clause_in_if_stmt1676 = frozenset([1, 96, 97])
    FOLLOW_96_in_if_stmt1680 = frozenset([25])
    FOLLOW_COLON_in_if_stmt1682 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_if_stmt1684 = frozenset([1])
    FOLLOW_97_in_elif_clause1698 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_elif_clause1700 = frozenset([25])
    FOLLOW_COLON_in_elif_clause1702 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_elif_clause1704 = frozenset([1])
    FOLLOW_98_in_while_stmt1716 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_while_stmt1718 = frozenset([25])
    FOLLOW_COLON_in_while_stmt1720 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_while_stmt1722 = frozenset([1, 96])
    FOLLOW_96_in_while_stmt1725 = frozenset([25])
    FOLLOW_COLON_in_while_stmt1727 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_while_stmt1729 = frozenset([1])
    FOLLOW_99_in_for_stmt1743 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_for_stmt1745 = frozenset([93])
    FOLLOW_93_in_for_stmt1747 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_for_stmt1749 = frozenset([25])
    FOLLOW_COLON_in_for_stmt1751 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_for_stmt1753 = frozenset([1, 96])
    FOLLOW_96_in_for_stmt1756 = frozenset([25])
    FOLLOW_COLON_in_for_stmt1758 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_for_stmt1760 = frozenset([1])
    FOLLOW_100_in_try_stmt1774 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1776 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1778 = frozenset([101, 104])
    FOLLOW_except_clause_in_try_stmt1785 = frozenset([1, 96, 101, 104])
    FOLLOW_96_in_try_stmt1789 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1791 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1793 = frozenset([1, 101])
    FOLLOW_101_in_try_stmt1798 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1800 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1802 = frozenset([1])
    FOLLOW_101_in_try_stmt1811 = frozenset([25])
    FOLLOW_COLON_in_try_stmt1813 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_try_stmt1815 = frozenset([1])
    FOLLOW_102_in_with_stmt1829 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_with_stmt1831 = frozenset([24, 25, 31, 103])
    FOLLOW_with_var_in_with_stmt1834 = frozenset([25])
    FOLLOW_COLON_in_with_stmt1838 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_with_stmt1840 = frozenset([1])
    FOLLOW_103_in_with_var1853 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_identifier_in_with_var1857 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_with_var1860 = frozenset([1])
    FOLLOW_104_in_except_clause1872 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_except_clause1875 = frozenset([25, 27])
    FOLLOW_COMMA_in_except_clause1878 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_except_clause1880 = frozenset([25])
    FOLLOW_COLON_in_except_clause1886 = frozenset([21, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 86, 87, 88, 89, 90, 91, 92, 94, 106, 107])
    FOLLOW_suite_in_except_clause1888 = frozenset([1])
    FOLLOW_simple_stmt_in_suite1900 = frozenset([1])
    FOLLOW_NEWLINE_in_suite1907 = frozenset([4])
    FOLLOW_INDENT_in_suite1909 = frozenset([21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_stmt_in_suite1912 = frozenset([5, 21, 22, 23, 24, 30, 31, 55, 70])
    FOLLOW_DEDENT_in_suite1916 = frozenset([1])
    FOLLOW_or_test_in_test1927 = frozenset([1, 95])
    FOLLOW_95_in_test1945 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_test1947 = frozenset([96])
    FOLLOW_96_in_test1949 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_test1951 = frozenset([1])
    FOLLOW_lambdef_in_test1959 = frozenset([1])
    FOLLOW_and_test_in_or_test1969 = frozenset([1, 52])
    FOLLOW_OR_in_or_test1972 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_and_test_in_or_test1974 = frozenset([1, 52])
    FOLLOW_not_test_in_and_test1986 = frozenset([1, 53])
    FOLLOW_AND_in_and_test1989 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_not_test_in_and_test1991 = frozenset([1, 53])
    FOLLOW_NOT_in_not_test2003 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_not_test_in_not_test2005 = frozenset([1])
    FOLLOW_comparison_in_not_test2010 = frozenset([1])
    FOLLOW_expr_in_comparison2020 = frozenset([1, 54, 55, 56, 57, 58, 59, 60, 61, 93, 105])
    FOLLOW_comp_op_in_comparison2023 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_comparison2025 = frozenset([1, 54, 55, 56, 57, 58, 59, 60, 61, 93, 105])
    FOLLOW_LESS_in_comp_op2037 = frozenset([1])
    FOLLOW_GREATER_in_comp_op2041 = frozenset([1])
    FOLLOW_EQUAL_in_comp_op2045 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comp_op2049 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comp_op2053 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comp_op2057 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comp_op2061 = frozenset([1])
    FOLLOW_93_in_comp_op2066 = frozenset([1])
    FOLLOW_NOT_in_comp_op2070 = frozenset([93])
    FOLLOW_93_in_comp_op2072 = frozenset([1])
    FOLLOW_105_in_comp_op2076 = frozenset([1])
    FOLLOW_NOT_in_comp_op2080 = frozenset([105])
    FOLLOW_105_in_comp_op2082 = frozenset([1])
    FOLLOW_xor_expr_in_expr2092 = frozenset([1, 62])
    FOLLOW_VBAR_in_expr2095 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_xor_expr_in_expr2097 = frozenset([1, 62])
    FOLLOW_and_expr_in_xor_expr2109 = frozenset([1, 63])
    FOLLOW_CIRCUMFLEX_in_xor_expr2112 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_and_expr_in_xor_expr2114 = frozenset([1, 63])
    FOLLOW_shift_expr_in_and_expr2126 = frozenset([1, 64])
    FOLLOW_AMPER_in_and_expr2129 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_shift_expr_in_and_expr2131 = frozenset([1, 64])
    FOLLOW_arith_expr_in_shift_expr2143 = frozenset([1, 51, 65])
    FOLLOW_set_in_shift_expr2146 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_arith_expr_in_shift_expr2152 = frozenset([1, 51, 65])
    FOLLOW_term_in_arith_expr2164 = frozenset([1, 28, 29])
    FOLLOW_set_in_arith_expr2167 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_term_in_arith_expr2173 = frozenset([1, 28, 29])
    FOLLOW_factor_in_term2185 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_set_in_term2188 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_term2205 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_PLUS_in_factor2217 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2219 = frozenset([1])
    FOLLOW_MINUS_in_factor2223 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2225 = frozenset([1])
    FOLLOW_TILDE_in_factor2229 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_factor2231 = frozenset([1])
    FOLLOW_power_in_factor2235 = frozenset([1])
    FOLLOW_atom_in_power2245 = frozenset([1, 35, 37, 70, 81])
    FOLLOW_trailer_in_power2248 = frozenset([1, 35, 37, 70, 81])
    FOLLOW_DOUBLESTAR_in_power2260 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_factor_in_power2262 = frozenset([1])
    FOLLOW_LPAREN_in_atom2274 = frozenset([24, 28, 29, 31, 37, 38, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 89, 90, 91, 106, 107])
    FOLLOW_yield_expr_in_atom2278 = frozenset([38])
    FOLLOW_testlist_gexp_in_atom2282 = frozenset([38])
    FOLLOW_RPAREN_in_atom2287 = frozenset([1])
    FOLLOW_LBRACK_in_atom2292 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_listmaker_in_atom2295 = frozenset([71])
    FOLLOW_RBRACK_in_atom2299 = frozenset([1])
    FOLLOW_LCURLY_in_atom2304 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_dictmaker_in_atom2307 = frozenset([73])
    FOLLOW_RCURLY_in_atom2311 = frozenset([1])
    FOLLOW_BACKQUOTE_in_atom2316 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_atom2318 = frozenset([74])
    FOLLOW_BACKQUOTE_in_atom2320 = frozenset([1])
    FOLLOW_identifier_in_atom2325 = frozenset([1])
    FOLLOW_NONE_in_atom2332 = frozenset([1])
    FOLLOW_INT_in_atom2337 = frozenset([1])
    FOLLOW_LONGINT_in_atom2342 = frozenset([1])
    FOLLOW_FLOAT_in_atom2347 = frozenset([1])
    FOLLOW_COMPLEX_in_atom2352 = frozenset([1])
    FOLLOW_STRING_in_atom2358 = frozenset([1, 80])
    FOLLOW_test_in_listmaker2370 = frozenset([1, 27, 99])
    FOLLOW_list_for_in_listmaker2373 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker2385 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_listmaker2387 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker2394 = frozenset([1])
    FOLLOW_test_in_testlist_gexp2406 = frozenset([1, 27, 99])
    FOLLOW_COMMA_in_testlist_gexp2419 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_testlist_gexp2421 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist_gexp2426 = frozenset([1])
    FOLLOW_gen_for_in_testlist_gexp2432 = frozenset([1])
    FOLLOW_106_in_lambdef2444 = frozenset([24, 25, 31, 34, 35, 37])
    FOLLOW_varargslist_in_lambdef2447 = frozenset([25])
    FOLLOW_COLON_in_lambdef2451 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_lambdef2453 = frozenset([1])
    FOLLOW_LPAREN_in_trailer2463 = frozenset([24, 28, 29, 31, 34, 35, 37, 38, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_arglist_in_trailer2466 = frozenset([38])
    FOLLOW_RPAREN_in_trailer2470 = frozenset([1])
    FOLLOW_LBRACK_in_trailer2475 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 106])
    FOLLOW_subscriptlist_in_trailer2477 = frozenset([71])
    FOLLOW_RBRACK_in_trailer2479 = frozenset([1])
    FOLLOW_DOT_in_trailer2484 = frozenset([24, 31])
    FOLLOW_identifier_in_trailer2486 = frozenset([1])
    FOLLOW_subscript_in_subscriptlist2496 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist2506 = frozenset([24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 106])
    FOLLOW_subscript_in_subscriptlist2508 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist2513 = frozenset([1])
    FOLLOW_DOT_in_subscript2525 = frozenset([81])
    FOLLOW_DOT_in_subscript2527 = frozenset([81])
    FOLLOW_DOT_in_subscript2529 = frozenset([1])
    FOLLOW_test_in_subscript2534 = frozenset([1, 25])
    FOLLOW_COLON_in_subscript2537 = frozenset([1, 24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_subscript2540 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript2545 = frozenset([1])
    FOLLOW_COLON_in_subscript2554 = frozenset([1, 24, 25, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_subscript2557 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript2562 = frozenset([1])
    FOLLOW_COLON_in_sliceop2574 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_sliceop2577 = frozenset([1])
    FOLLOW_expr_in_exprlist2589 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2600 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expr_in_exprlist2602 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2607 = frozenset([1])
    FOLLOW_test_in_testlist2619 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2630 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_testlist2632 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2637 = frozenset([1])
    FOLLOW_test_in_dictmaker2649 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2651 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2653 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2664 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2666 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2668 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_dictmaker2670 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2675 = frozenset([1])
    FOLLOW_argument_in_arglist2687 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2690 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_argument_in_arglist2692 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2698 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_arglist2702 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2704 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2707 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2709 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2711 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2717 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2719 = frozenset([1])
    FOLLOW_STAR_in_arglist2730 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2732 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2735 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2737 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2739 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2746 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_arglist2748 = frozenset([1])
    FOLLOW_test_in_argument2758 = frozenset([27, 36, 99])
    FOLLOW_ASSIGN_in_argument2764 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_argument2766 = frozenset([1])
    FOLLOW_gen_for_in_argument2772 = frozenset([1])
    FOLLOW_list_for_in_list_iter2785 = frozenset([1])
    FOLLOW_list_if_in_list_iter2789 = frozenset([1])
    FOLLOW_99_in_list_for2799 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_list_for2801 = frozenset([93])
    FOLLOW_93_in_list_for2803 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_list_for2805 = frozenset([1, 95, 99])
    FOLLOW_list_iter_in_list_for2808 = frozenset([1])
    FOLLOW_95_in_list_if2820 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_list_if2822 = frozenset([1, 95, 99])
    FOLLOW_list_iter_in_list_if2825 = frozenset([1])
    FOLLOW_gen_for_in_gen_iter2837 = frozenset([1])
    FOLLOW_gen_if_in_gen_iter2841 = frozenset([1])
    FOLLOW_99_in_gen_for2851 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_exprlist_in_gen_for2853 = frozenset([93])
    FOLLOW_93_in_gen_for2855 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_gen_for2857 = frozenset([1, 27, 95, 99])
    FOLLOW_gen_iter_in_gen_for2859 = frozenset([1])
    FOLLOW_95_in_gen_if2870 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_test_in_gen_if2872 = frozenset([1, 27, 95, 99])
    FOLLOW_gen_iter_in_gen_if2874 = frozenset([1])
    FOLLOW_107_in_yield_expr2885 = frozenset([1, 24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 106])
    FOLLOW_testlist_in_yield_expr2887 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_95_in_synpred1_kv1935 = frozenset([24, 28, 29, 31, 37, 54, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_or_test_in_synpred1_kv1937 = frozenset([96])
    FOLLOW_96_in_synpred1_kv1939 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("kvLexer", kvParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
