# DSL de Validação e Geração de SQL

Ferramenta completa para definir formulários, gerar tabelas SQL e validadores JavaScript automaticamente.

## 🚀 Como Usar

1. Edite o arquivo `formularios.dsl` com suas definições
2. Execute o script principal:

```powershell
python main.py
```

Isso irá gerar automaticamente:
- `formularios.sql`: Script SQL para criar as tabelas
- `formularios.js`: Módulo JavaScript com funções de validação

## 📝 Sintaxe da DSL

A sintaxe é simples e declarativa, agora em português:

```dsl
formulario NomeDoFormulario {
    campo nome_campo: tipo(min, max) flags
}
```

### Tipos Suportados

| Tipo | Descrição | Parâmetros `(min, max)` |
|------|-----------|-------------------------|
| `texto` | Texto curto | Comprimento min/max |
| `textolongo` | Texto longo | - |
| `inteiro` | Número inteiro | Valor min/max |
| `decimal` | Número decimal | Valor min/max |
| `email` | E-mail válido | - |
| `booleano` | Verdadeiro/Falso | - |
| `data` | Data | - |

### Flags

- `obrigatorio`: Torna o campo obrigatório
- `unico`: Cria índice único no banco de dados (SQL)

## 💡 Exemplo Completo

```dsl
formulario Usuario {
    campo nome: texto(3, 100) obrigatorio
    campo email: email unico obrigatorio
    campo idade: inteiro(18, 120)
    campo ativo: booleano obrigatorio
}

formulario Produto {
    campo nome: texto(3, 200) obrigatorio
    campo preco: decimal(0, 99999) obrigatorio
}
```

## 📂 Estrutura do Projeto e Explicação do Código

O projeto é modular, separado em responsabilidades específicas:

### 1. `main.py` (Orquestrador)
É o ponto de entrada da aplicação.
- **Função**: Lê o arquivo `.dsl`, chama o parser e distribui os dados para os geradores.
- **Fluxo**:
    1. Carrega o arquivo `.dsl`.
    2. Usa `dsl_parser.py` para converter o texto em objetos Python.
    3. Gera SQL usando `sql_generator.py`.
    4. Gera JavaScript usando `js_generator.py`.

### 2. `dsl_parser.py` (Interpretador)
Responsável por ler a sintaxe da DSL e transformá-la em estrutura de dados.
- **Tecnologia**: Usa **ANTLR** para análise léxica e sintática.
- **Classe `Field`**: Uma `dataclass` que armazena metadados de cada campo (nome, tipo, validações).
- **Funcionamento**:
    - Usa a gramática definida em `Formularios.g4`.
    - Percorre a árvore sintática gerada pelo ANTLR usando um `Listener`.
    - Extrai definições de `campo` e seus parâmetros.

### 3. `sql_generator.py` (Gerador de Banco de Dados)
Converte as definições da DSL em comandos DDL (Data Definition Language) para MySQL/MariaDB.
- **Mapeamento**: Converte tipos da DSL para tipos SQL (ex: `texto` -> `VARCHAR`, `inteiro` -> `INT`).
- **Automação**: Adiciona automaticamente:
    - `id`: Chave primária auto-incremento.
    - `created_at` e `updated_at`: Timestamps para auditoria.
    - `UNIQUE KEY`: Para campos marcados com a flag `unico`.

### 4. `js_generator.py` (Frontend)
Gera código para o navegador (Client-side).
- **Validação JS**: Cria funções `validateNomeFormulario(data)` que retornam `{ valid: boolean, errors: [] }`.
    - Implementa as mesmas regras de validação do Python (tamanho, tipo, regex de email).
