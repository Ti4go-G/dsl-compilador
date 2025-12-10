from dataclasses import dataclass
from typing import Optional
from antlr4 import *

try:
    from FormulariosLexer import FormulariosLexer
    from FormulariosParser import FormulariosParser
    from FormulariosListener import FormulariosListener
except ImportError:
    # Mock classes para evitar erro de importação imediato se os arquivos não existirem
    # Isso permite que o usuário leia o código sem crashar, mas vai falhar ao rodar
    class FormulariosLexer: pass
    class FormulariosParser: 
        class FormularioContext: pass
        class CampoContext: pass
    class FormulariosListener: pass


@dataclass
class Field:
    """Representa um campo do formulário"""
    name: str
    field_type: str
    min_val: Optional[int] = None
    max_val: Optional[int] = None
    required: bool = False
    unique: bool = False


class FormLoader(FormulariosListener):
    """Listener que percorre a árvore sintática e monta os objetos"""
    
    def __init__(self):
        self.forms = {}
        self.current_form_name = None

    def enterFormulario(self, ctx):
        self.current_form_name = ctx.ID().getText()
        self.forms[self.current_form_name] = []

    def exitCampo(self, ctx):
        name = ctx.ID().getText()
        
        # Tipo e parametros
        type_ctx = ctx.tipo()
        field_type = type_ctx.ID().getText()
        
        min_val = max_val = None
        params = type_ctx.param()
        if params:
            min_val = int(params[0].getText())
            if len(params) > 1:
                max_val = int(params[1].getText())

        # Flags
        flags_text = ctx.flags().getText()
        required = 'obrigatorio' in flags_text
        unique = 'unico' in flags_text

        field = Field(name, field_type, min_val, max_val, required, unique)
        self.forms[self.current_form_name].append(field)


def parse_dsl(dsl_code: str) -> dict:
    """
    Parse o código DSL usando ANTLR.
    Retorna {form_name: [Field]}
    """
    input_stream = InputStream(dsl_code)
    lexer = FormulariosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormulariosParser(stream)
    
    # Inicia o parse pela regra raiz 'arquivo'
    tree = parser.arquivo()
    
    # Percorre a árvore
    loader = FormLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)
    
    return loader.forms