from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser

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

print(tree.toStringTree(recog=parser))
