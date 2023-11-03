start: expresion;

//reglas

expresion:
    logicalexpression '\;'
    | funtioncreate '\;'
    | macthcreation '\;'
    | display '\;'
    | '\;'
    | expresion expresion
    ;

logicalexpression:
     parenle
    | logicalterminal
    | funcioncall
    | conditionals
    | logicaloperation
    ;

parenle: OPAR logicalexpression CPAR;

display: DISPLAY OPAR  logicalexpression CPAR;

conditionals:
     macthcall
    | ifs
    ;

macthcall: ID '\[' logicalexpression '\]';

localmactharguments: 
    OPAR logicalexpression CPAR '=>' logicalexpression
    | localmactharguments ',' localmactharguments
    ;

macthcreation: 
    ID '>=' '{' logicalexpression ',' logicalexpression ',' logicalexpression '}'
    | ID '>=' '{' localmactharguments ',' '_:' logicalexpression '}'
    ;
ifs: 
     OPAR logicalexpression CPAR '\?' logicalexpression '\:' logicalexpression
    | OPAR logicalexpression CPAR '\?' logicalexpression '\|' ifs
    ;

funtioncallarguments: 
    logicalexpression
    | funtioncallarguments ',' funtioncallarguments
    ;

funcioncall: 
    ID OPAR funtioncallarguments CPAR
    | ID OPAR CPAR
    ;

funtioncreatearguments:
    ID
    | funtioncreatearguments ',' funtioncreatearguments
    ;

funtioncreate:
    ID OPAR funtioncreatearguments CPAR '>=' logicalexpression
    | ID OPAR CPAR '>=' logicalexpression
    ;


logicalterminal:
    TRUE
    | FALSE
    | T0
    | T1
    | ID
    ;

logicaloperation:
    negation
    | ands
    | ors
    | imps
    | doubleimps
    ;

negation: '!' OPAR logicalexpression CPAR;

ands:    logicalexpression AND1 logicalexpression
        | logicalexpression AND2 logicalexpression
        ;

ors:     logicalexpression OR1 logicalexpression
        |logicalexpression OR2 logicalexpression
        ;

imps:    logicalexpression IMP logicalexpression;

doubleimps: DIMP;

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