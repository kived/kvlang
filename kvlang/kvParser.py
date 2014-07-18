# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 kv.g 2014-07-17 19:08:32

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

                 
from kvTree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INSTRUCTION=18
SLASHEQUAL=42
BACKQUOTE=74
STAR=34
CIRCUMFLEXEQUAL=46
GREATEREQUAL=57
WIDGET=9
COMPLEX=78
NOT=53
EOF=-1
CANVAS=30
NOTEQUAL=60
MINUSEQUAL=40
VBAR=61
T__91=91
RPAREN=38
NAME=31
T__92=92
GREATER=55
T__90=90
DOUBLESTAREQUAL=49
LESS=54
TEMPLATERULE=13
COMMENT=7
RBRACK=71
LCURLY=72
INT=75
T__85=85
RIGHTSHIFT=65
T__87=87
T__86=86
T__89=89
T__88=88
DOUBLESLASHEQUAL=50
WS=32
PROPERTY=10
VBAREQUAL=45
OR=51
RESETRULE=19
CLASSRULE=12
LONGINT=76
MULTICLASSRULE=15
PERCENTEQUAL=43
LESSEQUAL=58
DOUBLESLASH=68
LBRACK=70
DOUBLESTAR=35
ESC=83
DIGITS=81
Exponent=82
DEDENT=5
FLOAT=77
WNAME=24
RIGHTSHIFTEQUAL=48
AND=52
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
COMMA=27
AMPER=63
PYTHON=17
EQUAL=56
TILDE=69
LEFTSHIFTEQUAL=47
PLUS=28
LEFTSHIFT=64
DOT=80
PERCENT=67
CLASSLIST=16
HASH=84
MINUS=29
SEMI=33
COLON=25
CANVASRULE=11
NEWLINE=21
AMPEREQUAL=44
RCURLY=73
ASSIGN=36
STAREQUAL=41
CIRCUMFLEX=62
STRING=79
AUTOCLASS=20
ALT_NOTEQUAL=59

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
    "RIGHTSHIFTEQUAL", "DOUBLESTAREQUAL", "DOUBLESLASHEQUAL", "OR", "AND", 
    "NOT", "LESS", "GREATER", "EQUAL", "GREATEREQUAL", "LESSEQUAL", "ALT_NOTEQUAL", 
    "NOTEQUAL", "VBAR", "CIRCUMFLEX", "AMPER", "LEFTSHIFT", "RIGHTSHIFT", 
    "SLASH", "PERCENT", "DOUBLESLASH", "TILDE", "LBRACK", "RBRACK", "LCURLY", 
    "RCURLY", "BACKQUOTE", "INT", "LONGINT", "FLOAT", "COMPLEX", "STRING", 
    "DOT", "DIGITS", "Exponent", "ESC", "HASH", "'raise'", "'if'", "'else'", 
    "'in'", "'is'", "'lambda'", "'for'", "'yield'"
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

        self.dfa57 = self.DFA57(
            self, 57,
            eot = self.DFA57_eot,
            eof = self.DFA57_eof,
            min = self.DFA57_min,
            max = self.DFA57_max,
            accept = self.DFA57_accept,
            special = self.DFA57_special,
            transition = self.DFA57_transition
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

        self.dfa90 = self.DFA90(
            self, 90,
            eot = self.DFA90_eot,
            eof = self.DFA90_eof,
            min = self.DFA90_min,
            max = self.DFA90_max,
            accept = self.DFA90_accept,
            special = self.DFA90_special,
            transition = self.DFA90_transition
            )

        self.dfa92 = self.DFA92(
            self, 92,
            eot = self.DFA92_eot,
            eof = self.DFA92_eof,
            min = self.DFA92_min,
            max = self.DFA92_max,
            accept = self.DFA92_accept,
            special = self.DFA92_special,
            transition = self.DFA92_transition
            )

        self.dfa94 = self.DFA94(
            self, 94,
            eot = self.DFA94_eot,
            eof = self.DFA94_eof,
            min = self.DFA94_min,
            max = self.DFA94_max,
            accept = self.DFA94_accept,
            special = self.DFA94_special,
            transition = self.DFA94_transition
            )



                       	
        self.has_root = False
        def found_root():
        	if self.has_root:
        		raise RuntimeError()
        	self.has_root = True
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
    # kv.g:112:1: kvfile : ( blank | line )* ;
    def kvfile(self, ):

        retval = self.kvfile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        blank1 = None

        line2 = None



        try:
            try:
                # kv.g:113:5: ( ( blank | line )* )
                # kv.g:113:7: ( blank | line )*
                pass 
                root_0 = self._adaptor.nil()

                # kv.g:113:7: ( blank | line )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1
                    elif ((DIRECTIVETEXT <= LA1_0 <= WNAME) or LA1_0 == LESS or LA1_0 == LBRACK) :
                        alt1 = 2


                    if alt1 == 1:
                        # kv.g:113:8: blank
                        pass 
                        self._state.following.append(self.FOLLOW_blank_in_kvfile202)
                        blank1 = self.blank()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blank1.tree)


                    elif alt1 == 2:
                        # kv.g:113:16: line
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
    # kv.g:115:1: blank : NEWLINE -> ^( BLANKLINE ) ;
    def blank(self, ):

        retval = self.blank_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE3 = None

        NEWLINE3_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")

        try:
            try:
                # kv.g:115:7: ( NEWLINE -> ^( BLANKLINE ) )
                # kv.g:115:9: NEWLINE
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
                    # 115:17: -> ^( BLANKLINE )
                    # kv.g:115:20: ^( BLANKLINE )
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
    # kv.g:117:1: line : ( directive | root_rule | class_rule | template_rule | comment );
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
                # kv.g:118:2: ( directive | root_rule | class_rule | template_rule | comment )
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
                    # kv.g:118:4: directive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directive_in_line235)
                    directive4 = self.directive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, directive4.tree)


                elif alt2 == 2:
                    # kv.g:119:4: root_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_root_rule_in_line240)
                    root_rule5 = self.root_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, root_rule5.tree)


                elif alt2 == 3:
                    # kv.g:120:4: class_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_class_rule_in_line245)
                    class_rule6 = self.class_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, class_rule6.tree)


                elif alt2 == 4:
                    # kv.g:121:4: template_rule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_template_rule_in_line250)
                    template_rule7 = self.template_rule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, template_rule7.tree)


                elif alt2 == 5:
                    # kv.g:122:4: comment
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
    # kv.g:124:1: directive : DIRECTIVETEXT NEWLINE -> ^( DIRECTIVE[$DIRECTIVETEXT] ) ;
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
                # kv.g:125:2: ( DIRECTIVETEXT NEWLINE -> ^( DIRECTIVE[$DIRECTIVETEXT] ) )
                # kv.g:125:4: DIRECTIVETEXT NEWLINE
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
                    # 125:26: -> ^( DIRECTIVE[$DIRECTIVETEXT] )
                    # kv.g:125:29: ^( DIRECTIVE[$DIRECTIVETEXT] )
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
    # kv.g:127:1: comment : COMMENTTEXT NEWLINE -> ^( COMMENT[$COMMENTTEXT] ) ;
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
                # kv.g:128:5: ( COMMENTTEXT NEWLINE -> ^( COMMENT[$COMMENTTEXT] ) )
                # kv.g:128:7: COMMENTTEXT NEWLINE
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
                    # 128:27: -> ^( COMMENT[$COMMENTTEXT] )
                    # kv.g:128:30: ^( COMMENT[$COMMENTTEXT] )
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
    # kv.g:130:1: root_rule : widget ;
    def root_rule(self, ):

        retval = self.root_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        widget13 = None



        try:
            try:
                # kv.g:131:2: ( widget )
                # kv.g:131:4: widget
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_widget_in_root_rule312)
                widget13 = self.widget()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, widget13.tree)
                if self._state.backtracking == 0:
                    self.found_root()




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
    # kv.g:133:1: widget : ( WNAME ( COLON )? NEWLINE -> ^( WIDGET[$WNAME] ) | WNAME ( COLON )? widget_body -> ^( WIDGET[$WNAME] widget_body ) );
    def widget(self, ):

        retval = self.widget_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME14 = None
        COLON15 = None
        NEWLINE16 = None
        WNAME17 = None
        COLON18 = None
        widget_body19 = None


        WNAME14_tree = None
        COLON15_tree = None
        NEWLINE16_tree = None
        WNAME17_tree = None
        COLON18_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:134:2: ( WNAME ( COLON )? NEWLINE -> ^( WIDGET[$WNAME] ) | WNAME ( COLON )? widget_body -> ^( WIDGET[$WNAME] widget_body ) )
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
                    # kv.g:134:4: WNAME ( COLON )? NEWLINE
                    pass 
                    WNAME14=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget324) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME14)
                    # kv.g:134:10: ( COLON )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COLON) :
                        alt3 = 1
                    if alt3 == 1:
                        # kv.g:134:10: COLON
                        pass 
                        COLON15=self.match(self.input, COLON, self.FOLLOW_COLON_in_widget326) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON15)



                    NEWLINE16=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_widget329) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE16)

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
                        # 134:25: -> ^( WIDGET[$WNAME] )
                        # kv.g:134:28: ^( WIDGET[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(WidgetNode(WIDGET, WNAME14), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 2:
                    # kv.g:135:4: WNAME ( COLON )? widget_body
                    pass 
                    WNAME17=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget344) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME17)
                    # kv.g:135:10: ( COLON )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COLON) :
                        alt4 = 1
                    if alt4 == 1:
                        # kv.g:135:10: COLON
                        pass 
                        COLON18=self.match(self.input, COLON, self.FOLLOW_COLON_in_widget346) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON18)



                    self._state.following.append(self.FOLLOW_widget_body_in_widget349)
                    widget_body19 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body19.tree)

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
                        # 135:29: -> ^( WIDGET[$WNAME] widget_body )
                        # kv.g:135:32: ^( WIDGET[$WNAME] widget_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(WidgetNode(WIDGET, WNAME17), root_1)

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
    # kv.g:137:1: class_rule : ( '<' a= class_widget '>' ( COLON )? NEWLINE -> ^( CLASSRULE[$a.tree] ) | '<' a= class_widget '>' ( COLON )? widget_body -> ^( CLASSRULE[$a.tree] widget_body ) );
    def class_rule(self, ):

        retval = self.class_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal20 = None
        char_literal21 = None
        COLON22 = None
        NEWLINE23 = None
        char_literal24 = None
        char_literal25 = None
        COLON26 = None
        a = None

        widget_body27 = None


        char_literal20_tree = None
        char_literal21_tree = None
        COLON22_tree = None
        NEWLINE23_tree = None
        char_literal24_tree = None
        char_literal25_tree = None
        COLON26_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_GREATER = RewriteRuleTokenStream(self._adaptor, "token GREATER")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_LESS = RewriteRuleTokenStream(self._adaptor, "token LESS")
        stream_class_widget = RewriteRuleSubtreeStream(self._adaptor, "rule class_widget")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:138:2: ( '<' a= class_widget '>' ( COLON )? NEWLINE -> ^( CLASSRULE[$a.tree] ) | '<' a= class_widget '>' ( COLON )? widget_body -> ^( CLASSRULE[$a.tree] widget_body ) )
                alt8 = 2
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # kv.g:138:4: '<' a= class_widget '>' ( COLON )? NEWLINE
                    pass 
                    char_literal20=self.match(self.input, LESS, self.FOLLOW_LESS_in_class_rule371) 
                    if self._state.backtracking == 0:
                        stream_LESS.add(char_literal20)
                    self._state.following.append(self.FOLLOW_class_widget_in_class_rule375)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal21=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_class_rule377) 
                    if self._state.backtracking == 0:
                        stream_GREATER.add(char_literal21)
                    # kv.g:138:27: ( COLON )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COLON) :
                        alt6 = 1
                    if alt6 == 1:
                        # kv.g:138:27: COLON
                        pass 
                        COLON22=self.match(self.input, COLON, self.FOLLOW_COLON_in_class_rule379) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON22)



                    NEWLINE23=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_class_rule382) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE23)

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
                        # 138:42: -> ^( CLASSRULE[$a.tree] )
                        # kv.g:138:45: ^( CLASSRULE[$a.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassRuleNode(CLASSRULE, a.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt8 == 2:
                    # kv.g:139:4: '<' a= class_widget '>' ( COLON )? widget_body
                    pass 
                    char_literal24=self.match(self.input, LESS, self.FOLLOW_LESS_in_class_rule397) 
                    if self._state.backtracking == 0:
                        stream_LESS.add(char_literal24)
                    self._state.following.append(self.FOLLOW_class_widget_in_class_rule401)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal25=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_class_rule403) 
                    if self._state.backtracking == 0:
                        stream_GREATER.add(char_literal25)
                    # kv.g:139:27: ( COLON )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COLON) :
                        alt7 = 1
                    if alt7 == 1:
                        # kv.g:139:27: COLON
                        pass 
                        COLON26=self.match(self.input, COLON, self.FOLLOW_COLON_in_class_rule405) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON26)



                    self._state.following.append(self.FOLLOW_widget_body_in_class_rule408)
                    widget_body27 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body27.tree)

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
                        # 139:46: -> ^( CLASSRULE[$a.tree] widget_body )
                        # kv.g:139:49: ^( CLASSRULE[$a.tree] widget_body )
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
    # kv.g:141:1: class_widget : widget_comp ;
    def class_widget(self, ):

        retval = self.class_widget_return()
        retval.start = self.input.LT(1)

        root_0 = None

        widget_comp28 = None



        try:
            try:
                # kv.g:142:2: ( widget_comp )
                # kv.g:142:4: widget_comp
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_widget_comp_in_class_widget430)
                widget_comp28 = self.widget_comp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, widget_comp28.tree)



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
    # kv.g:144:1: widget_comp : ( widget_list -> widget_list | a= widget_list AT b= widget_base -> ^( AUTOCLASS[$a.tree,$b.tree] ) );
    def widget_comp(self, ):

        retval = self.widget_comp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AT30 = None
        a = None

        b = None

        widget_list29 = None


        AT30_tree = None
        stream_AT = RewriteRuleTokenStream(self._adaptor, "token AT")
        stream_widget_list = RewriteRuleSubtreeStream(self._adaptor, "rule widget_list")
        stream_widget_base = RewriteRuleSubtreeStream(self._adaptor, "rule widget_base")
        try:
            try:
                # kv.g:145:2: ( widget_list -> widget_list | a= widget_list AT b= widget_base -> ^( AUTOCLASS[$a.tree,$b.tree] ) )
                alt9 = 2
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # kv.g:145:6: widget_list
                    pass 
                    self._state.following.append(self.FOLLOW_widget_list_in_widget_comp442)
                    widget_list29 = self.widget_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_list.add(widget_list29.tree)

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
                        # 145:18: -> widget_list
                        self._adaptor.addChild(root_0, stream_widget_list.nextTree())



                        retval.tree = root_0


                elif alt9 == 2:
                    # kv.g:146:6: a= widget_list AT b= widget_base
                    pass 
                    self._state.following.append(self.FOLLOW_widget_list_in_widget_comp455)
                    a = self.widget_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_list.add(a.tree)
                    AT30=self.match(self.input, AT, self.FOLLOW_AT_in_widget_comp457) 
                    if self._state.backtracking == 0:
                        stream_AT.add(AT30)
                    self._state.following.append(self.FOLLOW_widget_base_in_widget_comp461)
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
                        # 146:37: -> ^( AUTOCLASS[$a.tree,$b.tree] )
                        # kv.g:146:40: ^( AUTOCLASS[$a.tree,$b.tree] )
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
    # kv.g:148:1: widget_list : ( widget_name -> widget_name | widget_name (m= COMMA widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) );
    def widget_list(self, ):

        retval = self.widget_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        m = None
        widget_name31 = None

        widget_name32 = None

        widget_name33 = None


        m_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_widget_name = RewriteRuleSubtreeStream(self._adaptor, "rule widget_name")
        try:
            try:
                # kv.g:149:2: ( widget_name -> widget_name | widget_name (m= COMMA widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == WNAME) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == COMMA) :
                        alt11 = 2
                    elif (LA11_1 == AT or LA11_1 == GREATER or LA11_1 == RBRACK) :
                        alt11 = 1
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
                    # kv.g:149:6: widget_name
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_list483)
                    widget_name31 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name31.tree)

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
                        # 149:18: -> widget_name
                        self._adaptor.addChild(root_0, stream_widget_name.nextTree())



                        retval.tree = root_0


                elif alt11 == 2:
                    # kv.g:150:6: widget_name (m= COMMA widget_name )+
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_list494)
                    widget_name32 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name32.tree)
                    # kv.g:150:18: (m= COMMA widget_name )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == COMMA) :
                            alt10 = 1


                        if alt10 == 1:
                            # kv.g:150:19: m= COMMA widget_name
                            pass 
                            m=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_widget_list499) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(m)
                            self._state.following.append(self.FOLLOW_widget_name_in_widget_list501)
                            widget_name33 = self.widget_name()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_widget_name.add(widget_name33.tree)


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
                        # 150:41: -> ^( CLASSLIST[$m] ( widget_name )* )
                        # kv.g:150:44: ^( CLASSLIST[$m] ( widget_name )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassListNode(CLASSLIST, m), root_1)

                        # kv.g:150:75: ( widget_name )*
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
    # kv.g:152:1: widget_base : ( widget_name -> widget_name | widget_name (m= PLUS widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) );
    def widget_base(self, ):

        retval = self.widget_base_return()
        retval.start = self.input.LT(1)

        root_0 = None

        m = None
        widget_name34 = None

        widget_name35 = None

        widget_name36 = None


        m_tree = None
        stream_PLUS = RewriteRuleTokenStream(self._adaptor, "token PLUS")
        stream_widget_name = RewriteRuleSubtreeStream(self._adaptor, "rule widget_name")
        try:
            try:
                # kv.g:153:2: ( widget_name -> widget_name | widget_name (m= PLUS widget_name )+ -> ^( CLASSLIST[$m] ( widget_name )* ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == WNAME) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == PLUS) :
                        alt13 = 2
                    elif (LA13_1 == GREATER or LA13_1 == RBRACK) :
                        alt13 = 1
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
                    # kv.g:153:6: widget_name
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_base528)
                    widget_name34 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name34.tree)

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
                        # 153:18: -> widget_name
                        self._adaptor.addChild(root_0, stream_widget_name.nextTree())



                        retval.tree = root_0


                elif alt13 == 2:
                    # kv.g:154:6: widget_name (m= PLUS widget_name )+
                    pass 
                    self._state.following.append(self.FOLLOW_widget_name_in_widget_base539)
                    widget_name35 = self.widget_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_name.add(widget_name35.tree)
                    # kv.g:154:18: (m= PLUS widget_name )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == PLUS) :
                            alt12 = 1


                        if alt12 == 1:
                            # kv.g:154:19: m= PLUS widget_name
                            pass 
                            m=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_widget_base544) 
                            if self._state.backtracking == 0:
                                stream_PLUS.add(m)
                            self._state.following.append(self.FOLLOW_widget_name_in_widget_base546)
                            widget_name36 = self.widget_name()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_widget_name.add(widget_name36.tree)


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
                        # 154:40: -> ^( CLASSLIST[$m] ( widget_name )* )
                        # kv.g:154:43: ^( CLASSLIST[$m] ( widget_name )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ClassListNode(CLASSLIST, m), root_1)

                        # kv.g:154:74: ( widget_name )*
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
    # kv.g:156:1: widget_name : ( WNAME -> WNAME | MINUS WNAME -> ^( RESETRULE[$WNAME] ) );
    def widget_name(self, ):

        retval = self.widget_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME37 = None
        MINUS38 = None
        WNAME39 = None

        WNAME37_tree = None
        MINUS38_tree = None
        WNAME39_tree = None
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")

        try:
            try:
                # kv.g:157:2: ( WNAME -> WNAME | MINUS WNAME -> ^( RESETRULE[$WNAME] ) )
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
                    # kv.g:157:6: WNAME
                    pass 
                    WNAME37=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget_name573) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME37)

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
                        # 157:12: -> WNAME
                        self._adaptor.addChild(root_0, stream_WNAME.nextNode())



                        retval.tree = root_0


                elif alt14 == 2:
                    # kv.g:158:6: MINUS WNAME
                    pass 
                    MINUS38=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_widget_name584) 
                    if self._state.backtracking == 0:
                        stream_MINUS.add(MINUS38)
                    WNAME39=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_widget_name586) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME39)

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
                        # 158:18: -> ^( RESETRULE[$WNAME] )
                        # kv.g:158:21: ^( RESETRULE[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(ResetRuleNode(RESETRULE, WNAME39), root_1)

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
    # kv.g:160:1: class_list : WNAME ( PLUS WNAME )* ;
    def class_list(self, ):

        retval = self.class_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME40 = None
        PLUS41 = None
        WNAME42 = None

        WNAME40_tree = None
        PLUS41_tree = None
        WNAME42_tree = None

        try:
            try:
                # kv.g:161:2: ( WNAME ( PLUS WNAME )* )
                # kv.g:161:4: WNAME ( PLUS WNAME )*
                pass 
                root_0 = self._adaptor.nil()

                WNAME40=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_class_list606)
                if self._state.backtracking == 0:

                    WNAME40_tree = self._adaptor.createWithPayload(WNAME40)
                    self._adaptor.addChild(root_0, WNAME40_tree)

                # kv.g:161:10: ( PLUS WNAME )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == PLUS) :
                        alt15 = 1


                    if alt15 == 1:
                        # kv.g:161:11: PLUS WNAME
                        pass 
                        PLUS41=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_class_list609)
                        if self._state.backtracking == 0:

                            PLUS41_tree = self._adaptor.createWithPayload(PLUS41)
                            self._adaptor.addChild(root_0, PLUS41_tree)

                        WNAME42=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_class_list611)
                        if self._state.backtracking == 0:

                            WNAME42_tree = self._adaptor.createWithPayload(WNAME42)
                            self._adaptor.addChild(root_0, WNAME42_tree)



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
    # kv.g:163:1: template_rule : ( '[' a= class_widget ']' ( COLON )? NEWLINE -> ^( TEMPLATERULE[$a.tree] ) | '[' a= class_widget ']' ( COLON )? widget_body -> ^( TEMPLATERULE[$a.tree] widget_body ) );
    def template_rule(self, ):

        retval = self.template_rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal43 = None
        char_literal44 = None
        COLON45 = None
        NEWLINE46 = None
        char_literal47 = None
        char_literal48 = None
        COLON49 = None
        a = None

        widget_body50 = None


        char_literal43_tree = None
        char_literal44_tree = None
        COLON45_tree = None
        NEWLINE46_tree = None
        char_literal47_tree = None
        char_literal48_tree = None
        COLON49_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_class_widget = RewriteRuleSubtreeStream(self._adaptor, "rule class_widget")
        stream_widget_body = RewriteRuleSubtreeStream(self._adaptor, "rule widget_body")
        try:
            try:
                # kv.g:164:2: ( '[' a= class_widget ']' ( COLON )? NEWLINE -> ^( TEMPLATERULE[$a.tree] ) | '[' a= class_widget ']' ( COLON )? widget_body -> ^( TEMPLATERULE[$a.tree] widget_body ) )
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # kv.g:164:4: '[' a= class_widget ']' ( COLON )? NEWLINE
                    pass 
                    char_literal43=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_template_rule623) 
                    if self._state.backtracking == 0:
                        stream_LBRACK.add(char_literal43)
                    self._state.following.append(self.FOLLOW_class_widget_in_template_rule627)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal44=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_template_rule629) 
                    if self._state.backtracking == 0:
                        stream_RBRACK.add(char_literal44)
                    # kv.g:164:27: ( COLON )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == COLON) :
                        alt16 = 1
                    if alt16 == 1:
                        # kv.g:164:27: COLON
                        pass 
                        COLON45=self.match(self.input, COLON, self.FOLLOW_COLON_in_template_rule631) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON45)



                    NEWLINE46=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_template_rule634) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE46)

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
                        # 164:42: -> ^( TEMPLATERULE[$a.tree] )
                        # kv.g:164:45: ^( TEMPLATERULE[$a.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(TemplateRuleNode(TEMPLATERULE, a.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt18 == 2:
                    # kv.g:165:4: '[' a= class_widget ']' ( COLON )? widget_body
                    pass 
                    char_literal47=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_template_rule649) 
                    if self._state.backtracking == 0:
                        stream_LBRACK.add(char_literal47)
                    self._state.following.append(self.FOLLOW_class_widget_in_template_rule653)
                    a = self.class_widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_widget.add(a.tree)
                    char_literal48=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_template_rule655) 
                    if self._state.backtracking == 0:
                        stream_RBRACK.add(char_literal48)
                    # kv.g:165:27: ( COLON )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == COLON) :
                        alt17 = 1
                    if alt17 == 1:
                        # kv.g:165:27: COLON
                        pass 
                        COLON49=self.match(self.input, COLON, self.FOLLOW_COLON_in_template_rule657) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON49)



                    self._state.following.append(self.FOLLOW_widget_body_in_template_rule660)
                    widget_body50 = self.widget_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_widget_body.add(widget_body50.tree)

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
                        # 165:46: -> ^( TEMPLATERULE[$a.tree] widget_body )
                        # kv.g:165:49: ^( TEMPLATERULE[$a.tree] widget_body )
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
    # kv.g:167:1: widget_body : NEWLINE INDENT ( stmt )+ DEDENT ;
    def widget_body(self, ):

        retval = self.widget_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE51 = None
        INDENT52 = None
        DEDENT54 = None
        stmt53 = None


        NEWLINE51_tree = None
        INDENT52_tree = None
        DEDENT54_tree = None

        try:
            try:
                # kv.g:168:5: ( NEWLINE INDENT ( stmt )+ DEDENT )
                # kv.g:168:7: NEWLINE INDENT ( stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE51=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_widget_body685)
                INDENT52=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_widget_body688)
                # kv.g:168:24: ( stmt )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == NEWLINE or (COMMENTTEXT <= LA19_0 <= WNAME) or (CANVAS <= LA19_0 <= NAME)) :
                        alt19 = 1


                    if alt19 == 1:
                        # kv.g:168:25: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_widget_body692)
                        stmt53 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stmt53.tree)


                    else:
                        if cnt19 >= 1:
                            break #loop19

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1
                DEDENT54=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_widget_body696)



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
    # kv.g:170:1: canvas_body : NEWLINE INDENT ( canvas_stmt )+ DEDENT ;
    def canvas_body(self, ):

        retval = self.canvas_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE55 = None
        INDENT56 = None
        DEDENT58 = None
        canvas_stmt57 = None


        NEWLINE55_tree = None
        INDENT56_tree = None
        DEDENT58_tree = None

        try:
            try:
                # kv.g:171:2: ( NEWLINE INDENT ( canvas_stmt )+ DEDENT )
                # kv.g:171:4: NEWLINE INDENT ( canvas_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE55=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_canvas_body707)
                INDENT56=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_canvas_body710)
                # kv.g:171:21: ( canvas_stmt )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == NEWLINE or (COMMENTTEXT <= LA20_0 <= WNAME)) :
                        alt20 = 1


                    if alt20 == 1:
                        # kv.g:171:22: canvas_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_canvas_stmt_in_canvas_body714)
                        canvas_stmt57 = self.canvas_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, canvas_stmt57.tree)


                    else:
                        if cnt20 >= 1:
                            break #loop20

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1
                DEDENT58=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_canvas_body718)



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
    # kv.g:173:1: stmt : ( widget | canvas | prop | comment | blank );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        widget59 = None

        canvas60 = None

        prop61 = None

        comment62 = None

        blank63 = None



        try:
            try:
                # kv.g:174:2: ( widget | canvas | prop | comment | blank )
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
                    # kv.g:174:4: widget
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_widget_in_stmt729)
                    widget59 = self.widget()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, widget59.tree)


                elif alt21 == 2:
                    # kv.g:175:4: canvas
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_canvas_in_stmt734)
                    canvas60 = self.canvas()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, canvas60.tree)


                elif alt21 == 3:
                    # kv.g:176:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_stmt739)
                    prop61 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop61.tree)


                elif alt21 == 4:
                    # kv.g:177:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_stmt744)
                    comment62 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment62.tree)


                elif alt21 == 5:
                    # kv.g:178:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_stmt749)
                    blank63 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank63.tree)


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
    # kv.g:180:1: canvas_stmt : ( instruction | comment | blank );
    def canvas_stmt(self, ):

        retval = self.canvas_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        instruction64 = None

        comment65 = None

        blank66 = None



        try:
            try:
                # kv.g:181:2: ( instruction | comment | blank )
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
                    # kv.g:181:4: instruction
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_instruction_in_canvas_stmt760)
                    instruction64 = self.instruction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, instruction64.tree)


                elif alt22 == 2:
                    # kv.g:182:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_canvas_stmt765)
                    comment65 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment65.tree)


                elif alt22 == 3:
                    # kv.g:183:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_canvas_stmt770)
                    blank66 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank66.tree)


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
    # kv.g:185:1: instruction : ( WNAME ( COLON )? NEWLINE -> ^( INSTRUCTION[$WNAME] ) | WNAME ( COLON )? instruction_body -> ^( INSTRUCTION[$WNAME] instruction_body ) );
    def instruction(self, ):

        retval = self.instruction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WNAME67 = None
        COLON68 = None
        NEWLINE69 = None
        WNAME70 = None
        COLON71 = None
        instruction_body72 = None


        WNAME67_tree = None
        COLON68_tree = None
        NEWLINE69_tree = None
        WNAME70_tree = None
        COLON71_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_WNAME = RewriteRuleTokenStream(self._adaptor, "token WNAME")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_instruction_body = RewriteRuleSubtreeStream(self._adaptor, "rule instruction_body")
        try:
            try:
                # kv.g:186:2: ( WNAME ( COLON )? NEWLINE -> ^( INSTRUCTION[$WNAME] ) | WNAME ( COLON )? instruction_body -> ^( INSTRUCTION[$WNAME] instruction_body ) )
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
                    # kv.g:186:4: WNAME ( COLON )? NEWLINE
                    pass 
                    WNAME67=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction781) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME67)
                    # kv.g:186:10: ( COLON )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == COLON) :
                        alt23 = 1
                    if alt23 == 1:
                        # kv.g:186:10: COLON
                        pass 
                        COLON68=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction783) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON68)



                    NEWLINE69=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction786) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE69)

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
                        # 186:25: -> ^( INSTRUCTION[$WNAME] )
                        # kv.g:186:28: ^( INSTRUCTION[$WNAME] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME67), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt25 == 2:
                    # kv.g:187:4: WNAME ( COLON )? instruction_body
                    pass 
                    WNAME70=self.match(self.input, WNAME, self.FOLLOW_WNAME_in_instruction801) 
                    if self._state.backtracking == 0:
                        stream_WNAME.add(WNAME70)
                    # kv.g:187:10: ( COLON )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COLON) :
                        alt24 = 1
                    if alt24 == 1:
                        # kv.g:187:10: COLON
                        pass 
                        COLON71=self.match(self.input, COLON, self.FOLLOW_COLON_in_instruction803) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON71)



                    self._state.following.append(self.FOLLOW_instruction_body_in_instruction806)
                    instruction_body72 = self.instruction_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_instruction_body.add(instruction_body72.tree)

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
                        # 187:34: -> ^( INSTRUCTION[$WNAME] instruction_body )
                        # kv.g:187:37: ^( INSTRUCTION[$WNAME] instruction_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(InstructionNode(INSTRUCTION, WNAME70), root_1)

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
    # kv.g:189:1: instruction_body : NEWLINE INDENT ( instruction_stmt )+ DEDENT ;
    def instruction_body(self, ):

        retval = self.instruction_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE73 = None
        INDENT74 = None
        DEDENT76 = None
        instruction_stmt75 = None


        NEWLINE73_tree = None
        INDENT74_tree = None
        DEDENT76_tree = None

        try:
            try:
                # kv.g:190:2: ( NEWLINE INDENT ( instruction_stmt )+ DEDENT )
                # kv.g:190:4: NEWLINE INDENT ( instruction_stmt )+ DEDENT
                pass 
                root_0 = self._adaptor.nil()

                NEWLINE73=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instruction_body829)
                INDENT74=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_instruction_body832)
                # kv.g:190:21: ( instruction_stmt )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == NEWLINE or LA26_0 == COMMENTTEXT or LA26_0 == NAME) :
                        alt26 = 1


                    if alt26 == 1:
                        # kv.g:190:22: instruction_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_instruction_stmt_in_instruction_body836)
                        instruction_stmt75 = self.instruction_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instruction_stmt75.tree)


                    else:
                        if cnt26 >= 1:
                            break #loop26

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1
                DEDENT76=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_instruction_body840)



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
    # kv.g:192:1: instruction_stmt : ( prop | comment | blank );
    def instruction_stmt(self, ):

        retval = self.instruction_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prop77 = None

        comment78 = None

        blank79 = None



        try:
            try:
                # kv.g:193:2: ( prop | comment | blank )
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
                    # kv.g:193:4: prop
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prop_in_instruction_stmt852)
                    prop77 = self.prop()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prop77.tree)


                elif alt27 == 2:
                    # kv.g:194:4: comment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comment_in_instruction_stmt857)
                    comment78 = self.comment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comment78.tree)


                elif alt27 == 3:
                    # kv.g:195:4: blank
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blank_in_instruction_stmt862)
                    blank79 = self.blank()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, blank79.tree)


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
    # kv.g:197:1: canvas : CANVAS COLON canvas_body -> ^( CANVASRULE[$CANVAS] canvas_body ) ;
    def canvas(self, ):

        retval = self.canvas_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CANVAS80 = None
        COLON81 = None
        canvas_body82 = None


        CANVAS80_tree = None
        COLON81_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_CANVAS = RewriteRuleTokenStream(self._adaptor, "token CANVAS")
        stream_canvas_body = RewriteRuleSubtreeStream(self._adaptor, "rule canvas_body")
        try:
            try:
                # kv.g:198:2: ( CANVAS COLON canvas_body -> ^( CANVASRULE[$CANVAS] canvas_body ) )
                # kv.g:198:4: CANVAS COLON canvas_body
                pass 
                CANVAS80=self.match(self.input, CANVAS, self.FOLLOW_CANVAS_in_canvas873) 
                if self._state.backtracking == 0:
                    stream_CANVAS.add(CANVAS80)
                COLON81=self.match(self.input, COLON, self.FOLLOW_COLON_in_canvas875) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON81)
                self._state.following.append(self.FOLLOW_canvas_body_in_canvas877)
                canvas_body82 = self.canvas_body()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_canvas_body.add(canvas_body82.tree)

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
                    # 198:29: -> ^( CANVASRULE[$CANVAS] canvas_body )
                    # kv.g:198:32: ^( CANVASRULE[$CANVAS] canvas_body )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(CanvasNode(CANVASRULE, CANVAS80), root_1)

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
    # kv.g:200:1: prop : ( NAME COLON ( WS )* v= prop_value NEWLINE -> ^( PROPERTY[$NAME,$v.tree] ) | NAME COLON ( WS )* NEWLINE INDENT v= prop_value NEWLINE DEDENT -> ^( PROPERTY[$NAME,$v.tree] ) );
    def prop(self, ):

        retval = self.prop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME83 = None
        COLON84 = None
        WS85 = None
        NEWLINE86 = None
        NAME87 = None
        COLON88 = None
        WS89 = None
        NEWLINE90 = None
        INDENT91 = None
        NEWLINE92 = None
        DEDENT93 = None
        v = None


        NAME83_tree = None
        COLON84_tree = None
        WS85_tree = None
        NEWLINE86_tree = None
        NAME87_tree = None
        COLON88_tree = None
        WS89_tree = None
        NEWLINE90_tree = None
        INDENT91_tree = None
        NEWLINE92_tree = None
        DEDENT93_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_prop_value = RewriteRuleSubtreeStream(self._adaptor, "rule prop_value")
        try:
            try:
                # kv.g:201:2: ( NAME COLON ( WS )* v= prop_value NEWLINE -> ^( PROPERTY[$NAME,$v.tree] ) | NAME COLON ( WS )* NEWLINE INDENT v= prop_value NEWLINE DEDENT -> ^( PROPERTY[$NAME,$v.tree] ) )
                alt30 = 2
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # kv.g:201:4: NAME COLON ( WS )* v= prop_value NEWLINE
                    pass 
                    NAME83=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop898) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME83)
                    COLON84=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop900) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON84)
                    # kv.g:201:15: ( WS )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == WS) :
                            alt28 = 1


                        if alt28 == 1:
                            # kv.g:201:15: WS
                            pass 
                            WS85=self.match(self.input, WS, self.FOLLOW_WS_in_prop902) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS85)


                        else:
                            break #loop28
                    self._state.following.append(self.FOLLOW_prop_value_in_prop907)
                    v = self.prop_value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prop_value.add(v.tree)
                    NEWLINE86=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_prop909) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE86)

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
                        # 201:40: -> ^( PROPERTY[$NAME,$v.tree] )
                        # kv.g:201:43: ^( PROPERTY[$NAME,$v.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME83, v.tree), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt30 == 2:
                    # kv.g:202:4: NAME COLON ( WS )* NEWLINE INDENT v= prop_value NEWLINE DEDENT
                    pass 
                    NAME87=self.match(self.input, NAME, self.FOLLOW_NAME_in_prop925) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME87)
                    COLON88=self.match(self.input, COLON, self.FOLLOW_COLON_in_prop927) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON88)
                    # kv.g:202:15: ( WS )*
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == WS) :
                            alt29 = 1


                        if alt29 == 1:
                            # kv.g:202:15: WS
                            pass 
                            WS89=self.match(self.input, WS, self.FOLLOW_WS_in_prop929) 
                            if self._state.backtracking == 0:
                                stream_WS.add(WS89)


                        else:
                            break #loop29
                    NEWLINE90=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_prop932) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE90)
                    INDENT91=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_prop934) 
                    if self._state.backtracking == 0:
                        stream_INDENT.add(INDENT91)
                    self._state.following.append(self.FOLLOW_prop_value_in_prop938)
                    v = self.prop_value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prop_value.add(v.tree)
                    NEWLINE92=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_prop940) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE92)
                    DEDENT93=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_prop942) 
                    if self._state.backtracking == 0:
                        stream_DEDENT.add(DEDENT93)

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
                        # 202:62: -> ^( PROPERTY[$NAME,$v.tree] )
                        # kv.g:202:65: ^( PROPERTY[$NAME,$v.tree] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(PropertyNode(PROPERTY, NAME87, v.tree), root_1)

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

    class prop_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.prop_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "prop_value"
    # kv.g:204:1: prop_value : p= python -> ^( PYTHON[$p.tree] ) ;
    def prop_value(self, ):

        retval = self.prop_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        p = None


        stream_python = RewriteRuleSubtreeStream(self._adaptor, "rule python")
        try:
            try:
                # kv.g:205:2: (p= python -> ^( PYTHON[$p.tree] ) )
                # kv.g:205:4: p= python
                pass 
                self._state.following.append(self.FOLLOW_python_in_prop_value963)
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
                    # 205:13: -> ^( PYTHON[$p.tree] )
                    # kv.g:205:16: ^( PYTHON[$p.tree] )
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
    # kv.g:210:1: python : small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )? ;
    def python(self, ):

        retval = self.python_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI95 = None
        SEMI97 = None
        small_stmt94 = None

        small_stmt96 = None


        SEMI95_tree = None
        SEMI97_tree = None

        try:
            try:
                # kv.g:211:2: ( small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )? )
                # kv.g:211:4: small_stmt ( options {greedy=true; } : SEMI small_stmt )* ( SEMI )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_small_stmt_in_python985)
                small_stmt94 = self.small_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, small_stmt94.tree)
                # kv.g:211:15: ( options {greedy=true; } : SEMI small_stmt )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == SEMI) :
                        LA31_1 = self.input.LA(2)

                        if (LA31_1 == WNAME or (PLUS <= LA31_1 <= MINUS) or LA31_1 == NAME or LA31_1 == LPAREN or LA31_1 == NOT or (TILDE <= LA31_1 <= LBRACK) or LA31_1 == LCURLY or (BACKQUOTE <= LA31_1 <= STRING) or LA31_1 == 85 or LA31_1 == 90 or LA31_1 == 92) :
                            alt31 = 1




                    if alt31 == 1:
                        # kv.g:211:39: SEMI small_stmt
                        pass 
                        SEMI95=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_python995)
                        if self._state.backtracking == 0:

                            SEMI95_tree = self._adaptor.createWithPayload(SEMI95)
                            self._adaptor.addChild(root_0, SEMI95_tree)

                        self._state.following.append(self.FOLLOW_small_stmt_in_python997)
                        small_stmt96 = self.small_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, small_stmt96.tree)


                    else:
                        break #loop31
                # kv.g:211:57: ( SEMI )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == SEMI) :
                    alt32 = 1
                if alt32 == 1:
                    # kv.g:211:58: SEMI
                    pass 
                    SEMI97=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_python1002)
                    if self._state.backtracking == 0:

                        SEMI97_tree = self._adaptor.createWithPayload(SEMI97)
                        self._adaptor.addChild(root_0, SEMI97_tree)







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

    class small_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.small_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "small_stmt"
    # kv.g:213:1: small_stmt : ( expr_stmt | raise_stmt | yield_stmt );
    def small_stmt(self, ):

        retval = self.small_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        expr_stmt98 = None

        raise_stmt99 = None

        yield_stmt100 = None



        try:
            try:
                # kv.g:214:2: ( expr_stmt | raise_stmt | yield_stmt )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 == WNAME or LA33 == PLUS or LA33 == MINUS or LA33 == NAME or LA33 == LPAREN or LA33 == NOT or LA33 == TILDE or LA33 == LBRACK or LA33 == LCURLY or LA33 == BACKQUOTE or LA33 == INT or LA33 == LONGINT or LA33 == FLOAT or LA33 == COMPLEX or LA33 == STRING or LA33 == 90:
                    alt33 = 1
                elif LA33 == 85:
                    alt33 = 2
                elif LA33 == 92:
                    alt33 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # kv.g:214:4: expr_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_stmt_in_small_stmt1015)
                    expr_stmt98 = self.expr_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr_stmt98.tree)


                elif alt33 == 2:
                    # kv.g:215:4: raise_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_raise_stmt_in_small_stmt1020)
                    raise_stmt99 = self.raise_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, raise_stmt99.tree)


                elif alt33 == 3:
                    # kv.g:216:4: yield_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_yield_stmt_in_small_stmt1025)
                    yield_stmt100 = self.yield_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_stmt100.tree)


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
    # kv.g:218:1: varargslist : ( defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )? | STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier );
    def varargslist(self, ):

        retval = self.varargslist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA102 = None
        COMMA104 = None
        STAR105 = None
        COMMA107 = None
        DOUBLESTAR108 = None
        DOUBLESTAR110 = None
        STAR112 = None
        COMMA114 = None
        DOUBLESTAR115 = None
        DOUBLESTAR117 = None
        defparameter101 = None

        defparameter103 = None

        identifier106 = None

        identifier109 = None

        identifier111 = None

        identifier113 = None

        identifier116 = None

        identifier118 = None


        COMMA102_tree = None
        COMMA104_tree = None
        STAR105_tree = None
        COMMA107_tree = None
        DOUBLESTAR108_tree = None
        DOUBLESTAR110_tree = None
        STAR112_tree = None
        COMMA114_tree = None
        DOUBLESTAR115_tree = None
        DOUBLESTAR117_tree = None

        try:
            try:
                # kv.g:219:2: ( defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )? | STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )
                alt39 = 3
                LA39 = self.input.LA(1)
                if LA39 == WNAME or LA39 == NAME or LA39 == LPAREN:
                    alt39 = 1
                elif LA39 == STAR:
                    alt39 = 2
                elif LA39 == DOUBLESTAR:
                    alt39 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # kv.g:219:4: defparameter ( options {greedy=true; } : COMMA defparameter )* ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_defparameter_in_varargslist1035)
                    defparameter101 = self.defparameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, defparameter101.tree)
                    # kv.g:219:17: ( options {greedy=true; } : COMMA defparameter )*
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == COMMA) :
                            LA34_1 = self.input.LA(2)

                            if (LA34_1 == WNAME or LA34_1 == NAME or LA34_1 == LPAREN) :
                                alt34 = 1




                        if alt34 == 1:
                            # kv.g:219:41: COMMA defparameter
                            pass 
                            COMMA102=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1045)
                            if self._state.backtracking == 0:

                                COMMA102_tree = self._adaptor.createWithPayload(COMMA102)
                                self._adaptor.addChild(root_0, COMMA102_tree)

                            self._state.following.append(self.FOLLOW_defparameter_in_varargslist1047)
                            defparameter103 = self.defparameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, defparameter103.tree)


                        else:
                            break #loop34
                    # kv.g:219:62: ( COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )? )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == COMMA) :
                        alt37 = 1
                    if alt37 == 1:
                        # kv.g:219:63: COMMA ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        pass 
                        COMMA104=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1052)
                        if self._state.backtracking == 0:

                            COMMA104_tree = self._adaptor.createWithPayload(COMMA104)
                            self._adaptor.addChild(root_0, COMMA104_tree)

                        # kv.g:219:69: ( STAR identifier ( COMMA DOUBLESTAR identifier )? | DOUBLESTAR identifier )?
                        alt36 = 3
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == STAR) :
                            alt36 = 1
                        elif (LA36_0 == DOUBLESTAR) :
                            alt36 = 2
                        if alt36 == 1:
                            # kv.g:219:71: STAR identifier ( COMMA DOUBLESTAR identifier )?
                            pass 
                            STAR105=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1056)
                            if self._state.backtracking == 0:

                                STAR105_tree = self._adaptor.createWithPayload(STAR105)
                                self._adaptor.addChild(root_0, STAR105_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1058)
                            identifier106 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier106.tree)
                            # kv.g:219:87: ( COMMA DOUBLESTAR identifier )?
                            alt35 = 2
                            LA35_0 = self.input.LA(1)

                            if (LA35_0 == COMMA) :
                                alt35 = 1
                            if alt35 == 1:
                                # kv.g:219:88: COMMA DOUBLESTAR identifier
                                pass 
                                COMMA107=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1061)
                                if self._state.backtracking == 0:

                                    COMMA107_tree = self._adaptor.createWithPayload(COMMA107)
                                    self._adaptor.addChild(root_0, COMMA107_tree)

                                DOUBLESTAR108=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1063)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR108_tree = self._adaptor.createWithPayload(DOUBLESTAR108)
                                    self._adaptor.addChild(root_0, DOUBLESTAR108_tree)

                                self._state.following.append(self.FOLLOW_identifier_in_varargslist1065)
                                identifier109 = self.identifier()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, identifier109.tree)





                        elif alt36 == 2:
                            # kv.g:219:120: DOUBLESTAR identifier
                            pass 
                            DOUBLESTAR110=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1071)
                            if self._state.backtracking == 0:

                                DOUBLESTAR110_tree = self._adaptor.createWithPayload(DOUBLESTAR110)
                                self._adaptor.addChild(root_0, DOUBLESTAR110_tree)

                            self._state.following.append(self.FOLLOW_identifier_in_varargslist1073)
                            identifier111 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier111.tree)








                elif alt39 == 2:
                    # kv.g:220:4: STAR identifier ( COMMA DOUBLESTAR identifier )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR112=self.match(self.input, STAR, self.FOLLOW_STAR_in_varargslist1084)
                    if self._state.backtracking == 0:

                        STAR112_tree = self._adaptor.createWithPayload(STAR112)
                        self._adaptor.addChild(root_0, STAR112_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1086)
                    identifier113 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier113.tree)
                    # kv.g:220:20: ( COMMA DOUBLESTAR identifier )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == COMMA) :
                        alt38 = 1
                    if alt38 == 1:
                        # kv.g:220:21: COMMA DOUBLESTAR identifier
                        pass 
                        COMMA114=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_varargslist1089)
                        if self._state.backtracking == 0:

                            COMMA114_tree = self._adaptor.createWithPayload(COMMA114)
                            self._adaptor.addChild(root_0, COMMA114_tree)

                        DOUBLESTAR115=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1091)
                        if self._state.backtracking == 0:

                            DOUBLESTAR115_tree = self._adaptor.createWithPayload(DOUBLESTAR115)
                            self._adaptor.addChild(root_0, DOUBLESTAR115_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_varargslist1093)
                        identifier116 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier116.tree)





                elif alt39 == 3:
                    # kv.g:221:4: DOUBLESTAR identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR117=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_varargslist1100)
                    if self._state.backtracking == 0:

                        DOUBLESTAR117_tree = self._adaptor.createWithPayload(DOUBLESTAR117)
                        self._adaptor.addChild(root_0, DOUBLESTAR117_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_varargslist1102)
                    identifier118 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier118.tree)


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
    # kv.g:223:1: defparameter : fpdef ( ASSIGN test )? ;
    def defparameter(self, ):

        retval = self.defparameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN120 = None
        fpdef119 = None

        test121 = None


        ASSIGN120_tree = None

        try:
            try:
                # kv.g:224:2: ( fpdef ( ASSIGN test )? )
                # kv.g:224:4: fpdef ( ASSIGN test )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_defparameter1112)
                fpdef119 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef119.tree)
                # kv.g:224:10: ( ASSIGN test )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == ASSIGN) :
                    alt40 = 1
                if alt40 == 1:
                    # kv.g:224:11: ASSIGN test
                    pass 
                    ASSIGN120=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_defparameter1115)
                    if self._state.backtracking == 0:

                        ASSIGN120_tree = self._adaptor.createWithPayload(ASSIGN120)
                        self._adaptor.addChild(root_0, ASSIGN120_tree)

                    self._state.following.append(self.FOLLOW_test_in_defparameter1117)
                    test121 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test121.tree)






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
    # kv.g:226:1: fpdef : ( identifier | LPAREN fplist RPAREN );
    def fpdef(self, ):

        retval = self.fpdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN123 = None
        RPAREN125 = None
        identifier122 = None

        fplist124 = None


        LPAREN123_tree = None
        RPAREN125_tree = None

        try:
            try:
                # kv.g:227:2: ( identifier | LPAREN fplist RPAREN )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == WNAME or LA41_0 == NAME) :
                    alt41 = 1
                elif (LA41_0 == LPAREN) :
                    alt41 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # kv.g:227:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_fpdef1129)
                    identifier122 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier122.tree)


                elif alt41 == 2:
                    # kv.g:228:4: LPAREN fplist RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN123=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_fpdef1134)
                    if self._state.backtracking == 0:

                        LPAREN123_tree = self._adaptor.createWithPayload(LPAREN123)
                        self._adaptor.addChild(root_0, LPAREN123_tree)

                    self._state.following.append(self.FOLLOW_fplist_in_fpdef1136)
                    fplist124 = self.fplist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fplist124.tree)
                    RPAREN125=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_fpdef1138)
                    if self._state.backtracking == 0:

                        RPAREN125_tree = self._adaptor.createWithPayload(RPAREN125)
                        self._adaptor.addChild(root_0, RPAREN125_tree)



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
    # kv.g:230:1: fplist : fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )? ;
    def fplist(self, ):

        retval = self.fplist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA127 = None
        COMMA129 = None
        fpdef126 = None

        fpdef128 = None


        COMMA127_tree = None
        COMMA129_tree = None

        try:
            try:
                # kv.g:231:2: ( fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )? )
                # kv.g:231:4: fpdef ( options {greedy=true; } : COMMA fpdef )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fpdef_in_fplist1148)
                fpdef126 = self.fpdef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fpdef126.tree)
                # kv.g:231:10: ( options {greedy=true; } : COMMA fpdef )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == COMMA) :
                        LA42_1 = self.input.LA(2)

                        if (LA42_1 == WNAME or LA42_1 == NAME or LA42_1 == LPAREN) :
                            alt42 = 1




                    if alt42 == 1:
                        # kv.g:231:34: COMMA fpdef
                        pass 
                        COMMA127=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1158)
                        if self._state.backtracking == 0:

                            COMMA127_tree = self._adaptor.createWithPayload(COMMA127)
                            self._adaptor.addChild(root_0, COMMA127_tree)

                        self._state.following.append(self.FOLLOW_fpdef_in_fplist1160)
                        fpdef128 = self.fpdef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fpdef128.tree)


                    else:
                        break #loop42
                # kv.g:231:48: ( COMMA )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == COMMA) :
                    alt43 = 1
                if alt43 == 1:
                    # kv.g:231:49: COMMA
                    pass 
                    COMMA129=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fplist1165)
                    if self._state.backtracking == 0:

                        COMMA129_tree = self._adaptor.createWithPayload(COMMA129)
                        self._adaptor.addChild(root_0, COMMA129_tree)







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
    # kv.g:233:1: expr_stmt : testlist ( augassign yield_expr | augassign testlist | assigns )? ;
    def expr_stmt(self, ):

        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        testlist130 = None

        augassign131 = None

        yield_expr132 = None

        augassign133 = None

        testlist134 = None

        assigns135 = None



        try:
            try:
                # kv.g:234:2: ( testlist ( augassign yield_expr | augassign testlist | assigns )? )
                # kv.g:234:4: testlist ( augassign yield_expr | augassign testlist | assigns )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1178)
                testlist130 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist130.tree)
                # kv.g:234:13: ( augassign yield_expr | augassign testlist | assigns )?
                alt44 = 4
                LA44_0 = self.input.LA(1)

                if ((PLUSEQUAL <= LA44_0 <= DOUBLESLASHEQUAL)) :
                    LA44_1 = self.input.LA(2)

                    if (LA44_1 == 92) :
                        alt44 = 1
                    elif (LA44_1 == WNAME or (PLUS <= LA44_1 <= MINUS) or LA44_1 == NAME or LA44_1 == LPAREN or LA44_1 == NOT or (TILDE <= LA44_1 <= LBRACK) or LA44_1 == LCURLY or (BACKQUOTE <= LA44_1 <= STRING) or LA44_1 == 90) :
                        alt44 = 2
                elif (LA44_0 == ASSIGN) :
                    alt44 = 3
                if alt44 == 1:
                    # kv.g:234:14: augassign yield_expr
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1181)
                    augassign131 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign131.tree)
                    self._state.following.append(self.FOLLOW_yield_expr_in_expr_stmt1183)
                    yield_expr132 = self.yield_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, yield_expr132.tree)


                elif alt44 == 2:
                    # kv.g:234:37: augassign testlist
                    pass 
                    self._state.following.append(self.FOLLOW_augassign_in_expr_stmt1187)
                    augassign133 = self.augassign()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, augassign133.tree)
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1189)
                    testlist134 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist134.tree)


                elif alt44 == 3:
                    # kv.g:234:58: assigns
                    pass 
                    self._state.following.append(self.FOLLOW_assigns_in_expr_stmt1193)
                    assigns135 = self.assigns()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assigns135.tree)






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
    # kv.g:236:1: assigns : ( ( assign_testlist )+ | ( assign_yield )+ );
    def assigns(self, ):

        retval = self.assigns_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_testlist136 = None

        assign_yield137 = None



        try:
            try:
                # kv.g:237:2: ( ( assign_testlist )+ | ( assign_yield )+ )
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == ASSIGN) :
                    LA47_1 = self.input.LA(2)

                    if (LA47_1 == 92) :
                        alt47 = 2
                    elif (LA47_1 == WNAME or (PLUS <= LA47_1 <= MINUS) or LA47_1 == NAME or LA47_1 == LPAREN or LA47_1 == NOT or (TILDE <= LA47_1 <= LBRACK) or LA47_1 == LCURLY or (BACKQUOTE <= LA47_1 <= STRING) or LA47_1 == 90) :
                        alt47 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 47, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # kv.g:237:4: ( assign_testlist )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:237:4: ( assign_testlist )+
                    cnt45 = 0
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == ASSIGN) :
                            alt45 = 1


                        if alt45 == 1:
                            # kv.g:237:4: assign_testlist
                            pass 
                            self._state.following.append(self.FOLLOW_assign_testlist_in_assigns1206)
                            assign_testlist136 = self.assign_testlist()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_testlist136.tree)


                        else:
                            if cnt45 >= 1:
                                break #loop45

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(45, self.input)
                            raise eee

                        cnt45 += 1


                elif alt47 == 2:
                    # kv.g:237:23: ( assign_yield )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:237:23: ( assign_yield )+
                    cnt46 = 0
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == ASSIGN) :
                            alt46 = 1


                        if alt46 == 1:
                            # kv.g:237:23: assign_yield
                            pass 
                            self._state.following.append(self.FOLLOW_assign_yield_in_assigns1211)
                            assign_yield137 = self.assign_yield()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assign_yield137.tree)


                        else:
                            if cnt46 >= 1:
                                break #loop46

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(46, self.input)
                            raise eee

                        cnt46 += 1


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
    # kv.g:239:1: assign_testlist : ASSIGN testlist ;
    def assign_testlist(self, ):

        retval = self.assign_testlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN138 = None
        testlist139 = None


        ASSIGN138_tree = None

        try:
            try:
                # kv.g:240:2: ( ASSIGN testlist )
                # kv.g:240:4: ASSIGN testlist
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN138=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_testlist1223)
                if self._state.backtracking == 0:

                    ASSIGN138_tree = self._adaptor.createWithPayload(ASSIGN138)
                    self._adaptor.addChild(root_0, ASSIGN138_tree)

                self._state.following.append(self.FOLLOW_testlist_in_assign_testlist1225)
                testlist139 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist139.tree)



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
    # kv.g:242:1: assign_yield : ASSIGN yield_expr ;
    def assign_yield(self, ):

        retval = self.assign_yield_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN140 = None
        yield_expr141 = None


        ASSIGN140_tree = None

        try:
            try:
                # kv.g:243:2: ( ASSIGN yield_expr )
                # kv.g:243:4: ASSIGN yield_expr
                pass 
                root_0 = self._adaptor.nil()

                ASSIGN140=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_yield1236)
                if self._state.backtracking == 0:

                    ASSIGN140_tree = self._adaptor.createWithPayload(ASSIGN140)
                    self._adaptor.addChild(root_0, ASSIGN140_tree)

                self._state.following.append(self.FOLLOW_yield_expr_in_assign_yield1238)
                yield_expr141 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr141.tree)



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
    # kv.g:245:1: augassign : ( PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL );
    def augassign(self, ):

        retval = self.augassign_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set142 = None

        set142_tree = None

        try:
            try:
                # kv.g:246:2: ( PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set142 = self.input.LT(1)
                if (PLUSEQUAL <= self.input.LA(1) <= DOUBLESLASHEQUAL):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set142))
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

    class yield_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.yield_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "yield_stmt"
    # kv.g:250:1: yield_stmt : yield_expr ;
    def yield_stmt(self, ):

        retval = self.yield_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        yield_expr143 = None



        try:
            try:
                # kv.g:251:2: ( yield_expr )
                # kv.g:251:4: yield_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_yield_expr_in_yield_stmt1306)
                yield_expr143 = self.yield_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, yield_expr143.tree)



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
    # kv.g:253:1: raise_stmt : 'raise' ( test ( COMMA test ( COMMA test )? )? )? ;
    def raise_stmt(self, ):

        retval = self.raise_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal144 = None
        COMMA146 = None
        COMMA148 = None
        test145 = None

        test147 = None

        test149 = None


        string_literal144_tree = None
        COMMA146_tree = None
        COMMA148_tree = None

        try:
            try:
                # kv.g:254:2: ( 'raise' ( test ( COMMA test ( COMMA test )? )? )? )
                # kv.g:254:4: 'raise' ( test ( COMMA test ( COMMA test )? )? )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal144=self.match(self.input, 85, self.FOLLOW_85_in_raise_stmt1316)
                if self._state.backtracking == 0:

                    string_literal144_tree = self._adaptor.createWithPayload(string_literal144)
                    self._adaptor.addChild(root_0, string_literal144_tree)

                # kv.g:254:12: ( test ( COMMA test ( COMMA test )? )? )?
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if (LA50_0 == WNAME or (PLUS <= LA50_0 <= MINUS) or LA50_0 == NAME or LA50_0 == LPAREN or LA50_0 == NOT or (TILDE <= LA50_0 <= LBRACK) or LA50_0 == LCURLY or (BACKQUOTE <= LA50_0 <= STRING) or LA50_0 == 90) :
                    alt50 = 1
                if alt50 == 1:
                    # kv.g:254:13: test ( COMMA test ( COMMA test )? )?
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_raise_stmt1319)
                    test145 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test145.tree)
                    # kv.g:254:18: ( COMMA test ( COMMA test )? )?
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == COMMA) :
                        alt49 = 1
                    if alt49 == 1:
                        # kv.g:254:19: COMMA test ( COMMA test )?
                        pass 
                        COMMA146=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1322)
                        if self._state.backtracking == 0:

                            COMMA146_tree = self._adaptor.createWithPayload(COMMA146)
                            self._adaptor.addChild(root_0, COMMA146_tree)

                        self._state.following.append(self.FOLLOW_test_in_raise_stmt1324)
                        test147 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test147.tree)
                        # kv.g:254:30: ( COMMA test )?
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == COMMA) :
                            alt48 = 1
                        if alt48 == 1:
                            # kv.g:254:31: COMMA test
                            pass 
                            COMMA148=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_stmt1327)
                            if self._state.backtracking == 0:

                                COMMA148_tree = self._adaptor.createWithPayload(COMMA148)
                                self._adaptor.addChild(root_0, COMMA148_tree)

                            self._state.following.append(self.FOLLOW_test_in_raise_stmt1329)
                            test149 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test149.tree)












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

    class test_return(ParserRuleReturnScope):
        def __init__(self):
            super(kvParser.test_return, self).__init__()

            self.tree = None




    # $ANTLR start "test"
    # kv.g:257:1: test : ( or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )? | lambdef );
    def test(self, ):

        retval = self.test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal151 = None
        string_literal153 = None
        or_test150 = None

        or_test152 = None

        test154 = None

        lambdef155 = None


        string_literal151_tree = None
        string_literal153_tree = None

        try:
            try:
                # kv.g:258:2: ( or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )? | lambdef )
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == WNAME or (PLUS <= LA52_0 <= MINUS) or LA52_0 == NAME or LA52_0 == LPAREN or LA52_0 == NOT or (TILDE <= LA52_0 <= LBRACK) or LA52_0 == LCURLY or (BACKQUOTE <= LA52_0 <= STRING)) :
                    alt52 = 1
                elif (LA52_0 == 90) :
                    alt52 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # kv.g:258:4: or_test ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_or_test_in_test1346)
                    or_test150 = self.or_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, or_test150.tree)
                    # kv.g:259:3: ( ( 'if' or_test 'else' )=> 'if' or_test 'else' test )?
                    alt51 = 2
                    alt51 = self.dfa51.predict(self.input)
                    if alt51 == 1:
                        # kv.g:259:5: ( 'if' or_test 'else' )=> 'if' or_test 'else' test
                        pass 
                        string_literal151=self.match(self.input, 86, self.FOLLOW_86_in_test1364)
                        if self._state.backtracking == 0:

                            string_literal151_tree = self._adaptor.createWithPayload(string_literal151)
                            self._adaptor.addChild(root_0, string_literal151_tree)

                        self._state.following.append(self.FOLLOW_or_test_in_test1366)
                        or_test152 = self.or_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, or_test152.tree)
                        string_literal153=self.match(self.input, 87, self.FOLLOW_87_in_test1368)
                        if self._state.backtracking == 0:

                            string_literal153_tree = self._adaptor.createWithPayload(string_literal153)
                            self._adaptor.addChild(root_0, string_literal153_tree)

                        self._state.following.append(self.FOLLOW_test_in_test1370)
                        test154 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test154.tree)





                elif alt52 == 2:
                    # kv.g:260:4: lambdef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_lambdef_in_test1378)
                    lambdef155 = self.lambdef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, lambdef155.tree)


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
    # kv.g:262:1: or_test : and_test ( OR and_test )* ;
    def or_test(self, ):

        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR157 = None
        and_test156 = None

        and_test158 = None


        OR157_tree = None

        try:
            try:
                # kv.g:263:2: ( and_test ( OR and_test )* )
                # kv.g:263:4: and_test ( OR and_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_test_in_or_test1388)
                and_test156 = self.and_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_test156.tree)
                # kv.g:263:13: ( OR and_test )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == OR) :
                        alt53 = 1


                    if alt53 == 1:
                        # kv.g:263:14: OR and_test
                        pass 
                        OR157=self.match(self.input, OR, self.FOLLOW_OR_in_or_test1391)
                        if self._state.backtracking == 0:

                            OR157_tree = self._adaptor.createWithPayload(OR157)
                            self._adaptor.addChild(root_0, OR157_tree)

                        self._state.following.append(self.FOLLOW_and_test_in_or_test1393)
                        and_test158 = self.and_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_test158.tree)


                    else:
                        break #loop53



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
    # kv.g:265:1: and_test : not_test ( AND not_test )* ;
    def and_test(self, ):

        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND160 = None
        not_test159 = None

        not_test161 = None


        AND160_tree = None

        try:
            try:
                # kv.g:266:2: ( not_test ( AND not_test )* )
                # kv.g:266:4: not_test ( AND not_test )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_not_test_in_and_test1405)
                not_test159 = self.not_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, not_test159.tree)
                # kv.g:266:13: ( AND not_test )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == AND) :
                        alt54 = 1


                    if alt54 == 1:
                        # kv.g:266:14: AND not_test
                        pass 
                        AND160=self.match(self.input, AND, self.FOLLOW_AND_in_and_test1408)
                        if self._state.backtracking == 0:

                            AND160_tree = self._adaptor.createWithPayload(AND160)
                            self._adaptor.addChild(root_0, AND160_tree)

                        self._state.following.append(self.FOLLOW_not_test_in_and_test1410)
                        not_test161 = self.not_test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, not_test161.tree)


                    else:
                        break #loop54



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
    # kv.g:268:1: not_test : ( NOT not_test | comparison );
    def not_test(self, ):

        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT162 = None
        not_test163 = None

        comparison164 = None


        NOT162_tree = None

        try:
            try:
                # kv.g:269:2: ( NOT not_test | comparison )
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == NOT) :
                    alt55 = 1
                elif (LA55_0 == WNAME or (PLUS <= LA55_0 <= MINUS) or LA55_0 == NAME or LA55_0 == LPAREN or (TILDE <= LA55_0 <= LBRACK) or LA55_0 == LCURLY or (BACKQUOTE <= LA55_0 <= STRING)) :
                    alt55 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # kv.g:269:4: NOT not_test
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT162=self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1422)
                    if self._state.backtracking == 0:

                        NOT162_tree = self._adaptor.createWithPayload(NOT162)
                        self._adaptor.addChild(root_0, NOT162_tree)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1424)
                    not_test163 = self.not_test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, not_test163.tree)


                elif alt55 == 2:
                    # kv.g:270:4: comparison
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comparison_in_not_test1429)
                    comparison164 = self.comparison()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comparison164.tree)


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
    # kv.g:272:1: comparison : expr ( comp_op expr )* ;
    def comparison(self, ):

        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        root_0 = None

        expr165 = None

        comp_op166 = None

        expr167 = None



        try:
            try:
                # kv.g:273:2: ( expr ( comp_op expr )* )
                # kv.g:273:4: expr ( comp_op expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_comparison1439)
                expr165 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr165.tree)
                # kv.g:273:9: ( comp_op expr )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if ((NOT <= LA56_0 <= NOTEQUAL) or (88 <= LA56_0 <= 89)) :
                        alt56 = 1


                    if alt56 == 1:
                        # kv.g:273:10: comp_op expr
                        pass 
                        self._state.following.append(self.FOLLOW_comp_op_in_comparison1442)
                        comp_op166 = self.comp_op()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, comp_op166.tree)
                        self._state.following.append(self.FOLLOW_expr_in_comparison1444)
                        expr167 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr167.tree)


                    else:
                        break #loop56



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
    # kv.g:275:1: comp_op : ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | NOT 'in' | 'is' | NOT 'is' );
    def comp_op(self, ):

        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LESS168 = None
        GREATER169 = None
        EQUAL170 = None
        GREATEREQUAL171 = None
        LESSEQUAL172 = None
        ALT_NOTEQUAL173 = None
        NOTEQUAL174 = None
        string_literal175 = None
        NOT176 = None
        string_literal177 = None
        string_literal178 = None
        NOT179 = None
        string_literal180 = None

        LESS168_tree = None
        GREATER169_tree = None
        EQUAL170_tree = None
        GREATEREQUAL171_tree = None
        LESSEQUAL172_tree = None
        ALT_NOTEQUAL173_tree = None
        NOTEQUAL174_tree = None
        string_literal175_tree = None
        NOT176_tree = None
        string_literal177_tree = None
        string_literal178_tree = None
        NOT179_tree = None
        string_literal180_tree = None

        try:
            try:
                # kv.g:276:2: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | NOT 'in' | 'is' | NOT 'is' )
                alt57 = 11
                alt57 = self.dfa57.predict(self.input)
                if alt57 == 1:
                    # kv.g:276:4: LESS
                    pass 
                    root_0 = self._adaptor.nil()

                    LESS168=self.match(self.input, LESS, self.FOLLOW_LESS_in_comp_op1456)
                    if self._state.backtracking == 0:

                        LESS168_tree = self._adaptor.createWithPayload(LESS168)
                        self._adaptor.addChild(root_0, LESS168_tree)



                elif alt57 == 2:
                    # kv.g:276:11: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER169=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comp_op1460)
                    if self._state.backtracking == 0:

                        GREATER169_tree = self._adaptor.createWithPayload(GREATER169)
                        self._adaptor.addChild(root_0, GREATER169_tree)



                elif alt57 == 3:
                    # kv.g:276:21: EQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    EQUAL170=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comp_op1464)
                    if self._state.backtracking == 0:

                        EQUAL170_tree = self._adaptor.createWithPayload(EQUAL170)
                        self._adaptor.addChild(root_0, EQUAL170_tree)



                elif alt57 == 4:
                    # kv.g:276:29: GREATEREQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATEREQUAL171=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comp_op1468)
                    if self._state.backtracking == 0:

                        GREATEREQUAL171_tree = self._adaptor.createWithPayload(GREATEREQUAL171)
                        self._adaptor.addChild(root_0, GREATEREQUAL171_tree)



                elif alt57 == 5:
                    # kv.g:276:44: LESSEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    LESSEQUAL172=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comp_op1472)
                    if self._state.backtracking == 0:

                        LESSEQUAL172_tree = self._adaptor.createWithPayload(LESSEQUAL172)
                        self._adaptor.addChild(root_0, LESSEQUAL172_tree)



                elif alt57 == 6:
                    # kv.g:276:56: ALT_NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    ALT_NOTEQUAL173=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comp_op1476)
                    if self._state.backtracking == 0:

                        ALT_NOTEQUAL173_tree = self._adaptor.createWithPayload(ALT_NOTEQUAL173)
                        self._adaptor.addChild(root_0, ALT_NOTEQUAL173_tree)



                elif alt57 == 7:
                    # kv.g:276:71: NOTEQUAL
                    pass 
                    root_0 = self._adaptor.nil()

                    NOTEQUAL174=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comp_op1480)
                    if self._state.backtracking == 0:

                        NOTEQUAL174_tree = self._adaptor.createWithPayload(NOTEQUAL174)
                        self._adaptor.addChild(root_0, NOTEQUAL174_tree)



                elif alt57 == 8:
                    # kv.g:277:4: 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal175=self.match(self.input, 88, self.FOLLOW_88_in_comp_op1485)
                    if self._state.backtracking == 0:

                        string_literal175_tree = self._adaptor.createWithPayload(string_literal175)
                        self._adaptor.addChild(root_0, string_literal175_tree)



                elif alt57 == 9:
                    # kv.g:277:11: NOT 'in'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT176=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1489)
                    if self._state.backtracking == 0:

                        NOT176_tree = self._adaptor.createWithPayload(NOT176)
                        self._adaptor.addChild(root_0, NOT176_tree)

                    string_literal177=self.match(self.input, 88, self.FOLLOW_88_in_comp_op1491)
                    if self._state.backtracking == 0:

                        string_literal177_tree = self._adaptor.createWithPayload(string_literal177)
                        self._adaptor.addChild(root_0, string_literal177_tree)



                elif alt57 == 10:
                    # kv.g:277:22: 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal178=self.match(self.input, 89, self.FOLLOW_89_in_comp_op1495)
                    if self._state.backtracking == 0:

                        string_literal178_tree = self._adaptor.createWithPayload(string_literal178)
                        self._adaptor.addChild(root_0, string_literal178_tree)



                elif alt57 == 11:
                    # kv.g:277:29: NOT 'is'
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT179=self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1499)
                    if self._state.backtracking == 0:

                        NOT179_tree = self._adaptor.createWithPayload(NOT179)
                        self._adaptor.addChild(root_0, NOT179_tree)

                    string_literal180=self.match(self.input, 89, self.FOLLOW_89_in_comp_op1501)
                    if self._state.backtracking == 0:

                        string_literal180_tree = self._adaptor.createWithPayload(string_literal180)
                        self._adaptor.addChild(root_0, string_literal180_tree)



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
    # kv.g:279:1: expr : xor_expr ( VBAR xor_expr )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VBAR182 = None
        xor_expr181 = None

        xor_expr183 = None


        VBAR182_tree = None

        try:
            try:
                # kv.g:280:2: ( xor_expr ( VBAR xor_expr )* )
                # kv.g:280:4: xor_expr ( VBAR xor_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_xor_expr_in_expr1511)
                xor_expr181 = self.xor_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, xor_expr181.tree)
                # kv.g:280:13: ( VBAR xor_expr )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == VBAR) :
                        alt58 = 1


                    if alt58 == 1:
                        # kv.g:280:14: VBAR xor_expr
                        pass 
                        VBAR182=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_expr1514)
                        if self._state.backtracking == 0:

                            VBAR182_tree = self._adaptor.createWithPayload(VBAR182)
                            self._adaptor.addChild(root_0, VBAR182_tree)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1516)
                        xor_expr183 = self.xor_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, xor_expr183.tree)


                    else:
                        break #loop58



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
    # kv.g:282:1: xor_expr : and_expr ( CIRCUMFLEX and_expr )* ;
    def xor_expr(self, ):

        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CIRCUMFLEX185 = None
        and_expr184 = None

        and_expr186 = None


        CIRCUMFLEX185_tree = None

        try:
            try:
                # kv.g:283:2: ( and_expr ( CIRCUMFLEX and_expr )* )
                # kv.g:283:4: and_expr ( CIRCUMFLEX and_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1528)
                and_expr184 = self.and_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expr184.tree)
                # kv.g:283:13: ( CIRCUMFLEX and_expr )*
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == CIRCUMFLEX) :
                        alt59 = 1


                    if alt59 == 1:
                        # kv.g:283:14: CIRCUMFLEX and_expr
                        pass 
                        CIRCUMFLEX185=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_xor_expr1531)
                        if self._state.backtracking == 0:

                            CIRCUMFLEX185_tree = self._adaptor.createWithPayload(CIRCUMFLEX185)
                            self._adaptor.addChild(root_0, CIRCUMFLEX185_tree)

                        self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1533)
                        and_expr186 = self.and_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_expr186.tree)


                    else:
                        break #loop59



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
    # kv.g:285:1: and_expr : shift_expr ( AMPER shift_expr )* ;
    def and_expr(self, ):

        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AMPER188 = None
        shift_expr187 = None

        shift_expr189 = None


        AMPER188_tree = None

        try:
            try:
                # kv.g:286:2: ( shift_expr ( AMPER shift_expr )* )
                # kv.g:286:4: shift_expr ( AMPER shift_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1545)
                shift_expr187 = self.shift_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, shift_expr187.tree)
                # kv.g:286:15: ( AMPER shift_expr )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == AMPER) :
                        alt60 = 1


                    if alt60 == 1:
                        # kv.g:286:16: AMPER shift_expr
                        pass 
                        AMPER188=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_and_expr1548)
                        if self._state.backtracking == 0:

                            AMPER188_tree = self._adaptor.createWithPayload(AMPER188)
                            self._adaptor.addChild(root_0, AMPER188_tree)

                        self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1550)
                        shift_expr189 = self.shift_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, shift_expr189.tree)


                    else:
                        break #loop60



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
    # kv.g:288:1: shift_expr : arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )* ;
    def shift_expr(self, ):

        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set191 = None
        arith_expr190 = None

        arith_expr192 = None


        set191_tree = None

        try:
            try:
                # kv.g:289:2: ( arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )* )
                # kv.g:289:4: arith_expr ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1562)
                arith_expr190 = self.arith_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arith_expr190.tree)
                # kv.g:289:15: ( ( LEFTSHIFT | RIGHTSHIFT ) arith_expr )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if ((LEFTSHIFT <= LA61_0 <= RIGHTSHIFT)) :
                        alt61 = 1


                    if alt61 == 1:
                        # kv.g:289:16: ( LEFTSHIFT | RIGHTSHIFT ) arith_expr
                        pass 
                        set191 = self.input.LT(1)
                        if (LEFTSHIFT <= self.input.LA(1) <= RIGHTSHIFT):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set191))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1571)
                        arith_expr192 = self.arith_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arith_expr192.tree)


                    else:
                        break #loop61



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
    # kv.g:291:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(self, ):

        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set194 = None
        term193 = None

        term195 = None


        set194_tree = None

        try:
            try:
                # kv.g:292:2: ( term ( ( PLUS | MINUS ) term )* )
                # kv.g:292:4: term ( ( PLUS | MINUS ) term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_arith_expr1583)
                term193 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term193.tree)
                # kv.g:292:9: ( ( PLUS | MINUS ) term )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if ((PLUS <= LA62_0 <= MINUS)) :
                        alt62 = 1


                    if alt62 == 1:
                        # kv.g:292:10: ( PLUS | MINUS ) term
                        pass 
                        set194 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set194))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_arith_expr1592)
                        term195 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term195.tree)


                    else:
                        break #loop62



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
    # kv.g:294:1: term : factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )* ;
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set197 = None
        factor196 = None

        factor198 = None


        set197_tree = None

        try:
            try:
                # kv.g:295:2: ( factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )* )
                # kv.g:295:4: factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_factor_in_term1604)
                factor196 = self.factor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, factor196.tree)
                # kv.g:295:11: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor )*
                while True: #loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if (LA63_0 == STAR or (SLASH <= LA63_0 <= DOUBLESLASH)) :
                        alt63 = 1


                    if alt63 == 1:
                        # kv.g:295:12: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor
                        pass 
                        set197 = self.input.LT(1)
                        if self.input.LA(1) == STAR or (SLASH <= self.input.LA(1) <= DOUBLESLASH):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set197))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term1624)
                        factor198 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, factor198.tree)


                    else:
                        break #loop63



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
    # kv.g:297:1: factor : ( PLUS factor | MINUS factor | TILDE factor | power );
    def factor(self, ):

        retval = self.factor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS199 = None
        MINUS201 = None
        TILDE203 = None
        factor200 = None

        factor202 = None

        factor204 = None

        power205 = None


        PLUS199_tree = None
        MINUS201_tree = None
        TILDE203_tree = None

        try:
            try:
                # kv.g:298:2: ( PLUS factor | MINUS factor | TILDE factor | power )
                alt64 = 4
                LA64 = self.input.LA(1)
                if LA64 == PLUS:
                    alt64 = 1
                elif LA64 == MINUS:
                    alt64 = 2
                elif LA64 == TILDE:
                    alt64 = 3
                elif LA64 == WNAME or LA64 == NAME or LA64 == LPAREN or LA64 == LBRACK or LA64 == LCURLY or LA64 == BACKQUOTE or LA64 == INT or LA64 == LONGINT or LA64 == FLOAT or LA64 == COMPLEX or LA64 == STRING:
                    alt64 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 64, 0, self.input)

                    raise nvae

                if alt64 == 1:
                    # kv.g:298:4: PLUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS199=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor1636)
                    if self._state.backtracking == 0:

                        PLUS199_tree = self._adaptor.createWithPayload(PLUS199)
                        self._adaptor.addChild(root_0, PLUS199_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor1638)
                    factor200 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor200.tree)


                elif alt64 == 2:
                    # kv.g:298:18: MINUS factor
                    pass 
                    root_0 = self._adaptor.nil()

                    MINUS201=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor1642)
                    if self._state.backtracking == 0:

                        MINUS201_tree = self._adaptor.createWithPayload(MINUS201)
                        self._adaptor.addChild(root_0, MINUS201_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor1644)
                    factor202 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor202.tree)


                elif alt64 == 3:
                    # kv.g:298:33: TILDE factor
                    pass 
                    root_0 = self._adaptor.nil()

                    TILDE203=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor1648)
                    if self._state.backtracking == 0:

                        TILDE203_tree = self._adaptor.createWithPayload(TILDE203)
                        self._adaptor.addChild(root_0, TILDE203_tree)

                    self._state.following.append(self.FOLLOW_factor_in_factor1650)
                    factor204 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor204.tree)


                elif alt64 == 4:
                    # kv.g:298:48: power
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_power_in_factor1654)
                    power205 = self.power()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, power205.tree)


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
    # kv.g:300:1: power : atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? ;
    def power(self, ):

        retval = self.power_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOUBLESTAR208 = None
        atom206 = None

        trailer207 = None

        factor209 = None


        DOUBLESTAR208_tree = None

        try:
            try:
                # kv.g:301:2: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # kv.g:301:4: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_in_power1664)
                atom206 = self.atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, atom206.tree)
                # kv.g:301:9: ( trailer )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == LPAREN or LA65_0 == LBRACK or LA65_0 == DOT) :
                        alt65 = 1


                    if alt65 == 1:
                        # kv.g:301:10: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power1667)
                        trailer207 = self.trailer()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, trailer207.tree)


                    else:
                        break #loop65
                # kv.g:301:20: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == DOUBLESTAR) :
                    alt66 = 1
                if alt66 == 1:
                    # kv.g:301:44: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR208=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power1679)
                    if self._state.backtracking == 0:

                        DOUBLESTAR208_tree = self._adaptor.createWithPayload(DOUBLESTAR208)
                        self._adaptor.addChild(root_0, DOUBLESTAR208_tree)

                    self._state.following.append(self.FOLLOW_factor_in_power1681)
                    factor209 = self.factor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, factor209.tree)






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
    # kv.g:303:1: atom : ( LPAREN ( yield_expr | testlist_gexp )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | BACKQUOTE testlist BACKQUOTE | identifier | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN210 = None
        RPAREN213 = None
        LBRACK214 = None
        RBRACK216 = None
        LCURLY217 = None
        RCURLY219 = None
        BACKQUOTE220 = None
        BACKQUOTE222 = None
        INT224 = None
        LONGINT225 = None
        FLOAT226 = None
        COMPLEX227 = None
        STRING228 = None
        yield_expr211 = None

        testlist_gexp212 = None

        listmaker215 = None

        dictmaker218 = None

        testlist221 = None

        identifier223 = None


        LPAREN210_tree = None
        RPAREN213_tree = None
        LBRACK214_tree = None
        RBRACK216_tree = None
        LCURLY217_tree = None
        RCURLY219_tree = None
        BACKQUOTE220_tree = None
        BACKQUOTE222_tree = None
        INT224_tree = None
        LONGINT225_tree = None
        FLOAT226_tree = None
        COMPLEX227_tree = None
        STRING228_tree = None

        try:
            try:
                # kv.g:304:2: ( LPAREN ( yield_expr | testlist_gexp )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | BACKQUOTE testlist BACKQUOTE | identifier | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
                alt71 = 10
                LA71 = self.input.LA(1)
                if LA71 == LPAREN:
                    alt71 = 1
                elif LA71 == LBRACK:
                    alt71 = 2
                elif LA71 == LCURLY:
                    alt71 = 3
                elif LA71 == BACKQUOTE:
                    alt71 = 4
                elif LA71 == WNAME or LA71 == NAME:
                    alt71 = 5
                elif LA71 == INT:
                    alt71 = 6
                elif LA71 == LONGINT:
                    alt71 = 7
                elif LA71 == FLOAT:
                    alt71 = 8
                elif LA71 == COMPLEX:
                    alt71 = 9
                elif LA71 == STRING:
                    alt71 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae

                if alt71 == 1:
                    # kv.g:304:4: LPAREN ( yield_expr | testlist_gexp )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN210=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1693)
                    if self._state.backtracking == 0:

                        LPAREN210_tree = self._adaptor.createWithPayload(LPAREN210)
                        self._adaptor.addChild(root_0, LPAREN210_tree)

                    # kv.g:304:11: ( yield_expr | testlist_gexp )?
                    alt67 = 3
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == 92) :
                        alt67 = 1
                    elif (LA67_0 == WNAME or (PLUS <= LA67_0 <= MINUS) or LA67_0 == NAME or LA67_0 == LPAREN or LA67_0 == NOT or (TILDE <= LA67_0 <= LBRACK) or LA67_0 == LCURLY or (BACKQUOTE <= LA67_0 <= STRING) or LA67_0 == 90) :
                        alt67 = 2
                    if alt67 == 1:
                        # kv.g:304:13: yield_expr
                        pass 
                        self._state.following.append(self.FOLLOW_yield_expr_in_atom1697)
                        yield_expr211 = self.yield_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, yield_expr211.tree)


                    elif alt67 == 2:
                        # kv.g:304:26: testlist_gexp
                        pass 
                        self._state.following.append(self.FOLLOW_testlist_gexp_in_atom1701)
                        testlist_gexp212 = self.testlist_gexp()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, testlist_gexp212.tree)



                    RPAREN213=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1706)
                    if self._state.backtracking == 0:

                        RPAREN213_tree = self._adaptor.createWithPayload(RPAREN213)
                        self._adaptor.addChild(root_0, RPAREN213_tree)



                elif alt71 == 2:
                    # kv.g:305:4: LBRACK ( listmaker )? RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK214=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1711)
                    if self._state.backtracking == 0:

                        LBRACK214_tree = self._adaptor.createWithPayload(LBRACK214)
                        self._adaptor.addChild(root_0, LBRACK214_tree)

                    # kv.g:305:11: ( listmaker )?
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == WNAME or (PLUS <= LA68_0 <= MINUS) or LA68_0 == NAME or LA68_0 == LPAREN or LA68_0 == NOT or (TILDE <= LA68_0 <= LBRACK) or LA68_0 == LCURLY or (BACKQUOTE <= LA68_0 <= STRING) or LA68_0 == 90) :
                        alt68 = 1
                    if alt68 == 1:
                        # kv.g:305:12: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom1714)
                        listmaker215 = self.listmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, listmaker215.tree)



                    RBRACK216=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1718)
                    if self._state.backtracking == 0:

                        RBRACK216_tree = self._adaptor.createWithPayload(RBRACK216)
                        self._adaptor.addChild(root_0, RBRACK216_tree)



                elif alt71 == 3:
                    # kv.g:306:4: LCURLY ( dictmaker )? RCURLY
                    pass 
                    root_0 = self._adaptor.nil()

                    LCURLY217=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom1723)
                    if self._state.backtracking == 0:

                        LCURLY217_tree = self._adaptor.createWithPayload(LCURLY217)
                        self._adaptor.addChild(root_0, LCURLY217_tree)

                    # kv.g:306:11: ( dictmaker )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == WNAME or (PLUS <= LA69_0 <= MINUS) or LA69_0 == NAME or LA69_0 == LPAREN or LA69_0 == NOT or (TILDE <= LA69_0 <= LBRACK) or LA69_0 == LCURLY or (BACKQUOTE <= LA69_0 <= STRING) or LA69_0 == 90) :
                        alt69 = 1
                    if alt69 == 1:
                        # kv.g:306:12: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom1726)
                        dictmaker218 = self.dictmaker()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, dictmaker218.tree)



                    RCURLY219=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom1730)
                    if self._state.backtracking == 0:

                        RCURLY219_tree = self._adaptor.createWithPayload(RCURLY219)
                        self._adaptor.addChild(root_0, RCURLY219_tree)



                elif alt71 == 4:
                    # kv.g:307:4: BACKQUOTE testlist BACKQUOTE
                    pass 
                    root_0 = self._adaptor.nil()

                    BACKQUOTE220=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom1735)
                    if self._state.backtracking == 0:

                        BACKQUOTE220_tree = self._adaptor.createWithPayload(BACKQUOTE220)
                        self._adaptor.addChild(root_0, BACKQUOTE220_tree)

                    self._state.following.append(self.FOLLOW_testlist_in_atom1737)
                    testlist221 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist221.tree)
                    BACKQUOTE222=self.match(self.input, BACKQUOTE, self.FOLLOW_BACKQUOTE_in_atom1739)
                    if self._state.backtracking == 0:

                        BACKQUOTE222_tree = self._adaptor.createWithPayload(BACKQUOTE222)
                        self._adaptor.addChild(root_0, BACKQUOTE222_tree)



                elif alt71 == 5:
                    # kv.g:308:4: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_atom1744)
                    identifier223 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier223.tree)


                elif alt71 == 6:
                    # kv.g:309:4: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT224=self.match(self.input, INT, self.FOLLOW_INT_in_atom1749)
                    if self._state.backtracking == 0:

                        INT224_tree = self._adaptor.createWithPayload(INT224)
                        self._adaptor.addChild(root_0, INT224_tree)



                elif alt71 == 7:
                    # kv.g:310:4: LONGINT
                    pass 
                    root_0 = self._adaptor.nil()

                    LONGINT225=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom1754)
                    if self._state.backtracking == 0:

                        LONGINT225_tree = self._adaptor.createWithPayload(LONGINT225)
                        self._adaptor.addChild(root_0, LONGINT225_tree)



                elif alt71 == 8:
                    # kv.g:311:4: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()

                    FLOAT226=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom1759)
                    if self._state.backtracking == 0:

                        FLOAT226_tree = self._adaptor.createWithPayload(FLOAT226)
                        self._adaptor.addChild(root_0, FLOAT226_tree)



                elif alt71 == 9:
                    # kv.g:312:4: COMPLEX
                    pass 
                    root_0 = self._adaptor.nil()

                    COMPLEX227=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom1764)
                    if self._state.backtracking == 0:

                        COMPLEX227_tree = self._adaptor.createWithPayload(COMPLEX227)
                        self._adaptor.addChild(root_0, COMPLEX227_tree)



                elif alt71 == 10:
                    # kv.g:313:4: ( STRING )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # kv.g:313:4: ( STRING )+
                    cnt70 = 0
                    while True: #loop70
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if (LA70_0 == STRING) :
                            alt70 = 1


                        if alt70 == 1:
                            # kv.g:313:5: STRING
                            pass 
                            STRING228=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1770)
                            if self._state.backtracking == 0:

                                STRING228_tree = self._adaptor.createWithPayload(STRING228)
                                self._adaptor.addChild(root_0, STRING228_tree)



                        else:
                            if cnt70 >= 1:
                                break #loop70

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(70, self.input)
                            raise eee

                        cnt70 += 1


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
    # kv.g:315:1: listmaker : test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )? ;
    def listmaker(self, ):

        retval = self.listmaker_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA231 = None
        COMMA233 = None
        test229 = None

        list_for230 = None

        test232 = None


        COMMA231_tree = None
        COMMA233_tree = None

        try:
            try:
                # kv.g:316:2: ( test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )? )
                # kv.g:316:4: test ( list_for | ( options {greedy=true; } : COMMA test )* ) ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_listmaker1782)
                test229 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test229.tree)
                # kv.g:316:9: ( list_for | ( options {greedy=true; } : COMMA test )* )
                alt73 = 2
                LA73_0 = self.input.LA(1)

                if (LA73_0 == 91) :
                    alt73 = 1
                elif (LA73_0 == COMMA or LA73_0 == RBRACK) :
                    alt73 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 73, 0, self.input)

                    raise nvae

                if alt73 == 1:
                    # kv.g:316:10: list_for
                    pass 
                    self._state.following.append(self.FOLLOW_list_for_in_listmaker1785)
                    list_for230 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for230.tree)


                elif alt73 == 2:
                    # kv.g:316:21: ( options {greedy=true; } : COMMA test )*
                    pass 
                    # kv.g:316:21: ( options {greedy=true; } : COMMA test )*
                    while True: #loop72
                        alt72 = 2
                        LA72_0 = self.input.LA(1)

                        if (LA72_0 == COMMA) :
                            LA72_1 = self.input.LA(2)

                            if (LA72_1 == WNAME or (PLUS <= LA72_1 <= MINUS) or LA72_1 == NAME or LA72_1 == LPAREN or LA72_1 == NOT or (TILDE <= LA72_1 <= LBRACK) or LA72_1 == LCURLY or (BACKQUOTE <= LA72_1 <= STRING) or LA72_1 == 90) :
                                alt72 = 1




                        if alt72 == 1:
                            # kv.g:316:45: COMMA test
                            pass 
                            COMMA231=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker1797)
                            if self._state.backtracking == 0:

                                COMMA231_tree = self._adaptor.createWithPayload(COMMA231)
                                self._adaptor.addChild(root_0, COMMA231_tree)

                            self._state.following.append(self.FOLLOW_test_in_listmaker1799)
                            test232 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test232.tree)


                        else:
                            break #loop72



                # kv.g:316:60: ( COMMA )?
                alt74 = 2
                LA74_0 = self.input.LA(1)

                if (LA74_0 == COMMA) :
                    alt74 = 1
                if alt74 == 1:
                    # kv.g:316:61: COMMA
                    pass 
                    COMMA233=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker1806)
                    if self._state.backtracking == 0:

                        COMMA233_tree = self._adaptor.createWithPayload(COMMA233)
                        self._adaptor.addChild(root_0, COMMA233_tree)







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
    # kv.g:318:1: testlist_gexp : test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for ) ;
    def testlist_gexp(self, ):

        retval = self.testlist_gexp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA235 = None
        COMMA237 = None
        test234 = None

        test236 = None

        gen_for238 = None


        COMMA235_tree = None
        COMMA237_tree = None

        try:
            try:
                # kv.g:319:2: ( test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for ) )
                # kv.g:319:4: test ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist_gexp1818)
                test234 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test234.tree)
                # kv.g:319:9: ( ( options {k=2; } : COMMA test )* ( COMMA )? | gen_for )
                alt77 = 2
                LA77_0 = self.input.LA(1)

                if (LA77_0 == COMMA or LA77_0 == RPAREN) :
                    alt77 = 1
                elif (LA77_0 == 91) :
                    alt77 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 77, 0, self.input)

                    raise nvae

                if alt77 == 1:
                    # kv.g:319:11: ( options {k=2; } : COMMA test )* ( COMMA )?
                    pass 
                    # kv.g:319:11: ( options {k=2; } : COMMA test )*
                    while True: #loop75
                        alt75 = 2
                        alt75 = self.dfa75.predict(self.input)
                        if alt75 == 1:
                            # kv.g:319:28: COMMA test
                            pass 
                            COMMA235=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp1831)
                            if self._state.backtracking == 0:

                                COMMA235_tree = self._adaptor.createWithPayload(COMMA235)
                                self._adaptor.addChild(root_0, COMMA235_tree)

                            self._state.following.append(self.FOLLOW_test_in_testlist_gexp1833)
                            test236 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test236.tree)


                        else:
                            break #loop75
                    # kv.g:319:41: ( COMMA )?
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == COMMA) :
                        alt76 = 1
                    if alt76 == 1:
                        # kv.g:319:42: COMMA
                        pass 
                        COMMA237=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist_gexp1838)
                        if self._state.backtracking == 0:

                            COMMA237_tree = self._adaptor.createWithPayload(COMMA237)
                            self._adaptor.addChild(root_0, COMMA237_tree)






                elif alt77 == 2:
                    # kv.g:319:52: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_testlist_gexp1844)
                    gen_for238 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for238.tree)






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
    # kv.g:321:1: lambdef : 'lambda' ( varargslist )? COLON test ;
    def lambdef(self, ):

        retval = self.lambdef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal239 = None
        COLON241 = None
        varargslist240 = None

        test242 = None


        string_literal239_tree = None
        COLON241_tree = None

        try:
            try:
                # kv.g:322:2: ( 'lambda' ( varargslist )? COLON test )
                # kv.g:322:4: 'lambda' ( varargslist )? COLON test
                pass 
                root_0 = self._adaptor.nil()

                string_literal239=self.match(self.input, 90, self.FOLLOW_90_in_lambdef1856)
                if self._state.backtracking == 0:

                    string_literal239_tree = self._adaptor.createWithPayload(string_literal239)
                    self._adaptor.addChild(root_0, string_literal239_tree)

                # kv.g:322:13: ( varargslist )?
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if (LA78_0 == WNAME or LA78_0 == NAME or (STAR <= LA78_0 <= DOUBLESTAR) or LA78_0 == LPAREN) :
                    alt78 = 1
                if alt78 == 1:
                    # kv.g:322:14: varargslist
                    pass 
                    self._state.following.append(self.FOLLOW_varargslist_in_lambdef1859)
                    varargslist240 = self.varargslist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, varargslist240.tree)



                COLON241=self.match(self.input, COLON, self.FOLLOW_COLON_in_lambdef1863)
                if self._state.backtracking == 0:

                    COLON241_tree = self._adaptor.createWithPayload(COLON241)
                    self._adaptor.addChild(root_0, COLON241_tree)

                self._state.following.append(self.FOLLOW_test_in_lambdef1865)
                test242 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test242.tree)



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
    # kv.g:324:1: trailer : ( LPAREN ( arglist )? RPAREN | LBRACK subscriptlist RBRACK | DOT identifier );
    def trailer(self, ):

        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN243 = None
        RPAREN245 = None
        LBRACK246 = None
        RBRACK248 = None
        DOT249 = None
        arglist244 = None

        subscriptlist247 = None

        identifier250 = None


        LPAREN243_tree = None
        RPAREN245_tree = None
        LBRACK246_tree = None
        RBRACK248_tree = None
        DOT249_tree = None

        try:
            try:
                # kv.g:325:2: ( LPAREN ( arglist )? RPAREN | LBRACK subscriptlist RBRACK | DOT identifier )
                alt80 = 3
                LA80 = self.input.LA(1)
                if LA80 == LPAREN:
                    alt80 = 1
                elif LA80 == LBRACK:
                    alt80 = 2
                elif LA80 == DOT:
                    alt80 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # kv.g:325:4: LPAREN ( arglist )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN243=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer1875)
                    if self._state.backtracking == 0:

                        LPAREN243_tree = self._adaptor.createWithPayload(LPAREN243)
                        self._adaptor.addChild(root_0, LPAREN243_tree)

                    # kv.g:325:11: ( arglist )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if (LA79_0 == WNAME or (PLUS <= LA79_0 <= MINUS) or LA79_0 == NAME or (STAR <= LA79_0 <= DOUBLESTAR) or LA79_0 == LPAREN or LA79_0 == NOT or (TILDE <= LA79_0 <= LBRACK) or LA79_0 == LCURLY or (BACKQUOTE <= LA79_0 <= STRING) or LA79_0 == 90) :
                        alt79 = 1
                    if alt79 == 1:
                        # kv.g:325:12: arglist
                        pass 
                        self._state.following.append(self.FOLLOW_arglist_in_trailer1878)
                        arglist244 = self.arglist()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arglist244.tree)



                    RPAREN245=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer1882)
                    if self._state.backtracking == 0:

                        RPAREN245_tree = self._adaptor.createWithPayload(RPAREN245)
                        self._adaptor.addChild(root_0, RPAREN245_tree)



                elif alt80 == 2:
                    # kv.g:326:4: LBRACK subscriptlist RBRACK
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK246=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1887)
                    if self._state.backtracking == 0:

                        LBRACK246_tree = self._adaptor.createWithPayload(LBRACK246)
                        self._adaptor.addChild(root_0, LBRACK246_tree)

                    self._state.following.append(self.FOLLOW_subscriptlist_in_trailer1889)
                    subscriptlist247 = self.subscriptlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, subscriptlist247.tree)
                    RBRACK248=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1891)
                    if self._state.backtracking == 0:

                        RBRACK248_tree = self._adaptor.createWithPayload(RBRACK248)
                        self._adaptor.addChild(root_0, RBRACK248_tree)



                elif alt80 == 3:
                    # kv.g:327:4: DOT identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT249=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1896)
                    if self._state.backtracking == 0:

                        DOT249_tree = self._adaptor.createWithPayload(DOT249)
                        self._adaptor.addChild(root_0, DOT249_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_trailer1898)
                    identifier250 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier250.tree)


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
    # kv.g:329:1: subscriptlist : subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )? ;
    def subscriptlist(self, ):

        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA252 = None
        COMMA254 = None
        subscript251 = None

        subscript253 = None


        COMMA252_tree = None
        COMMA254_tree = None

        try:
            try:
                # kv.g:330:2: ( subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )? )
                # kv.g:330:4: subscript ( options {greedy=true; } : COMMA subscript )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_subscript_in_subscriptlist1908)
                subscript251 = self.subscript()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, subscript251.tree)
                # kv.g:330:14: ( options {greedy=true; } : COMMA subscript )*
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == COMMA) :
                        LA81_1 = self.input.LA(2)

                        if ((WNAME <= LA81_1 <= COLON) or (PLUS <= LA81_1 <= MINUS) or LA81_1 == NAME or LA81_1 == LPAREN or LA81_1 == NOT or (TILDE <= LA81_1 <= LBRACK) or LA81_1 == LCURLY or (BACKQUOTE <= LA81_1 <= DOT) or LA81_1 == 90) :
                            alt81 = 1




                    if alt81 == 1:
                        # kv.g:330:38: COMMA subscript
                        pass 
                        COMMA252=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1918)
                        if self._state.backtracking == 0:

                            COMMA252_tree = self._adaptor.createWithPayload(COMMA252)
                            self._adaptor.addChild(root_0, COMMA252_tree)

                        self._state.following.append(self.FOLLOW_subscript_in_subscriptlist1920)
                        subscript253 = self.subscript()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, subscript253.tree)


                    else:
                        break #loop81
                # kv.g:330:56: ( COMMA )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == COMMA) :
                    alt82 = 1
                if alt82 == 1:
                    # kv.g:330:57: COMMA
                    pass 
                    COMMA254=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1925)
                    if self._state.backtracking == 0:

                        COMMA254_tree = self._adaptor.createWithPayload(COMMA254)
                        self._adaptor.addChild(root_0, COMMA254_tree)







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
    # kv.g:332:1: subscript : ( DOT DOT DOT | test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript(self, ):

        retval = self.subscript_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT255 = None
        DOT256 = None
        DOT257 = None
        COLON259 = None
        COLON262 = None
        test258 = None

        test260 = None

        sliceop261 = None

        test263 = None

        sliceop264 = None


        DOT255_tree = None
        DOT256_tree = None
        DOT257_tree = None
        COLON259_tree = None
        COLON262_tree = None

        try:
            try:
                # kv.g:333:2: ( DOT DOT DOT | test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt88 = 3
                LA88 = self.input.LA(1)
                if LA88 == DOT:
                    alt88 = 1
                elif LA88 == WNAME or LA88 == PLUS or LA88 == MINUS or LA88 == NAME or LA88 == LPAREN or LA88 == NOT or LA88 == TILDE or LA88 == LBRACK or LA88 == LCURLY or LA88 == BACKQUOTE or LA88 == INT or LA88 == LONGINT or LA88 == FLOAT or LA88 == COMPLEX or LA88 == STRING or LA88 == 90:
                    alt88 = 2
                elif LA88 == COLON:
                    alt88 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae

                if alt88 == 1:
                    # kv.g:333:4: DOT DOT DOT
                    pass 
                    root_0 = self._adaptor.nil()

                    DOT255=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript1937)
                    if self._state.backtracking == 0:

                        DOT255_tree = self._adaptor.createWithPayload(DOT255)
                        self._adaptor.addChild(root_0, DOT255_tree)

                    DOT256=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript1939)
                    if self._state.backtracking == 0:

                        DOT256_tree = self._adaptor.createWithPayload(DOT256)
                        self._adaptor.addChild(root_0, DOT256_tree)

                    DOT257=self.match(self.input, DOT, self.FOLLOW_DOT_in_subscript1941)
                    if self._state.backtracking == 0:

                        DOT257_tree = self._adaptor.createWithPayload(DOT257)
                        self._adaptor.addChild(root_0, DOT257_tree)



                elif alt88 == 2:
                    # kv.g:334:4: test ( COLON ( test )? ( sliceop )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_test_in_subscript1946)
                    test258 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test258.tree)
                    # kv.g:334:9: ( COLON ( test )? ( sliceop )? )?
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == COLON) :
                        alt85 = 1
                    if alt85 == 1:
                        # kv.g:334:10: COLON ( test )? ( sliceop )?
                        pass 
                        COLON259=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript1949)
                        if self._state.backtracking == 0:

                            COLON259_tree = self._adaptor.createWithPayload(COLON259)
                            self._adaptor.addChild(root_0, COLON259_tree)

                        # kv.g:334:16: ( test )?
                        alt83 = 2
                        LA83_0 = self.input.LA(1)

                        if (LA83_0 == WNAME or (PLUS <= LA83_0 <= MINUS) or LA83_0 == NAME or LA83_0 == LPAREN or LA83_0 == NOT or (TILDE <= LA83_0 <= LBRACK) or LA83_0 == LCURLY or (BACKQUOTE <= LA83_0 <= STRING) or LA83_0 == 90) :
                            alt83 = 1
                        if alt83 == 1:
                            # kv.g:334:17: test
                            pass 
                            self._state.following.append(self.FOLLOW_test_in_subscript1952)
                            test260 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test260.tree)



                        # kv.g:334:24: ( sliceop )?
                        alt84 = 2
                        LA84_0 = self.input.LA(1)

                        if (LA84_0 == COLON) :
                            alt84 = 1
                        if alt84 == 1:
                            # kv.g:334:25: sliceop
                            pass 
                            self._state.following.append(self.FOLLOW_sliceop_in_subscript1957)
                            sliceop261 = self.sliceop()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, sliceop261.tree)








                elif alt88 == 3:
                    # kv.g:335:4: COLON ( test )? ( sliceop )?
                    pass 
                    root_0 = self._adaptor.nil()

                    COLON262=self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript1966)
                    if self._state.backtracking == 0:

                        COLON262_tree = self._adaptor.createWithPayload(COLON262)
                        self._adaptor.addChild(root_0, COLON262_tree)

                    # kv.g:335:10: ( test )?
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == WNAME or (PLUS <= LA86_0 <= MINUS) or LA86_0 == NAME or LA86_0 == LPAREN or LA86_0 == NOT or (TILDE <= LA86_0 <= LBRACK) or LA86_0 == LCURLY or (BACKQUOTE <= LA86_0 <= STRING) or LA86_0 == 90) :
                        alt86 = 1
                    if alt86 == 1:
                        # kv.g:335:11: test
                        pass 
                        self._state.following.append(self.FOLLOW_test_in_subscript1969)
                        test263 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test263.tree)



                    # kv.g:335:18: ( sliceop )?
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == COLON) :
                        alt87 = 1
                    if alt87 == 1:
                        # kv.g:335:19: sliceop
                        pass 
                        self._state.following.append(self.FOLLOW_sliceop_in_subscript1974)
                        sliceop264 = self.sliceop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sliceop264.tree)





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
    # kv.g:337:1: sliceop : COLON ( test )? ;
    def sliceop(self, ):

        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON265 = None
        test266 = None


        COLON265_tree = None

        try:
            try:
                # kv.g:338:2: ( COLON ( test )? )
                # kv.g:338:4: COLON ( test )?
                pass 
                root_0 = self._adaptor.nil()

                COLON265=self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1986)
                if self._state.backtracking == 0:

                    COLON265_tree = self._adaptor.createWithPayload(COLON265)
                    self._adaptor.addChild(root_0, COLON265_tree)

                # kv.g:338:10: ( test )?
                alt89 = 2
                LA89_0 = self.input.LA(1)

                if (LA89_0 == WNAME or (PLUS <= LA89_0 <= MINUS) or LA89_0 == NAME or LA89_0 == LPAREN or LA89_0 == NOT or (TILDE <= LA89_0 <= LBRACK) or LA89_0 == LCURLY or (BACKQUOTE <= LA89_0 <= STRING) or LA89_0 == 90) :
                    alt89 = 1
                if alt89 == 1:
                    # kv.g:338:11: test
                    pass 
                    self._state.following.append(self.FOLLOW_test_in_sliceop1989)
                    test266 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test266.tree)






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
    # kv.g:340:1: exprlist : expr ( options {k=2; } : COMMA expr )* ( COMMA )? ;
    def exprlist(self, ):

        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA268 = None
        COMMA270 = None
        expr267 = None

        expr269 = None


        COMMA268_tree = None
        COMMA270_tree = None

        try:
            try:
                # kv.g:341:2: ( expr ( options {k=2; } : COMMA expr )* ( COMMA )? )
                # kv.g:341:4: expr ( options {k=2; } : COMMA expr )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_exprlist2001)
                expr267 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr267.tree)
                # kv.g:341:9: ( options {k=2; } : COMMA expr )*
                while True: #loop90
                    alt90 = 2
                    alt90 = self.dfa90.predict(self.input)
                    if alt90 == 1:
                        # kv.g:341:26: COMMA expr
                        pass 
                        COMMA268=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2012)
                        if self._state.backtracking == 0:

                            COMMA268_tree = self._adaptor.createWithPayload(COMMA268)
                            self._adaptor.addChild(root_0, COMMA268_tree)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist2014)
                        expr269 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr269.tree)


                    else:
                        break #loop90
                # kv.g:341:39: ( COMMA )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if (LA91_0 == COMMA) :
                    alt91 = 1
                if alt91 == 1:
                    # kv.g:341:40: COMMA
                    pass 
                    COMMA270=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2019)
                    if self._state.backtracking == 0:

                        COMMA270_tree = self._adaptor.createWithPayload(COMMA270)
                        self._adaptor.addChild(root_0, COMMA270_tree)







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
    # kv.g:343:1: testlist : test ( options {k=2; } : COMMA test )* ( COMMA )? ;
    def testlist(self, ):

        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA272 = None
        COMMA274 = None
        test271 = None

        test273 = None


        COMMA272_tree = None
        COMMA274_tree = None

        try:
            try:
                # kv.g:344:2: ( test ( options {k=2; } : COMMA test )* ( COMMA )? )
                # kv.g:344:4: test ( options {k=2; } : COMMA test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_testlist2031)
                test271 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test271.tree)
                # kv.g:344:9: ( options {k=2; } : COMMA test )*
                while True: #loop92
                    alt92 = 2
                    alt92 = self.dfa92.predict(self.input)
                    if alt92 == 1:
                        # kv.g:344:26: COMMA test
                        pass 
                        COMMA272=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2042)
                        if self._state.backtracking == 0:

                            COMMA272_tree = self._adaptor.createWithPayload(COMMA272)
                            self._adaptor.addChild(root_0, COMMA272_tree)

                        self._state.following.append(self.FOLLOW_test_in_testlist2044)
                        test273 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test273.tree)


                    else:
                        break #loop92
                # kv.g:344:39: ( COMMA )?
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if (LA93_0 == COMMA) :
                    alt93 = 1
                if alt93 == 1:
                    # kv.g:344:40: COMMA
                    pass 
                    COMMA274=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2049)
                    if self._state.backtracking == 0:

                        COMMA274_tree = self._adaptor.createWithPayload(COMMA274)
                        self._adaptor.addChild(root_0, COMMA274_tree)







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
    # kv.g:346:1: dictmaker : test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )? ;
    def dictmaker(self, ):

        retval = self.dictmaker_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON276 = None
        COMMA278 = None
        COLON280 = None
        COMMA282 = None
        test275 = None

        test277 = None

        test279 = None

        test281 = None


        COLON276_tree = None
        COMMA278_tree = None
        COLON280_tree = None
        COMMA282_tree = None

        try:
            try:
                # kv.g:347:2: ( test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )? )
                # kv.g:347:4: test COLON test ( options {k=2; } : COMMA test COLON test )* ( COMMA )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_dictmaker2061)
                test275 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test275.tree)
                COLON276=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2063)
                if self._state.backtracking == 0:

                    COLON276_tree = self._adaptor.createWithPayload(COLON276)
                    self._adaptor.addChild(root_0, COLON276_tree)

                self._state.following.append(self.FOLLOW_test_in_dictmaker2065)
                test277 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test277.tree)
                # kv.g:347:20: ( options {k=2; } : COMMA test COLON test )*
                while True: #loop94
                    alt94 = 2
                    alt94 = self.dfa94.predict(self.input)
                    if alt94 == 1:
                        # kv.g:347:37: COMMA test COLON test
                        pass 
                        COMMA278=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2076)
                        if self._state.backtracking == 0:

                            COMMA278_tree = self._adaptor.createWithPayload(COMMA278)
                            self._adaptor.addChild(root_0, COMMA278_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2078)
                        test279 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test279.tree)
                        COLON280=self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2080)
                        if self._state.backtracking == 0:

                            COLON280_tree = self._adaptor.createWithPayload(COLON280)
                            self._adaptor.addChild(root_0, COLON280_tree)

                        self._state.following.append(self.FOLLOW_test_in_dictmaker2082)
                        test281 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test281.tree)


                    else:
                        break #loop94
                # kv.g:347:61: ( COMMA )?
                alt95 = 2
                LA95_0 = self.input.LA(1)

                if (LA95_0 == COMMA) :
                    alt95 = 1
                if alt95 == 1:
                    # kv.g:347:62: COMMA
                    pass 
                    COMMA282=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2087)
                    if self._state.backtracking == 0:

                        COMMA282_tree = self._adaptor.createWithPayload(COMMA282)
                        self._adaptor.addChild(root_0, COMMA282_tree)







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
    # kv.g:349:1: arglist : ( argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )? | STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test );
    def arglist(self, ):

        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA284 = None
        COMMA286 = None
        STAR287 = None
        COMMA289 = None
        DOUBLESTAR290 = None
        DOUBLESTAR292 = None
        STAR294 = None
        COMMA296 = None
        DOUBLESTAR297 = None
        DOUBLESTAR299 = None
        argument283 = None

        argument285 = None

        test288 = None

        test291 = None

        test293 = None

        test295 = None

        test298 = None

        test300 = None


        COMMA284_tree = None
        COMMA286_tree = None
        STAR287_tree = None
        COMMA289_tree = None
        DOUBLESTAR290_tree = None
        DOUBLESTAR292_tree = None
        STAR294_tree = None
        COMMA296_tree = None
        DOUBLESTAR297_tree = None
        DOUBLESTAR299_tree = None

        try:
            try:
                # kv.g:350:2: ( argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )? | STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )
                alt101 = 3
                LA101 = self.input.LA(1)
                if LA101 == WNAME or LA101 == PLUS or LA101 == MINUS or LA101 == NAME or LA101 == LPAREN or LA101 == NOT or LA101 == TILDE or LA101 == LBRACK or LA101 == LCURLY or LA101 == BACKQUOTE or LA101 == INT or LA101 == LONGINT or LA101 == FLOAT or LA101 == COMPLEX or LA101 == STRING or LA101 == 90:
                    alt101 = 1
                elif LA101 == STAR:
                    alt101 = 2
                elif LA101 == DOUBLESTAR:
                    alt101 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 101, 0, self.input)

                    raise nvae

                if alt101 == 1:
                    # kv.g:350:4: argument ( COMMA argument )* ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_argument_in_arglist2099)
                    argument283 = self.argument()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, argument283.tree)
                    # kv.g:350:13: ( COMMA argument )*
                    while True: #loop96
                        alt96 = 2
                        LA96_0 = self.input.LA(1)

                        if (LA96_0 == COMMA) :
                            LA96_1 = self.input.LA(2)

                            if (LA96_1 == WNAME or (PLUS <= LA96_1 <= MINUS) or LA96_1 == NAME or LA96_1 == LPAREN or LA96_1 == NOT or (TILDE <= LA96_1 <= LBRACK) or LA96_1 == LCURLY or (BACKQUOTE <= LA96_1 <= STRING) or LA96_1 == 90) :
                                alt96 = 1




                        if alt96 == 1:
                            # kv.g:350:14: COMMA argument
                            pass 
                            COMMA284=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2102)
                            if self._state.backtracking == 0:

                                COMMA284_tree = self._adaptor.createWithPayload(COMMA284)
                                self._adaptor.addChild(root_0, COMMA284_tree)

                            self._state.following.append(self.FOLLOW_argument_in_arglist2104)
                            argument285 = self.argument()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, argument285.tree)


                        else:
                            break #loop96
                    # kv.g:350:31: ( COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )? )?
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if (LA99_0 == COMMA) :
                        alt99 = 1
                    if alt99 == 1:
                        # kv.g:350:33: COMMA ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        pass 
                        COMMA286=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2110)
                        if self._state.backtracking == 0:

                            COMMA286_tree = self._adaptor.createWithPayload(COMMA286)
                            self._adaptor.addChild(root_0, COMMA286_tree)

                        # kv.g:350:39: ( STAR test ( COMMA DOUBLESTAR test )? | DOUBLESTAR test )?
                        alt98 = 3
                        LA98_0 = self.input.LA(1)

                        if (LA98_0 == STAR) :
                            alt98 = 1
                        elif (LA98_0 == DOUBLESTAR) :
                            alt98 = 2
                        if alt98 == 1:
                            # kv.g:350:41: STAR test ( COMMA DOUBLESTAR test )?
                            pass 
                            STAR287=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2114)
                            if self._state.backtracking == 0:

                                STAR287_tree = self._adaptor.createWithPayload(STAR287)
                                self._adaptor.addChild(root_0, STAR287_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2116)
                            test288 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test288.tree)
                            # kv.g:350:51: ( COMMA DOUBLESTAR test )?
                            alt97 = 2
                            LA97_0 = self.input.LA(1)

                            if (LA97_0 == COMMA) :
                                alt97 = 1
                            if alt97 == 1:
                                # kv.g:350:52: COMMA DOUBLESTAR test
                                pass 
                                COMMA289=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2119)
                                if self._state.backtracking == 0:

                                    COMMA289_tree = self._adaptor.createWithPayload(COMMA289)
                                    self._adaptor.addChild(root_0, COMMA289_tree)

                                DOUBLESTAR290=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2121)
                                if self._state.backtracking == 0:

                                    DOUBLESTAR290_tree = self._adaptor.createWithPayload(DOUBLESTAR290)
                                    self._adaptor.addChild(root_0, DOUBLESTAR290_tree)

                                self._state.following.append(self.FOLLOW_test_in_arglist2123)
                                test291 = self.test()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, test291.tree)





                        elif alt98 == 2:
                            # kv.g:350:78: DOUBLESTAR test
                            pass 
                            DOUBLESTAR292=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2129)
                            if self._state.backtracking == 0:

                                DOUBLESTAR292_tree = self._adaptor.createWithPayload(DOUBLESTAR292)
                                self._adaptor.addChild(root_0, DOUBLESTAR292_tree)

                            self._state.following.append(self.FOLLOW_test_in_arglist2131)
                            test293 = self.test()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, test293.tree)








                elif alt101 == 2:
                    # kv.g:351:4: STAR test ( COMMA DOUBLESTAR test )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR294=self.match(self.input, STAR, self.FOLLOW_STAR_in_arglist2142)
                    if self._state.backtracking == 0:

                        STAR294_tree = self._adaptor.createWithPayload(STAR294)
                        self._adaptor.addChild(root_0, STAR294_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2144)
                    test295 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test295.tree)
                    # kv.g:351:14: ( COMMA DOUBLESTAR test )?
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == COMMA) :
                        alt100 = 1
                    if alt100 == 1:
                        # kv.g:351:15: COMMA DOUBLESTAR test
                        pass 
                        COMMA296=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2147)
                        if self._state.backtracking == 0:

                            COMMA296_tree = self._adaptor.createWithPayload(COMMA296)
                            self._adaptor.addChild(root_0, COMMA296_tree)

                        DOUBLESTAR297=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2149)
                        if self._state.backtracking == 0:

                            DOUBLESTAR297_tree = self._adaptor.createWithPayload(DOUBLESTAR297)
                            self._adaptor.addChild(root_0, DOUBLESTAR297_tree)

                        self._state.following.append(self.FOLLOW_test_in_arglist2151)
                        test298 = self.test()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, test298.tree)





                elif alt101 == 3:
                    # kv.g:352:4: DOUBLESTAR test
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLESTAR299=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_arglist2158)
                    if self._state.backtracking == 0:

                        DOUBLESTAR299_tree = self._adaptor.createWithPayload(DOUBLESTAR299)
                        self._adaptor.addChild(root_0, DOUBLESTAR299_tree)

                    self._state.following.append(self.FOLLOW_test_in_arglist2160)
                    test300 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test300.tree)


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
    # kv.g:354:1: argument : test ( ( ASSIGN test ) | gen_for )? ;
    def argument(self, ):

        retval = self.argument_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSIGN302 = None
        test301 = None

        test303 = None

        gen_for304 = None


        ASSIGN302_tree = None

        try:
            try:
                # kv.g:355:2: ( test ( ( ASSIGN test ) | gen_for )? )
                # kv.g:355:4: test ( ( ASSIGN test ) | gen_for )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_test_in_argument2170)
                test301 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test301.tree)
                # kv.g:355:9: ( ( ASSIGN test ) | gen_for )?
                alt102 = 3
                LA102_0 = self.input.LA(1)

                if (LA102_0 == ASSIGN) :
                    alt102 = 1
                elif (LA102_0 == 91) :
                    alt102 = 2
                if alt102 == 1:
                    # kv.g:355:11: ( ASSIGN test )
                    pass 
                    # kv.g:355:11: ( ASSIGN test )
                    # kv.g:355:13: ASSIGN test
                    pass 
                    ASSIGN302=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument2176)
                    if self._state.backtracking == 0:

                        ASSIGN302_tree = self._adaptor.createWithPayload(ASSIGN302)
                        self._adaptor.addChild(root_0, ASSIGN302_tree)

                    self._state.following.append(self.FOLLOW_test_in_argument2178)
                    test303 = self.test()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, test303.tree)





                elif alt102 == 2:
                    # kv.g:355:29: gen_for
                    pass 
                    self._state.following.append(self.FOLLOW_gen_for_in_argument2184)
                    gen_for304 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for304.tree)






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
    # kv.g:357:1: list_iter : ( list_for | list_if );
    def list_iter(self, ):

        retval = self.list_iter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        list_for305 = None

        list_if306 = None



        try:
            try:
                # kv.g:358:2: ( list_for | list_if )
                alt103 = 2
                LA103_0 = self.input.LA(1)

                if (LA103_0 == 91) :
                    alt103 = 1
                elif (LA103_0 == 86) :
                    alt103 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 103, 0, self.input)

                    raise nvae

                if alt103 == 1:
                    # kv.g:358:4: list_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_for_in_list_iter2197)
                    list_for305 = self.list_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_for305.tree)


                elif alt103 == 2:
                    # kv.g:358:15: list_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_if_in_list_iter2201)
                    list_if306 = self.list_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_if306.tree)


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
    # kv.g:360:1: list_for : 'for' exprlist 'in' testlist ( list_iter )? ;
    def list_for(self, ):

        retval = self.list_for_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal307 = None
        string_literal309 = None
        exprlist308 = None

        testlist310 = None

        list_iter311 = None


        string_literal307_tree = None
        string_literal309_tree = None

        try:
            try:
                # kv.g:361:2: ( 'for' exprlist 'in' testlist ( list_iter )? )
                # kv.g:361:4: 'for' exprlist 'in' testlist ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal307=self.match(self.input, 91, self.FOLLOW_91_in_list_for2211)
                if self._state.backtracking == 0:

                    string_literal307_tree = self._adaptor.createWithPayload(string_literal307)
                    self._adaptor.addChild(root_0, string_literal307_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_list_for2213)
                exprlist308 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist308.tree)
                string_literal309=self.match(self.input, 88, self.FOLLOW_88_in_list_for2215)
                if self._state.backtracking == 0:

                    string_literal309_tree = self._adaptor.createWithPayload(string_literal309)
                    self._adaptor.addChild(root_0, string_literal309_tree)

                self._state.following.append(self.FOLLOW_testlist_in_list_for2217)
                testlist310 = self.testlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, testlist310.tree)
                # kv.g:361:33: ( list_iter )?
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if (LA104_0 == 86 or LA104_0 == 91) :
                    alt104 = 1
                if alt104 == 1:
                    # kv.g:361:34: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_for2220)
                    list_iter311 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter311.tree)






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
    # kv.g:363:1: list_if : 'if' test ( list_iter )? ;
    def list_if(self, ):

        retval = self.list_if_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal312 = None
        test313 = None

        list_iter314 = None


        string_literal312_tree = None

        try:
            try:
                # kv.g:364:2: ( 'if' test ( list_iter )? )
                # kv.g:364:4: 'if' test ( list_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal312=self.match(self.input, 86, self.FOLLOW_86_in_list_if2232)
                if self._state.backtracking == 0:

                    string_literal312_tree = self._adaptor.createWithPayload(string_literal312)
                    self._adaptor.addChild(root_0, string_literal312_tree)

                self._state.following.append(self.FOLLOW_test_in_list_if2234)
                test313 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test313.tree)
                # kv.g:364:14: ( list_iter )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == 86 or LA105_0 == 91) :
                    alt105 = 1
                if alt105 == 1:
                    # kv.g:364:15: list_iter
                    pass 
                    self._state.following.append(self.FOLLOW_list_iter_in_list_if2237)
                    list_iter314 = self.list_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_iter314.tree)






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
    # kv.g:366:1: gen_iter : ( gen_for | gen_if );
    def gen_iter(self, ):

        retval = self.gen_iter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        gen_for315 = None

        gen_if316 = None



        try:
            try:
                # kv.g:367:2: ( gen_for | gen_if )
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == 91) :
                    alt106 = 1
                elif (LA106_0 == 86) :
                    alt106 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 106, 0, self.input)

                    raise nvae

                if alt106 == 1:
                    # kv.g:367:4: gen_for
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_for_in_gen_iter2249)
                    gen_for315 = self.gen_for()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_for315.tree)


                elif alt106 == 2:
                    # kv.g:367:14: gen_if
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_gen_if_in_gen_iter2253)
                    gen_if316 = self.gen_if()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_if316.tree)


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
    # kv.g:369:1: gen_for : 'for' exprlist 'in' or_test ( gen_iter )? ;
    def gen_for(self, ):

        retval = self.gen_for_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal317 = None
        string_literal319 = None
        exprlist318 = None

        or_test320 = None

        gen_iter321 = None


        string_literal317_tree = None
        string_literal319_tree = None

        try:
            try:
                # kv.g:370:2: ( 'for' exprlist 'in' or_test ( gen_iter )? )
                # kv.g:370:4: 'for' exprlist 'in' or_test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal317=self.match(self.input, 91, self.FOLLOW_91_in_gen_for2263)
                if self._state.backtracking == 0:

                    string_literal317_tree = self._adaptor.createWithPayload(string_literal317)
                    self._adaptor.addChild(root_0, string_literal317_tree)

                self._state.following.append(self.FOLLOW_exprlist_in_gen_for2265)
                exprlist318 = self.exprlist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exprlist318.tree)
                string_literal319=self.match(self.input, 88, self.FOLLOW_88_in_gen_for2267)
                if self._state.backtracking == 0:

                    string_literal319_tree = self._adaptor.createWithPayload(string_literal319)
                    self._adaptor.addChild(root_0, string_literal319_tree)

                self._state.following.append(self.FOLLOW_or_test_in_gen_for2269)
                or_test320 = self.or_test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_test320.tree)
                # kv.g:370:32: ( gen_iter )?
                alt107 = 2
                LA107_0 = self.input.LA(1)

                if (LA107_0 == 86 or LA107_0 == 91) :
                    alt107 = 1
                if alt107 == 1:
                    # kv.g:370:32: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_for2271)
                    gen_iter321 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter321.tree)






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
    # kv.g:372:1: gen_if : 'if' test ( gen_iter )? ;
    def gen_if(self, ):

        retval = self.gen_if_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal322 = None
        test323 = None

        gen_iter324 = None


        string_literal322_tree = None

        try:
            try:
                # kv.g:373:2: ( 'if' test ( gen_iter )? )
                # kv.g:373:4: 'if' test ( gen_iter )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal322=self.match(self.input, 86, self.FOLLOW_86_in_gen_if2282)
                if self._state.backtracking == 0:

                    string_literal322_tree = self._adaptor.createWithPayload(string_literal322)
                    self._adaptor.addChild(root_0, string_literal322_tree)

                self._state.following.append(self.FOLLOW_test_in_gen_if2284)
                test323 = self.test()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, test323.tree)
                # kv.g:373:14: ( gen_iter )?
                alt108 = 2
                LA108_0 = self.input.LA(1)

                if (LA108_0 == 86 or LA108_0 == 91) :
                    alt108 = 1
                if alt108 == 1:
                    # kv.g:373:14: gen_iter
                    pass 
                    self._state.following.append(self.FOLLOW_gen_iter_in_gen_if2286)
                    gen_iter324 = self.gen_iter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, gen_iter324.tree)






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
    # kv.g:375:1: yield_expr : 'yield' ( testlist )? ;
    def yield_expr(self, ):

        retval = self.yield_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal325 = None
        testlist326 = None


        string_literal325_tree = None

        try:
            try:
                # kv.g:376:2: ( 'yield' ( testlist )? )
                # kv.g:376:4: 'yield' ( testlist )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal325=self.match(self.input, 92, self.FOLLOW_92_in_yield_expr2297)
                if self._state.backtracking == 0:

                    string_literal325_tree = self._adaptor.createWithPayload(string_literal325)
                    self._adaptor.addChild(root_0, string_literal325_tree)

                # kv.g:376:12: ( testlist )?
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if (LA109_0 == WNAME or (PLUS <= LA109_0 <= MINUS) or LA109_0 == NAME or LA109_0 == LPAREN or LA109_0 == NOT or (TILDE <= LA109_0 <= LBRACK) or LA109_0 == LCURLY or (BACKQUOTE <= LA109_0 <= STRING) or LA109_0 == 90) :
                    alt109 = 1
                if alt109 == 1:
                    # kv.g:376:12: testlist
                    pass 
                    self._state.following.append(self.FOLLOW_testlist_in_yield_expr2299)
                    testlist326 = self.testlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, testlist326.tree)






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
    # kv.g:467:1: identifier : ( WNAME | NAME );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set327 = None

        set327_tree = None

        try:
            try:
                # kv.g:468:2: ( WNAME | NAME )
                # kv.g:
                pass 
                root_0 = self._adaptor.nil()

                set327 = self.input.LT(1)
                if self.input.LA(1) == WNAME or self.input.LA(1) == NAME:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set327))
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
        # kv.g:259:5: ( 'if' or_test 'else' )
        # kv.g:259:7: 'if' or_test 'else'
        pass 
        self.match(self.input, 86, self.FOLLOW_86_in_synpred1_kv1354)
        self._state.following.append(self.FOLLOW_or_test_in_synpred1_kv1356)
        self.or_test()

        self._state.following.pop()
        self.match(self.input, 87, self.FOLLOW_87_in_synpred1_kv1358)


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
        u"\1\66\1\30\1\32\3\30\1\25\2\32\1\30\1\34\1\30\1\25\1\4\1\32\1\30"
        u"\1\34\2\uffff\1\34\1\30\1\34"
        )

    DFA8_max = DFA.unpack(
        u"\1\66\1\35\1\67\1\30\2\35\1\31\2\67\1\30\1\67\1\30\1\25\1\106\1"
        u"\67\1\35\1\67\2\uffff\1\67\1\30\1\67"
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
        DFA.unpack(u"\1\5\1\4\33\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\11"),
        DFA.unpack(u"\1\12\4\uffff\1\13"),
        DFA.unpack(u"\1\15\3\uffff\1\14"),
        DFA.unpack(u"\1\5\1\4\33\uffff\1\6"),
        DFA.unpack(u"\1\5\1\4\33\uffff\1\6"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17\32\uffff\1\6"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\21\20\uffff\4\22\35\uffff\1\22\17\uffff\1\22"),
        DFA.unpack(u"\1\5\1\4\33\uffff\1\6"),
        DFA.unpack(u"\1\23\4\uffff\1\24"),
        DFA.unpack(u"\1\17\32\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\32\uffff\1\6"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\17\32\uffff\1\6")
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
        u"\1\30\1\32\2\30\2\uffff\2\32\1\30\1\32"
        )

    DFA9_max = DFA.unpack(
        u"\1\35\1\107\1\30\1\35\2\uffff\2\107\1\30\1\107"
        )

    DFA9_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1\4\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\1\4\uffff\1\2"),
        DFA.unpack(u"\1\4\1\3\33\uffff\1\5\17\uffff\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\7\4\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\3\33\uffff\1\5\17\uffff\1\5"),
        DFA.unpack(u"\1\4\1\3\33\uffff\1\5\17\uffff\1\5"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\4\1\3\33\uffff\1\5\17\uffff\1\5")
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
        DFA.unpack(u"\1\21\20\uffff\4\22\35\uffff\1\22\17\uffff\1\22"),
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
        u"\1\37\1\31\2\134\2\uffff"
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
        DFA.unpack(u"\1\4\2\uffff\1\5\3\uffff\2\5\1\uffff\1\5\1\3\4\uffff"
        u"\1\5\17\uffff\1\5\17\uffff\2\5\1\uffff\1\5\1\uffff\6\5\5\uffff"
        u"\1\5\4\uffff\1\5\1\uffff\1\5"),
        DFA.unpack(u"\1\4\2\uffff\1\5\3\uffff\2\5\1\uffff\1\5\1\3\4\uffff"
        u"\1\5\17\uffff\1\5\17\uffff\2\5\1\uffff\1\5\1\uffff\6\5\5\uffff"
        u"\1\5\4\uffff\1\5\1\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA51_min = DFA.unpack(
        u"\1\25\1\0\14\uffff"
        )

    DFA51_max = DFA.unpack(
        u"\1\133\1\0\14\uffff"
        )

    DFA51_accept = DFA.unpack(
        u"\2\uffff\1\2\12\uffff\1\1"
        )

    DFA51_special = DFA.unpack(
        u"\1\uffff\1\0\14\uffff"
        )

            
    DFA51_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\2\1\uffff\1\2\5\uffff\1\2\2\uffff\1\2"
        u"\1\uffff\15\2\24\uffff\1\2\1\uffff\2\2\13\uffff\1\1\4\uffff\1\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #51

    class DFA51(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA51_1 = input.LA(1)

                 
                index51_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_kv()):
                    s = 13

                elif (True):
                    s = 2

                 
                input.seek(index51_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 51, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #57

    DFA57_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA57_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA57_min = DFA.unpack(
        u"\1\65\10\uffff\1\130\3\uffff"
        )

    DFA57_max = DFA.unpack(
        u"\1\131\10\uffff\1\131\3\uffff"
        )

    DFA57_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\uffff\1\12\1\11\1\13"
        )

    DFA57_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA57_transition = [
        DFA.unpack(u"\1\11\1\1\1\2\1\3\1\4\1\5\1\6\1\7\33\uffff\1\10\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #57

    class DFA57(DFA):
        pass


    # lookup tables for DFA #75

    DFA75_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA75_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA75_min = DFA.unpack(
        u"\1\33\1\30\21\uffff"
        )

    DFA75_max = DFA.unpack(
        u"\1\46\1\132\21\uffff"
        )

    DFA75_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\16\uffff"
        )

    DFA75_special = DFA.unpack(
        u"\23\uffff"
        )

            
    DFA75_transition = [
        DFA.unpack(u"\1\1\12\uffff\1\2"),
        DFA.unpack(u"\1\4\3\uffff\2\4\1\uffff\1\4\5\uffff\1\4\1\2\16\uffff"
        u"\1\4\17\uffff\2\4\1\uffff\1\4\1\uffff\6\4\12\uffff\1\4"),
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


    # lookup tables for DFA #90

    DFA90_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA90_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA90_min = DFA.unpack(
        u"\1\33\1\30\17\uffff"
        )

    DFA90_max = DFA.unpack(
        u"\2\130\17\uffff"
        )

    DFA90_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\14\uffff"
        )

    DFA90_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA90_transition = [
        DFA.unpack(u"\1\1\74\uffff\1\2"),
        DFA.unpack(u"\1\4\3\uffff\2\4\1\uffff\1\4\5\uffff\1\4\37\uffff\2"
        u"\4\1\uffff\1\4\1\uffff\6\4\10\uffff\1\2"),
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

    # class definition for DFA #90

    class DFA90(DFA):
        pass


    # lookup tables for DFA #92

    DFA92_eot = DFA.unpack(
        u"\43\uffff"
        )

    DFA92_eof = DFA.unpack(
        u"\43\uffff"
        )

    DFA92_min = DFA.unpack(
        u"\2\25\41\uffff"
        )

    DFA92_max = DFA.unpack(
        u"\2\133\41\uffff"
        )

    DFA92_accept = DFA.unpack(
        u"\2\uffff\1\2\14\uffff\1\1\5\uffff\1\1\15\uffff"
        )

    DFA92_special = DFA.unpack(
        u"\43\uffff"
        )

            
    DFA92_transition = [
        DFA.unpack(u"\1\2\5\uffff\1\1\5\uffff\1\2\2\uffff\1\2\1\uffff\15"
        u"\2\24\uffff\1\2\2\uffff\1\2\13\uffff\1\2\4\uffff\1\2"),
        DFA.unpack(u"\1\2\2\uffff\1\25\2\uffff\1\2\2\25\1\uffff\1\25\1\uffff"
        u"\1\2\2\uffff\1\2\1\25\15\2\2\uffff\1\25\17\uffff\2\25\1\2\1\25"
        u"\1\uffff\1\17\5\25\6\uffff\1\2\3\uffff\1\25\1\2"),
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

    # class definition for DFA #92

    class DFA92(DFA):
        pass


    # lookup tables for DFA #94

    DFA94_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA94_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA94_min = DFA.unpack(
        u"\1\33\1\30\21\uffff"
        )

    DFA94_max = DFA.unpack(
        u"\1\111\1\132\21\uffff"
        )

    DFA94_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\17\uffff"
        )

    DFA94_special = DFA.unpack(
        u"\23\uffff"
        )

            
    DFA94_transition = [
        DFA.unpack(u"\1\1\55\uffff\1\2"),
        DFA.unpack(u"\1\3\3\uffff\2\3\1\uffff\1\3\5\uffff\1\3\17\uffff\1"
        u"\3\17\uffff\2\3\1\uffff\1\3\1\2\6\3\12\uffff\1\3"),
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

    # class definition for DFA #94

    class DFA94(DFA):
        pass


 

    FOLLOW_blank_in_kvfile202 = frozenset([1, 21, 22, 23, 24, 54, 70])
    FOLLOW_line_in_kvfile206 = frozenset([1, 21, 22, 23, 24, 54, 70])
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
    FOLLOW_widget_in_root_rule312 = frozenset([1])
    FOLLOW_WNAME_in_widget324 = frozenset([21, 25])
    FOLLOW_COLON_in_widget326 = frozenset([21])
    FOLLOW_NEWLINE_in_widget329 = frozenset([1])
    FOLLOW_WNAME_in_widget344 = frozenset([21, 25])
    FOLLOW_COLON_in_widget346 = frozenset([21, 25])
    FOLLOW_widget_body_in_widget349 = frozenset([1])
    FOLLOW_LESS_in_class_rule371 = frozenset([24, 29])
    FOLLOW_class_widget_in_class_rule375 = frozenset([55])
    FOLLOW_GREATER_in_class_rule377 = frozenset([21, 25])
    FOLLOW_COLON_in_class_rule379 = frozenset([21])
    FOLLOW_NEWLINE_in_class_rule382 = frozenset([1])
    FOLLOW_LESS_in_class_rule397 = frozenset([24, 29])
    FOLLOW_class_widget_in_class_rule401 = frozenset([55])
    FOLLOW_GREATER_in_class_rule403 = frozenset([21, 25])
    FOLLOW_COLON_in_class_rule405 = frozenset([21, 25])
    FOLLOW_widget_body_in_class_rule408 = frozenset([1])
    FOLLOW_widget_comp_in_class_widget430 = frozenset([1])
    FOLLOW_widget_list_in_widget_comp442 = frozenset([1])
    FOLLOW_widget_list_in_widget_comp455 = frozenset([26])
    FOLLOW_AT_in_widget_comp457 = frozenset([24, 29])
    FOLLOW_widget_base_in_widget_comp461 = frozenset([1])
    FOLLOW_widget_name_in_widget_list483 = frozenset([1])
    FOLLOW_widget_name_in_widget_list494 = frozenset([27])
    FOLLOW_COMMA_in_widget_list499 = frozenset([24, 29])
    FOLLOW_widget_name_in_widget_list501 = frozenset([1, 27])
    FOLLOW_widget_name_in_widget_base528 = frozenset([1])
    FOLLOW_widget_name_in_widget_base539 = frozenset([28])
    FOLLOW_PLUS_in_widget_base544 = frozenset([24, 29])
    FOLLOW_widget_name_in_widget_base546 = frozenset([1, 28])
    FOLLOW_WNAME_in_widget_name573 = frozenset([1])
    FOLLOW_MINUS_in_widget_name584 = frozenset([24])
    FOLLOW_WNAME_in_widget_name586 = frozenset([1])
    FOLLOW_WNAME_in_class_list606 = frozenset([1, 28])
    FOLLOW_PLUS_in_class_list609 = frozenset([24])
    FOLLOW_WNAME_in_class_list611 = frozenset([1, 28])
    FOLLOW_LBRACK_in_template_rule623 = frozenset([24, 29])
    FOLLOW_class_widget_in_template_rule627 = frozenset([71])
    FOLLOW_RBRACK_in_template_rule629 = frozenset([21, 25])
    FOLLOW_COLON_in_template_rule631 = frozenset([21])
    FOLLOW_NEWLINE_in_template_rule634 = frozenset([1])
    FOLLOW_LBRACK_in_template_rule649 = frozenset([24, 29])
    FOLLOW_class_widget_in_template_rule653 = frozenset([71])
    FOLLOW_RBRACK_in_template_rule655 = frozenset([21, 25])
    FOLLOW_COLON_in_template_rule657 = frozenset([21, 25])
    FOLLOW_widget_body_in_template_rule660 = frozenset([1])
    FOLLOW_NEWLINE_in_widget_body685 = frozenset([4])
    FOLLOW_INDENT_in_widget_body688 = frozenset([21, 22, 23, 24, 30, 31, 54, 70])
    FOLLOW_stmt_in_widget_body692 = frozenset([5, 21, 22, 23, 24, 30, 31, 54, 70])
    FOLLOW_DEDENT_in_widget_body696 = frozenset([1])
    FOLLOW_NEWLINE_in_canvas_body707 = frozenset([4])
    FOLLOW_INDENT_in_canvas_body710 = frozenset([21, 22, 23, 24, 54, 70])
    FOLLOW_canvas_stmt_in_canvas_body714 = frozenset([5, 21, 22, 23, 24, 54, 70])
    FOLLOW_DEDENT_in_canvas_body718 = frozenset([1])
    FOLLOW_widget_in_stmt729 = frozenset([1])
    FOLLOW_canvas_in_stmt734 = frozenset([1])
    FOLLOW_prop_in_stmt739 = frozenset([1])
    FOLLOW_comment_in_stmt744 = frozenset([1])
    FOLLOW_blank_in_stmt749 = frozenset([1])
    FOLLOW_instruction_in_canvas_stmt760 = frozenset([1])
    FOLLOW_comment_in_canvas_stmt765 = frozenset([1])
    FOLLOW_blank_in_canvas_stmt770 = frozenset([1])
    FOLLOW_WNAME_in_instruction781 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction783 = frozenset([21])
    FOLLOW_NEWLINE_in_instruction786 = frozenset([1])
    FOLLOW_WNAME_in_instruction801 = frozenset([21, 25])
    FOLLOW_COLON_in_instruction803 = frozenset([21, 25])
    FOLLOW_instruction_body_in_instruction806 = frozenset([1])
    FOLLOW_NEWLINE_in_instruction_body829 = frozenset([4])
    FOLLOW_INDENT_in_instruction_body832 = frozenset([21, 22, 23, 24, 31, 54, 70])
    FOLLOW_instruction_stmt_in_instruction_body836 = frozenset([5, 21, 22, 23, 24, 31, 54, 70])
    FOLLOW_DEDENT_in_instruction_body840 = frozenset([1])
    FOLLOW_prop_in_instruction_stmt852 = frozenset([1])
    FOLLOW_comment_in_instruction_stmt857 = frozenset([1])
    FOLLOW_blank_in_instruction_stmt862 = frozenset([1])
    FOLLOW_CANVAS_in_canvas873 = frozenset([25])
    FOLLOW_COLON_in_canvas875 = frozenset([21])
    FOLLOW_canvas_body_in_canvas877 = frozenset([1])
    FOLLOW_NAME_in_prop898 = frozenset([25])
    FOLLOW_COLON_in_prop900 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_WS_in_prop902 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_prop_value_in_prop907 = frozenset([21])
    FOLLOW_NEWLINE_in_prop909 = frozenset([1])
    FOLLOW_NAME_in_prop925 = frozenset([25])
    FOLLOW_COLON_in_prop927 = frozenset([21, 32])
    FOLLOW_WS_in_prop929 = frozenset([21, 32])
    FOLLOW_NEWLINE_in_prop932 = frozenset([4])
    FOLLOW_INDENT_in_prop934 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_prop_value_in_prop938 = frozenset([21])
    FOLLOW_NEWLINE_in_prop940 = frozenset([5])
    FOLLOW_DEDENT_in_prop942 = frozenset([1])
    FOLLOW_python_in_prop_value963 = frozenset([1])
    FOLLOW_small_stmt_in_python985 = frozenset([1, 33])
    FOLLOW_SEMI_in_python995 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_small_stmt_in_python997 = frozenset([1, 33])
    FOLLOW_SEMI_in_python1002 = frozenset([1])
    FOLLOW_expr_stmt_in_small_stmt1015 = frozenset([1])
    FOLLOW_raise_stmt_in_small_stmt1020 = frozenset([1])
    FOLLOW_yield_stmt_in_small_stmt1025 = frozenset([1])
    FOLLOW_defparameter_in_varargslist1035 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1045 = frozenset([24, 31, 37])
    FOLLOW_defparameter_in_varargslist1047 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1052 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_varargslist1056 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1058 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1061 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1063 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1065 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1071 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1073 = frozenset([1])
    FOLLOW_STAR_in_varargslist1084 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1086 = frozenset([1, 27])
    FOLLOW_COMMA_in_varargslist1089 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_varargslist1091 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1093 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_varargslist1100 = frozenset([24, 31])
    FOLLOW_identifier_in_varargslist1102 = frozenset([1])
    FOLLOW_fpdef_in_defparameter1112 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_defparameter1115 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_defparameter1117 = frozenset([1])
    FOLLOW_identifier_in_fpdef1129 = frozenset([1])
    FOLLOW_LPAREN_in_fpdef1134 = frozenset([24, 31, 37])
    FOLLOW_fplist_in_fpdef1136 = frozenset([38])
    FOLLOW_RPAREN_in_fpdef1138 = frozenset([1])
    FOLLOW_fpdef_in_fplist1148 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1158 = frozenset([24, 31, 37])
    FOLLOW_fpdef_in_fplist1160 = frozenset([1, 27])
    FOLLOW_COMMA_in_fplist1165 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt1178 = frozenset([1, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    FOLLOW_augassign_in_expr_stmt1181 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_yield_expr_in_expr_stmt1183 = frozenset([1])
    FOLLOW_augassign_in_expr_stmt1187 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_testlist_in_expr_stmt1189 = frozenset([1])
    FOLLOW_assigns_in_expr_stmt1193 = frozenset([1])
    FOLLOW_assign_testlist_in_assigns1206 = frozenset([1, 36])
    FOLLOW_assign_yield_in_assigns1211 = frozenset([1, 36])
    FOLLOW_ASSIGN_in_assign_testlist1223 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_testlist_in_assign_testlist1225 = frozenset([1])
    FOLLOW_ASSIGN_in_assign_yield1236 = frozenset([24, 28, 29, 31, 32, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_yield_expr_in_assign_yield1238 = frozenset([1])
    FOLLOW_set_in_augassign0 = frozenset([1])
    FOLLOW_yield_expr_in_yield_stmt1306 = frozenset([1])
    FOLLOW_85_in_raise_stmt1316 = frozenset([1, 24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_raise_stmt1319 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1322 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_raise_stmt1324 = frozenset([1, 27])
    FOLLOW_COMMA_in_raise_stmt1327 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_raise_stmt1329 = frozenset([1])
    FOLLOW_or_test_in_test1346 = frozenset([1, 86])
    FOLLOW_86_in_test1364 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_or_test_in_test1366 = frozenset([87])
    FOLLOW_87_in_test1368 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_test1370 = frozenset([1])
    FOLLOW_lambdef_in_test1378 = frozenset([1])
    FOLLOW_and_test_in_or_test1388 = frozenset([1, 51])
    FOLLOW_OR_in_or_test1391 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_and_test_in_or_test1393 = frozenset([1, 51])
    FOLLOW_not_test_in_and_test1405 = frozenset([1, 52])
    FOLLOW_AND_in_and_test1408 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_not_test_in_and_test1410 = frozenset([1, 52])
    FOLLOW_NOT_in_not_test1422 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_not_test_in_not_test1424 = frozenset([1])
    FOLLOW_comparison_in_not_test1429 = frozenset([1])
    FOLLOW_expr_in_comparison1439 = frozenset([1, 53, 54, 55, 56, 57, 58, 59, 60, 88, 89])
    FOLLOW_comp_op_in_comparison1442 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_expr_in_comparison1444 = frozenset([1, 53, 54, 55, 56, 57, 58, 59, 60, 88, 89])
    FOLLOW_LESS_in_comp_op1456 = frozenset([1])
    FOLLOW_GREATER_in_comp_op1460 = frozenset([1])
    FOLLOW_EQUAL_in_comp_op1464 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comp_op1468 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comp_op1472 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comp_op1476 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comp_op1480 = frozenset([1])
    FOLLOW_88_in_comp_op1485 = frozenset([1])
    FOLLOW_NOT_in_comp_op1489 = frozenset([88])
    FOLLOW_88_in_comp_op1491 = frozenset([1])
    FOLLOW_89_in_comp_op1495 = frozenset([1])
    FOLLOW_NOT_in_comp_op1499 = frozenset([89])
    FOLLOW_89_in_comp_op1501 = frozenset([1])
    FOLLOW_xor_expr_in_expr1511 = frozenset([1, 61])
    FOLLOW_VBAR_in_expr1514 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_xor_expr_in_expr1516 = frozenset([1, 61])
    FOLLOW_and_expr_in_xor_expr1528 = frozenset([1, 62])
    FOLLOW_CIRCUMFLEX_in_xor_expr1531 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_and_expr_in_xor_expr1533 = frozenset([1, 62])
    FOLLOW_shift_expr_in_and_expr1545 = frozenset([1, 63])
    FOLLOW_AMPER_in_and_expr1548 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_shift_expr_in_and_expr1550 = frozenset([1, 63])
    FOLLOW_arith_expr_in_shift_expr1562 = frozenset([1, 64, 65])
    FOLLOW_set_in_shift_expr1565 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_arith_expr_in_shift_expr1571 = frozenset([1, 64, 65])
    FOLLOW_term_in_arith_expr1583 = frozenset([1, 28, 29])
    FOLLOW_set_in_arith_expr1586 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_term_in_arith_expr1592 = frozenset([1, 28, 29])
    FOLLOW_factor_in_term1604 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_set_in_term1607 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_factor_in_term1624 = frozenset([1, 34, 66, 67, 68])
    FOLLOW_PLUS_in_factor1636 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_factor_in_factor1638 = frozenset([1])
    FOLLOW_MINUS_in_factor1642 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_factor_in_factor1644 = frozenset([1])
    FOLLOW_TILDE_in_factor1648 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_factor_in_factor1650 = frozenset([1])
    FOLLOW_power_in_factor1654 = frozenset([1])
    FOLLOW_atom_in_power1664 = frozenset([1, 35, 37, 70, 80])
    FOLLOW_trailer_in_power1667 = frozenset([1, 35, 37, 70, 80])
    FOLLOW_DOUBLESTAR_in_power1679 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_factor_in_power1681 = frozenset([1])
    FOLLOW_LPAREN_in_atom1693 = frozenset([24, 28, 29, 31, 32, 37, 38, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 85, 90, 92])
    FOLLOW_yield_expr_in_atom1697 = frozenset([38])
    FOLLOW_testlist_gexp_in_atom1701 = frozenset([38])
    FOLLOW_RPAREN_in_atom1706 = frozenset([1])
    FOLLOW_LBRACK_in_atom1711 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_listmaker_in_atom1714 = frozenset([71])
    FOLLOW_RBRACK_in_atom1718 = frozenset([1])
    FOLLOW_LCURLY_in_atom1723 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_dictmaker_in_atom1726 = frozenset([73])
    FOLLOW_RCURLY_in_atom1730 = frozenset([1])
    FOLLOW_BACKQUOTE_in_atom1735 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_testlist_in_atom1737 = frozenset([74])
    FOLLOW_BACKQUOTE_in_atom1739 = frozenset([1])
    FOLLOW_identifier_in_atom1744 = frozenset([1])
    FOLLOW_INT_in_atom1749 = frozenset([1])
    FOLLOW_LONGINT_in_atom1754 = frozenset([1])
    FOLLOW_FLOAT_in_atom1759 = frozenset([1])
    FOLLOW_COMPLEX_in_atom1764 = frozenset([1])
    FOLLOW_STRING_in_atom1770 = frozenset([1, 79])
    FOLLOW_test_in_listmaker1782 = frozenset([1, 27, 91])
    FOLLOW_list_for_in_listmaker1785 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker1797 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_listmaker1799 = frozenset([1, 27])
    FOLLOW_COMMA_in_listmaker1806 = frozenset([1])
    FOLLOW_test_in_testlist_gexp1818 = frozenset([1, 27, 91])
    FOLLOW_COMMA_in_testlist_gexp1831 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_testlist_gexp1833 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist_gexp1838 = frozenset([1])
    FOLLOW_gen_for_in_testlist_gexp1844 = frozenset([1])
    FOLLOW_90_in_lambdef1856 = frozenset([24, 25, 31, 34, 35, 37])
    FOLLOW_varargslist_in_lambdef1859 = frozenset([25])
    FOLLOW_COLON_in_lambdef1863 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_lambdef1865 = frozenset([1])
    FOLLOW_LPAREN_in_trailer1875 = frozenset([24, 28, 29, 31, 34, 35, 37, 38, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_arglist_in_trailer1878 = frozenset([38])
    FOLLOW_RPAREN_in_trailer1882 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1887 = frozenset([24, 25, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 90])
    FOLLOW_subscriptlist_in_trailer1889 = frozenset([71])
    FOLLOW_RBRACK_in_trailer1891 = frozenset([1])
    FOLLOW_DOT_in_trailer1896 = frozenset([24, 31])
    FOLLOW_identifier_in_trailer1898 = frozenset([1])
    FOLLOW_subscript_in_subscriptlist1908 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist1918 = frozenset([24, 25, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 80, 90])
    FOLLOW_subscript_in_subscriptlist1920 = frozenset([1, 27])
    FOLLOW_COMMA_in_subscriptlist1925 = frozenset([1])
    FOLLOW_DOT_in_subscript1937 = frozenset([80])
    FOLLOW_DOT_in_subscript1939 = frozenset([80])
    FOLLOW_DOT_in_subscript1941 = frozenset([1])
    FOLLOW_test_in_subscript1946 = frozenset([1, 25])
    FOLLOW_COLON_in_subscript1949 = frozenset([1, 24, 25, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_subscript1952 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript1957 = frozenset([1])
    FOLLOW_COLON_in_subscript1966 = frozenset([1, 24, 25, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_subscript1969 = frozenset([1, 25])
    FOLLOW_sliceop_in_subscript1974 = frozenset([1])
    FOLLOW_COLON_in_sliceop1986 = frozenset([1, 24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_sliceop1989 = frozenset([1])
    FOLLOW_expr_in_exprlist2001 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2012 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_expr_in_exprlist2014 = frozenset([1, 27])
    FOLLOW_COMMA_in_exprlist2019 = frozenset([1])
    FOLLOW_test_in_testlist2031 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2042 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_testlist2044 = frozenset([1, 27])
    FOLLOW_COMMA_in_testlist2049 = frozenset([1])
    FOLLOW_test_in_dictmaker2061 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2063 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_dictmaker2065 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2076 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_dictmaker2078 = frozenset([25])
    FOLLOW_COLON_in_dictmaker2080 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_dictmaker2082 = frozenset([1, 27])
    FOLLOW_COMMA_in_dictmaker2087 = frozenset([1])
    FOLLOW_argument_in_arglist2099 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2102 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_argument_in_arglist2104 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2110 = frozenset([1, 34, 35])
    FOLLOW_STAR_in_arglist2114 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2116 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2119 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2121 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2123 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2129 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2131 = frozenset([1])
    FOLLOW_STAR_in_arglist2142 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2144 = frozenset([1, 27])
    FOLLOW_COMMA_in_arglist2147 = frozenset([35])
    FOLLOW_DOUBLESTAR_in_arglist2149 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2151 = frozenset([1])
    FOLLOW_DOUBLESTAR_in_arglist2158 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_arglist2160 = frozenset([1])
    FOLLOW_test_in_argument2170 = frozenset([27, 36, 91])
    FOLLOW_ASSIGN_in_argument2176 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_argument2178 = frozenset([1])
    FOLLOW_gen_for_in_argument2184 = frozenset([1])
    FOLLOW_list_for_in_list_iter2197 = frozenset([1])
    FOLLOW_list_if_in_list_iter2201 = frozenset([1])
    FOLLOW_91_in_list_for2211 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_exprlist_in_list_for2213 = frozenset([88])
    FOLLOW_88_in_list_for2215 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_testlist_in_list_for2217 = frozenset([1, 86, 91])
    FOLLOW_list_iter_in_list_for2220 = frozenset([1])
    FOLLOW_86_in_list_if2232 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_list_if2234 = frozenset([1, 86, 91])
    FOLLOW_list_iter_in_list_if2237 = frozenset([1])
    FOLLOW_gen_for_in_gen_iter2249 = frozenset([1])
    FOLLOW_gen_if_in_gen_iter2253 = frozenset([1])
    FOLLOW_91_in_gen_for2263 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_exprlist_in_gen_for2265 = frozenset([88])
    FOLLOW_88_in_gen_for2267 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_or_test_in_gen_for2269 = frozenset([1, 27, 86, 91])
    FOLLOW_gen_iter_in_gen_for2271 = frozenset([1])
    FOLLOW_86_in_gen_if2282 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_test_in_gen_if2284 = frozenset([1, 27, 86, 91])
    FOLLOW_gen_iter_in_gen_if2286 = frozenset([1])
    FOLLOW_92_in_yield_expr2297 = frozenset([1, 24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79, 90])
    FOLLOW_testlist_in_yield_expr2299 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_86_in_synpred1_kv1354 = frozenset([24, 28, 29, 31, 37, 53, 69, 70, 72, 74, 75, 76, 77, 78, 79])
    FOLLOW_or_test_in_synpred1_kv1356 = frozenset([87])
    FOLLOW_87_in_synpred1_kv1358 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("kvLexer", kvParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
