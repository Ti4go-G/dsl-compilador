grammar Formularios;

arquivo: formulario* EOF;

formulario: 'formulario' ID '{' campo* '}';

campo: 'campo' ID ':' tipo flags;

tipo: ID ('(' param (',' param)? ')')?;

param: INT;

flags: (OBRIGATORIO | UNICO)*;

OBRIGATORIO: 'obrigatorio';
UNICO: 'unico';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
