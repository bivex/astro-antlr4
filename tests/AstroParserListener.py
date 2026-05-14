# Generated from AstroParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AstroParser import AstroParser
else:
    from AstroParser import AstroParser

# This class defines a complete listener for a parse tree produced by AstroParser.
class AstroParserListener(ParseTreeListener):

    # Enter a parse tree produced by AstroParser#astroFile.
    def enterAstroFile(self, ctx:AstroParser.AstroFileContext):
        pass

    # Exit a parse tree produced by AstroParser#astroFile.
    def exitAstroFile(self, ctx:AstroParser.AstroFileContext):
        pass


    # Enter a parse tree produced by AstroParser#frontmatter.
    def enterFrontmatter(self, ctx:AstroParser.FrontmatterContext):
        pass

    # Exit a parse tree produced by AstroParser#frontmatter.
    def exitFrontmatter(self, ctx:AstroParser.FrontmatterContext):
        pass


    # Enter a parse tree produced by AstroParser#fmLine.
    def enterFmLine(self, ctx:AstroParser.FmLineContext):
        pass

    # Exit a parse tree produced by AstroParser#fmLine.
    def exitFmLine(self, ctx:AstroParser.FmLineContext):
        pass


    # Enter a parse tree produced by AstroParser#template.
    def enterTemplate(self, ctx:AstroParser.TemplateContext):
        pass

    # Exit a parse tree produced by AstroParser#template.
    def exitTemplate(self, ctx:AstroParser.TemplateContext):
        pass


    # Enter a parse tree produced by AstroParser#templateItem.
    def enterTemplateItem(self, ctx:AstroParser.TemplateItemContext):
        pass

    # Exit a parse tree produced by AstroParser#templateItem.
    def exitTemplateItem(self, ctx:AstroParser.TemplateItemContext):
        pass


    # Enter a parse tree produced by AstroParser#text.
    def enterText(self, ctx:AstroParser.TextContext):
        pass

    # Exit a parse tree produced by AstroParser#text.
    def exitText(self, ctx:AstroParser.TextContext):
        pass


    # Enter a parse tree produced by AstroParser#htmlElement.
    def enterHtmlElement(self, ctx:AstroParser.HtmlElementContext):
        pass

    # Exit a parse tree produced by AstroParser#htmlElement.
    def exitHtmlElement(self, ctx:AstroParser.HtmlElementContext):
        pass


    # Enter a parse tree produced by AstroParser#htmlOpenTag.
    def enterHtmlOpenTag(self, ctx:AstroParser.HtmlOpenTagContext):
        pass

    # Exit a parse tree produced by AstroParser#htmlOpenTag.
    def exitHtmlOpenTag(self, ctx:AstroParser.HtmlOpenTagContext):
        pass


    # Enter a parse tree produced by AstroParser#htmlVoidTag.
    def enterHtmlVoidTag(self, ctx:AstroParser.HtmlVoidTagContext):
        pass

    # Exit a parse tree produced by AstroParser#htmlVoidTag.
    def exitHtmlVoidTag(self, ctx:AstroParser.HtmlVoidTagContext):
        pass


    # Enter a parse tree produced by AstroParser#htmlCloseTag.
    def enterHtmlCloseTag(self, ctx:AstroParser.HtmlCloseTagContext):
        pass

    # Exit a parse tree produced by AstroParser#htmlCloseTag.
    def exitHtmlCloseTag(self, ctx:AstroParser.HtmlCloseTagContext):
        pass


    # Enter a parse tree produced by AstroParser#htmlTagName.
    def enterHtmlTagName(self, ctx:AstroParser.HtmlTagNameContext):
        pass

    # Exit a parse tree produced by AstroParser#htmlTagName.
    def exitHtmlTagName(self, ctx:AstroParser.HtmlTagNameContext):
        pass


    # Enter a parse tree produced by AstroParser#componentElement.
    def enterComponentElement(self, ctx:AstroParser.ComponentElementContext):
        pass

    # Exit a parse tree produced by AstroParser#componentElement.
    def exitComponentElement(self, ctx:AstroParser.ComponentElementContext):
        pass


    # Enter a parse tree produced by AstroParser#componentOpenTag.
    def enterComponentOpenTag(self, ctx:AstroParser.ComponentOpenTagContext):
        pass

    # Exit a parse tree produced by AstroParser#componentOpenTag.
    def exitComponentOpenTag(self, ctx:AstroParser.ComponentOpenTagContext):
        pass


    # Enter a parse tree produced by AstroParser#componentSelfCloseTag.
    def enterComponentSelfCloseTag(self, ctx:AstroParser.ComponentSelfCloseTagContext):
        pass

    # Exit a parse tree produced by AstroParser#componentSelfCloseTag.
    def exitComponentSelfCloseTag(self, ctx:AstroParser.ComponentSelfCloseTagContext):
        pass


    # Enter a parse tree produced by AstroParser#componentCloseTag.
    def enterComponentCloseTag(self, ctx:AstroParser.ComponentCloseTagContext):
        pass

    # Exit a parse tree produced by AstroParser#componentCloseTag.
    def exitComponentCloseTag(self, ctx:AstroParser.ComponentCloseTagContext):
        pass


    # Enter a parse tree produced by AstroParser#componentTagName.
    def enterComponentTagName(self, ctx:AstroParser.ComponentTagNameContext):
        pass

    # Exit a parse tree produced by AstroParser#componentTagName.
    def exitComponentTagName(self, ctx:AstroParser.ComponentTagNameContext):
        pass


    # Enter a parse tree produced by AstroParser#fragmentElement.
    def enterFragmentElement(self, ctx:AstroParser.FragmentElementContext):
        pass

    # Exit a parse tree produced by AstroParser#fragmentElement.
    def exitFragmentElement(self, ctx:AstroParser.FragmentElementContext):
        pass


    # Enter a parse tree produced by AstroParser#fragmentOpenTag.
    def enterFragmentOpenTag(self, ctx:AstroParser.FragmentOpenTagContext):
        pass

    # Exit a parse tree produced by AstroParser#fragmentOpenTag.
    def exitFragmentOpenTag(self, ctx:AstroParser.FragmentOpenTagContext):
        pass


    # Enter a parse tree produced by AstroParser#fragmentSelfCloseTag.
    def enterFragmentSelfCloseTag(self, ctx:AstroParser.FragmentSelfCloseTagContext):
        pass

    # Exit a parse tree produced by AstroParser#fragmentSelfCloseTag.
    def exitFragmentSelfCloseTag(self, ctx:AstroParser.FragmentSelfCloseTagContext):
        pass


    # Enter a parse tree produced by AstroParser#fragmentCloseTag.
    def enterFragmentCloseTag(self, ctx:AstroParser.FragmentCloseTagContext):
        pass

    # Exit a parse tree produced by AstroParser#fragmentCloseTag.
    def exitFragmentCloseTag(self, ctx:AstroParser.FragmentCloseTagContext):
        pass


    # Enter a parse tree produced by AstroParser#styleBlock.
    def enterStyleBlock(self, ctx:AstroParser.StyleBlockContext):
        pass

    # Exit a parse tree produced by AstroParser#styleBlock.
    def exitStyleBlock(self, ctx:AstroParser.StyleBlockContext):
        pass


    # Enter a parse tree produced by AstroParser#scriptBlock.
    def enterScriptBlock(self, ctx:AstroParser.ScriptBlockContext):
        pass

    # Exit a parse tree produced by AstroParser#scriptBlock.
    def exitScriptBlock(self, ctx:AstroParser.ScriptBlockContext):
        pass


    # Enter a parse tree produced by AstroParser#rawTextBlock.
    def enterRawTextBlock(self, ctx:AstroParser.RawTextBlockContext):
        pass

    # Exit a parse tree produced by AstroParser#rawTextBlock.
    def exitRawTextBlock(self, ctx:AstroParser.RawTextBlockContext):
        pass


    # Enter a parse tree produced by AstroParser#rawTagName.
    def enterRawTagName(self, ctx:AstroParser.RawTagNameContext):
        pass

    # Exit a parse tree produced by AstroParser#rawTagName.
    def exitRawTagName(self, ctx:AstroParser.RawTagNameContext):
        pass


    # Enter a parse tree produced by AstroParser#attribute.
    def enterAttribute(self, ctx:AstroParser.AttributeContext):
        pass

    # Exit a parse tree produced by AstroParser#attribute.
    def exitAttribute(self, ctx:AstroParser.AttributeContext):
        pass


    # Enter a parse tree produced by AstroParser#normalAttr.
    def enterNormalAttr(self, ctx:AstroParser.NormalAttrContext):
        pass

    # Exit a parse tree produced by AstroParser#normalAttr.
    def exitNormalAttr(self, ctx:AstroParser.NormalAttrContext):
        pass


    # Enter a parse tree produced by AstroParser#exprAttr.
    def enterExprAttr(self, ctx:AstroParser.ExprAttrContext):
        pass

    # Exit a parse tree produced by AstroParser#exprAttr.
    def exitExprAttr(self, ctx:AstroParser.ExprAttrContext):
        pass


    # Enter a parse tree produced by AstroParser#booleanAttr.
    def enterBooleanAttr(self, ctx:AstroParser.BooleanAttrContext):
        pass

    # Exit a parse tree produced by AstroParser#booleanAttr.
    def exitBooleanAttr(self, ctx:AstroParser.BooleanAttrContext):
        pass


    # Enter a parse tree produced by AstroParser#spreadAttr.
    def enterSpreadAttr(self, ctx:AstroParser.SpreadAttrContext):
        pass

    # Exit a parse tree produced by AstroParser#spreadAttr.
    def exitSpreadAttr(self, ctx:AstroParser.SpreadAttrContext):
        pass


    # Enter a parse tree produced by AstroParser#astroDirectiveAttr.
    def enterAstroDirectiveAttr(self, ctx:AstroParser.AstroDirectiveAttrContext):
        pass

    # Exit a parse tree produced by AstroParser#astroDirectiveAttr.
    def exitAstroDirectiveAttr(self, ctx:AstroParser.AstroDirectiveAttrContext):
        pass


    # Enter a parse tree produced by AstroParser#attrName.
    def enterAttrName(self, ctx:AstroParser.AttrNameContext):
        pass

    # Exit a parse tree produced by AstroParser#attrName.
    def exitAttrName(self, ctx:AstroParser.AttrNameContext):
        pass


    # Enter a parse tree produced by AstroParser#attrValue.
    def enterAttrValue(self, ctx:AstroParser.AttrValueContext):
        pass

    # Exit a parse tree produced by AstroParser#attrValue.
    def exitAttrValue(self, ctx:AstroParser.AttrValueContext):
        pass


    # Enter a parse tree produced by AstroParser#directiveName.
    def enterDirectiveName(self, ctx:AstroParser.DirectiveNameContext):
        pass

    # Exit a parse tree produced by AstroParser#directiveName.
    def exitDirectiveName(self, ctx:AstroParser.DirectiveNameContext):
        pass


    # Enter a parse tree produced by AstroParser#templateExpr.
    def enterTemplateExpr(self, ctx:AstroParser.TemplateExprContext):
        pass

    # Exit a parse tree produced by AstroParser#templateExpr.
    def exitTemplateExpr(self, ctx:AstroParser.TemplateExprContext):
        pass


    # Enter a parse tree produced by AstroParser#exprBody.
    def enterExprBody(self, ctx:AstroParser.ExprBodyContext):
        pass

    # Exit a parse tree produced by AstroParser#exprBody.
    def exitExprBody(self, ctx:AstroParser.ExprBodyContext):
        pass


    # Enter a parse tree produced by AstroParser#exprChunk.
    def enterExprChunk(self, ctx:AstroParser.ExprChunkContext):
        pass

    # Exit a parse tree produced by AstroParser#exprChunk.
    def exitExprChunk(self, ctx:AstroParser.ExprChunkContext):
        pass


    # Enter a parse tree produced by AstroParser#nestedExpr.
    def enterNestedExpr(self, ctx:AstroParser.NestedExprContext):
        pass

    # Exit a parse tree produced by AstroParser#nestedExpr.
    def exitNestedExpr(self, ctx:AstroParser.NestedExprContext):
        pass


    # Enter a parse tree produced by AstroParser#exprComment.
    def enterExprComment(self, ctx:AstroParser.ExprCommentContext):
        pass

    # Exit a parse tree produced by AstroParser#exprComment.
    def exitExprComment(self, ctx:AstroParser.ExprCommentContext):
        pass



del AstroParser