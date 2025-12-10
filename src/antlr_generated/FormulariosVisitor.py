# Generated from grammar/Formularios.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FormulariosParser import FormulariosParser
else:
    from FormulariosParser import FormulariosParser

# This class defines a complete generic visitor for a parse tree produced by FormulariosParser.

class FormulariosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulariosParser#arquivo.
    def visitArquivo(self, ctx:FormulariosParser.ArquivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulariosParser#formulario.
    def visitFormulario(self, ctx:FormulariosParser.FormularioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulariosParser#campo.
    def visitCampo(self, ctx:FormulariosParser.CampoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulariosParser#tipo.
    def visitTipo(self, ctx:FormulariosParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulariosParser#param.
    def visitParam(self, ctx:FormulariosParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulariosParser#flags.
    def visitFlags(self, ctx:FormulariosParser.FlagsContext):
        return self.visitChildren(ctx)



del FormulariosParser