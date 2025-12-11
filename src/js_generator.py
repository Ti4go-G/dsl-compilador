def generate_js_validator(form_name: str, fields: list) -> str:
    
    js = f"// Validador para {form_name}\n"
    js += f"function validate{form_name}(data) {{\n"
    js += "  const errors = [];\n\n"
    
    for field in fields:
        js += f"  // Validação: {field.name}\n"
        
        if field.required:
            js += f"  if (!data.{field.name}) {{\n"
            js += f"    errors.push('{field.name} é obrigatório');\n"
            js += f"  }} else {{\n"
            js += _generate_field_validation(field, indent="    ")
            js += "  }\n\n"
        else:
            js += f"  if (data.{field.name}) {{\n"
            js += _generate_field_validation(field, indent="    ")
            js += "  }\n\n"
    
    js += "  return {\n"
    js += "    valid: errors.length === 0,\n"
    js += "    errors: errors\n"
    js += "  };\n"
    js += "}\n"
    
    return js


def _generate_field_validation(field, indent="  ") -> str:
    """Gera validação específica para cada tipo de campo"""
    code = ""
    name = field.name
    
    if field.field_type == 'texto':
        if field.min_val:
            code += f"{indent}if (data.{name}.length < {field.min_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ter no mínimo {field.min_val} caracteres');\n"
            code += f"{indent}}}\n"
        if field.max_val:
            code += f"{indent}if (data.{name}.length > {field.max_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ter no máximo {field.max_val} caracteres');\n"
            code += f"{indent}}}\n"
    
    elif field.field_type == 'email':
        code += f"{indent}const emailRegex = /^[^@]+@[^@]+\\.[^@]+$/;\n"
        code += f"{indent}if (!emailRegex.test(data.{name})) {{\n"
        code += f"{indent}  errors.push('{name} deve ser um email válido');\n"
        code += f"{indent}}}\n"
    
    elif field.field_type == 'inteiro':
        code += f"{indent}if (!Number.isInteger(data.{name})) {{\n"
        code += f"{indent}  errors.push('{name} deve ser número inteiro');\n"
        code += f"{indent}}}\n"
        if field.min_val is not None:
            code += f"{indent}if (data.{name} < {field.min_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ser no mínimo {field.min_val}');\n"
            code += f"{indent}}}\n"
        if field.max_val is not None:
            code += f"{indent}if (data.{name} > {field.max_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ser no máximo {field.max_val}');\n"
            code += f"{indent}}}\n"
    
    elif field.field_type == 'decimal':
        code += f"{indent}if (typeof data.{name} !== 'number') {{\n"
        code += f"{indent}  errors.push('{name} deve ser um número');\n"
        code += f"{indent}}}\n"
        if field.min_val is not None:
            code += f"{indent}if (data.{name} < {field.min_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ser no mínimo {field.min_val}');\n"
            code += f"{indent}}}\n"
        if field.max_val is not None:
            code += f"{indent}if (data.{name} > {field.max_val}) {{\n"
            code += f"{indent}  errors.push('{name} deve ser no máximo {field.max_val}');\n"
            code += f"{indent}}}\n"
    
    elif field.field_type == 'booleano':
        code += f"{indent}if (typeof data.{name} !== 'boolean') {{\n"
        code += f"{indent}  errors.push('{name} deve ser verdadeiro ou falso');\n"
        code += f"{indent}}}\n"
    
    return code


def generate_js_module(forms: dict) -> str:
    """Gera módulo JavaScript completo com todas as validações"""
    
    js = "/**\n"
    js += " * Validadores gerados automaticamente pela DSL\n"
    js += " * Não editar manualmente\n"
    js += " */\n\n"
    
    for form_name, fields in forms.items():
        js += generate_js_validator(form_name, fields)
        js += "\n\n"
    
    js += "// Exportar validadores\n"
    if len(forms) > 0:
        js += "module.exports = {\n"
        validators = [f"  validate{name}" for name in forms.keys()]
        js += ",\n".join(validators)
        js += "\n};\n"
    
    return js

