# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 kv.g 2014-07-23 13:02:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INSTRUCTION=18
SLASHEQUAL=42
BACKQUOTE=74
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
RPAREN=38
T__91=91
NAME=31
T__92=92
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
AMPEREQUAL=44
NEWLINE=21
RCURLY=73
ASSIGN=36
STAREQUAL=41
CIRCUMFLEX=63
STRING=80
ALT_NOTEQUAL=60
AUTOCLASS=20


class kvLexer(Lexer):

    grammarFileName = "kv.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(kvLexer, self).__init__(input, state)


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

        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )

        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )

        self.dfa25 = self.DFA25(
            self, 25,
            eot = self.DFA25_eot,
            eof = self.DFA25_eof,
            min = self.DFA25_min,
            max = self.DFA25_max,
            accept = self.DFA25_accept,
            special = self.DFA25_special,
            transition = self.DFA25_transition
            )


                             
        self.startPos = -1
        def nextToken():
        	self.startPos = self.getCharPositionInLine()
        	return Lexer.nextToken(self)
        self.nextToken = nextToken





    # $ANTLR start "T__86"
    def mT__86(self, ):

        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # kv.g:15:7: ( 'print' )
            # kv.g:15:9: 'print'
            pass 
            self.match("print")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):

        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # kv.g:16:7: ( 'del' )
            # kv.g:16:9: 'del'
            pass 
            self.match("del")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):

        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # kv.g:17:7: ( 'pass' )
            # kv.g:17:9: 'pass'
            pass 
            self.match("pass")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):

        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # kv.g:18:7: ( 'break' )
            # kv.g:18:9: 'break'
            pass 
            self.match("break")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):

        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # kv.g:19:7: ( 'continue' )
            # kv.g:19:9: 'continue'
            pass 
            self.match("continue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):

        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # kv.g:20:7: ( 'raise' )
            # kv.g:20:9: 'raise'
            pass 
            self.match("raise")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):

        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # kv.g:21:7: ( 'exec' )
            # kv.g:21:9: 'exec'
            pass 
            self.match("exec")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):

        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # kv.g:22:7: ( 'in' )
            # kv.g:22:9: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):

        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # kv.g:23:7: ( 'assert' )
            # kv.g:23:9: 'assert'
            pass 
            self.match("assert")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):

        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # kv.g:24:7: ( 'if' )
            # kv.g:24:9: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):

        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # kv.g:25:7: ( 'else' )
            # kv.g:25:9: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):

        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # kv.g:26:7: ( 'elif' )
            # kv.g:26:9: 'elif'
            pass 
            self.match("elif")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):

        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # kv.g:27:7: ( 'while' )
            # kv.g:27:9: 'while'
            pass 
            self.match("while")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):

        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # kv.g:28:7: ( 'for' )
            # kv.g:28:9: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):

        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # kv.g:29:8: ( 'try' )
            # kv.g:29:10: 'try'
            pass 
            self.match("try")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):

        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # kv.g:30:8: ( 'finally' )
            # kv.g:30:10: 'finally'
            pass 
            self.match("finally")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):

        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # kv.g:31:8: ( 'with' )
            # kv.g:31:10: 'with'
            pass 
            self.match("with")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):

        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # kv.g:32:8: ( 'as' )
            # kv.g:32:10: 'as'
            pass 
            self.match("as")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__103"



    # $ANTLR start "T__104"
    def mT__104(self, ):

        try:
            _type = T__104
            _channel = DEFAULT_CHANNEL

            # kv.g:33:8: ( 'except' )
            # kv.g:33:10: 'except'
            pass 
            self.match("except")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__104"



    # $ANTLR start "T__105"
    def mT__105(self, ):

        try:
            _type = T__105
            _channel = DEFAULT_CHANNEL

            # kv.g:34:8: ( 'is' )
            # kv.g:34:10: 'is'
            pass 
            self.match("is")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__105"



    # $ANTLR start "T__106"
    def mT__106(self, ):

        try:
            _type = T__106
            _channel = DEFAULT_CHANNEL

            # kv.g:35:8: ( 'lambda' )
            # kv.g:35:10: 'lambda'
            pass 
            self.match("lambda")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__106"



    # $ANTLR start "T__107"
    def mT__107(self, ):

        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # kv.g:36:8: ( 'yield' )
            # kv.g:36:10: 'yield'
            pass 
            self.match("yield")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__107"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # kv.g:461:8: ( '(' )
            # kv.g:461:11: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # kv.g:462:8: ( ')' )
            # kv.g:462:11: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACK"
    def mLBRACK(self, ):

        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # kv.g:463:8: ( '[' )
            # kv.g:463:11: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACK"



    # $ANTLR start "RBRACK"
    def mRBRACK(self, ):

        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # kv.g:464:8: ( ']' )
            # kv.g:464:11: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACK"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # kv.g:465:7: ( ':' )
            # kv.g:465:11: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # kv.g:466:7: ( ',' )
            # kv.g:466:11: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):

        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # kv.g:467:6: ( ';' )
            # kv.g:467:10: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # kv.g:468:6: ( '+' )
            # kv.g:468:10: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # kv.g:469:7: ( '-' )
            # kv.g:469:11: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # kv.g:470:6: ( '*' )
            # kv.g:470:10: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "SLASH"
    def mSLASH(self, ):

        try:
            _type = SLASH
            _channel = DEFAULT_CHANNEL

            # kv.g:471:7: ( '/' )
            # kv.g:471:11: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASH"



    # $ANTLR start "VBAR"
    def mVBAR(self, ):

        try:
            _type = VBAR
            _channel = DEFAULT_CHANNEL

            # kv.g:472:6: ( '|' )
            # kv.g:472:10: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VBAR"



    # $ANTLR start "AMPER"
    def mAMPER(self, ):

        try:
            _type = AMPER
            _channel = DEFAULT_CHANNEL

            # kv.g:473:7: ( '&' )
            # kv.g:473:11: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AMPER"



    # $ANTLR start "LESS"
    def mLESS(self, ):

        try:
            _type = LESS
            _channel = DEFAULT_CHANNEL

            # kv.g:474:6: ( '<' )
            # kv.g:474:10: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS"



    # $ANTLR start "GREATER"
    def mGREATER(self, ):

        try:
            _type = GREATER
            _channel = DEFAULT_CHANNEL

            # kv.g:475:9: ( '>' )
            # kv.g:475:12: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # kv.g:476:8: ( '=' )
            # kv.g:476:11: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "PERCENT"
    def mPERCENT(self, ):

        try:
            _type = PERCENT
            _channel = DEFAULT_CHANNEL

            # kv.g:477:9: ( '%' )
            # kv.g:477:12: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENT"



    # $ANTLR start "BACKQUOTE"
    def mBACKQUOTE(self, ):

        try:
            _type = BACKQUOTE
            _channel = DEFAULT_CHANNEL

            # kv.g:478:11: ( '`' )
            # kv.g:478:14: '`'
            pass 
            self.match(96)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BACKQUOTE"



    # $ANTLR start "LCURLY"
    def mLCURLY(self, ):

        try:
            _type = LCURLY
            _channel = DEFAULT_CHANNEL

            # kv.g:479:8: ( '{' )
            # kv.g:479:11: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LCURLY"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):

        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # kv.g:480:8: ( '}' )
            # kv.g:480:11: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RCURLY"



    # $ANTLR start "CIRCUMFLEX"
    def mCIRCUMFLEX(self, ):

        try:
            _type = CIRCUMFLEX
            _channel = DEFAULT_CHANNEL

            # kv.g:481:12: ( '^' )
            # kv.g:481:14: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CIRCUMFLEX"



    # $ANTLR start "TILDE"
    def mTILDE(self, ):

        try:
            _type = TILDE
            _channel = DEFAULT_CHANNEL

            # kv.g:482:7: ( '~' )
            # kv.g:482:11: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TILDE"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:483:7: ( '==' )
            # kv.g:483:11: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "NOTEQUAL"
    def mNOTEQUAL(self, ):

        try:
            _type = NOTEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:484:10: ( '!=' )
            # kv.g:484:13: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTEQUAL"



    # $ANTLR start "ALT_NOTEQUAL"
    def mALT_NOTEQUAL(self, ):

        try:
            _type = ALT_NOTEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:485:14: ( '<>' )
            # kv.g:485:16: '<>'
            pass 
            self.match("<>")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALT_NOTEQUAL"



    # $ANTLR start "LESSEQUAL"
    def mLESSEQUAL(self, ):

        try:
            _type = LESSEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:486:11: ( '<=' )
            # kv.g:486:14: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESSEQUAL"



    # $ANTLR start "LEFTSHIFT"
    def mLEFTSHIFT(self, ):

        try:
            _type = LEFTSHIFT
            _channel = DEFAULT_CHANNEL

            # kv.g:487:11: ( '<<' )
            # kv.g:487:14: '<<'
            pass 
            self.match("<<")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFTSHIFT"



    # $ANTLR start "GREATEREQUAL"
    def mGREATEREQUAL(self, ):

        try:
            _type = GREATEREQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:488:14: ( '>=' )
            # kv.g:488:16: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATEREQUAL"



    # $ANTLR start "RIGHTSHIFT"
    def mRIGHTSHIFT(self, ):

        try:
            _type = RIGHTSHIFT
            _channel = DEFAULT_CHANNEL

            # kv.g:489:12: ( '>>' )
            # kv.g:489:14: '>>'
            pass 
            self.match(">>")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHTSHIFT"



    # $ANTLR start "PLUSEQUAL"
    def mPLUSEQUAL(self, ):

        try:
            _type = PLUSEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:490:11: ( '+=' )
            # kv.g:490:14: '+='
            pass 
            self.match("+=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUSEQUAL"



    # $ANTLR start "MINUSEQUAL"
    def mMINUSEQUAL(self, ):

        try:
            _type = MINUSEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:491:12: ( '-=' )
            # kv.g:491:14: '-='
            pass 
            self.match("-=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUSEQUAL"



    # $ANTLR start "DOUBLESTAR"
    def mDOUBLESTAR(self, ):

        try:
            _type = DOUBLESTAR
            _channel = DEFAULT_CHANNEL

            # kv.g:492:12: ( '**' )
            # kv.g:492:14: '**'
            pass 
            self.match("**")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESTAR"



    # $ANTLR start "STAREQUAL"
    def mSTAREQUAL(self, ):

        try:
            _type = STAREQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:493:11: ( '*=' )
            # kv.g:493:14: '*='
            pass 
            self.match("*=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAREQUAL"



    # $ANTLR start "DOUBLESLASH"
    def mDOUBLESLASH(self, ):

        try:
            _type = DOUBLESLASH
            _channel = DEFAULT_CHANNEL

            # kv.g:494:13: ( '//' )
            # kv.g:494:15: '//'
            pass 
            self.match("//")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESLASH"



    # $ANTLR start "SLASHEQUAL"
    def mSLASHEQUAL(self, ):

        try:
            _type = SLASHEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:495:12: ( '/=' )
            # kv.g:495:14: '/='
            pass 
            self.match("/=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASHEQUAL"



    # $ANTLR start "VBAREQUAL"
    def mVBAREQUAL(self, ):

        try:
            _type = VBAREQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:496:11: ( '|=' )
            # kv.g:496:14: '|='
            pass 
            self.match("|=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VBAREQUAL"



    # $ANTLR start "PERCENTEQUAL"
    def mPERCENTEQUAL(self, ):

        try:
            _type = PERCENTEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:497:14: ( '%=' )
            # kv.g:497:16: '%='
            pass 
            self.match("%=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENTEQUAL"



    # $ANTLR start "AMPEREQUAL"
    def mAMPEREQUAL(self, ):

        try:
            _type = AMPEREQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:498:12: ( '&=' )
            # kv.g:498:14: '&='
            pass 
            self.match("&=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AMPEREQUAL"



    # $ANTLR start "CIRCUMFLEXEQUAL"
    def mCIRCUMFLEXEQUAL(self, ):

        try:
            _type = CIRCUMFLEXEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:499:17: ( '^=' )
            # kv.g:499:19: '^='
            pass 
            self.match("^=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CIRCUMFLEXEQUAL"



    # $ANTLR start "LEFTSHIFTEQUAL"
    def mLEFTSHIFTEQUAL(self, ):

        try:
            _type = LEFTSHIFTEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:500:16: ( '<<=' )
            # kv.g:500:18: '<<='
            pass 
            self.match("<<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFTSHIFTEQUAL"



    # $ANTLR start "RIGHTSHIFTEQUAL"
    def mRIGHTSHIFTEQUAL(self, ):

        try:
            _type = RIGHTSHIFTEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:501:17: ( '>>=' )
            # kv.g:501:19: '>>='
            pass 
            self.match(">>=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHTSHIFTEQUAL"



    # $ANTLR start "DOUBLESTAREQUAL"
    def mDOUBLESTAREQUAL(self, ):

        try:
            _type = DOUBLESTAREQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:502:17: ( '**=' )
            # kv.g:502:19: '**='
            pass 
            self.match("**=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESTAREQUAL"



    # $ANTLR start "DOUBLESLASHEQUAL"
    def mDOUBLESLASHEQUAL(self, ):

        try:
            _type = DOUBLESLASHEQUAL
            _channel = DEFAULT_CHANNEL

            # kv.g:503:18: ( '//=' )
            # kv.g:503:20: '//='
            pass 
            self.match("//=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESLASHEQUAL"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # kv.g:504:5: ( '.' )
            # kv.g:504:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "AT"
    def mAT(self, ):

        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # kv.g:505:4: ( '@' )
            # kv.g:505:8: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AT"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # kv.g:506:5: ( 'and' )
            # kv.g:506:9: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # kv.g:507:4: ( 'or' )
            # kv.g:507:8: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # kv.g:508:5: ( 'not' )
            # kv.g:508:9: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # kv.g:511:2: ( '.' DIGITS ( Exponent )? | DIGITS '.' Exponent | DIGITS ( '.' ( DIGITS ( Exponent )? )? | Exponent ) )
            alt5 = 3
            alt5 = self.dfa5.predict(self.input)
            if alt5 == 1:
                # kv.g:511:4: '.' DIGITS ( Exponent )?
                pass 
                self.match(46)
                self.mDIGITS()
                # kv.g:511:15: ( Exponent )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 69 or LA1_0 == 101) :
                    alt1 = 1
                if alt1 == 1:
                    # kv.g:511:16: Exponent
                    pass 
                    self.mExponent()





            elif alt5 == 2:
                # kv.g:512:4: DIGITS '.' Exponent
                pass 
                self.mDIGITS()
                self.match(46)
                self.mExponent()


            elif alt5 == 3:
                # kv.g:513:4: DIGITS ( '.' ( DIGITS ( Exponent )? )? | Exponent )
                pass 
                self.mDIGITS()
                # kv.g:513:11: ( '.' ( DIGITS ( Exponent )? )? | Exponent )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 46) :
                    alt4 = 1
                elif (LA4_0 == 69 or LA4_0 == 101) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # kv.g:513:12: '.' ( DIGITS ( Exponent )? )?
                    pass 
                    self.match(46)
                    # kv.g:513:16: ( DIGITS ( Exponent )? )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1
                    if alt3 == 1:
                        # kv.g:513:17: DIGITS ( Exponent )?
                        pass 
                        self.mDIGITS()
                        # kv.g:513:24: ( Exponent )?
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 69 or LA2_0 == 101) :
                            alt2 = 1
                        if alt2 == 1:
                            # kv.g:513:25: Exponent
                            pass 
                            self.mExponent()








                elif alt4 == 2:
                    # kv.g:513:40: Exponent
                    pass 
                    self.mExponent()





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "LONGINT"
    def mLONGINT(self, ):

        try:
            _type = LONGINT
            _channel = DEFAULT_CHANNEL

            # kv.g:516:2: ( INT ( 'l' | 'L' ) )
            # kv.g:516:4: INT ( 'l' | 'L' )
            pass 
            self.mINT()
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LONGINT"



    # $ANTLR start "Exponent"
    def mExponent(self, ):

        try:
            # kv.g:520:2: ( ( 'e' | 'E' ) ( '+' | '-' )? DIGITS )
            # kv.g:520:4: ( 'e' | 'E' ) ( '+' | '-' )? DIGITS
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # kv.g:520:16: ( '+' | '-' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 43 or LA6_0 == 45) :
                alt6 = 1
            if alt6 == 1:
                # kv.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            self.mDIGITS()




        finally:

            pass

    # $ANTLR end "Exponent"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # kv.g:522:5: ( '0' ( 'x' | 'X' ) ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+ | '0' ( DIGITS )* | '1' .. '9' ( DIGITS )* )
            alt10 = 3
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 48) :
                LA10_1 = self.input.LA(2)

                if (LA10_1 == 88 or LA10_1 == 120) :
                    alt10 = 1
                else:
                    alt10 = 2
            elif ((49 <= LA10_0 <= 57)) :
                alt10 = 3
            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae

            if alt10 == 1:
                # kv.g:522:7: '0' ( 'x' | 'X' ) ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
                pass 
                self.match(48)
                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # kv.g:522:23: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((48 <= LA7_0 <= 57) or (65 <= LA7_0 <= 70) or (97 <= LA7_0 <= 102)) :
                        alt7 = 1


                    if alt7 == 1:
                        # kv.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


            elif alt10 == 2:
                # kv.g:523:4: '0' ( DIGITS )*
                pass 
                self.match(48)
                # kv.g:523:8: ( DIGITS )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # kv.g:523:8: DIGITS
                        pass 
                        self.mDIGITS()


                    else:
                        break #loop8


            elif alt10 == 3:
                # kv.g:524:4: '1' .. '9' ( DIGITS )*
                pass 
                self.matchRange(49, 57)
                # kv.g:524:15: ( DIGITS )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # kv.g:524:15: DIGITS
                        pass 
                        self.mDIGITS()


                    else:
                        break #loop9


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "COMPLEX"
    def mCOMPLEX(self, ):

        try:
            _type = COMPLEX
            _channel = DEFAULT_CHANNEL

            # kv.g:527:2: ( INT ( 'j' | 'J' ) | FLOAT ( 'j' | 'J' ) )
            alt11 = 2
            alt11 = self.dfa11.predict(self.input)
            if alt11 == 1:
                # kv.g:527:4: INT ( 'j' | 'J' )
                pass 
                self.mINT()
                if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt11 == 2:
                # kv.g:528:4: FLOAT ( 'j' | 'J' )
                pass 
                self.mFLOAT()
                if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMPLEX"



    # $ANTLR start "DIGITS"
    def mDIGITS(self, ):

        try:
            # kv.g:532:2: ( ( '0' .. '9' )+ )
            # kv.g:532:4: ( '0' .. '9' )+
            pass 
            # kv.g:532:4: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)) :
                    alt12 = 1


                if alt12 == 1:
                    # kv.g:532:6: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1




        finally:

            pass

    # $ANTLR end "DIGITS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # kv.g:535:2: ( ( 'r' | 'u' | 'ur' )? ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' ) )
            # kv.g:535:4: ( 'r' | 'u' | 'ur' )? ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
            pass 
            # kv.g:535:4: ( 'r' | 'u' | 'ur' )?
            alt13 = 4
            LA13_0 = self.input.LA(1)

            if (LA13_0 == 114) :
                alt13 = 1
            elif (LA13_0 == 117) :
                LA13_2 = self.input.LA(2)

                if (LA13_2 == 114) :
                    alt13 = 3
                elif (LA13_2 == 34 or LA13_2 == 39) :
                    alt13 = 2
            if alt13 == 1:
                # kv.g:535:5: 'r'
                pass 
                self.match(114)


            elif alt13 == 2:
                # kv.g:535:11: 'u'
                pass 
                self.match(117)


            elif alt13 == 3:
                # kv.g:535:17: 'ur'
                pass 
                self.match("ur")



            # kv.g:536:3: ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
            alt16 = 2
            LA16_0 = self.input.LA(1)

            if (LA16_0 == 34) :
                alt16 = 1
            elif (LA16_0 == 39) :
                alt16 = 2
            else:
                nvae = NoViableAltException("", 16, 0, self.input)

                raise nvae

            if alt16 == 1:
                # kv.g:536:5: '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"'
                pass 
                self.match(34)
                # kv.g:536:9: ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )*
                while True: #loop14
                    alt14 = 3
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 92) :
                        alt14 = 1
                    elif ((0 <= LA14_0 <= 9) or (11 <= LA14_0 <= 33) or (35 <= LA14_0 <= 91) or (93 <= LA14_0 <= 65535)) :
                        alt14 = 2


                    if alt14 == 1:
                        # kv.g:536:10: ESC
                        pass 
                        self.mESC()


                    elif alt14 == 2:
                        # kv.g:536:14: ~ ( '\\\\' | '\\n' | '\"' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop14
                self.match(34)


            elif alt16 == 2:
                # kv.g:537:5: '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\''
                pass 
                self.match(39)
                # kv.g:537:10: ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )*
                while True: #loop15
                    alt15 = 3
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 92) :
                        alt15 = 1
                    elif ((0 <= LA15_0 <= 9) or (11 <= LA15_0 <= 38) or (40 <= LA15_0 <= 91) or (93 <= LA15_0 <= 65535)) :
                        alt15 = 2


                    if alt15 == 1:
                        # kv.g:537:11: ESC
                        pass 
                        self.mESC()


                    elif alt15 == 2:
                        # kv.g:537:15: ~ ( '\\\\' | '\\n' | '\\'' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop15
                self.match(39)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ESC"
    def mESC(self, ):

        try:
            # kv.g:541:5: ( '\\\\' . )
            # kv.g:541:7: '\\\\' .
            pass 
            self.match(92)
            self.matchAny()




        finally:

            pass

    # $ANTLR end "ESC"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # kv.g:543:9: ( ( ( '\\u000C' )? ( '\\r' )? '\\n' ) )
            # kv.g:543:17: ( ( '\\u000C' )? ( '\\r' )? '\\n' )
            pass 
            # kv.g:543:17: ( ( '\\u000C' )? ( '\\r' )? '\\n' )
            # kv.g:543:18: ( '\\u000C' )? ( '\\r' )? '\\n'
            pass 
            # kv.g:543:18: ( '\\u000C' )?
            alt17 = 2
            LA17_0 = self.input.LA(1)

            if (LA17_0 == 12) :
                alt17 = 1
            if alt17 == 1:
                # kv.g:543:19: '\\u000C'
                pass 
                self.match(12)



            # kv.g:543:29: ( '\\r' )?
            alt18 = 2
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 13) :
                alt18 = 1
            if alt18 == 1:
                # kv.g:543:30: '\\r'
                pass 
                self.match(13)



            self.match(10)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # kv.g:544:5: ( ( ' ' | '\\t' )+ )
            # kv.g:544:9: ( ' ' | '\\t' )+
            pass 
            # kv.g:544:9: ( ' ' | '\\t' )+
            cnt19 = 0
            while True: #loop19
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == 9 or LA19_0 == 32) :
                    alt19 = 1


                if alt19 == 1:
                    # kv.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt19 >= 1:
                        break #loop19

                    eee = EarlyExitException(19, self.input)
                    raise eee

                cnt19 += 1
            #action start
            _channel=HIDDEN
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "NONE"
    def mNONE(self, ):

        try:
            _type = NONE
            _channel = DEFAULT_CHANNEL

            # kv.g:554:2: ( 'None' )
            # kv.g:554:6: 'None'
            pass 
            self.match("None")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NONE"



    # $ANTLR start "WNAME"
    def mWNAME(self, ):

        try:
            _type = WNAME
            _channel = DEFAULT_CHANNEL

            # kv.g:557:2: ( ( 'A' .. 'Z' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* )
            # kv.g:557:4: ( 'A' .. 'Z' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            pass 
            # kv.g:557:4: ( 'A' .. 'Z' )
            # kv.g:557:6: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)



            # kv.g:557:19: ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            while True: #loop20
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((48 <= LA20_0 <= 57) or (65 <= LA20_0 <= 90) or LA20_0 == 95 or (97 <= LA20_0 <= 122)) :
                    alt20 = 1


                if alt20 == 1:
                    # kv.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop20



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WNAME"



    # $ANTLR start "CANVAS"
    def mCANVAS(self, ):

        try:
            _type = CANVAS
            _channel = DEFAULT_CHANNEL

            # kv.g:560:2: ( 'canvas' | 'canvas.before' | 'canvas.after' )
            alt21 = 3
            alt21 = self.dfa21.predict(self.input)
            if alt21 == 1:
                # kv.g:560:4: 'canvas'
                pass 
                self.match("canvas")


            elif alt21 == 2:
                # kv.g:560:15: 'canvas.before'
                pass 
                self.match("canvas.before")


            elif alt21 == 3:
                # kv.g:560:33: 'canvas.after'
                pass 
                self.match("canvas.after")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CANVAS"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # kv.g:563:2: ( ( 'a' .. 'z' | '_' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* )
            # kv.g:563:4: ( 'a' .. 'z' | '_' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            pass 
            if self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # kv.g:563:25: ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            while True: #loop22
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if ((48 <= LA22_0 <= 57) or (65 <= LA22_0 <= 90) or LA22_0 == 95 or (97 <= LA22_0 <= 122)) :
                    alt22 = 1


                if alt22 == 1:
                    # kv.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop22



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "DIRECTIVETEXT"
    def mDIRECTIVETEXT(self, ):

        try:
            _type = DIRECTIVETEXT
            _channel = DEFAULT_CHANNEL

            # kv.g:566:2: ( HASH COLON (~ '\\n' )* )
            # kv.g:566:4: HASH COLON (~ '\\n' )*
            pass 
            self.mHASH()
            self.mCOLON()
            # kv.g:566:15: (~ '\\n' )*
            while True: #loop23
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((0 <= LA23_0 <= 9) or (11 <= LA23_0 <= 65535)) :
                    alt23 = 1


                if alt23 == 1:
                    # kv.g:566:16: ~ '\\n'
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop23



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIRECTIVETEXT"



    # $ANTLR start "COMMENTTEXT"
    def mCOMMENTTEXT(self, ):

        try:
            _type = COMMENTTEXT
            _channel = DEFAULT_CHANNEL

            # kv.g:569:2: ( HASH (~ '\\n' )* )
            # kv.g:569:4: HASH (~ '\\n' )*
            pass 
            self.mHASH()
            # kv.g:569:9: (~ '\\n' )*
            while True: #loop24
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((0 <= LA24_0 <= 9) or (11 <= LA24_0 <= 65535)) :
                    alt24 = 1


                if alt24 == 1:
                    # kv.g:569:10: ~ '\\n'
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop24



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENTTEXT"



    # $ANTLR start "HASH"
    def mHASH(self, ):

        try:
            # kv.g:572:6: ( '#' )
            # kv.g:572:17: '#'
            pass 
            self.match(35)




        finally:

            pass

    # $ANTLR end "HASH"



    def mTokens(self):
        # kv.g:1:8: ( T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | T__104 | T__105 | T__106 | T__107 | LPAREN | RPAREN | LBRACK | RBRACK | COLON | COMMA | SEMI | PLUS | MINUS | STAR | SLASH | VBAR | AMPER | LESS | GREATER | ASSIGN | PERCENT | BACKQUOTE | LCURLY | RCURLY | CIRCUMFLEX | TILDE | EQUAL | NOTEQUAL | ALT_NOTEQUAL | LESSEQUAL | LEFTSHIFT | GREATEREQUAL | RIGHTSHIFT | PLUSEQUAL | MINUSEQUAL | DOUBLESTAR | STAREQUAL | DOUBLESLASH | SLASHEQUAL | VBAREQUAL | PERCENTEQUAL | AMPEREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL | DOT | AT | AND | OR | NOT | FLOAT | LONGINT | INT | COMPLEX | STRING | NEWLINE | WS | NONE | WNAME | CANVAS | NAME | DIRECTIVETEXT | COMMENTTEXT )
        alt25 = 83
        alt25 = self.dfa25.predict(self.input)
        if alt25 == 1:
            # kv.g:1:10: T__86
            pass 
            self.mT__86()


        elif alt25 == 2:
            # kv.g:1:16: T__87
            pass 
            self.mT__87()


        elif alt25 == 3:
            # kv.g:1:22: T__88
            pass 
            self.mT__88()


        elif alt25 == 4:
            # kv.g:1:28: T__89
            pass 
            self.mT__89()


        elif alt25 == 5:
            # kv.g:1:34: T__90
            pass 
            self.mT__90()


        elif alt25 == 6:
            # kv.g:1:40: T__91
            pass 
            self.mT__91()


        elif alt25 == 7:
            # kv.g:1:46: T__92
            pass 
            self.mT__92()


        elif alt25 == 8:
            # kv.g:1:52: T__93
            pass 
            self.mT__93()


        elif alt25 == 9:
            # kv.g:1:58: T__94
            pass 
            self.mT__94()


        elif alt25 == 10:
            # kv.g:1:64: T__95
            pass 
            self.mT__95()


        elif alt25 == 11:
            # kv.g:1:70: T__96
            pass 
            self.mT__96()


        elif alt25 == 12:
            # kv.g:1:76: T__97
            pass 
            self.mT__97()


        elif alt25 == 13:
            # kv.g:1:82: T__98
            pass 
            self.mT__98()


        elif alt25 == 14:
            # kv.g:1:88: T__99
            pass 
            self.mT__99()


        elif alt25 == 15:
            # kv.g:1:94: T__100
            pass 
            self.mT__100()


        elif alt25 == 16:
            # kv.g:1:101: T__101
            pass 
            self.mT__101()


        elif alt25 == 17:
            # kv.g:1:108: T__102
            pass 
            self.mT__102()


        elif alt25 == 18:
            # kv.g:1:115: T__103
            pass 
            self.mT__103()


        elif alt25 == 19:
            # kv.g:1:122: T__104
            pass 
            self.mT__104()


        elif alt25 == 20:
            # kv.g:1:129: T__105
            pass 
            self.mT__105()


        elif alt25 == 21:
            # kv.g:1:136: T__106
            pass 
            self.mT__106()


        elif alt25 == 22:
            # kv.g:1:143: T__107
            pass 
            self.mT__107()


        elif alt25 == 23:
            # kv.g:1:150: LPAREN
            pass 
            self.mLPAREN()


        elif alt25 == 24:
            # kv.g:1:157: RPAREN
            pass 
            self.mRPAREN()


        elif alt25 == 25:
            # kv.g:1:164: LBRACK
            pass 
            self.mLBRACK()


        elif alt25 == 26:
            # kv.g:1:171: RBRACK
            pass 
            self.mRBRACK()


        elif alt25 == 27:
            # kv.g:1:178: COLON
            pass 
            self.mCOLON()


        elif alt25 == 28:
            # kv.g:1:184: COMMA
            pass 
            self.mCOMMA()


        elif alt25 == 29:
            # kv.g:1:190: SEMI
            pass 
            self.mSEMI()


        elif alt25 == 30:
            # kv.g:1:195: PLUS
            pass 
            self.mPLUS()


        elif alt25 == 31:
            # kv.g:1:200: MINUS
            pass 
            self.mMINUS()


        elif alt25 == 32:
            # kv.g:1:206: STAR
            pass 
            self.mSTAR()


        elif alt25 == 33:
            # kv.g:1:211: SLASH
            pass 
            self.mSLASH()


        elif alt25 == 34:
            # kv.g:1:217: VBAR
            pass 
            self.mVBAR()


        elif alt25 == 35:
            # kv.g:1:222: AMPER
            pass 
            self.mAMPER()


        elif alt25 == 36:
            # kv.g:1:228: LESS
            pass 
            self.mLESS()


        elif alt25 == 37:
            # kv.g:1:233: GREATER
            pass 
            self.mGREATER()


        elif alt25 == 38:
            # kv.g:1:241: ASSIGN
            pass 
            self.mASSIGN()


        elif alt25 == 39:
            # kv.g:1:248: PERCENT
            pass 
            self.mPERCENT()


        elif alt25 == 40:
            # kv.g:1:256: BACKQUOTE
            pass 
            self.mBACKQUOTE()


        elif alt25 == 41:
            # kv.g:1:266: LCURLY
            pass 
            self.mLCURLY()


        elif alt25 == 42:
            # kv.g:1:273: RCURLY
            pass 
            self.mRCURLY()


        elif alt25 == 43:
            # kv.g:1:280: CIRCUMFLEX
            pass 
            self.mCIRCUMFLEX()


        elif alt25 == 44:
            # kv.g:1:291: TILDE
            pass 
            self.mTILDE()


        elif alt25 == 45:
            # kv.g:1:297: EQUAL
            pass 
            self.mEQUAL()


        elif alt25 == 46:
            # kv.g:1:303: NOTEQUAL
            pass 
            self.mNOTEQUAL()


        elif alt25 == 47:
            # kv.g:1:312: ALT_NOTEQUAL
            pass 
            self.mALT_NOTEQUAL()


        elif alt25 == 48:
            # kv.g:1:325: LESSEQUAL
            pass 
            self.mLESSEQUAL()


        elif alt25 == 49:
            # kv.g:1:335: LEFTSHIFT
            pass 
            self.mLEFTSHIFT()


        elif alt25 == 50:
            # kv.g:1:345: GREATEREQUAL
            pass 
            self.mGREATEREQUAL()


        elif alt25 == 51:
            # kv.g:1:358: RIGHTSHIFT
            pass 
            self.mRIGHTSHIFT()


        elif alt25 == 52:
            # kv.g:1:369: PLUSEQUAL
            pass 
            self.mPLUSEQUAL()


        elif alt25 == 53:
            # kv.g:1:379: MINUSEQUAL
            pass 
            self.mMINUSEQUAL()


        elif alt25 == 54:
            # kv.g:1:390: DOUBLESTAR
            pass 
            self.mDOUBLESTAR()


        elif alt25 == 55:
            # kv.g:1:401: STAREQUAL
            pass 
            self.mSTAREQUAL()


        elif alt25 == 56:
            # kv.g:1:411: DOUBLESLASH
            pass 
            self.mDOUBLESLASH()


        elif alt25 == 57:
            # kv.g:1:423: SLASHEQUAL
            pass 
            self.mSLASHEQUAL()


        elif alt25 == 58:
            # kv.g:1:434: VBAREQUAL
            pass 
            self.mVBAREQUAL()


        elif alt25 == 59:
            # kv.g:1:444: PERCENTEQUAL
            pass 
            self.mPERCENTEQUAL()


        elif alt25 == 60:
            # kv.g:1:457: AMPEREQUAL
            pass 
            self.mAMPEREQUAL()


        elif alt25 == 61:
            # kv.g:1:468: CIRCUMFLEXEQUAL
            pass 
            self.mCIRCUMFLEXEQUAL()


        elif alt25 == 62:
            # kv.g:1:484: LEFTSHIFTEQUAL
            pass 
            self.mLEFTSHIFTEQUAL()


        elif alt25 == 63:
            # kv.g:1:499: RIGHTSHIFTEQUAL
            pass 
            self.mRIGHTSHIFTEQUAL()


        elif alt25 == 64:
            # kv.g:1:515: DOUBLESTAREQUAL
            pass 
            self.mDOUBLESTAREQUAL()


        elif alt25 == 65:
            # kv.g:1:531: DOUBLESLASHEQUAL
            pass 
            self.mDOUBLESLASHEQUAL()


        elif alt25 == 66:
            # kv.g:1:548: DOT
            pass 
            self.mDOT()


        elif alt25 == 67:
            # kv.g:1:552: AT
            pass 
            self.mAT()


        elif alt25 == 68:
            # kv.g:1:555: AND
            pass 
            self.mAND()


        elif alt25 == 69:
            # kv.g:1:559: OR
            pass 
            self.mOR()


        elif alt25 == 70:
            # kv.g:1:562: NOT
            pass 
            self.mNOT()


        elif alt25 == 71:
            # kv.g:1:566: FLOAT
            pass 
            self.mFLOAT()


        elif alt25 == 72:
            # kv.g:1:572: LONGINT
            pass 
            self.mLONGINT()


        elif alt25 == 73:
            # kv.g:1:580: INT
            pass 
            self.mINT()


        elif alt25 == 74:
            # kv.g:1:584: COMPLEX
            pass 
            self.mCOMPLEX()


        elif alt25 == 75:
            # kv.g:1:592: STRING
            pass 
            self.mSTRING()


        elif alt25 == 76:
            # kv.g:1:599: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt25 == 77:
            # kv.g:1:607: WS
            pass 
            self.mWS()


        elif alt25 == 78:
            # kv.g:1:610: NONE
            pass 
            self.mNONE()


        elif alt25 == 79:
            # kv.g:1:615: WNAME
            pass 
            self.mWNAME()


        elif alt25 == 80:
            # kv.g:1:621: CANVAS
            pass 
            self.mCANVAS()


        elif alt25 == 81:
            # kv.g:1:628: NAME
            pass 
            self.mNAME()


        elif alt25 == 82:
            # kv.g:1:633: DIRECTIVETEXT
            pass 
            self.mDIRECTIVETEXT()


        elif alt25 == 83:
            # kv.g:1:647: COMMENTTEXT
            pass 
            self.mCOMMENTTEXT()







    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\3\uffff\1\4\2\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\56\1\uffff\1\56\1\105\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\71\1\uffff\2\145\2\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\1\uffff\1\1\2\uffff\1\3\1\2"
        )

    DFA5_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\1\1\uffff\12\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\2\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u"\1\5\37\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\3\56\2\uffff\2\56"
        )

    DFA11_max = DFA.unpack(
        u"\1\71\1\170\1\152\2\uffff\2\152"
        )

    DFA11_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1\2\uffff"
        )

    DFA11_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\1\3\1\uffff\1\1\11\2"),
        DFA.unpack(u"\1\3\1\uffff\12\5\13\uffff\1\3\4\uffff\1\4\15\uffff"
        u"\1\4\14\uffff\1\3\4\uffff\1\4\15\uffff\1\4"),
        DFA.unpack(u"\1\3\1\uffff\12\6\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\5\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4"),
        DFA.unpack(u"\1\3\1\uffff\12\6\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\6\uffff\1\10\4\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\143\1\141\1\156\1\166\1\141\1\163\1\56\1\141\3\uffff"
        )

    DFA21_max = DFA.unpack(
        u"\1\143\1\141\1\156\1\166\1\141\1\163\1\56\1\142\3\uffff"
        )

    DFA21_accept = DFA.unpack(
        u"\10\uffff\1\1\1\2\1\3"
        )

    DFA21_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA21_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\12\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        pass


    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\1\uffff\15\61\7\uffff\1\111\1\113\1\116\1\121\1\123\1\125\1\131"
        u"\1\134\1\136\1\140\3\uffff\1\142\2\uffff\1\144\1\uffff\2\61\2\150"
        u"\1\61\3\uffff\1\60\2\uffff\1\161\11\61\1\176\1\177\1\u0080\1\u0082"
        u"\10\61\4\uffff\1\u008c\2\uffff\1\u008e\10\uffff\1\u0090\2\uffff"
        u"\1\u0092\7\uffff\1\u0093\1\uffff\1\u0095\1\61\2\uffff\1\u0093\1"
        u"\150\3\uffff\1\150\1\61\1\60\1\uffff\1\u009d\2\61\1\u00a1\10\61"
        u"\3\uffff\1\61\1\uffff\1\u00ab\2\61\1\u00ae\1\61\1\u00b0\2\61\13"
        u"\uffff\1\u00b5\1\150\1\u0093\2\uffff\1\u0093\1\60\1\uffff\1\u009d"
        u"\1\61\1\u00bb\1\uffff\4\61\1\u00c0\1\61\1\u00c2\1\u00c3\1\61\1"
        u"\uffff\1\61\1\u00c6\1\uffff\1\61\1\uffff\2\61\1\uffff\1\u0093\3"
        u"\uffff\1\u0093\1\u00cc\1\u00cd\1\uffff\1\u00ce\2\61\1\u00d1\1\uffff"
        u"\1\61\2\uffff\1\61\1\u00d4\1\uffff\2\61\1\u00d7\1\uffff\1\u0093"
        u"\3\uffff\1\61\1\u00d9\1\uffff\1\u00da\1\u00db\1\uffff\1\61\1\u00dd"
        u"\1\uffff\1\61\3\uffff\1\u00df\1\uffff\1\u00e0\2\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\u00e1\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\11\1\141\1\145\1\162\1\141\1\42\1\154\1\146\1\156\1\150\1\151"
        u"\1\162\1\141\1\151\7\uffff\2\75\1\52\1\57\2\75\1\74\3\75\3\uffff"
        u"\1\75\2\uffff\1\60\1\uffff\1\162\1\157\2\56\1\42\3\uffff\1\157"
        u"\2\uffff\1\72\1\151\1\163\1\154\1\145\2\156\1\151\1\143\1\151\4"
        u"\60\1\144\1\151\1\164\1\162\1\156\1\171\1\155\1\145\4\uffff\1\75"
        u"\2\uffff\1\75\10\uffff\1\75\2\uffff\1\75\7\uffff\1\60\1\uffff\1"
        u"\60\1\164\1\60\1\uffff\1\60\1\56\1\53\2\uffff\1\56\1\42\1\156\1"
        u"\uffff\1\0\1\156\1\163\1\60\1\141\1\164\1\166\1\163\1\143\2\145"
        u"\1\146\3\uffff\1\145\1\uffff\1\60\1\154\1\150\1\60\1\141\1\60\1"
        u"\142\1\154\11\uffff\1\53\1\uffff\3\60\1\53\2\60\1\145\1\uffff\1"
        u"\0\1\164\1\60\1\uffff\1\153\1\151\1\141\1\145\1\60\1\160\2\60\1"
        u"\162\1\uffff\1\145\1\60\1\uffff\1\154\1\uffff\2\144\2\60\1\uffff"
        u"\1\53\4\60\1\uffff\1\60\1\156\1\163\1\60\1\uffff\1\164\2\uffff"
        u"\1\164\1\60\1\uffff\1\154\1\141\3\60\3\uffff\1\165\1\60\1\uffff"
        u"\2\60\1\uffff\1\171\1\60\1\uffff\1\145\3\uffff\1\60\1\uffff\1\60"
        u"\2\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\176\1\162\1\145\1\162\1\157\1\141\1\170\2\163\1\151\1\157\1"
        u"\162\1\141\1\151\7\uffff\6\75\2\76\2\75\3\uffff\1\75\2\uffff\1"
        u"\71\1\uffff\1\162\1\157\1\170\1\154\1\162\3\uffff\1\157\2\uffff"
        u"\1\72\1\151\1\163\1\154\1\145\2\156\1\151\1\145\1\163\4\172\1\144"
        u"\1\151\1\164\1\162\1\156\1\171\1\155\1\145\4\uffff\1\75\2\uffff"
        u"\1\75\10\uffff\1\75\2\uffff\1\75\7\uffff\1\152\1\uffff\1\172\1"
        u"\164\1\146\1\uffff\1\152\1\154\1\71\2\uffff\1\154\1\47\1\156\1"
        u"\uffff\1\uffff\1\156\1\163\1\172\1\141\1\164\1\166\1\163\1\143"
        u"\2\145\1\146\3\uffff\1\145\1\uffff\1\172\1\154\1\150\1\172\1\141"
        u"\1\172\1\142\1\154\11\uffff\1\71\1\uffff\1\172\1\154\1\152\2\71"
        u"\1\152\1\145\1\uffff\1\uffff\1\164\1\172\1\uffff\1\153\1\151\1"
        u"\141\1\145\1\172\1\160\2\172\1\162\1\uffff\1\145\1\172\1\uffff"
        u"\1\154\1\uffff\2\144\1\71\1\152\1\uffff\2\71\1\152\2\172\1\uffff"
        u"\1\172\1\156\1\163\1\172\1\uffff\1\164\2\uffff\1\164\1\172\1\uffff"
        u"\1\154\1\141\1\172\1\71\1\152\3\uffff\1\165\1\172\1\uffff\2\172"
        u"\1\uffff\1\171\1\172\1\uffff\1\145\3\uffff\1\172\1\uffff\1\172"
        u"\2\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\16\uffff\1\27\1\30\1\31\1\32\1\33\1\34\1\35\12\uffff\1\50\1\51"
        u"\1\52\1\uffff\1\54\1\56\1\uffff\1\103\5\uffff\1\113\1\114\1\115"
        u"\1\uffff\1\117\1\121\26\uffff\1\64\1\36\1\65\1\37\1\uffff\1\67"
        u"\1\40\1\uffff\1\71\1\41\1\72\1\42\1\74\1\43\1\57\1\60\1\uffff\1"
        u"\44\1\62\1\uffff\1\45\1\55\1\46\1\73\1\47\1\75\1\53\1\uffff\1\102"
        u"\3\uffff\1\111\3\uffff\1\110\1\112\3\uffff\1\123\14\uffff\1\10"
        u"\1\12\1\24\1\uffff\1\22\10\uffff\1\100\1\66\1\101\1\70\1\76\1\61"
        u"\1\77\1\63\1\107\1\uffff\1\105\7\uffff\1\122\3\uffff\1\2\11\uffff"
        u"\1\104\2\uffff\1\16\1\uffff\1\17\4\uffff\1\106\5\uffff\1\3\4\uffff"
        u"\1\7\1\uffff\1\13\1\14\2\uffff\1\21\5\uffff\1\116\1\1\1\4\2\uffff"
        u"\1\6\2\uffff\1\15\2\uffff\1\26\1\uffff\1\120\1\23\1\11\1\uffff"
        u"\1\25\1\uffff\1\20\1\5"
        )

    DFA25_special = DFA.unpack(
        u"\162\uffff\1\0\53\uffff\1\1\102\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\1\56\1\55\1\uffff\2\55\22\uffff\1\56\1\44\1\54\1\62"
        u"\1\uffff\1\36\1\32\1\54\1\16\1\17\1\27\1\25\1\23\1\26\1\45\1\30"
        u"\1\51\11\52\1\22\1\24\1\33\1\35\1\34\1\uffff\1\46\15\60\1\57\14"
        u"\60\1\20\1\uffff\1\21\1\42\1\61\1\37\1\10\1\3\1\4\1\2\1\6\1\12"
        u"\2\61\1\7\2\61\1\14\1\61\1\50\1\47\1\1\1\61\1\5\1\61\1\13\1\53"
        u"\1\61\1\11\1\61\1\15\1\61\1\40\1\31\1\41\1\43"),
        DFA.unpack(u"\1\64\20\uffff\1\63"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\70\15\uffff\1\67"),
        DFA.unpack(u"\1\54\4\uffff\1\54\71\uffff\1\71"),
        DFA.unpack(u"\1\73\13\uffff\1\72"),
        DFA.unpack(u"\1\75\7\uffff\1\74\4\uffff\1\76"),
        DFA.unpack(u"\1\100\4\uffff\1\77"),
        DFA.unpack(u"\1\101\1\102"),
        DFA.unpack(u"\1\104\5\uffff\1\103"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\114\22\uffff\1\115"),
        DFA.unpack(u"\1\117\15\uffff\1\120"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\130\1\127\1\126"),
        DFA.unpack(u"\1\132\1\133"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\143"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\151\1\uffff\12\152\13\uffff\1\153\4\uffff\1\155"
        u"\1\uffff\1\154\13\uffff\1\147\14\uffff\1\153\4\uffff\1\155\1\uffff"
        u"\1\154\13\uffff\1\147"),
        DFA.unpack(u"\1\151\1\uffff\12\156\13\uffff\1\153\4\uffff\1\155"
        u"\1\uffff\1\154\30\uffff\1\153\4\uffff\1\155\1\uffff\1\154"),
        DFA.unpack(u"\1\54\4\uffff\1\54\112\uffff\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\173\1\uffff\1\172"),
        DFA.unpack(u"\1\175\11\uffff\1\174"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\22\61\1\u0081"
        u"\7\61"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\143\13\uffff\1\u0094\4\uffff\1\155\32\uffff\1\u0094"
        u"\4\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\12\u0097\7\uffff\6\u0097\32\uffff\6\u0097"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u0098\13\uffff\1\u0099\4\uffff\1\155\32\uffff\1"
        u"\u0099\4\uffff\1\155"),
        DFA.unpack(u"\1\151\1\uffff\12\152\13\uffff\1\153\4\uffff\1\155"
        u"\1\uffff\1\154\30\uffff\1\153\4\uffff\1\155\1\uffff\1\154"),
        DFA.unpack(u"\1\u009a\1\uffff\1\u009a\2\uffff\12\u009b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\151\1\uffff\12\156\13\uffff\1\153\4\uffff\1\155"
        u"\1\uffff\1\154\30\uffff\1\153\4\uffff\1\155\1\uffff\1\154"),
        DFA.unpack(u"\1\54\4\uffff\1\54"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u009e\1\uffff\ufff5\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b3\1\uffff\1\u00b3\2\uffff\12\u00b4"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\u0097\7\uffff\6\u0097\3\uffff\1\155\1\uffff\1\154"
        u"\24\uffff\6\u0097\3\uffff\1\155\1\uffff\1\154"),
        DFA.unpack(u"\12\u0098\13\uffff\1\u00b6\4\uffff\1\155\32\uffff\1"
        u"\u00b6\4\uffff\1\155"),
        DFA.unpack(u"\1\u00b7\1\uffff\1\u00b7\2\uffff\12\u00b8"),
        DFA.unpack(u"\12\u009b"),
        DFA.unpack(u"\12\u009b\20\uffff\1\155\37\uffff\1\155"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u009e\1\uffff\ufff5\u009e"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c5"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\12\u00b4"),
        DFA.unpack(u"\12\u00b4\20\uffff\1\155\37\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ca\1\uffff\1\u00ca\2\uffff\12\u00cb"),
        DFA.unpack(u"\12\u00b8"),
        DFA.unpack(u"\12\u00b8\20\uffff\1\155\37\uffff\1\155"),
        DFA.unpack(u"\12\60\7\uffff\32\60\4\uffff\1\60\1\uffff\32\60"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\u00cb"),
        DFA.unpack(u"\12\u00cb\20\uffff\1\155\37\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\61\7\uffff\32\61\4\uffff\1\61\1\uffff\32\61"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #25

    class DFA25(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA25_114 = input.LA(1)

                s = -1
                if ((0 <= LA25_114 <= 9) or (11 <= LA25_114 <= 65535)):
                    s = 158

                else:
                    s = 157

                if s >= 0:
                    return s
            elif s == 1: 
                LA25_158 = input.LA(1)

                s = -1
                if ((0 <= LA25_158 <= 9) or (11 <= LA25_158 <= 65535)):
                    s = 158

                else:
                    s = 157

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 25, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(kvLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
