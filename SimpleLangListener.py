# Generated from ./SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#IfElse.
    def enterIfElse(self, ctx:SimpleLangParser.IfElseContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#IfElse.
    def exitIfElse(self, ctx:SimpleLangParser.IfElseContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#WhileLoop.
    def enterWhileLoop(self, ctx:SimpleLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#WhileLoop.
    def exitWhileLoop(self, ctx:SimpleLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:SimpleLangParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:SimpleLangParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:SimpleLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:SimpleLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDiv.
    def enterMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDiv.
    def exitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSub.
    def enterAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSub.
    def exitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Comparison.
    def enterComparison(self, ctx:SimpleLangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Comparison.
    def exitComparison(self, ctx:SimpleLangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:SimpleLangParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:SimpleLangParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#primary.
    def enterPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#primary.
    def exitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass



del SimpleLangParser