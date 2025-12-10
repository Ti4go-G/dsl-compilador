grammar Formularios;

// --- Parser Rules (Sintaxe) ---

arquivo: formulario* EOF;

formulario: 'formulario' ID '{' campo* '}';

campo: 'campo' ID ':' tipo flags;

tipo: ID ('(' param (',' param)? ')')?;

param: INT;

flags: (OBRIGATORIO | UNICO)*;

// --- Lexer Rules (Tokens) ---

OBRIGATORIO: 'obrigatorio';
UNICO: 'unico';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip; // Ignora espaços
COMMENT: '#' ~[\r\n]* -> skip; // Ignora comentários
