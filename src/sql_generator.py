SQL_TYPES = {
    'texto': 'VARCHAR',
    'email': 'VARCHAR',
    'inteiro': 'INT',
    'decimal': 'DECIMAL(10,2)',
    'booleano': 'BOOLEAN',
    'data': 'DATE',
    'datahora': 'DATETIME',
    'textolongo': 'TEXT'
}


def generate_sql(table_name: str, fields: list) -> str:
    """Gera CREATE TABLE a partir dos campos"""
    lines = [f"CREATE TABLE {table_name} (", "    id INT AUTO_INCREMENT PRIMARY KEY"]
    
    for field in fields:
        lines.append(_field_to_sql(field))
    
    for field in fields:
        if field.unique:
            lines.append(f"    UNIQUE KEY unique_{field.name} ({field.name})")
    
    lines.append("    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    lines.append("    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    
    return ",\n".join(lines) + "\n);\n"


def _field_to_sql(field) -> str:
    """Converte um campo para definição SQL"""
    sql_type = SQL_TYPES.get(field.field_type, 'VARCHAR')
    
    if sql_type == 'VARCHAR':
        size = field.max_val or 255
        sql_type = f"VARCHAR({size})"
    
    sql = f"    {field.name} {sql_type}"
    
    if field.required:
        sql += " NOT NULL"
    
    return sql