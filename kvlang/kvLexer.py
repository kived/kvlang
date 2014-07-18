# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 kv.g 2014-07-17 21:34:08

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INSTRUCTION=18
BACKQUOTE=74
SLASHEQUAL=42
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
T__92=92
NAME=31
GREATER=55
T__90=90
DOUBLESTAREQUAL=49
LESS=54
TEMPLATERULE=13
COMMENT=7
RBRACK=71
LCURLY=72
INT=75
RIGHTSHIFT=65
T__85=85
T__87=87
T__86=86
T__89=89
T__88=88
DOUBLESLASHEQUAL=50
WS=32
PROPERTY=10
VBAREQUAL=45
OR=51
CLASSRULE=12
RESETRULE=19
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
ALT_NOTEQUAL=59
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





    # $ANTLR start "T__85"
    def mT__85(self, ):

        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # kv.g:15:7: ( 'raise' )
            # kv.g:15:9: 'raise'
            pass 
            self.match("raise")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):

        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # kv.g:16:7: ( 'if' )
            # kv.g:16:9: 'if'
            pass 
            self.match("if")



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

            # kv.g:17:7: ( 'else' )
            # kv.g:17:9: 'else'
            pass 
            self.match("else")



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

            # kv.g:18:7: ( 'in' )
            # kv.g:18:9: 'in'
            pass 
            self.match("in")



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

            # kv.g:19:7: ( 'is' )
            # kv.g:19:9: 'is'
            pass 
            self.match("is")



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

            # kv.g:20:7: ( 'lambda' )
            # kv.g:20:9: 'lambda'
            pass 
            self.match("lambda")



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

            # kv.g:21:7: ( 'for' )
            # kv.g:21:9: 'for'
            pass 
            self.match("for")



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

            # kv.g:22:7: ( 'yield' )
            # kv.g:22:9: 'yield'
            pass 
            self.match("yield")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__92"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # kv.g:378:8: ( '(' )
            # kv.g:378:11: '('
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

            # kv.g:379:8: ( ')' )
            # kv.g:379:11: ')'
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

            # kv.g:380:8: ( '[' )
            # kv.g:380:11: '['
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

            # kv.g:381:8: ( ']' )
            # kv.g:381:11: ']'
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

            # kv.g:382:7: ( ':' )
            # kv.g:382:11: ':'
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

            # kv.g:383:7: ( ',' )
            # kv.g:383:11: ','
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

            # kv.g:384:6: ( ';' )
            # kv.g:384:10: ';'
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

            # kv.g:385:6: ( '+' )
            # kv.g:385:10: '+'
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

            # kv.g:386:7: ( '-' )
            # kv.g:386:11: '-'
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

            # kv.g:387:6: ( '*' )
            # kv.g:387:10: '*'
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

            # kv.g:388:7: ( '/' )
            # kv.g:388:11: '/'
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

            # kv.g:389:6: ( '|' )
            # kv.g:389:10: '|'
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

            # kv.g:390:7: ( '&' )
            # kv.g:390:11: '&'
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

            # kv.g:391:6: ( '<' )
            # kv.g:391:10: '<'
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

            # kv.g:392:9: ( '>' )
            # kv.g:392:12: '>'
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

            # kv.g:393:8: ( '=' )
            # kv.g:393:11: '='
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

            # kv.g:394:9: ( '%' )
            # kv.g:394:12: '%'
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

            # kv.g:395:11: ( '`' )
            # kv.g:395:14: '`'
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

            # kv.g:396:8: ( '{' )
            # kv.g:396:11: '{'
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

            # kv.g:397:8: ( '}' )
            # kv.g:397:11: '}'
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

            # kv.g:398:12: ( '^' )
            # kv.g:398:14: '^'
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

            # kv.g:399:7: ( '~' )
            # kv.g:399:11: '~'
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

            # kv.g:400:7: ( '==' )
            # kv.g:400:11: '=='
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

            # kv.g:401:10: ( '!=' )
            # kv.g:401:13: '!='
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

            # kv.g:402:14: ( '<>' )
            # kv.g:402:16: '<>'
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

            # kv.g:403:11: ( '<=' )
            # kv.g:403:14: '<='
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

            # kv.g:404:11: ( '<<' )
            # kv.g:404:14: '<<'
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

            # kv.g:405:14: ( '>=' )
            # kv.g:405:16: '>='
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

            # kv.g:406:12: ( '>>' )
            # kv.g:406:14: '>>'
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

            # kv.g:407:11: ( '+=' )
            # kv.g:407:14: '+='
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

            # kv.g:408:12: ( '-=' )
            # kv.g:408:14: '-='
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

            # kv.g:409:12: ( '**' )
            # kv.g:409:14: '**'
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

            # kv.g:410:11: ( '*=' )
            # kv.g:410:14: '*='
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

            # kv.g:411:13: ( '//' )
            # kv.g:411:15: '//'
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

            # kv.g:412:12: ( '/=' )
            # kv.g:412:14: '/='
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

            # kv.g:413:11: ( '|=' )
            # kv.g:413:14: '|='
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

            # kv.g:414:14: ( '%=' )
            # kv.g:414:16: '%='
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

            # kv.g:415:12: ( '&=' )
            # kv.g:415:14: '&='
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

            # kv.g:416:17: ( '^=' )
            # kv.g:416:19: '^='
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

            # kv.g:417:16: ( '<<=' )
            # kv.g:417:18: '<<='
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

            # kv.g:418:17: ( '>>=' )
            # kv.g:418:19: '>>='
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

            # kv.g:419:17: ( '**=' )
            # kv.g:419:19: '**='
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

            # kv.g:420:18: ( '//=' )
            # kv.g:420:20: '//='
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

            # kv.g:421:5: ( '.' )
            # kv.g:421:9: '.'
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

            # kv.g:422:4: ( '@' )
            # kv.g:422:8: '@'
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

            # kv.g:423:5: ( 'and' )
            # kv.g:423:9: 'and'
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

            # kv.g:424:4: ( 'or' )
            # kv.g:424:8: 'or'
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

            # kv.g:425:5: ( 'not' )
            # kv.g:425:9: 'not'
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

            # kv.g:428:2: ( '.' DIGITS ( Exponent )? | DIGITS '.' Exponent | DIGITS ( '.' ( DIGITS ( Exponent )? )? | Exponent ) )
            alt5 = 3
            alt5 = self.dfa5.predict(self.input)
            if alt5 == 1:
                # kv.g:428:4: '.' DIGITS ( Exponent )?
                pass 
                self.match(46)
                self.mDIGITS()
                # kv.g:428:15: ( Exponent )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 69 or LA1_0 == 101) :
                    alt1 = 1
                if alt1 == 1:
                    # kv.g:428:16: Exponent
                    pass 
                    self.mExponent()





            elif alt5 == 2:
                # kv.g:429:4: DIGITS '.' Exponent
                pass 
                self.mDIGITS()
                self.match(46)
                self.mExponent()


            elif alt5 == 3:
                # kv.g:430:4: DIGITS ( '.' ( DIGITS ( Exponent )? )? | Exponent )
                pass 
                self.mDIGITS()
                # kv.g:430:11: ( '.' ( DIGITS ( Exponent )? )? | Exponent )
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
                    # kv.g:430:12: '.' ( DIGITS ( Exponent )? )?
                    pass 
                    self.match(46)
                    # kv.g:430:16: ( DIGITS ( Exponent )? )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1
                    if alt3 == 1:
                        # kv.g:430:17: DIGITS ( Exponent )?
                        pass 
                        self.mDIGITS()
                        # kv.g:430:24: ( Exponent )?
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 69 or LA2_0 == 101) :
                            alt2 = 1
                        if alt2 == 1:
                            # kv.g:430:25: Exponent
                            pass 
                            self.mExponent()








                elif alt4 == 2:
                    # kv.g:430:40: Exponent
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

            # kv.g:433:2: ( INT ( 'l' | 'L' ) )
            # kv.g:433:4: INT ( 'l' | 'L' )
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
            # kv.g:437:2: ( ( 'e' | 'E' ) ( '+' | '-' )? DIGITS )
            # kv.g:437:4: ( 'e' | 'E' ) ( '+' | '-' )? DIGITS
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # kv.g:437:16: ( '+' | '-' )?
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

            # kv.g:439:5: ( '0' ( 'x' | 'X' ) ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+ | '0' ( DIGITS )* | '1' .. '9' ( DIGITS )* )
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
                # kv.g:439:7: '0' ( 'x' | 'X' ) ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
                pass 
                self.match(48)
                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # kv.g:439:23: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
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
                # kv.g:440:4: '0' ( DIGITS )*
                pass 
                self.match(48)
                # kv.g:440:8: ( DIGITS )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # kv.g:440:8: DIGITS
                        pass 
                        self.mDIGITS()


                    else:
                        break #loop8


            elif alt10 == 3:
                # kv.g:441:4: '1' .. '9' ( DIGITS )*
                pass 
                self.matchRange(49, 57)
                # kv.g:441:15: ( DIGITS )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # kv.g:441:15: DIGITS
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

            # kv.g:444:2: ( INT ( 'j' | 'J' ) | FLOAT ( 'j' | 'J' ) )
            alt11 = 2
            alt11 = self.dfa11.predict(self.input)
            if alt11 == 1:
                # kv.g:444:4: INT ( 'j' | 'J' )
                pass 
                self.mINT()
                if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt11 == 2:
                # kv.g:445:4: FLOAT ( 'j' | 'J' )
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
            # kv.g:449:2: ( ( '0' .. '9' )+ )
            # kv.g:449:4: ( '0' .. '9' )+
            pass 
            # kv.g:449:4: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)) :
                    alt12 = 1


                if alt12 == 1:
                    # kv.g:449:6: '0' .. '9'
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

            # kv.g:452:2: ( ( 'r' | 'u' | 'ur' )? ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' ) )
            # kv.g:452:4: ( 'r' | 'u' | 'ur' )? ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
            pass 
            # kv.g:452:4: ( 'r' | 'u' | 'ur' )?
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
                # kv.g:452:5: 'r'
                pass 
                self.match(114)


            elif alt13 == 2:
                # kv.g:452:11: 'u'
                pass 
                self.match(117)


            elif alt13 == 3:
                # kv.g:452:17: 'ur'
                pass 
                self.match("ur")



            # kv.g:453:3: ( '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
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
                # kv.g:453:5: '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"'
                pass 
                self.match(34)
                # kv.g:453:9: ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )*
                while True: #loop14
                    alt14 = 3
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 92) :
                        alt14 = 1
                    elif ((0 <= LA14_0 <= 9) or (11 <= LA14_0 <= 33) or (35 <= LA14_0 <= 91) or (93 <= LA14_0 <= 65535)) :
                        alt14 = 2


                    if alt14 == 1:
                        # kv.g:453:10: ESC
                        pass 
                        self.mESC()


                    elif alt14 == 2:
                        # kv.g:453:14: ~ ( '\\\\' | '\\n' | '\"' )
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
                # kv.g:454:5: '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\''
                pass 
                self.match(39)
                # kv.g:454:10: ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )*
                while True: #loop15
                    alt15 = 3
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 92) :
                        alt15 = 1
                    elif ((0 <= LA15_0 <= 9) or (11 <= LA15_0 <= 38) or (40 <= LA15_0 <= 91) or (93 <= LA15_0 <= 65535)) :
                        alt15 = 2


                    if alt15 == 1:
                        # kv.g:454:11: ESC
                        pass 
                        self.mESC()


                    elif alt15 == 2:
                        # kv.g:454:15: ~ ( '\\\\' | '\\n' | '\\'' )
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
            # kv.g:458:5: ( '\\\\' . )
            # kv.g:458:7: '\\\\' .
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

            # kv.g:460:9: ( ( ( '\\u000C' )? ( '\\r' )? '\\n' ) )
            # kv.g:460:17: ( ( '\\u000C' )? ( '\\r' )? '\\n' )
            pass 
            # kv.g:460:17: ( ( '\\u000C' )? ( '\\r' )? '\\n' )
            # kv.g:460:18: ( '\\u000C' )? ( '\\r' )? '\\n'
            pass 
            # kv.g:460:18: ( '\\u000C' )?
            alt17 = 2
            LA17_0 = self.input.LA(1)

            if (LA17_0 == 12) :
                alt17 = 1
            if alt17 == 1:
                # kv.g:460:19: '\\u000C'
                pass 
                self.match(12)



            # kv.g:460:29: ( '\\r' )?
            alt18 = 2
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 13) :
                alt18 = 1
            if alt18 == 1:
                # kv.g:460:30: '\\r'
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

            # kv.g:461:5: ( ( ' ' | '\\t' )+ )
            # kv.g:461:9: ( ' ' | '\\t' )+
            pass 
            # kv.g:461:9: ( ' ' | '\\t' )+
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



    # $ANTLR start "WNAME"
    def mWNAME(self, ):

        try:
            _type = WNAME
            _channel = DEFAULT_CHANNEL

            # kv.g:471:2: ( ( 'A' .. 'Z' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* )
            # kv.g:471:4: ( 'A' .. 'Z' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            pass 
            # kv.g:471:4: ( 'A' .. 'Z' )
            # kv.g:471:6: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)



            # kv.g:471:19: ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
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

            # kv.g:474:2: ( 'canvas' | 'canvas.before' | 'canvas.after' )
            alt21 = 3
            alt21 = self.dfa21.predict(self.input)
            if alt21 == 1:
                # kv.g:474:4: 'canvas'
                pass 
                self.match("canvas")


            elif alt21 == 2:
                # kv.g:474:15: 'canvas.before'
                pass 
                self.match("canvas.before")


            elif alt21 == 3:
                # kv.g:474:33: 'canvas.after'
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

            # kv.g:477:2: ( ( 'a' .. 'z' | '_' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )* )
            # kv.g:477:4: ( 'a' .. 'z' | '_' ) ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
            pass 
            if self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # kv.g:477:25: ( 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' )*
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

            # kv.g:480:2: ( HASH COLON (~ '\\n' )* )
            # kv.g:480:4: HASH COLON (~ '\\n' )*
            pass 
            self.mHASH()
            self.mCOLON()
            # kv.g:480:15: (~ '\\n' )*
            while True: #loop23
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((0 <= LA23_0 <= 9) or (11 <= LA23_0 <= 65535)) :
                    alt23 = 1


                if alt23 == 1:
                    # kv.g:480:16: ~ '\\n'
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

            # kv.g:483:2: ( HASH (~ '\\n' )* )
            # kv.g:483:4: HASH (~ '\\n' )*
            pass 
            self.mHASH()
            # kv.g:483:9: (~ '\\n' )*
            while True: #loop24
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((0 <= LA24_0 <= 9) or (11 <= LA24_0 <= 65535)) :
                    alt24 = 1


                if alt24 == 1:
                    # kv.g:483:10: ~ '\\n'
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
            # kv.g:486:6: ( '#' )
            # kv.g:486:17: '#'
            pass 
            self.match(35)




        finally:

            pass

    # $ANTLR end "HASH"



    def mTokens(self):
        # kv.g:1:8: ( T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | LPAREN | RPAREN | LBRACK | RBRACK | COLON | COMMA | SEMI | PLUS | MINUS | STAR | SLASH | VBAR | AMPER | LESS | GREATER | ASSIGN | PERCENT | BACKQUOTE | LCURLY | RCURLY | CIRCUMFLEX | TILDE | EQUAL | NOTEQUAL | ALT_NOTEQUAL | LESSEQUAL | LEFTSHIFT | GREATEREQUAL | RIGHTSHIFT | PLUSEQUAL | MINUSEQUAL | DOUBLESTAR | STAREQUAL | DOUBLESLASH | SLASHEQUAL | VBAREQUAL | PERCENTEQUAL | AMPEREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL | DOT | AT | AND | OR | NOT | FLOAT | LONGINT | INT | COMPLEX | STRING | NEWLINE | WS | WNAME | CANVAS | NAME | DIRECTIVETEXT | COMMENTTEXT )
        alt25 = 68
        alt25 = self.dfa25.predict(self.input)
        if alt25 == 1:
            # kv.g:1:10: T__85
            pass 
            self.mT__85()


        elif alt25 == 2:
            # kv.g:1:16: T__86
            pass 
            self.mT__86()


        elif alt25 == 3:
            # kv.g:1:22: T__87
            pass 
            self.mT__87()


        elif alt25 == 4:
            # kv.g:1:28: T__88
            pass 
            self.mT__88()


        elif alt25 == 5:
            # kv.g:1:34: T__89
            pass 
            self.mT__89()


        elif alt25 == 6:
            # kv.g:1:40: T__90
            pass 
            self.mT__90()


        elif alt25 == 7:
            # kv.g:1:46: T__91
            pass 
            self.mT__91()


        elif alt25 == 8:
            # kv.g:1:52: T__92
            pass 
            self.mT__92()


        elif alt25 == 9:
            # kv.g:1:58: LPAREN
            pass 
            self.mLPAREN()


        elif alt25 == 10:
            # kv.g:1:65: RPAREN
            pass 
            self.mRPAREN()


        elif alt25 == 11:
            # kv.g:1:72: LBRACK
            pass 
            self.mLBRACK()


        elif alt25 == 12:
            # kv.g:1:79: RBRACK
            pass 
            self.mRBRACK()


        elif alt25 == 13:
            # kv.g:1:86: COLON
            pass 
            self.mCOLON()


        elif alt25 == 14:
            # kv.g:1:92: COMMA
            pass 
            self.mCOMMA()


        elif alt25 == 15:
            # kv.g:1:98: SEMI
            pass 
            self.mSEMI()


        elif alt25 == 16:
            # kv.g:1:103: PLUS
            pass 
            self.mPLUS()


        elif alt25 == 17:
            # kv.g:1:108: MINUS
            pass 
            self.mMINUS()


        elif alt25 == 18:
            # kv.g:1:114: STAR
            pass 
            self.mSTAR()


        elif alt25 == 19:
            # kv.g:1:119: SLASH
            pass 
            self.mSLASH()


        elif alt25 == 20:
            # kv.g:1:125: VBAR
            pass 
            self.mVBAR()


        elif alt25 == 21:
            # kv.g:1:130: AMPER
            pass 
            self.mAMPER()


        elif alt25 == 22:
            # kv.g:1:136: LESS
            pass 
            self.mLESS()


        elif alt25 == 23:
            # kv.g:1:141: GREATER
            pass 
            self.mGREATER()


        elif alt25 == 24:
            # kv.g:1:149: ASSIGN
            pass 
            self.mASSIGN()


        elif alt25 == 25:
            # kv.g:1:156: PERCENT
            pass 
            self.mPERCENT()


        elif alt25 == 26:
            # kv.g:1:164: BACKQUOTE
            pass 
            self.mBACKQUOTE()


        elif alt25 == 27:
            # kv.g:1:174: LCURLY
            pass 
            self.mLCURLY()


        elif alt25 == 28:
            # kv.g:1:181: RCURLY
            pass 
            self.mRCURLY()


        elif alt25 == 29:
            # kv.g:1:188: CIRCUMFLEX
            pass 
            self.mCIRCUMFLEX()


        elif alt25 == 30:
            # kv.g:1:199: TILDE
            pass 
            self.mTILDE()


        elif alt25 == 31:
            # kv.g:1:205: EQUAL
            pass 
            self.mEQUAL()


        elif alt25 == 32:
            # kv.g:1:211: NOTEQUAL
            pass 
            self.mNOTEQUAL()


        elif alt25 == 33:
            # kv.g:1:220: ALT_NOTEQUAL
            pass 
            self.mALT_NOTEQUAL()


        elif alt25 == 34:
            # kv.g:1:233: LESSEQUAL
            pass 
            self.mLESSEQUAL()


        elif alt25 == 35:
            # kv.g:1:243: LEFTSHIFT
            pass 
            self.mLEFTSHIFT()


        elif alt25 == 36:
            # kv.g:1:253: GREATEREQUAL
            pass 
            self.mGREATEREQUAL()


        elif alt25 == 37:
            # kv.g:1:266: RIGHTSHIFT
            pass 
            self.mRIGHTSHIFT()


        elif alt25 == 38:
            # kv.g:1:277: PLUSEQUAL
            pass 
            self.mPLUSEQUAL()


        elif alt25 == 39:
            # kv.g:1:287: MINUSEQUAL
            pass 
            self.mMINUSEQUAL()


        elif alt25 == 40:
            # kv.g:1:298: DOUBLESTAR
            pass 
            self.mDOUBLESTAR()


        elif alt25 == 41:
            # kv.g:1:309: STAREQUAL
            pass 
            self.mSTAREQUAL()


        elif alt25 == 42:
            # kv.g:1:319: DOUBLESLASH
            pass 
            self.mDOUBLESLASH()


        elif alt25 == 43:
            # kv.g:1:331: SLASHEQUAL
            pass 
            self.mSLASHEQUAL()


        elif alt25 == 44:
            # kv.g:1:342: VBAREQUAL
            pass 
            self.mVBAREQUAL()


        elif alt25 == 45:
            # kv.g:1:352: PERCENTEQUAL
            pass 
            self.mPERCENTEQUAL()


        elif alt25 == 46:
            # kv.g:1:365: AMPEREQUAL
            pass 
            self.mAMPEREQUAL()


        elif alt25 == 47:
            # kv.g:1:376: CIRCUMFLEXEQUAL
            pass 
            self.mCIRCUMFLEXEQUAL()


        elif alt25 == 48:
            # kv.g:1:392: LEFTSHIFTEQUAL
            pass 
            self.mLEFTSHIFTEQUAL()


        elif alt25 == 49:
            # kv.g:1:407: RIGHTSHIFTEQUAL
            pass 
            self.mRIGHTSHIFTEQUAL()


        elif alt25 == 50:
            # kv.g:1:423: DOUBLESTAREQUAL
            pass 
            self.mDOUBLESTAREQUAL()


        elif alt25 == 51:
            # kv.g:1:439: DOUBLESLASHEQUAL
            pass 
            self.mDOUBLESLASHEQUAL()


        elif alt25 == 52:
            # kv.g:1:456: DOT
            pass 
            self.mDOT()


        elif alt25 == 53:
            # kv.g:1:460: AT
            pass 
            self.mAT()


        elif alt25 == 54:
            # kv.g:1:463: AND
            pass 
            self.mAND()


        elif alt25 == 55:
            # kv.g:1:467: OR
            pass 
            self.mOR()


        elif alt25 == 56:
            # kv.g:1:470: NOT
            pass 
            self.mNOT()


        elif alt25 == 57:
            # kv.g:1:474: FLOAT
            pass 
            self.mFLOAT()


        elif alt25 == 58:
            # kv.g:1:480: LONGINT
            pass 
            self.mLONGINT()


        elif alt25 == 59:
            # kv.g:1:488: INT
            pass 
            self.mINT()


        elif alt25 == 60:
            # kv.g:1:492: COMPLEX
            pass 
            self.mCOMPLEX()


        elif alt25 == 61:
            # kv.g:1:500: STRING
            pass 
            self.mSTRING()


        elif alt25 == 62:
            # kv.g:1:507: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt25 == 63:
            # kv.g:1:515: WS
            pass 
            self.mWS()


        elif alt25 == 64:
            # kv.g:1:518: WNAME
            pass 
            self.mWNAME()


        elif alt25 == 65:
            # kv.g:1:524: CANVAS
            pass 
            self.mCANVAS()


        elif alt25 == 66:
            # kv.g:1:531: NAME
            pass 
            self.mNAME()


        elif alt25 == 67:
            # kv.g:1:536: DIRECTIVETEXT
            pass 
            self.mDIRECTIVETEXT()


        elif alt25 == 68:
            # kv.g:1:550: COMMENTTEXT
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
        u"\1\uffff\6\53\7\uffff\1\66\1\70\1\73\1\76\1\100\1\102\1\106\1\111"
        u"\1\113\1\115\3\uffff\1\117\2\uffff\1\120\1\uffff\3\53\2\126\1\53"
        u"\4\uffff\1\53\1\uffff\1\137\1\53\1\142\1\143\1\144\4\53\4\uffff"
        u"\1\152\2\uffff\1\154\10\uffff\1\156\2\uffff\1\160\10\uffff\1\161"
        u"\1\53\1\164\1\53\2\uffff\1\161\1\uffff\1\126\2\uffff\1\126\2\53"
        u"\1\uffff\1\174\1\53\3\uffff\2\53\1\u0081\1\53\12\uffff\1\u0085"
        u"\1\uffff\1\u0086\1\126\1\uffff\1\161\1\uffff\1\161\1\53\1\uffff"
        u"\1\174\1\53\1\u008c\1\53\1\uffff\1\53\1\uffff\1\161\3\uffff\1\161"
        u"\1\uffff\1\53\1\u0092\1\uffff\1\53\1\u0094\1\uffff\1\161\1\53\1"
        u"\uffff\1\u0096\1\uffff\1\u0097\2\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\u0098\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\11\1\42\1\146\1\154\1\141\1\157\1\151\7\uffff\2\75\1\52\1\57"
        u"\2\75\1\74\3\75\3\uffff\1\75\2\uffff\1\60\1\uffff\1\156\1\162\1"
        u"\157\2\56\1\42\4\uffff\1\141\1\uffff\1\72\1\151\3\60\1\163\1\155"
        u"\1\162\1\145\4\uffff\1\75\2\uffff\1\75\10\uffff\1\75\2\uffff\1"
        u"\75\10\uffff\1\60\1\144\1\60\1\164\1\60\1\uffff\1\60\1\53\1\56"
        u"\2\uffff\1\56\1\42\1\156\1\uffff\1\0\1\163\3\uffff\1\145\1\142"
        u"\1\60\1\154\11\uffff\1\53\1\60\1\uffff\2\60\1\53\3\60\1\166\1\uffff"
        u"\1\0\1\145\1\60\1\144\1\uffff\1\144\2\60\2\uffff\2\60\1\53\1\141"
        u"\1\60\1\uffff\1\141\3\60\1\163\1\uffff\1\60\1\uffff\1\60\2\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\176\1\141\1\163\1\154\1\141\1\157\1\151\7\uffff\6\75\2\76\2"
        u"\75\3\uffff\1\75\2\uffff\1\71\1\uffff\1\156\1\162\1\157\1\170\1"
        u"\154\1\162\4\uffff\1\141\1\uffff\1\72\1\151\3\172\1\163\1\155\1"
        u"\162\1\145\4\uffff\1\75\2\uffff\1\75\10\uffff\1\75\2\uffff\1\75"
        u"\10\uffff\1\152\1\144\1\172\1\164\1\146\1\uffff\1\152\1\71\1\154"
        u"\2\uffff\1\154\1\47\1\156\1\uffff\1\uffff\1\163\3\uffff\1\145\1"
        u"\142\1\172\1\154\11\uffff\1\71\1\172\1\uffff\1\172\1\154\1\71\1"
        u"\152\1\71\1\152\1\166\1\uffff\1\uffff\1\145\1\172\1\144\1\uffff"
        u"\1\144\1\71\1\152\2\uffff\1\71\1\152\1\71\1\141\1\172\1\uffff\1"
        u"\141\1\172\1\71\1\152\1\163\1\uffff\1\172\1\uffff\1\172\2\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\7\uffff\1\11\1\12\1\13\1\14\1\15\1\16\1\17\12\uffff\1\32\1\33"
        u"\1\34\1\uffff\1\36\1\40\1\uffff\1\65\6\uffff\1\75\1\76\1\77\1\100"
        u"\1\uffff\1\102\11\uffff\1\46\1\20\1\47\1\21\1\uffff\1\51\1\22\1"
        u"\uffff\1\53\1\23\1\54\1\24\1\56\1\25\1\41\1\42\1\uffff\1\26\1\44"
        u"\1\uffff\1\27\1\37\1\30\1\55\1\31\1\57\1\35\1\64\5\uffff\1\73\3"
        u"\uffff\1\74\1\72\3\uffff\1\104\2\uffff\1\2\1\4\1\5\4\uffff\1\62"
        u"\1\50\1\63\1\52\1\60\1\43\1\61\1\45\1\71\2\uffff\1\67\7\uffff\1"
        u"\103\4\uffff\1\7\3\uffff\1\66\1\70\5\uffff\1\3\5\uffff\1\1\1\uffff"
        u"\1\10\1\uffff\1\6\1\101"
        )

    DFA25_special = DFA.unpack(
        u"\140\uffff\1\1\34\uffff\1\0\32\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\1\50\1\47\1\uffff\2\47\22\uffff\1\50\1\35\1\46\1\54"
        u"\1\uffff\1\27\1\23\1\46\1\7\1\10\1\20\1\16\1\14\1\17\1\36\1\21"
        u"\1\43\11\44\1\13\1\15\1\24\1\26\1\25\1\uffff\1\37\32\51\1\11\1"
        u"\uffff\1\12\1\33\1\53\1\30\1\40\1\53\1\52\1\53\1\3\1\5\2\53\1\2"
        u"\2\53\1\4\1\53\1\42\1\41\2\53\1\1\2\53\1\45\3\53\1\6\1\53\1\31"
        u"\1\22\1\32\1\34"),
        DFA.unpack(u"\1\46\4\uffff\1\46\71\uffff\1\55"),
        DFA.unpack(u"\1\56\7\uffff\1\57\4\uffff\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\71\22\uffff\1\72"),
        DFA.unpack(u"\1\74\15\uffff\1\75"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\105\1\104\1\103"),
        DFA.unpack(u"\1\107\1\110"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\121"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\127\1\uffff\12\131\13\uffff\1\130\4\uffff\1\132"
        u"\1\uffff\1\133\13\uffff\1\125\14\uffff\1\130\4\uffff\1\132\1\uffff"
        u"\1\133\13\uffff\1\125"),
        DFA.unpack(u"\1\127\1\uffff\12\134\13\uffff\1\130\4\uffff\1\132"
        u"\1\uffff\1\133\30\uffff\1\130\4\uffff\1\132\1\uffff\1\133"),
        DFA.unpack(u"\1\46\4\uffff\1\46\112\uffff\1\135"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\121\13\uffff\1\162\4\uffff\1\132\32\uffff\1\162"
        u"\4\uffff\1\132"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\12\166\7\uffff\6\166\32\uffff\6\166"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\170\13\uffff\1\167\4\uffff\1\132\32\uffff\1\167"
        u"\4\uffff\1\132"),
        DFA.unpack(u"\1\171\1\uffff\1\171\2\uffff\12\172"),
        DFA.unpack(u"\1\127\1\uffff\12\131\13\uffff\1\130\4\uffff\1\132"
        u"\1\uffff\1\133\30\uffff\1\130\4\uffff\1\132\1\uffff\1\133"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127\1\uffff\12\134\13\uffff\1\130\4\uffff\1\132"
        u"\1\uffff\1\133\30\uffff\1\130\4\uffff\1\132\1\uffff\1\133"),
        DFA.unpack(u"\1\46\4\uffff\1\46"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\175\1\uffff\ufff5\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0083\1\uffff\1\u0083\2\uffff\12\u0084"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\166\7\uffff\6\166\3\uffff\1\132\1\uffff\1\133\24"
        u"\uffff\6\166\3\uffff\1\132\1\uffff\1\133"),
        DFA.unpack(u"\1\u0087\1\uffff\1\u0087\2\uffff\12\u0088"),
        DFA.unpack(u"\12\170\13\uffff\1\u0089\4\uffff\1\132\32\uffff\1\u0089"
        u"\4\uffff\1\132"),
        DFA.unpack(u"\12\172"),
        DFA.unpack(u"\12\172\20\uffff\1\132\37\uffff\1\132"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\175\1\uffff\ufff5\175"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\12\u0084"),
        DFA.unpack(u"\12\u0084\20\uffff\1\132\37\uffff\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u0088"),
        DFA.unpack(u"\12\u0088\20\uffff\1\132\37\uffff\1\132"),
        DFA.unpack(u"\1\u008f\1\uffff\1\u008f\2\uffff\12\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\u0090"),
        DFA.unpack(u"\12\u0090\20\uffff\1\132\37\uffff\1\132"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
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
                LA25_125 = input.LA(1)

                s = -1
                if ((0 <= LA25_125 <= 9) or (11 <= LA25_125 <= 65535)):
                    s = 125

                else:
                    s = 124

                if s >= 0:
                    return s
            elif s == 1: 
                LA25_96 = input.LA(1)

                s = -1
                if ((0 <= LA25_96 <= 9) or (11 <= LA25_96 <= 65535)):
                    s = 125

                else:
                    s = 124

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
