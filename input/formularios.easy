# Formulário de cadastro de usuário
formulario Usuario {
    campo nome: texto(3, 100) obrigatorio
    campo email: email unico obrigatorio
    campo telefone: texto(10, 15)
    campo cpf: texto(11, 11) unico obrigatorio
    campo data_nascimento: texto(10, 10) obrigatorio
    campo senha: texto(8, 50) obrigatorio
    campo ativo: booleano obrigatorio
}

# Formulário de endereço
formulario Endereco {
    campo usuario_id: inteiro(1, 999999) obrigatorio
    campo rua: texto(5, 200) obrigatorio
    campo numero: texto(1, 10) obrigatorio
    campo complemento: texto(0, 100)
    campo bairro: texto(3, 100) obrigatorio
    campo cidade: texto(3, 100) obrigatorio
    campo estado: texto(2, 2) obrigatorio
    campo cep: texto(8, 8) obrigatorio
}

# Formulário de produto
formulario Produto {
    campo nome: texto(3, 200) obrigatorio
    campo descricao: textolongo
    campo preco: decimal(0, 999999) obrigatorio
    campo estoque: inteiro(0, 10000)
    campo categoria_id: inteiro(1, 999999) obrigatorio
    campo codigo_barras: texto(13, 13) unico
    campo ativo: booleano obrigatorio
}

formulario Login {
    campo email: email msg "Por favor, insira um e-mail corporativo válido" obrigatorio
    campo senha: texto(6, 20) msg "A senha deve ter entre 6 e 20 caracteres" obrigatorio
}