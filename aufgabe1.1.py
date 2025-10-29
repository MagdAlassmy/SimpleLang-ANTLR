# pretty_printer.py
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser

INDENT = 4  # Leerzeichen pro Einrückung

# ---------- Ausdruck formatieren ----------
def fmt_expr(ctx: SimpleLangParser.ExpressionContext) -> str:
    n = ctx.getChildCount()
    # 1 Kind: Literal/Identifier
    if n == 1:
        ch = ctx.getChild(0)
        return ch.getText()
    # '(' expr ')'
    if n == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
        return f"({fmt_expr(ctx.getChild(1))})"
    # binär: left op right
    if n == 3:
        left = fmt_expr(ctx.getChild(0))
        op   = ctx.getChild(1).getText()
        right= fmt_expr(ctx.getChild(2))
        return f"{left} {op} {right}"
    # Fallback: alles zusammenziehen
    parts = []
    for i in range(n):
        ch = ctx.getChild(i)
        parts.append(ch.getText() if isinstance(ch, TerminalNode) else fmt_expr(ch))
    return " ".join(parts)

# ---------- Statements formatieren ----------
def fmt_statement(stmt: SimpleLangParser.StatementContext, level: int) -> list[str]:
    pad = " " * (INDENT * level)

    a = getattr(stmt, "assignmentStatement", None)
    if a and a():
        actx = a()
        ident = actx.IDENTIFIER().getText()
        expr  = fmt_expr(actx.expression())
        return [f"{pad}{ident} := {expr}"]

    i = getattr(stmt, "ifStatement", None)
    if i and i():
        ictx = i()
        cond = fmt_expr(ictx.expression())     # in deiner Grammatik gibt es genau 1 expression()
        lines = [f"{pad}if {cond} do"]
        # then/else anhand der Kinder trennen
        then_stmts, else_stmts, in_else = [], [], False
        for ch in ictx.getChildren():
            if isinstance(ch, TerminalNode) and ch.getText() == "else":
                in_else = True
            elif isinstance(ch, SimpleLangParser.StatementContext):
                (else_stmts if in_else else then_stmts).append(ch)
        for s in then_stmts:
            lines.extend(fmt_statement(s, level + 1))
        if else_stmts:
            lines.append(f"{pad}else do")
            for s in else_stmts:
                lines.extend(fmt_statement(s, level + 1))
        lines.append(f"{pad}end")
        return lines

    w = getattr(stmt, "whileStatement", None)
    if w and w():
        wctx = w()
        cond = fmt_expr(wctx.expression())
        lines = [f"{pad}while {cond} do"]
        inner = [ch for ch in wctx.getChildren() if isinstance(ch, SimpleLangParser.StatementContext)]
        for s in inner:
            lines.extend(fmt_statement(s, level + 1))
        lines.append(f"{pad}end")
        return lines

    e = getattr(stmt, "expression", None)
    if e and e():
        return [f"{pad}{fmt_expr(e())}"]

    # Fallback
    return [pad + stmt.getText()]

def fmt_program(pctx: SimpleLangParser.ProgramContext) -> str:
    out: list[str] = []
    # Nur Statement-Knoten nehmen; NEWLINE-Tokens ignorieren
    for ch in pctx.getChildren():
        if isinstance(ch, SimpleLangParser.StatementContext):
            out.extend(fmt_statement(ch, 0))
    return "\n".join(out) + "\n"

def pretty_print_text(src: str) -> str:
    # Normalisierte Zeilenumbrüche, Kommentare bleiben bis NEWLINE ignoriert (laut Grammatik)
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    input_stream = InputStream(src)
    lexer = SimpleLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleLangParser(tokens)
    tree = parser.program()
    return fmt_program(tree)

if __name__ == "__main__":
    ugly = """a     := 0
    if    10 < 1
       do
a    :=     42      # Zuweisung
else do
        a :=      7
  end
"""
    print(pretty_print_text(ugly))
