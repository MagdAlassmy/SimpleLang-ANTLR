# Generated from ./SimpleLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,4,0,17,8,0,11,0,12,0,18,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,42,
        8,3,10,3,12,3,45,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,55,8,4,
        10,4,12,4,58,9,4,1,4,1,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,3,4,
        69,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,86,8,5,10,5,12,5,89,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,98,
        8,6,1,6,0,1,10,7,0,2,4,6,8,10,12,0,3,1,0,9,10,1,0,7,8,1,0,11,16,
        107,0,16,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,36,1,0,0,0,8,49,1,0,
        0,0,10,73,1,0,0,0,12,97,1,0,0,0,14,17,5,23,0,0,15,17,3,2,1,0,16,
        14,1,0,0,0,16,15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,
        0,19,20,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,4,2,0,23,24,5,
        23,0,0,24,31,1,0,0,0,25,31,3,8,4,0,26,31,3,6,3,0,27,28,3,10,5,0,
        28,29,5,23,0,0,29,31,1,0,0,0,30,22,1,0,0,0,30,25,1,0,0,0,30,26,1,
        0,0,0,30,27,1,0,0,0,31,3,1,0,0,0,32,33,5,21,0,0,33,34,5,6,0,0,34,
        35,3,10,5,0,35,5,1,0,0,0,36,37,5,1,0,0,37,38,3,10,5,0,38,39,5,2,
        0,0,39,43,5,23,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,1,0,0,0,43,
        41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,3,0,
        0,47,48,5,23,0,0,48,7,1,0,0,0,49,50,5,4,0,0,50,51,3,10,5,0,51,52,
        5,2,0,0,52,56,5,23,0,0,53,55,3,2,1,0,54,53,1,0,0,0,55,58,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,68,1,0,0,0,58,56,1,0,0,0,59,60,5,
        5,0,0,60,61,5,2,0,0,61,65,5,23,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,
        0,68,59,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,3,0,0,71,72,
        5,23,0,0,72,9,1,0,0,0,73,74,6,5,-1,0,74,75,3,12,6,0,75,87,1,0,0,
        0,76,77,10,4,0,0,77,78,7,0,0,0,78,86,3,10,5,5,79,80,10,3,0,0,80,
        81,7,1,0,0,81,86,3,10,5,4,82,83,10,2,0,0,83,84,7,2,0,0,84,86,3,10,
        5,3,85,76,1,0,0,0,85,79,1,0,0,0,85,82,1,0,0,0,86,89,1,0,0,0,87,85,
        1,0,0,0,87,88,1,0,0,0,88,11,1,0,0,0,89,87,1,0,0,0,90,98,5,19,0,0,
        91,98,5,20,0,0,92,98,5,21,0,0,93,94,5,17,0,0,94,95,3,10,5,0,95,96,
        5,18,0,0,96,98,1,0,0,0,97,90,1,0,0,0,97,91,1,0,0,0,97,92,1,0,0,0,
        97,93,1,0,0,0,98,13,1,0,0,0,10,16,18,30,43,56,65,68,85,87,97
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'do'", "'end'", "'if'", "'else'", 
                     "':='", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WHILE", "DO", "END", "IF", "ELSE", "ASSIGN", 
                      "PLUS", "MINUS", "MULT", "DIV", "EQUAL", "NOTEQUAL", 
                      "GREATER", "LESS", "GE", "LE", "LPAREN", "RPAREN", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
                      "COMMENT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignmentStatement = 2
    RULE_whileStatement = 3
    RULE_ifStatement = 4
    RULE_expression = 5
    RULE_primary = 6

    ruleNames =  [ "program", "statement", "assignmentStatement", "whileStatement", 
                   "ifStatement", "expression", "primary" ]

    EOF = Token.EOF
    WHILE=1
    DO=2
    END=3
    IF=4
    ELSE=5
    ASSIGN=6
    PLUS=7
    MINUS=8
    MULT=9
    DIV=10
    EQUAL=11
    NOTEQUAL=12
    GREATER=13
    LESS=14
    GE=15
    LE=16
    LPAREN=17
    RPAREN=18
    INTEGER_LITERAL=19
    STRING_LITERAL=20
    IDENTIFIER=21
    COMMENT=22
    NEWLINE=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.NEWLINE)
            else:
                return self.getToken(SimpleLangParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 14
                    self.match(SimpleLangParser.NEWLINE)
                    pass
                elif token in [1, 4, 17, 19, 20, 21]:
                    self.state = 15
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12189714) != 0)):
                    break

            self.state = 20
            self.match(SimpleLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignmentStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentStatementContext,0)

        def NEWLINE(self):
            return self.getToken(SimpleLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class IfElseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(SimpleLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)


    class WhileLoopContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.WhileStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)



    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignmentStatement()
                self.state = 23
                self.match(SimpleLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.ifStatement()
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.WhileLoopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.whileStatement()
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.expression(0)
                self.state = 28
                self.match(SimpleLangParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(SimpleLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = SimpleLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 33
            self.match(SimpleLangParser.ASSIGN)
            self.state = 34
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimpleLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(SimpleLangParser.DO, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.NEWLINE)
            else:
                return self.getToken(SimpleLangParser.NEWLINE, i)

        def END(self):
            return self.getToken(SimpleLangParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = SimpleLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SimpleLangParser.WHILE)
            self.state = 37
            self.expression(0)
            self.state = 38
            self.match(SimpleLangParser.DO)
            self.state = 39
            self.match(SimpleLangParser.NEWLINE)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3801106) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(SimpleLangParser.END)
            self.state = 47
            self.match(SimpleLangParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def DO(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.DO)
            else:
                return self.getToken(SimpleLangParser.DO, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.NEWLINE)
            else:
                return self.getToken(SimpleLangParser.NEWLINE, i)

        def END(self):
            return self.getToken(SimpleLangParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(SimpleLangParser.ELSE, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = SimpleLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SimpleLangParser.IF)
            self.state = 50
            self.expression(0)
            self.state = 51
            self.match(SimpleLangParser.DO)
            self.state = 52
            self.match(SimpleLangParser.NEWLINE)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3801106) != 0):
                self.state = 53
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 59
                self.match(SimpleLangParser.ELSE)
                self.state = 60
                self.match(SimpleLangParser.DO)
                self.state = 61
                self.match(SimpleLangParser.NEWLINE)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3801106) != 0):
                    self.state = 62
                    self.statement()
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 70
            self.match(SimpleLangParser.END)
            self.state = 71
            self.match(SimpleLangParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)

        def MULT(self):
            return self.getToken(SimpleLangParser.MULT, 0)
        def DIV(self):
            return self.getToken(SimpleLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(SimpleLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SimpleLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ComparisonContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(SimpleLangParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(SimpleLangParser.NOTEQUAL, 0)
        def GREATER(self):
            return self.getToken(SimpleLangParser.GREATER, 0)
        def LESS(self):
            return self.getToken(SimpleLangParser.LESS, 0)
        def GE(self):
            return self.getToken(SimpleLangParser.GE, 0)
        def LE(self):
            return self.getToken(SimpleLangParser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class PrimaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(SimpleLangParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleLangParser.PrimaryExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 74
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 80
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.ComparisonContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 83
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expression(3)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(SimpleLangParser.INTEGER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(SimpleLangParser.STRING_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(SimpleLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SimpleLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = SimpleLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(SimpleLangParser.INTEGER_LITERAL)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(SimpleLangParser.STRING_LITERAL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(SimpleLangParser.IDENTIFIER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.match(SimpleLangParser.LPAREN)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(SimpleLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




