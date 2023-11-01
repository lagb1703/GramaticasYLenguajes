start: expresion;

//reglas

expresion:
    logicalexpression '\;'
    | funtioncreate '\;'
    | macthcreation '\;'
    | reduce '\;'
    | display '\;'
    | '\;'
    | expresion expresion
    ;

logicalexpression:
     OPAR logicalexpression CPAR
    | negation
    | logicalterminal
    | name
    | funcioncall
    | conditionals
    |logicalexpression logicaloperation logicalexpression
    ;

reduce: REDUCE OPAR logicalexpression CPAR;

display: DISPLAY OPAR  logicalexpression CPAR;

conditionals:
     macthcall
    | if
    ;

macthcall: name '\[' logicalexpression '\]';

localmactharguments: 
    OPAR logicalexpression CPAR '=>' logicalexpression
    | localmactharguments ',' localmactharguments
    ;

macthcreation: 
    ID '>=' '{' logicalexpression ',' logicalexpression ',' logicalexpression '}'
    | ID '>=' '{' localmactharguments ',' '_:' logicalexpression '}'
    ;
if: 
     OPAR logicalexpression CPAR '\?' logicalexpression '\:' logicalexpression
    | OPAR logicalexpression CPAR '\?' logicalexpression '\|' if
    ;

funtioncallarguments: 
    logicalexpression
    | funtioncallarguments ',' funtioncallarguments
    ;

name: ID;

funcioncall: 
    name OPAR funtioncallarguments CPAR
    | name OPAR CPAR
    ;

funtioncreatearguments:
    name
    | funtioncreatearguments ',' funtioncreatearguments
    ;

funtioncreate:
    ID OPAR funtioncreatearguments CPAR '>=' logicalexpression
    | ID OPAR CPAR '>=' logicalexpression
    ;

negation: '!' OPAR logicalexpression CPAR;

logicalterminal:
    TRUE
    | FALSE
    | T0
    | T1
    ;

logicaloperation:
    and
    | or
    | imp
    ;

and:    AND1
        |AND2
        ;

or:     OR1
        |OR2
        ;

imp:    IMP;

doubleimp: DIMP;

//elementos

ID: '[a-z]+' (%unless
        AND1:   'and';
        IF:     'if';
        TRUE: 'true';
        FALSE: 'false';
        OR1:    'or';
        REDUCE: 'reduce';
        DISPLAY: 'display';
    );

T1: '1';
T0: '0';
AND2:   '\*';
OR2:    '\+';
IMP:    '=>';
DIMP:   '<=>';
OPAR:   '\(';
CPAR:   '\)';
NEGATIONSIMBOL: '!';

//Python comments
COMMENT: '\#''.*?''\n' (%ignore);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);	