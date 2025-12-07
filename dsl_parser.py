"""
Parser simplificado para a DSL de validação de formulários
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Field:
    """Representa um campo do formulário"""
    name: str
    field_type: str
    min_val: Optional[int] = None
    max_val: Optional[int] = None
    required: bool = False
    unique: bool = False


def parse_dsl(dsl_code: str) -> dict:
    """
    Parse o código DSL linha por linha com detecção de erros.
    Retorna {form_name: [Field]} ou lança SyntaxError.
    """
    forms = {}
    current_form = None
    
    lines = dsl_code.splitlines()
    
    for i, line in enumerate(lines):
        line_num = i + 1
        original_line = line
        
        # Remove comentários e espaços
        line = re.sub(r'#.*$', '', line).strip()
        
        if not line:
            continue
            
        # 1. Início de formulário: formulario Nome {
        form_match = re.match(r'^formulario\s+(\w+)\s*\{$', line)
        if form_match:
            if current_form:
                raise SyntaxError(f"Linha {line_num}: Formulário aninhado não permitido. Feche '{current_form}' antes de abrir outro.")
            
            current_form = form_match.group(1)
            forms[current_form] = []
            continue
            
        # 2. Fim de formulário: }
        if line == '}':
            if not current_form:
                raise SyntaxError(f"Linha {line_num}: Fechamento de bloco '}}' encontrado sem formulário aberto.")
            current_form = None
            continue
            
        # 3. Definição de campo (apenas dentro de formulário)
        if current_form:
            # campo nome: tipo(min, max) flags
            field_match = re.match(r'^campo\s+(\w+)\s*:\s*(\w+)(?:\(([^)]+)\))?(.*)$', line)
            
            if field_match:
                name, field_type, params, flags_str = field_match.groups()
                
                # Parse parâmetros (min, max)
                min_val = max_val = None
                if params:
                    try:
                        parts = [p.strip() for p in params.split(',')]
                        if len(parts) > 0 and parts[0]:
                            min_val = int(parts[0])
                        if len(parts) > 1 and parts[1]:
                            max_val = int(parts[1])
                    except ValueError:
                        raise SyntaxError(f"Linha {line_num}: Parâmetros inválidos em '{params}'. Use números inteiros.")
                
                fields = forms[current_form]
                fields.append(Field(
                    name=name,
                    field_type=field_type,
                    min_val=min_val,
                    max_val=max_val,
                    required='obrigatorio' in flags_str,
                    unique='unico' in flags_str
                ))
                continue
            else:
                # Se está dentro de um form e não é 'campo ...', é erro
                raise SyntaxError(f"Linha {line_num}: Sintaxe inválida no formulário '{current_form}'.\n   Esperado: 'campo nome: tipo(min,max) flags'\n   Encontrado: '{original_line.strip()}'")
        
        # 4. Se chegou aqui, é texto fora de formulário que não foi reconhecido
        raise SyntaxError(f"Linha {line_num}: Comando não reconhecido fora de bloco.\n   Encontrado: '{original_line.strip()}'")

    if current_form:
        raise SyntaxError(f"Erro: O arquivo terminou com o formulário '{current_form}' aberto. Faltou fechar com '}}'.")
    
    return forms


def _parse_fields(form_body: str) -> list:
    """(Depreciado) Mantido apenas para compatibilidade se necessário, mas não usado pelo novo parser"""
    return []