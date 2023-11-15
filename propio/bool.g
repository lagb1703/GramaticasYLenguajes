start: logicalexpression;

logicalexpression:
     OPAR logicalexpression CPAR
    | '!' logicalexpression 
    | 'true'
    | 'false'
    |logicalexpression and logicalexpression
    |logicalexpression or logicalexpression
    |logicalexpression imp logicalexpression
    |variable
    ;

   
variable: ID;

ID: '[a-z]+' (%unless
        AND1:   'and';
        AND2:   '\*';
        OR1:    'or';
        OR2:    '\+';
        IMP:    '=>';
        DIMP:   '<=>';
        OPAR:   '\(';
        CPAR:   '\)';
        IF:     'if';
        ELSE:   'else';
        THEN:   'then';
        TRUE: 'true';
        FALSE: 'false';
    );

and:    AND1
        |AND2
        ;

or:     OR1
        |OR2
        ;

imp:    IMP    
        |DIMP  
        ;

//Python comments
COMMENT: '\#''.*?''\n' (%ignore);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);	