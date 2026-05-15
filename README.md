# ANTLR4 Astro Grammar

ANTLR4 grammars for parsing [Astro](https://astro.build) component files (`.astro`).

## Overview

This repository contains lexer and parser grammars that define the syntax of Astro component files. The grammar handles Astro's hybrid syntax combining HTML-like markup, frontmatter, template expressions, and special Astro directives.

## Project Structure

```
AstroAntlr4/
├── AstroLexer.g4        # ANTLR4 lexer grammar (7 lexer modes)
├── AstroParser.g4       # ANTLR4 parser grammar
├── tests/               # Generated lexer and parser (Python target)
│   ├── AstroLexer.py
│   ├── AstroParser.py
│   ├── AstroLexer.tokens
│   ├── AstroParser.tokens
│   ├── AstroLexer.interp
│   ├── AstroParser.interp
│   ├── AstroParserListener.py
│   └── AstroParserVisitor.py
├── test_grammar.py      # Basic parsing tests
├── test_edge_cases.py   # Comprehensive edge case tests
└── .gitignore           # Excludes generated ANTLR files
```

## Features

The grammar supports all core Astro syntax:

- **Frontmatter**: YAML metadata between `---` delimiters
- **HTML elements**: Standard lowercase HTML tags (`<div>`, `<span>`, etc.)
- **Astro components**: UpperCamelCase component tags (`<MyComponent>`, `<Component.Child>`)
- **Fragments**: `<Fragment>` wrapper elements
- **Template expressions**: JavaScript/TypeScript expressions in `{...}` braces
- **Script & style blocks**: Special handling for `<script>` and `<style>` content
- **Directives**: Astro-specific attributes:
  - `client:load`, `client:idle`, `client:visible`, `client:media`, `client:only`
  - `server:prefetch`, `server:load`
  - `set:html`, `set:text`
  - `is:raw`
  - `class:list`
  - `transition:name`, `transition:animate`, `transition:persist`
  - `slot`
- **Expressions in attributes**: `class:list={expression}`, `transition:name={expr}`
- **Comments**: HTML `<!-- -->` and expression comments `{/* */}`

## Lexer Modes

The lexer uses 7 modes to handle different contexts:

| Mode | Description |
|------|-------------|
| `DEFAULT` | Template-level text and HTML tags |
| `FRONTMATTER` | YAML frontmatter content |
| `TAG` | Inside HTML/component opening/closing tags |
| `EXPR` | Inside `{...}` template expressions |
| `SCRIPT` | Inside `<script>` tags |
| `STYLE` | Inside `<style>` tags |
| `EXPR_COMMENT` | Inside `{/* ... */}` comments |

## Requirements

- ANTLR 4.13.1 or later
- Python 3.8+
- ANTLR4 Python runtime: `pip install antlr4-python3-runtime`

## Generating the Parser

The `tests/` directory contains generated files in `.gitignore`. To regenerate:

```bash
# Using ANTLR tool
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 AstroLexer.g4
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 AstroParser.g4 -visitor

# Output files will be placed in tests/ directory
```

Or use the provided script if available.

## Running Tests

### Basic tests
```bash
python test_grammar.py
```

### Edge cases
```bash
python test_edge_cases.py
```

Both scripts parse sample Astro files and print token streams or parse trees.

## Example

```astro
---
layout: '../layouts/MainLayout.astro'
title: 'Welcome'
---

<Layout>
  <h1>Hello {name}!</h1>
  
  <button 
    class:list={['primary', {active: isActive}]}
    onclick:once={handleClick}
  >
    Click me
  </button>
  
  <script>
    console.log("Client-side script here");
  </script>
</Layout>
```

## License

MIT

## Contributing

Contributions are welcome! Please open issues or PRs for grammar improvements, edge cases, or bug fixes.
