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
    
    sql = f"CREATE TABLE {table_name} (\n"
    
    columns = ["    id INT AUTO_INCREMENT PRIMARY KEY"]
    
    for field in fields:
        columns.append(_field_to_sql(field))
    
    for field in fields:
        if field.unique:
            columns.append(f"    UNIQUE KEY unique_{field.name} ({field.name})")
    
    columns.append("    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    columns.append("    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    
    sql += ",\n".join(columns)
    sql += "\n);\n"
    
    return sql

def _field_to_sql(field) -> str:
    """Converte um campo para definição SQL"""
    sql_type = SQL_TYPES.get(field.field_type, 'VARCHAR')
    
    if sql_type == 'VARCHAR':
        size = int(field.max_val) if field.max_val else 255
        sql_type = f"VARCHAR({size})"
    
    sql = f"    {field.name} {sql_type}"
    
    if field.required:
        sql += " NOT NULL"
    
    return sql