import sys
from pathlib import Path
from src.easy_parser import parse_easyform
from src.sql_generator import generate_sql
from src.js_generator import generate_js_module

def processar_easyform(arquivo: str):
    """Processa arquivo .easy e gera SQL + JavaScript"""
    caminho = Path(arquivo)
    
    if not caminho.exists():
        print(f"[ERRO] Arquivo não encontrado: {arquivo}")
        return
    
    print(f"[INFO] Processando: {caminho.name}")
    print("=" * 70)
    
    try:
        easy_code = caminho.read_text(encoding='utf-8')
        forms = parse_easyform(easy_code)
    except SyntaxError as e:
        print(f"\n[ERRO DE SINTAXE] Ocorreu um erro ao ler o arquivo EasyForm:")
        print(f"{e}")
        return
    except Exception as e:
        print(f"\n[ERRO INESPERADO] {e}")
        return
    
    print(f"\n[OK] {len(forms)} formulário(s) encontrado(s):")
    for nome in forms:
        print(f"  - {nome}")
    
    Path('output').mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 70)
    print("[INFO] SQL GERADO")
    print("=" * 70)

    sql_output = []
    for nome, fields in forms.items():
        sql = generate_sql(nome.lower(), fields)
        print(f"\n-- Tabela: {nome}")
        print(sql)
        sql_output.append(f"-- Tabela: {nome}\n{sql}\n")
    
    arquivo_sql = Path('output') / f"{caminho.stem}.sql"
    arquivo_sql.write_text(
        "-- SQL gerado automaticamente\n"
        f"-- Fonte: {caminho.name}\n\n" +
        "".join(sql_output),
        encoding='utf-8'
    )
    print(f"[OK] SQL salvo em: {arquivo_sql}")
    
    print("\n" + "=" * 70)
    print("[INFO] JAVASCRIPT GERADO")
    print("=" * 70)
    
    js_code = generate_js_module(forms)
    
    arquivo_js = Path('output') / f"{caminho.stem}.js"
    arquivo_js.write_text(js_code, encoding='utf-8')
    
    print(f"\n{js_code[:500]}...")
    print(f"\n[OK] JavaScript salvo em: {arquivo_js}")

def main():

    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        pasta_input = Path('input')

        if not pasta_input.exists():
            pasta_input.mkdir()
            print("[AVISO] Pasta 'input/' não existia e foi criada.")
            print("Por favor, coloque seu arquivo .easy dentro dela e tente novamente.")
            return
        arquivos_easy = list(Path('input').glob('*.easy'))
        
        if not arquivos_easy:
            print("[ERRO] A pasta 'input/' está vazia.")
            print("Crie um arquivo (ex: teste.easy) dentro dela.")
            return
        
        arquivo = arquivos_easy[0]
    
    processar_easyform(arquivo)
    
    print("\n" + "=" * 70)
    print("[OK] GERAÇÃO CONCLUÍDA")
    print("=" * 70)
    print("\nArquivos gerados:")
    print("  - *.sql  - Tabelas do banco de dados")
    print("  - *.js   - Validadores JavaScript")


if __name__ == "__main__":
    main()
