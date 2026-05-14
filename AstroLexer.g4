lexer grammar AstroLexer;

@members {
    self.in_raw = False
    self.pending_script = False
    self.pending_style = False
    self.pending_raw = False
}

// ════════════════════════════════════════════════════════════
//  Astro Lexer — 7 modes:
//    DEFAULT     template text / HTML
//    FRONTMATTER JS/TS code between ---
//    TAG         inside < ... >
//    EXPR        inside { ... }
//    SCRIPT      inside <script> ... </script>
//    STYLE       inside <style> ... </style>
// ════════════════════════════════════════════════════════════

// ────────────────────────────────────────────────────────────
//  DEFAULT MODE  —  template level
// ────────────────────────────────────────────────────────────

// Frontmatter open: --- at start of file
FRONTMATTER_OPEN
    : '---' -> pushMode(FRONTMATTER)
    ;

// HTML comments — skipped
HTML_COMMENT
    : '<!--' .*? '-->' -> skip
    ;

// Special tag blocks: script and style
// These push TAG mode to parse attributes, then after '>' we'll switch to SCRIPT/STYLE content mode
SCRIPT_OPEN
    : '<script' {self.pending_script = True} -> pushMode(TAG)
    ;

STYLE_OPEN
    : '<style'  {self.pending_style = True} -> pushMode(TAG)
    ;

// HTML tag open
TAG_OPEN
    : '<' {if self.in_raw: self.in_raw = False} -> pushMode(TAG)
    ;

// HTML close tag open
TAG_OPEN_CLOSE
    : '</' {if self.in_raw: self.in_raw = False} -> pushMode(TAG)
    ;

// Template expression (disabled inside raw blocks via predicate)
TEMPLATE_EXPR_OPEN
    : {not self.in_raw}? '{' -> pushMode(EXPR)
    ;

// Raw text content (used inside is:raw blocks, enabled only when in_raw flag is set)
RAW_TEXT_CONTENT
    : {self.in_raw}? ~[<]+
    ;

// Plain text content (used outside raw blocks, enabled when in_raw is false)
// Exclude newlines to allow frontmatter delimiter recognition
TEXT
    : {not self.in_raw}? ~[<{\r\n]+
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
    : '>' {
        # Determine which pending mode to activate, if any
        mode = None
        if self.pending_script:
            mode = 'SCRIPT'
        elif self.pending_style:
            mode = 'STYLE'
        elif self.pending_raw:
            mode = 'RAW'
        # Clear all pending flags
        self.pending_script = False
        self.pending_style = False
        self.pending_raw = False
        # Pop back to previous mode (exit TAG)
        self.popMode()
        # Activate the new mode if needed
        if mode == 'SCRIPT':
            self.pushMode(self.SCRIPT)
        elif mode == 'STYLE':
            self.pushMode(self.STYLE)
        elif mode == 'RAW':
            self.in_raw = True
      }
    ;

TAG_SELF_CLOSE
    : '/>' {
        # Clear any pending mode flags (self-closing tags have no content)
        self.pending_script = False
        self.pending_style = False
        self.pending_raw = False
        self.popMode()
      }
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
    : 'is:raw' {self.pending_raw = True}
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

EXPR_DOT
    : '.'
    ;

SPREAD
    : '...'
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
    : ~[{}"'`/.]+
    | '/' ~[*]
    ;

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

