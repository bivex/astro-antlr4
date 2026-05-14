"""Comprehensive test suite for the Astro ANTLR4 grammar."""

import sys
import os
import traceback
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Add parent dir to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tests.AstroLexer import AstroLexer
from tests.AstroParser import AstroParser


class ErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"L{line}:{column} {msg}")


def parse(input_text):
    """Parse input and return (tree, errors)."""
    lexer = AstroLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = AstroParser(stream)

    collector = ErrorCollector()
    parser.removeErrorListeners()
    parser.addErrorListener(collector)

    tree = parser.astroFile()
    return tree, collector.errors


def test(name, input_text, expect_errors=False):
    """Run a single test case."""
    tree, errors = parse(input_text)
    passed = (len(errors) == 0) if not expect_errors else (len(errors) > 0)
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {name}")
    if not passed and not expect_errors:
        for e in errors:
            print(f"         ERROR: {e}")
    if not passed and expect_errors:
        print(f"         Expected errors but parsed clean")
    return passed


def run_all():
    total = 0
    passed = 0

    # ── Frontmatter ──────────────────────────────────────────
    print("\n== Frontmatter ==")

    total += 1; passed += test("Empty frontmatter",
        "---\n---\n")
    total += 1; passed += test("Simple frontmatter",
        "---\ntitle: Hello\n---\n")
    total += 1; passed += test("Multi-line frontmatter",
        "---\ntitle: Test\nlayout: Base\nprops: { a: 1 }\n---\n")
    total += 1; passed += test("Frontmatter with import",
        "---\nimport Layout from '../layouts/Base.astro';\n---\n")
    total += 1; passed += test("Frontmatter with TypeScript types",
        "---\ninterface Props {\n  name: string;\n}\n---\n")

    # ── HTML Elements ────────────────────────────────────────
    print("\n== HTML Elements ==")

    total += 1; passed += test("Simple div",
        "---\n---\n<div>hello</div>")
    total += 1; passed += test("Nested elements",
        "---\n---\n<div><p>text</p></div>")
    total += 1; passed += test("Deeply nested",
        "---\n---\n<div><section><article><p>deep</p></article></section></div>")
    total += 1; passed += test("Void/self-closing tag",
        "---\n---\n<br />")
    total += 1; passed += test("Self-closing img",
        "---\n---\n<img src=\"photo.jpg\" />")
    total += 1; passed += test("Void tag with attributes",
        "---\n---\n<input type=\"text\" name=\"foo\" />")
    total += 1; passed += test("Multiple siblings",
        "---\n---\n<h1>Title</h1>\n<p>Para 1</p>\n<p>Para 2</p>")
    total += 1; passed += test("Void tag hr",
        "---\n---\n<hr />")

    # ── Attributes ───────────────────────────────────────────
    print("\n== Attributes ==")

    total += 1; passed += test("Double-quoted attribute",
        "---\n---\n<div class=\"container\">text</div>")
    total += 1; passed += test("Single-quoted attribute",
        "---\n---\n<div class='container'>text</div>")
    total += 1; passed += test("Boolean attribute",
        "---\n---\n<input disabled />")
    total += 1; passed += test("Multiple attributes",
        "---\n---\n<a href=\"/link\" class=\"link\" id=\"main\">text</a>")
    total += 1; passed += test("Expression attribute",
        "---\n---\n<div class={activeClass}>text</div>")
    total += 1; passed += test("Expression attribute with object",
        "---\n---\n<div class:list={[\"base\", { active: true }]}>text</div>")
    total += 1; passed += test("Spread attribute",
        "---\n---\n<div {...props}>text</div>")
    total += 1; passed += test("Colon attribute name",
        "---\n---\n<div :class=\"foo\">text</div>")

    # ── Astro Directives ─────────────────────────────────────
    print("\n== Astro Directives ==")

    total += 1; passed += test("client:load directive",
        "---\n---\n<ReactComp client:load />")
    total += 1; passed += test("client:only directive with expression",
        "---\n---\n<ReactComp client:only=\"react\" />")
    total += 1; passed += test("client:visible directive",
        "---\n---\n<HeavyComp client:visible />")
    total += 1; passed += test("client:idle directive",
        "---\n---\n<MyWidget client:idle />")
    total += 1; passed += test("set:html directive",
        "---\n---\n<div set:html={content} />")
    total += 1; passed += test("set:text directive",
        "---\n---\n<span set:text={label} />")
    total += 1; passed += test("is:raw directive",
        "---\n---\n<div is:raw>{rawContent}</div>")
    total += 1; passed += test("transition:animate directive",
        "---\n---\n<div transition:animate=\"fade\">content</div>")
    total += 1; passed += test("transition:name directive",
        "---\n---\n<h1 transition:name=\"title\">Hello</h1>")
    total += 1; passed += test("transition:persist directive",
        "---\n---\n<nav transition:persist>links</nav>")
    total += 1; passed += test("slot attribute",
        "---\n---\n<div slot=\"header\">content</div>")

    # ── Components ───────────────────────────────────────────
    print("\n== Components ==")

    total += 1; passed += test("Simple component",
        "---\n---\n<Layout>content</Layout>")
    total += 1; passed += test("Self-closing component",
        "---\n---\n<Header />")
    total += 1; passed += test("Component with props",
        "---\n---\n<Card title=\"Hello\" count={5} />")
    total += 1; passed += test("Nested components",
        "---\n---\n<Layout><Header /><Main><Footer /></Main></Layout>")
    total += 1; passed += test("Dotted component name",
        "---\n---\n<Ui.Card>content</Ui.Card>")
    total += 1; passed += test("Component with spread",
        "---\n---\n<Button {...props} />")
    total += 1; passed += test("Component with children",
        "---\n---\n<Layout>\n  <h1>Title</h1>\n  <p>Content</p>\n</Layout>")

    # ── Fragment ─────────────────────────────────────────────
    print("\n== Fragment ==")

    total += 1; passed += test("Fragment element",
        "---\n---\n<Fragment>content</Fragment>")
    total += 1; passed += test("Fragment self-close",
        "---\n---\n<Fragment />")
    total += 1; passed += test("Fragment with children",
        "---\n---\n<Fragment><div>a</div><div>b</div></Fragment>")

    # ── Script blocks ────────────────────────────────────────
    print("\n== Script Blocks ==")

    total += 1; passed += test("Empty script",
        "---\n---\n<script></script>")
    total += 1; passed += test("Script with code",
        "---\n---\n<script>\n  console.log('hello');\n</script>")
    total += 1; passed += test("Script with comparison operators",
        "---\n---\n<script>\n  if (a < b && b > c) { console.log('ok'); }\n</script>")
    total += 1; passed += test("Script with template literals",
        "---\n---\n<script>\n  const msg = `Hello ${name}`;\n</script>")
    total += 1; passed += test("Script with nested braces",
        "---\n---\n<script>\n  const obj = { a: { b: 1 } };\n</script>")
    total += 1; passed += test("Script with string containing angle brackets",
        "---\n---\n<script>\n  console.log(\"<div>test</div>\");\n</script>")
    total += 1; passed += test("Script with comments",
        "---\n---\n<script>\n  // line comment\n  /* block comment */\n</script>")
    total += 1; passed += test("Script with attributes",
        "---\n---\n<script src=\"app.js\"></script>")

    # ── Style blocks ─────────────────────────────────────────
    print("\n== Style Blocks ==")

    total += 1; passed += test("Empty style",
        "---\n---\n<style></style>")
    total += 1; passed += test("Style with rules",
        "---\n---\n<style>\n  h1 { color: red; }\n  .container { margin: 0; }\n</style>")
    total += 1; passed += test("Style with selectors and pseudo",
        "---\n---\n<style>\n  a:hover { color: blue; }\n  ::selection { background: yellow; }\n</style>")
    total += 1; passed += test("Style with media query",
        "---\n---\n<style>\n  @media (max-width: 600px) {\n    .container { width: 100%; }\n  }\n</style>")
    total += 1; passed += test("Style with attribute",
        "---\n---\n<style is:global>\n  body { margin: 0; }\n</style>")

    # ── Template Expressions ─────────────────────────────────
    print("\n== Template Expressions ==")

    total += 1; passed += test("Simple expression",
        "---\n---\n<div>{title}</div>")
    total += 1; passed += test("Expression with ternary",
        "---\n---\n<div>{active ? 'yes' : 'no'}</div>")
    total += 1; passed += test("Expression with map",
        "---\n---\n<ul>{items.map(item => <li>{item}</li>)}</ul>")
    total += 1; passed += test("Expression with nested braces",
        "---\n---\n<div>{obj && obj.key}</div>")
    total += 1; passed += test("Expression with string literals",
        "---\n---\n<div>{`Hello ${name}`}</div>")
    total += 1; passed += test("Expression with function call",
        "---\n---\n<div>{formatDate(date)}</div>")
    total += 1; passed += test("Multiple expressions",
        "---\n---\n<div>{a} and {b}</div>")

    # ── Comments ─────────────────────────────────────────────
    print("\n== Comments ==")

    total += 1; passed += test("HTML comment",
        "---\n---\n<div><!-- comment -->text</div>")
    total += 1; passed += test("HTML comment multiline",
        "---\n---\n<div><!--\n  multiline\n  comment\n-->text</div>")
    total += 1; passed += test("JSX-style expression comment",
        "---\n---\n<div>{/* a comment */}</div>")

    # ── Plain text ───────────────────────────────────────────
    print("\n== Plain Text ==")

    total += 1; passed += test("Text only, no elements",
        "---\n---\nHello world")
    total += 1; passed += test("Text between elements",
        "---\n---\n<h1>Title</h1>\nSubtitle text\n<p>para</p>")

    # ── Mixed content ────────────────────────────────────────
    print("\n== Mixed / Complex ==")

    total += 1; passed += test("Full page layout",
"""---
title: My Page
layout: Base
---
<Layout title={title}>
  <header>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
    </nav>
  </header>
  <main>
    <h1>Welcome</h1>
    <p>This is {name}'s page.</p>
    <ul>
      {items.map((item) => (
        <li>{item}</li>
      ))}
    </ul>
  </main>
  <Footer year={2024} />
</Layout>
""")

    total += 1; passed += test("Component with script and style",
"""---
---
<Layout>
  <script>
    const count = 0;
    function increment() { count++; }
  </script>
  <style>
    .counter { color: blue; }
  </style>
  <div class="counter">{count}</div>
</Layout>
""")

    total += 1; passed += test("Slot pattern",
"""---
---
<Layout>
  <div slot="header">
    <h1>Header</h1>
  </div>
  <div slot="footer">
    <p>Footer</p>
  </div>
</Layout>
""")

    total += 1; passed += test("Nested expressions in attributes",
"""---
---
<div
  class:list={["base", { active: isActive, hidden: isHidden }]}
  style={`color: ${color}`}
>
  content
</div>
""")

    total += 1; passed += test("Multiple scripts",
"""---
---
<script>const a = 1;</script>
<script src="external.js"></script>
<div>{a}</div>
""")

    total += 1; passed += test("Component with client directive and children",
"""---
---
<InteractiveChart client:visible data={chartData}>
  <p>Loading...</p>
</InteractiveChart>
""")

    # ── Edge cases ───────────────────────────────────────────
    print("\n== Edge Cases ==")

    total += 1; passed += test("No frontmatter just HTML",
        "<div>hello</div>")
    total += 1; passed += test("Empty after frontmatter",
        "---\n---\n")
    total += 1; passed += test("Self-closing void element",
        "---\n---\n<input />")
    total += 1; passed += test("Boolean attribute on component",
        "---\n---\n<Modal open />")
    total += 1; passed += test("Component with many props",
        "---\n---\n<Card title=\"hi\" count={5} active disabled {...rest} />")

    # ── Summary ──────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{total} passed")
    if passed == total:
        print("All tests passed!")
    else:
        print(f"{total - passed} test(s) FAILED")
    return passed == total


if __name__ == '__main__':
    success = run_all()
    sys.exit(0 if success else 1)
