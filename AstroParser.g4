parser grammar AstroParser;

options { tokenVocab = AstroLexer; }

// ════════════════════════════════════════════════════════════
//  Top-level
// ════════════════════════════════════════════════════════════

astroFile
    : (frontmatter)? template EOF
    ;

// ════════════════════════════════════════════════════════════
//  Frontmatter  (--- ... ---)
// ════════════════════════════════════════════════════════════

frontmatter
    : FRONTMATTER_OPEN FM_TEXT* FM_CLOSE
    ;

// ════════════════════════════════════════════════════════════
//  Template
// ════════════════════════════════════════════════════════════

template
    : templateItem*
    ;

templateItem
    : htmlElement
    | componentElement
    | fragmentElement
    | styleBlock
    | scriptBlock
    | rawTextBlock
    | templateExpr
    | text
    ;

// ── Plain text ──────────────────────────────────────────────
text
    : TEXT+
    ;

// ════════════════════════════════════════════════════════════
//  HTML Elements  (lowercase tags)
// ════════════════════════════════════════════════════════════

htmlElement
    : htmlOpenTag template htmlCloseTag
    | htmlVoidTag
    ;

htmlOpenTag
    : TAG_OPEN htmlTagName attribute* '>'
    ;

htmlVoidTag
    : TAG_OPEN htmlTagName attribute* TAG_SELF_CLOSE
    ;

htmlCloseTag
    : TAG_OPEN_CLOSE htmlTagName '>'
    ;

htmlTagName
    : LOWER_IDENT
    ;

// ════════════════════════════════════════════════════════════
//  Component Elements  (Capitalized tags)
// ════════════════════════════════════════════════════════════

componentElement
    : componentOpenTag template componentCloseTag
    | componentSelfCloseTag
    ;

componentOpenTag
    : TAG_OPEN componentTagName attribute* '>'
    ;

componentSelfCloseTag
    : TAG_OPEN componentTagName attribute* TAG_SELF_CLOSE
    ;

componentCloseTag
    : TAG_OPEN_CLOSE componentTagName '>'
    ;

componentTagName
    : UPPER_IDENT (DOT UPPER_IDENT)*
    ;

// ════════════════════════════════════════════════════════════
//  Fragment Element
// ════════════════════════════════════════════════════════════

fragmentElement
    : fragmentOpenTag template fragmentCloseTag
    | fragmentSelfCloseTag
    ;

fragmentOpenTag
    : TAG_OPEN FRAGMENT_TOKEN attribute* '>'
    ;

fragmentSelfCloseTag
    : TAG_OPEN FRAGMENT_TOKEN attribute* TAG_SELF_CLOSE
    ;

fragmentCloseTag
    : TAG_OPEN_CLOSE FRAGMENT_TOKEN '>'
    ;

// ════════════════════════════════════════════════════════════
//  <style> Block  — raw CSS content
// ════════════════════════════════════════════════════════════

styleBlock
    : STYLE_OPEN attribute* '>' STYLE_CONTENT* STYLE_CLOSE
    ;

// ════════════════════════════════════════════════════════════
//  <script> Block  — raw JS content
// ════════════════════════════════════════════════════════════

scriptBlock
    : SCRIPT_OPEN attribute* '>' SCRIPT_CONTENT* SCRIPT_CLOSE
    ;

// ════════════════════════════════════════════════════════════
//  is:raw Block  — raw text content
// ════════════════════════════════════════════════════════════

rawTextBlock
    : TAG_OPEN rawTagName attribute* '>' RAW_TEXT_CONTENT* TAG_OPEN_CLOSE rawTagName '>'
    ;

rawTagName
    : LOWER_IDENT
    | UPPER_IDENT
    ;

// ════════════════════════════════════════════════════════════
//  Attributes
// ════════════════════════════════════════════════════════════

attribute
    : astroDirectiveAttr
    | normalAttr
    | exprAttr
    | booleanAttr
    | spreadAttr
    ;

normalAttr
    : attrName EQUALS attrValue
    ;

exprAttr
    : attrName EQUALS TAG_EXPR_OPEN exprBody EXPR_CLOSE
    ;

booleanAttr
    : attrName
    ;

spreadAttr
    : TAG_EXPR_OPEN SPREAD exprBody EXPR_CLOSE
    ;

astroDirectiveAttr
    : directiveName (EQUALS (TAG_EXPR_OPEN exprBody EXPR_CLOSE | ATTR_VALUE_DQ | ATTR_VALUE_SQ))?
    ;

attrName
    : LOWER_IDENT
    | UPPER_IDENT
    | COLON_IDENT
    ;

attrValue
    : ATTR_VALUE_DQ
    | ATTR_VALUE_SQ
    ;

directiveName
    : CLIENT_DIRECTIVE
    | SERVER_DIRECTIVE
    | SET_HTML
    | SET_TEXT
    | IS_RAW
    | CLASS_LIST
    | TRANSITION_ANIMATE
    | TRANSITION_PERSIST
    | TRANSITION_NAME
    | SLOT_ATTR
    ;

// ════════════════════════════════════════════════════════════
//  Template Expressions  { ... }
// ════════════════════════════════════════════════════════════

templateExpr
    : TEMPLATE_EXPR_OPEN exprBody EXPR_CLOSE
    ;

exprBody
    : exprChunk*
    ;

exprChunk
    : EXPR_TEXT
    | EXPR_STRING_DQ
    | EXPR_STRING_SQ
    | EXPR_TEMPLATE
    | nestedExpr
    | exprComment
    | EXPR_DOT
    ;

nestedExpr
    : EXPR_OPEN exprBody EXPR_CLOSE
    ;

exprComment
    : EXPR_COMMENT_OPEN EXPR_COMMENT_TEXT* EXPR_COMMENT_CLOSE
    ;
