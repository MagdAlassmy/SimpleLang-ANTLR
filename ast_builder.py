from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser


# ---------------------------------------------
# AST-KLASSEN
# ---------------------------------------------
class Node:
    pass


class Program(Node):
    def __init__(self, statements):
        self.statements = statements


class Assignment(Node):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class If(Node):
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Var(Node):
    def __init__(self, name):
        self.name = name


class IntLiteral(Node):
    def __init__(self, value):
        self.value = int(value)


class StringLiteral(Node):
    def __init__(self, value):
        self.value = value.strip('"')


# ---------------------------------------------
# AST-BUILDER (robust für deinen ParseTree)
# ---------------------------------------------
class ASTBuilder:
    def build(self, parse_tree):
        statements = []
        for child in parse_tree.getChildren():
            stmt = self.build_node(child)
            if stmt:
                statements.append(stmt)
        return Program(statements)

    def build_node(self, node):
        if node is None:
            return None
        name = type(node).__name__

        # Zuweisung
        if "Assignment" in name:
            if node.getChildCount() >= 3:
                var_name = node.getChild(0).getText()
                expr = self.build_expr(node.getChild(2))
                return Assignment(var_name, expr)

        # If-Struktur
        if "If" in name:
            cond = self.find_expr_or_primary(node)
            then_body, else_body = [], []
            in_else = False
            for ch in node.getChildren():
                if isinstance(ch, TerminalNode) and ch.getText() == "else":
                    in_else = True
                elif "Statement" in type(ch).__name__:
                    stmt = self.build_node(ch)
                    if stmt:
                        (else_body if in_else else then_body).append(stmt)
            return If(cond, then_body, else_body if else_body else None)

        # While-Schleife
        if "While" in name:
            cond = self.find_expr_or_primary(node)
            body = []
            for ch in node.getChildren():
                if "Statement" in type(ch).__name__:
                    stmt = self.build_node(ch)
                    if stmt:
                        body.append(stmt)
            return While(cond, body)

        # Expression-Statement
        if "Expression" in name:
            expr = self.find_expr_or_primary(node)
            if expr:
                return expr

        return None

    # -----------------------------------------
    # Ausdruckssuche – erkennt expression & primary
    # -----------------------------------------
    def find_expr_or_primary(self, node):
        if node is None or isinstance(node, TerminalNode):
            return None
        name = type(node).__name__.lower()
        if "expression" in name or "primary" in name:
            return self.build_expr(node)
        if not hasattr(node, "getChildren"):
            return None
        for ch in node.getChildren():
            expr = self.find_expr_or_primary(ch)
            if expr:
                return expr
        return None

    # -----------------------------------------
    # Ausdrucksverarbeitung
    # -----------------------------------------
    def build_expr(self, node):
        if node is None:
            return Var("?")
        if not hasattr(node, "getChildCount"):
            return Var(str(node))

        n = node.getChildCount()

        # Primary-Knoten (z.B. Literale oder Variablen)
        if "primary" in type(node).__name__.lower():
            if n == 1:
                tok = node.getChild(0)
                if isinstance(tok, TerminalNode):
                    text = tok.getText()
                    ttype = getattr(tok.symbol, "type", None)
                    if ttype == SimpleLangLexer.INTEGER_LITERAL:
                        return IntLiteral(text)
                    elif ttype == SimpleLangLexer.STRING_LITERAL:
                        return StringLiteral(text)
                    else:
                        return Var(text)
            return Var("?")

        # Binäre Operation (expr op expr)
        if n == 3:
            left = self.build_expr(node.getChild(0))
            op_node = node.getChild(1)
            right = self.build_expr(node.getChild(2))
            op = op_node.getText() if op_node else "?"
            return BinaryOp(left, op, right)

        # Falls geschachtelt (expression expression ...)
        for ch in node.getChildren():
            expr = self.build_expr(ch)
            if expr:
                return expr

        return Var(node.getText() if node else "?")


# ---------------------------------------------
# PRETTY PRINTER
# ---------------------------------------------
def print_ast(node, indent=0):
    pad = " " * (indent * 4)
    if isinstance(node, Program):
        for s in node.statements:
            print_ast(s, indent)
    elif isinstance(node, Assignment):
        print(f"{pad}{node.name} := {expr_to_str(node.expr)}")
    elif isinstance(node, While):
        print(f"{pad}while {expr_to_str(node.condition)} do")
        for s in node.body:
            print_ast(s, indent + 1)
        print(f"{pad}end")
    elif isinstance(node, If):
        print(f"{pad}if {expr_to_str(node.condition)} do")
        for s in node.then_body:
            print_ast(s, indent + 1)
        if node.else_body:
            print(f"{pad}else do")
            for s in node.else_body:
                print_ast(s, indent + 1)
        print(f"{pad}end")


def expr_to_str(expr):
    if isinstance(expr, BinaryOp):
        return f"{expr_to_str(expr.left)} {expr.op} {expr_to_str(expr.right)}"
    elif isinstance(expr, Var):
        return expr.name
    elif isinstance(expr, IntLiteral):
        return str(expr.value)
    elif isinstance(expr, StringLiteral):
        return f'"{expr.value}"'
    else:
        return "?"


# ---------------------------------------------
# HAUPTPROGRAMM
# ---------------------------------------------
if __name__ == "__main__":
    code = """
    a := 0
    if 10 < 1 do
        a := 42
    else do
        a := 7
    end
    while a > 0 do
        a := a - 1
    end
    """

    input_stream = InputStream(code)
    lexer = SimpleLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleLangParser(tokens)
    tree = parser.program()

    builder = ASTBuilder()
    ast = builder.build(tree)

    print("--- AST Pretty Print ---")
    print_ast(ast)
