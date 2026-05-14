import sys
from antlr4 import *
from tests.AstroLexer import AstroLexer
from tests.AstroParser import AstroParser

def test_parse(input_text):
    lexer = AstroLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = AstroParser(stream)
    tree = parser.astroFile()
    print(f"Parsed successfully: {input_text[:50]}...")

if __name__ == '__main__':
    test_parse('--- title: Hello --- <h1>Hello World</h1>')
    test_parse('<script>console.log("hi")</script>')
    test_parse('<style>body { color: red; }</style>')
    test_parse('<Fragment><div>test</div></Fragment>')
