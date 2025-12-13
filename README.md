# 📝 EasyForm - DSL de Geração de Formulários

Este projeto implementa o compilador da **EasyForm**, uma **Linguagem de Domínio Específico (DSL)** focada na definição de formulários. O objetivo é automatizar a criação de código repetitivo no desenvolvimento Fullstack.

A partir de uma sintaxe simples e legível, o compilador gera automaticamente:
1.  **Frontend:** Código JavaScript para validação de dados.
2.  **Backend:** Scripts SQL (`CREATE TABLE`) para criação do banco de dados.

## 👥 Equipe
*   **Tiago Gaspar**
*   **Weslley Mattheus**

---

## 💡 Motivação
No desenvolvimento de sistemas corporativos, a criação de telas de cadastro (CRUDs) é uma tarefa repetitiva e propensa a erros. Frequentemente, as regras de validação (como "campo obrigatório" ou "tamanho máximo") precisam ser duplicadas manualmente no Frontend e no Backend.

*   **Problema:** Se uma regra muda, o desenvolvedor precisa lembrar de alterar em dois lugares diferentes (JS e SQL).
*   **Solução:** A **EasyForm** centraliza a definição em um único arquivo `.easy`. O compilador garante a consistência entre as camadas e economiza tempo de codificação.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
*   **Python 3.8+** instalado.
*   **Java (JDK 11+)** instalado (Necessário apenas para gerar os arquivos do ANTLR).

### 1. Instalação das Dependências
No terminal, instale a biblioteca de runtime do ANTLR para Python:

```bash
pip install antlr4-python3-runtime
```

### 2. Geração do Parser (ANTLR)
Antes de rodar o projeto pela primeira vez (ou se alterar a gramática), é necessário gerar os arquivos Python a partir do arquivo `.g4`.

Certifique-se de que o arquivo `antlr-4.13.2-complete.jar` está na raiz do projeto e execute:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/antlr_generated grammar/Formularios.g4
```

### 3. Compilação
Crie ou edite o arquivo com a extensão `.easy` na pasta `input/` (ex: `input/meu_projeto.easy`) e adicione suas definições.

Em seguida, execute o compilador:

```bash
python main.py
```

Os arquivos gerados estarão na pasta `output`:
*   `output/formularios.sql`
*   `output/formularios.js`

---

## 📘 Guia da Linguagem EasyForm

A **EasyForm** utiliza uma estrutura declarativa simples.

### Estrutura Básica
```easy
formulario NomeDoFormulario {
    campo nome_do_campo: tipo(parametros) flags
}
```

### Tipos de Dados Suportados
| Tipo EasyForm | Parâmetros | Tradução SQL | Validação JS |
| :--- | :--- | :--- | :--- |
| `texto` | `(min, max)` | `VARCHAR(max)` | Tamanho min/max |
| `inteiro` | `(min, max)` | `INT` | Valor min/max |
| `decimal` | `(min, max)` | `DECIMAL(10,2)` | Valor min/max |
| `email` | - | `VARCHAR(255)` | Regex de E-mail |
| `booleano`| - | `BOOLEAN` | - |
| `data` | - | `DATE` | - |

### Flags (Opcionais)
*   `obrigatorio`: Adiciona `NOT NULL` no SQL e verificação de preenchimento no JS.
*   `unico`: Adiciona restrição `UNIQUE` no SQL.

---

## 💻 Exemplo de Código

### Entrada (`input/formularios.easy`)
```easy
formulario Usuario {
    campo nome: texto(3, 100) obrigatorio
    campo email: email unico obrigatorio
    campo idade: inteiro(18, 120)
}
```

### Saída Gerada

**SQL (`output/formularios.sql`):**
```sql
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    idade INT
);
```

**JavaScript (`output/formularios.js`):**
```javascript
export function validateUsuario(data) {
    const errors = [];
    if (!data.nome) errors.push('nome é obrigatório');
    if (data.nome && data.nome.length < 3) errors.push('nome deve ter no mínimo 3 caracteres');
    // ... validações de email e idade ...
    return errors;
}
```

---

## 📂 Estrutura de Arquivos

```text
.
├── main.py                # Orquestrador do compilador
├── grammar/               
│   └── Formularios.g4     # Definição formal da gramática (ANTLR)
├── src/
│   ├── easy_parser.py     # Listener que transforma a Árvore Sintática em Objetos
│   ├── sql_generator.py   # Backend: Gera código SQL
│   ├── js_generator.py    # Backend: Gera código JavaScript
│   └── antlr_generated/   # (Gerado) Lexer e Parser do ANTLR
├── input/                 # Arquivos fonte (.easy)
└── output/                # Arquivos compilados (.sql, .js)
```