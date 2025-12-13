def generate_js_validator(form_name: str, fields: list) -> str:
    js = f"// Validador para {form_name}\n"
    js += f"function validate{form_name}(data) {{\n"
    js += "  const errors = [];\n\n"
    
    for field in fields:
        js += f"  // Validação: {field.name}\n"

        if field.custom_error:
            msg_required = f"'{field.custom_error}'"
        else:
            msg_required = f"'{field.name} é obrigatório'"

        if field.required:
            js += f"  if (!data.{field.name}) {{\n"
            js += f"    errors.push({msg_required});\n"
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
    code = ""
    name = field.name
    
    def get_msg(default_msg):
        return f"'{field.custom_error}'" if field.custom_error else f"'{default_msg}'"

    if field.field_type == 'texto':
        if field.min_val:
            msg = get_msg(f"{name} deve ter no mínimo {int(field.min_val)} caracteres")
            code += f"{indent}if (data.{name}.length < {field.min_val}) errors.push({msg});\n"
        if field.max_val:
            msg = get_msg(f"{name} deve ter no máximo {int(field.max_val)} caracteres")
            code += f"{indent}if (data.{name}.length > {field.max_val}) errors.push({msg});\n"
    
    elif field.field_type == 'email':
        msg = get_msg(f"{name} deve ser um email válido")
        code += f"{indent}const emailRegex = /^[^@]+@[^@]+\\.[^@]+$/;\n"
        code += f"{indent}if (!emailRegex.test(data.{name})) errors.push({msg});\n"
    
    elif field.field_type == 'inteiro':
        msg_type = get_msg(f"{name} deve ser número inteiro")
        code += f"{indent}if (!Number.isInteger(data.{name})) errors.push({msg_type});\n"
        
        if field.min_val is not None:
            msg = get_msg(f"{name} deve ser no mínimo {int(field.min_val)}")
            code += f"{indent}if (data.{name} < {field.min_val}) errors.push({msg});\n"
        if field.max_val is not None:
            msg = get_msg(f"{name} deve ser no máximo {int(field.max_val)}")
            code += f"{indent}if (data.{name} > {field.max_val}) errors.push({msg});\n"
    
    return code

def generate_js_module(forms: dict) -> str:
    js = "/**\n * Validadores gerados automaticamente\n */\n\n"
    for form_name, fields in forms.items():
        js += generate_js_validator(form_name, fields) + "\n\n"
    
    if len(forms) > 0:
        js += "module.exports = {\n"
        validators = [f"  validate{name}" for name in forms.keys()]
        js += ",\n".join(validators)
        js += "\n};\n"
    return js