# Generated from grammar/Formularios.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FormulariosParser import FormulariosParser
else:
    from FormulariosParser import FormulariosParser

# This class defines a complete listener for a parse tree produced by FormulariosParser.
class FormulariosListener(ParseTreeListener):

    # Enter a parse tree produced by FormulariosParser#arquivo.
    def enterArquivo(self, ctx:FormulariosParser.ArquivoContext):
        pass

    # Exit a parse tree produced by FormulariosParser#arquivo.
    def exitArquivo(self, ctx:FormulariosParser.ArquivoContext):
        pass


    # Enter a parse tree produced by FormulariosParser#formulario.
    def enterFormulario(self, ctx:FormulariosParser.FormularioContext):
        pass

    # Exit a parse tree produced by FormulariosParser#formulario.
    def exitFormulario(self, ctx:FormulariosParser.FormularioContext):
        pass


    # Enter a parse tree produced by FormulariosParser#campo.
    def enterCampo(self, ctx:FormulariosParser.CampoContext):
        pass

    # Exit a parse tree produced by FormulariosParser#campo.
    def exitCampo(self, ctx:FormulariosParser.CampoContext):
        pass


    # Enter a parse tree produced by FormulariosParser#tipo.
    def enterTipo(self, ctx:FormulariosParser.TipoContext):
        pass

    # Exit a parse tree produced by FormulariosParser#tipo.
    def exitTipo(self, ctx:FormulariosParser.TipoContext):
        pass


    # Enter a parse tree produced by FormulariosParser#param.
    def enterParam(self, ctx:FormulariosParser.ParamContext):
        pass

    # Exit a parse tree produced by FormulariosParser#param.
    def exitParam(self, ctx:FormulariosParser.ParamContext):
        pass


    # Enter a parse tree produced by FormulariosParser#flags.
    def enterFlags(self, ctx:FormulariosParser.FlagsContext):
        pass

    # Exit a parse tree produced by FormulariosParser#flags.
    def exitFlags(self, ctx:FormulariosParser.FlagsContext):
        pass



del FormulariosParser