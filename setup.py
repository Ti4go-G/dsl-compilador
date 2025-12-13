import os

if not os.path.exists('input'):
    os.makedirs('input')

with open(os.path.join('input', 'teste.dsl'), 'w', encoding='utf-8') as f:
    f.write("form Teste { nome: texto }")

print("Arquivo criado com sucesso!")