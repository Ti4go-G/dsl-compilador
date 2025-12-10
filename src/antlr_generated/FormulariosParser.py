# Generated from grammar/Formularios.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,3,3,43,8,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,5,5,5,52,8,5,10,5,12,5,
        55,9,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,9,10,55,0,15,1,0,0,0,2,20,
        1,0,0,0,4,31,1,0,0,0,6,37,1,0,0,0,8,48,1,0,0,0,10,53,1,0,0,0,12,
        14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,
        0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,21,5,
        1,0,0,21,22,5,11,0,0,22,26,5,2,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,
        28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,
        0,29,30,5,3,0,0,30,3,1,0,0,0,31,32,5,4,0,0,32,33,5,11,0,0,33,34,
        5,5,0,0,34,35,3,6,3,0,35,36,3,10,5,0,36,5,1,0,0,0,37,46,5,11,0,0,
        38,39,5,6,0,0,39,42,3,8,4,0,40,41,5,7,0,0,41,43,3,8,4,0,42,40,1,
        0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,8,0,0,45,47,1,0,0,0,46,
        38,1,0,0,0,46,47,1,0,0,0,47,7,1,0,0,0,48,49,5,12,0,0,49,9,1,0,0,
        0,50,52,7,0,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,11,1,0,0,0,55,53,1,0,0,0,5,15,26,42,46,53
    ]

class FormulariosParser ( Parser ):

    grammarFileName = "Formularios.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'formulario'", "'{'", "'}'", "'campo'", 
                     "':'", "'('", "','", "')'", "'obrigatorio'", "'unico'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OBRIGATORIO", "UNICO", "ID", "INT", 
                      "WS", "COMMENT" ]

    RULE_arquivo = 0
    RULE_formulario = 1
    RULE_campo = 2
    RULE_tipo = 3
    RULE_param = 4
    RULE_flags = 5

    ruleNames =  [ "arquivo", "formulario", "campo", "tipo", "param", "flags" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    OBRIGATORIO=9
    UNICO=10
    ID=11
    INT=12
    WS=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ArquivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FormulariosParser.EOF, 0)

        def formulario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulariosParser.FormularioContext)
            else:
                return self.getTypedRuleContext(FormulariosParser.FormularioContext,i)


        def getRuleIndex(self):
            return FormulariosParser.RULE_arquivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArquivo" ):
                listener.enterArquivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArquivo" ):
                listener.exitArquivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArquivo" ):
                return visitor.visitArquivo(self)
            else:
                return visitor.visitChildren(self)




    def arquivo(self):

        localctx = FormulariosParser.ArquivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_arquivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 12
                self.formulario()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(FormulariosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormularioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FormulariosParser.ID, 0)

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulariosParser.CampoContext)
            else:
                return self.getTypedRuleContext(FormulariosParser.CampoContext,i)


        def getRuleIndex(self):
            return FormulariosParser.RULE_formulario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormulario" ):
                listener.enterFormulario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormulario" ):
                listener.exitFormulario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormulario" ):
                return visitor.visitFormulario(self)
            else:
                return visitor.visitChildren(self)




    def formulario(self):

        localctx = FormulariosParser.FormularioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formulario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(FormulariosParser.T__0)
            self.state = 21
            self.match(FormulariosParser.ID)
            self.state = 22
            self.match(FormulariosParser.T__1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 23
                self.campo()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(FormulariosParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FormulariosParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(FormulariosParser.TipoContext,0)


        def flags(self):
            return self.getTypedRuleContext(FormulariosParser.FlagsContext,0)


        def getRuleIndex(self):
            return FormulariosParser.RULE_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo" ):
                listener.enterCampo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo" ):
                listener.exitCampo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampo" ):
                return visitor.visitCampo(self)
            else:
                return visitor.visitChildren(self)




    def campo(self):

        localctx = FormulariosParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_campo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(FormulariosParser.T__3)
            self.state = 32
            self.match(FormulariosParser.ID)
            self.state = 33
            self.match(FormulariosParser.T__4)
            self.state = 34
            self.tipo()
            self.state = 35
            self.flags()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FormulariosParser.ID, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulariosParser.ParamContext)
            else:
                return self.getTypedRuleContext(FormulariosParser.ParamContext,i)


        def getRuleIndex(self):
            return FormulariosParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = FormulariosParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(FormulariosParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 38
                self.match(FormulariosParser.T__5)
                self.state = 39
                self.param()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 40
                    self.match(FormulariosParser.T__6)
                    self.state = 41
                    self.param()


                self.state = 44
                self.match(FormulariosParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(FormulariosParser.INT, 0)

        def getRuleIndex(self):
            return FormulariosParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = FormulariosParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(FormulariosParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBRIGATORIO(self, i:int=None):
            if i is None:
                return self.getTokens(FormulariosParser.OBRIGATORIO)
            else:
                return self.getToken(FormulariosParser.OBRIGATORIO, i)

        def UNICO(self, i:int=None):
            if i is None:
                return self.getTokens(FormulariosParser.UNICO)
            else:
                return self.getToken(FormulariosParser.UNICO, i)

        def getRuleIndex(self):
            return FormulariosParser.RULE_flags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlags" ):
                listener.enterFlags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlags" ):
                listener.exitFlags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlags" ):
                return visitor.visitFlags(self)
            else:
                return visitor.visitChildren(self)




    def flags(self):

        localctx = FormulariosParser.FlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_flags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





