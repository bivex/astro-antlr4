import sys
from antlr4 import *
from tests.AstroLexer import AstroLexer
from tests.AstroParser import AstroParser

def test_full_grammar():
    input_text = """---
title: Edge Case Test
---
<Layout>
  <!-- Comment test -->
  <header>
    <nav class:list={["nav", {active: true}]}>
      <a href="/home">Home</a>
    </nav>
  </header>
  
  <main>
    <h1 transition:name="title">Hello World</h1>
    <script>
      console.log("Nested < tags are fine here");
      if (a < b && b > c) { console.log('ok'); }
    </script>
    
    <style>
      body { background: <red>; }
      .test { content: ">"; }
    </style>

    <Fragment>
      <RawComponent {...props} />
    </Fragment>
  </main>
</Layout>
"""
    lexer = AstroLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    stream.fill()
    for token in stream.tokens:
        print(f"Token: {token.type} - {token.text}")
    parser = AstroParser(stream)
    
    # Enable error listener tracking
    from antlr4.error.ErrorListener import ErrorListener
    class VerboseErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"ERROR: line {line}:{column} {msg}")
            
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())
    
    tree = parser.astroFile()
    print("Parsing completed.")

if __name__ == '__main__':
    test_full_grammar()
