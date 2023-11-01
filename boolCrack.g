start: logicalstart;

logicalstart: 
     logicalstart ';' logicalstart
    | logicalcall
    | logicalfuntion
    | logicalif
    ;

logicalarg:
     logicalarg ',' logicalarg
    | logicalexpression
    ;

logicalcall: ID '(' logicalarg ')';

expresion: 
     logicalexpression
    | logicalcall
    ;
expresionblock: '{' expresion '}';

logicalfuntion: 'fun' ID '(' logicalcallarg ')' expresionblock;

logicalif: 'if' '(' expresion ',' expresion ',' expresion ')';

logicalcallarg: 
     ID
    | logicalarg ',' logicalarg
    ;

logicalexpression:
     logicalterminal
    | '!' logicalexpression 
    | parenle
    |logicalexpression logicaloperation logicalexpression
    ;

parenle : '\(' logicalexpression '\)';

logicaloperation:
    TCONJ
    | TDISJ;

logicalterminal:
    TRUE
    | FALSE
    | T1
    | T0
    ;

ID: '[a-z]+'
    (%unless
        FUN: 'fun';
        IF    : 'if';
        TRUE  : 'true';
        FALSE : 'false';        
    );
TCONJ : '\*';
TDISJ: '\+';
TRUE : 'true';
FALSE : 'false';
T1: '1';
T0: '0';

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		