lexer grammar AstroLexer;

// ════════════════════════════════════════════════════════════
//  Astro Lexer — 4 modes:
//    DEFAULT     template text / HTML
//    FRONTMATTER JS/TS code between ---
//    TAG         inside < ... >
//    EXPR        inside { ... }
// ════════════════════════════════════════════════════════════

// ────────────────────────────────────────────────────────────
//  DEFAULT MODE  —  template level
// ────────────────────────────────────────────────────────────

// Frontmatter open: --- at start of file (optionally preceded by whitespace)
FRONTMATTER_OPEN
    : '---' -> pushMode(FRONTMATTER)
    ;

// HTML comments — skipped
HTML_COMMENT
    : '<!--' .*? '-->' -> skip
    ;

// Special tag blocks
SCRIPT_OPEN : '<script' -> pushMode(SCRIPT);
STYLE_OPEN  : '<style'  -> pushMode(STYLE);

// HTML tag open
TAG_OPEN
    : '<' -> pushMode(TAG)
    ;

// HTML close tag
TAG_OPEN_CLOSE
    : '</' -> pushMode(TAG)
    ;

// Template expression
TEMPLATE_EXPR_OPEN
    : '{' -> pushMode(EXPR)
    ;

RAW_TEXT_CONTENT
    : ~[<]+
    ;

// Plain text content
TEXT
    : ~[<{]+
    ;

// Whitespace
WS
    : [ \t\r\n]+ -> skip
    ;

// ────────────────────────────────────────────────────────────
//  FRONTMATTER MODE  —  JS/TS between ---
// ────────────────────────────────────────────────────────────
mode FRONTMATTER;

FM_CLOSE
    : [ \t]* '---' -> popMode
    ;

FM_NEWLINE
    : [\r\n]+ -> skip
    ;

FM_TEXT
    : ~[\r\n]+
    ;

// ────────────────────────────────────────────────────────────
//  TAG MODE  —  inside < ... >
// ────────────────────────────────────────────────────────────
mode TAG;

TAG_CLOSE
    : '>' -> popMode
    ;

TAG_SELF_CLOSE
    : '/>' -> popMode
    ;

TAG_WS
    : [ \t\r\n]+ -> skip
    ;

// Astro directives (must come before generic identifiers)
CLIENT_DIRECTIVE
    : 'client:' [a-zA-Z]+
    ;

FRAGMENT_TOKEN
    : 'Fragment'
    ;

// No RAW_TEXT_CONTENT here. It's just tags and attributes.
SERVER_DIRECTIVE
    : 'server:' [a-zA-Z]+
    ;

SET_HTML
    : 'set:html'
    ;

SET_TEXT
    : 'set:text'
    ;

IS_RAW
    : 'is:raw'
    ;

CLASS_LIST
    : 'class:list'
    ;

TRANSITION_ANIMATE
    : 'transition:animate'
    ;

TRANSITION_PERSIST
    : 'transition:persist'
    ;

TRANSITION_NAME
    : 'transition:name'
    ;

SLOT_ATTR
    : 'slot'
    ;

// Identifiers
LOWER_IDENT
    : [a-z] [a-zA-Z0-9_-]*
    ;

UPPER_IDENT
    : [A-Z] [a-zA-Z0-9_]*
    ;

COLON_IDENT
    : ':' [a-zA-Z] [a-zA-Z0-9_-]*
    ;

// Attribute operators
EQUALS
    : '='
    ;

// Attribute values (quoted)
ATTR_VALUE_DQ
    : '"' (~["\\] | '\\' .)* '"'
    ;

ATTR_VALUE_SQ
    : '\'' (~['\\] | '\\' .)* '\''
    ;

// Expression inside attribute value  class:list={...}
TAG_EXPR_OPEN
    : '{' -> pushMode(EXPR)
    ;

DOT
    : '.'
    ;

SPREAD
    : '...'
    ;

// ────────────────────────────────────────────────────────────
//  EXPR MODE  —  inside { ... }
// ────────────────────────────────────────────────────────────
mode EXPR;

EXPR_CLOSE
    : '}' -> popMode
    ;

EXPR_OPEN
    : '{' -> pushMode(EXPR)
    ;

// Strings keep brace counting balanced
EXPR_STRING_DQ
    : '"' (~["\\] | '\\' .)* '"'
    ;

EXPR_STRING_SQ
    : '\'' (~['\\] | '\\' .)* '\''
    ;

EXPR_TEMPLATE
    : '`' (~[`\\] | '\\' .)* '`'
    ;

// JSX-style comment  {/* ... */}
EXPR_COMMENT_OPEN
    : '/*' -> pushMode(EXPR_COMMENT)
    ;

// Everything else inside expression
EXPR_TEXT
    : ~[{}"'`/]+
    | '/' ~[*]
    ;

// ────────────────────────────────────────────────────────────
//  SCRIPT MODE  —  inside <script> ... </script>
// ────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────
//  EXPR_COMMENT MODE  —  {/* ... */}
// ────────────────────────────────────────────────────────────
mode EXPR_COMMENT;

EXPR_COMMENT_CLOSE
    : '*/' -> popMode
    ;

EXPR_COMMENT_TEXT
    : ~[*]+
    | '*' ~[/]
    ;

// ────────────────────────────────────────────────────────────
//  SCRIPT MODE  —  inside <script> ... </script>
// ────────────────────────────────────────────────────────────
mode SCRIPT;

SCRIPT_CLOSE
    : '</script>' -> popMode
    ;

SCRIPT_CONTENT
    : (~[<] | '<' ~[/])+
    ;

// ────────────────────────────────────────────────────────────
//  STYLE MODE  —  inside <style> ... </style>
// ────────────────────────────────────────────────────────────
mode STYLE;

STYLE_CLOSE
    : '</style>' -> popMode
    ;

STYLE_CONTENT
    : (~[<] | '<' ~[/])+
    ;
