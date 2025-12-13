grammar Formularios;

arquivo: formulario* EOF;

formulario: FORMULARIO ID '{' campo* '}';

campo: CAMPO ID ':' tipo (MSG STRING)? flags;

tipo: ID ('(' param (',' param)? ')')?;

param: INT | FLOAT;

flags: (OBRIGATORIO | UNICO)*;

FORMULARIO: 'formulario';
CAMPO:      'campo';
OBRIGATORIO: 'obrigatorio';
UNICO:      'unico';
MSG:        'msg';

STRING: '"' ~["]* '"'; 
FLOAT: [0-9]+ '.' [0-9]+;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;