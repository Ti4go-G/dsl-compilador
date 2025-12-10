"""
Script principal - Gera SQL e JavaScript a partir do .dsl
"""

import sys
from pathlib import Path
from dsl_parser import parse_dsl
from sql_generator import generate_sql
from js_generator import generate_js_module


def processar_dsl(arquivo: str):
    """Processa arquivo .dsl e gera SQL + JavaScript"""
    
    # Ler arquivo
    caminho = Path(arquivo)
    if not caminho.exists():
        print(f"[ERRO] Arquivo não encontrado: {arquivo}")
        return
    
    print(f"[INFO] Processando: {caminho.name}")
    print("=" * 70)
    
    try:
        dsl_code = caminho.read_text(encoding='utf-8')
        forms = parse_dsl(dsl_code)
    except SyntaxError as e:
        print(f"\n[ERRO DE SINTAXE] Ocorreu um erro ao ler o arquivo DSL:")
        print(f"{e}")
        return
    except Exception as e:
        print(f"\n[ERRO INESPERADO] {e}")
        return
    
    # Listar formulários
    print(f"\n[OK] {len(forms)} formulário(s) encontrado(s):")
    for nome in forms:
        print(f"  - {nome}")
    
    # ========== GERAR SQL ==========
    print("\n" + "=" * 70)
    print("[INFO] SQL GERADO")
    print("=" * 70)
    
    sql_output = []
    for nome, fields in forms.items():
        sql = generate_sql(nome.lower(), fields)
        print(f"\n-- Tabela: {nome}")
        print(sql)
        sql_output.append(f"-- Tabela: {nome}\n{sql}\n")
    
    # Salvar SQL
    arquivo_sql = caminho.with_suffix('.sql')
    arquivo_sql.write_text(
        "-- SQL gerado automaticamente\n"
        f"-- Fonte: {caminho.name}\n\n" +
        "".join(sql_output),
        encoding='utf-8'
    )
    print(f"[OK] SQL salvo em: {arquivo_sql.name}")
    
    # ========== GERAR JAVASCRIPT ==========
    print("\n" + "=" * 70)
    print("[INFO] JAVASCRIPT GERADO")
    print("=" * 70)
    
    js_code = generate_js_module(forms)
    
    arquivo_js = caminho.with_suffix('.js')
    arquivo_js.write_text(js_code, encoding='utf-8')
    
    print(f"\n{js_code[:500]}...")
    print(f"\n[OK] JavaScript salvo em: {arquivo_js.name}")


def main():
    """Função principal"""
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        # Procura arquivo .dsl
        arquivos_dsl = list(Path('.').glob('*.dsl'))
        
        if not arquivos_dsl:
            print("[ERRO] Nenhum arquivo .dsl encontrado")
            print("\nUso: python main.py [arquivo.dsl]")
            return
        
        arquivo = arquivos_dsl[0]
    
    processar_dsl(arquivo)
    
    print("\n" + "=" * 70)
    print("[OK] GERAÇÃO CONCLUÍDA")
    print("=" * 70)
    print("\nArquivos gerados:")
    print("  - *.sql  - Tabelas do banco de dados")
    print("  - *.js   - Validadores JavaScript")


if __name__ == "__main__":
    main()