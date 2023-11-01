start: logicalexpression;

logicalexpression:
     parenle
     |logicalexpression TCONJ logicalexpression
    | '!' logicalexpression 
    |TRUE
    |FALSE
    ;

parenle : '\(' logicalexpression '\)';

// ID: '[a-z]+';
TCONJ : 'and';
TRUE : 'true';
FALSE : 'false';

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);