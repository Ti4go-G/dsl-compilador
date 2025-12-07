"""
DSL simplificada para Validação e Geração de SQL

Exemplo:
    formulario Usuario {
        campo nome: texto(3, 100) obrigatorio
        campo email: email unico obrigatorio
        campo senha: texto(8, 50) obrigatorio
    }
"""

from dsl_parser import parse_dsl
from sql_generator import generate_sql


class FormDSL:
    """Interface principal da DSL"""
    
    def __init__(self, dsl_code: str):
        self.forms = parse_dsl(dsl_code)
    
    def get_sql(self, form_name: str) -> str:
        """Gera SQL CREATE TABLE"""
        if form_name not in self.forms:
            raise ValueError(f"Formulário '{form_name}' não existe")
        
        return generate_sql(form_name.lower(), self.forms[form_name])
    
    def list_forms(self) -> list:
        """Lista formulários disponíveis"""
        return list(self.forms.keys())
