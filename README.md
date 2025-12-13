# DSL de Geração de Formulários (Fullstack)

## 👥 Equipe
* Tiago Gaspar
* Weslley Mattheus

## 💡 Motivação
No desenvolvimento de sistemas corporativos, a criação de telas de cadastro (CRUDs) é uma tarefa repetitiva e propensa a erros. Frequentemente, as regras de validação (como "campo obrigatório" ou "tamanho máximo") precisam ser duplicadas manualmente no Frontend (JavaScript) e no Backend (SQL/Banco de Dados).
**Problema:** Se uma regra muda, o desenvolvedor precisa lembrar de alterar em dois lugares diferentes.
**Solução:** Nossa DSL centraliza a definição do formulário em um único arquivo `.dsl`. O compilador lê essa definição e gera automaticamente tanto o código de validação JavaScript quanto o script de criação de tabelas SQL, garantindo consistência e economizando tempo.

## 📖 Descrição da Linguagem
A linguagem foi projetada para ser declarativa e legível, assemelhando-se a uma estrutura JSON simplificada ou a definição de structs em C, mas focada em regras de negócio.
Exemplo: `campo email: texto(10, 100) obrigatorio` define, em uma linha, o nome, tipo, limites de caracteres e obrigatoriedade.

# DSL de Formulários - Compilador

Este projeto implementa um compilador para uma **Linguagem de Domínio Específico (DSL)** focada na definição de formulários. A partir de uma sintaxe simples e legível, o compilador gera automaticamente:

1.  **Frontend:** Código JavaScript para validação de dados.
2.  **Backend:** Scripts SQL (`CREATE TABLE`) para criação do banco de dados.

## 📂 Estrutura do Projeto

```text
.
├── main.py                # Ponto de entrada (Entry point) do compilador
├── requirements.txt       # Dependências do Python
├── grammar/               
│   └── Formularios.g4     # Arquivo da gramática ANTLR4
├── input/                 # Coloque seus arquivos .dsl aqui
├── output/                # Os arquivos .js e .sql gerados aparecerão aqui
└── src/
    ├── dsl_parser.py      # Lógica de parsing e transformação (Listener)
    ├── sql_generator.py   # Gerador de código SQL
    ├── js_generator.py    # Gerador de código JavaScript
    └── antlr_generated/   # Classes geradas automaticamente pelo ANTLR