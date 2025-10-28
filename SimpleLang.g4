grammar SimpleLang;

// ----------------------------------------------------
// PARSER RULES
// ----------------------------------------------------

// Erlaubt auch leere Zeilen überall
program
    : (NEWLINE | statement)+ EOF
    ;

statement
    : assignmentStatement NEWLINE          # Assignment
    | ifStatement                          # IfElse          // enthält eigenes NEWLINE am Ende
    | whileStatement                       # WhileLoop       // enthält eigenes NEWLINE am Ende
    | expression NEWLINE                   # ExpressionStatement
    ;

assignmentStatement
    : IDENTIFIER ASSIGN expression
    ;

// Kontrollstrukturen
whileStatement
    : WHILE expression DO NEWLINE statement* END NEWLINE
    ;

ifStatement
    : IF expression DO NEWLINE statement*
      (ELSE DO NEWLINE statement*)?
      END NEWLINE
    ;

// Ausdrücke mit richtiger Vorrangfolge: * / > + - > Vergleiche
expression
    : expression (MULT | DIV) expression                               # MulDiv
    | expression (PLUS | MINUS) expression                             # AddSub
    | expression (EQUAL | NOTEQUAL | GREATER | LESS | GE | LE) expression # Comparison
    | primary                                                          # PrimaryExpr
    ;

// Elementare Ausdrücke
primary
    : INTEGER_LITERAL
    | STRING_LITERAL
    | IDENTIFIER
    | LPAREN expression RPAREN
    ;

// ----------------------------------------------------
// LEXER RULES
// ----------------------------------------------------

// Schlüsselwörter
WHILE     : 'while' ;
DO        : 'do' ;
END       : 'end' ;
IF        : 'if' ;
ELSE      : 'else' ;

// Operatoren
ASSIGN    : ':=' ;
PLUS      : '+' ;
MINUS     : '-' ;
MULT      : '*' ;
DIV       : '/' ;
EQUAL     : '==' ;
NOTEQUAL  : '!=' ;
GREATER   : '>' ;
LESS      : '<' ;
GE        : '>=' ;
LE        : '<=' ;

// Sonstige Tokens
LPAREN    : '(' ;
RPAREN    : ')' ;

// Literale
INTEGER_LITERAL : [0-9]+ ;
// Strings in "..." ; erlaubt Escapes wie \"
STRING_LITERAL  : '"' ( ~["\\\r\n] | '\\' . )* '"' ;

// Bezeichner
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ;

// Kommentare & Whitespace
COMMENT : '#' ~[\r\n]* -> skip ;
NEWLINE : ('\r'? '\n' | '\r')+ ;
WS      : [ \t]+ -> skip ;
