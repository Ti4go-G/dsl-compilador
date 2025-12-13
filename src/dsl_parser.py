from dataclasses import dataclass
from typing import Optional
from antlr4 import *

from .antlr_generated.FormulariosLexer import FormulariosLexer
from .antlr_generated.FormulariosParser import FormulariosParser
from .antlr_generated.FormulariosListener import FormulariosListener

@dataclass
class Field:
    """Representa um campo do formulário"""
    name: str
    field_type: str
    min_val: Optional[float] = None
    max_val: Optional[float] = None
    required: bool = False
    unique: bool = False
    custom_error: Optional[str] = None

class FormLoader(FormulariosListener):
    def __init__(self):
        self.forms = {}
        self.current_form_name = None

    def enterFormulario(self, ctx):
        self.current_form_name = ctx.ID().getText()
        self.forms[self.current_form_name] = []

    def exitCampo(self, ctx):
        name = ctx.ID().getText()

        type_ctx = ctx.tipo()
        field_type = type_ctx.ID().getText()
        
        min_val = max_val = None
        params = type_ctx.param()
        if params:
            min_val = float(params[0].getText())
            if len(params) > 1:
                max_val = float(params[1].getText())

        custom_error = None

        flags_text = ""
        if ctx.flags():
            flags_text = ctx.flags().getText()
            
        required = 'obrigatorio' in flags_text
        unique = 'unico' in flags_text

        field = Field(name, field_type, min_val, max_val, required, unique, custom_error)
        self.forms[self.current_form_name].append(field)

def parse_dsl(dsl_code: str) -> dict:
    input_stream = InputStream(dsl_code)
    lexer = FormulariosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormulariosParser(stream)
    tree = parser.arquivo()
    
    loader = FormLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)
    
    return loader.forms