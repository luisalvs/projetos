from utilitarios import *

# categorias
categorias_receitas = cadastrar_categoria('Receitas')
categorias_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# transacoes
cadastrar_transacao(
    descricao='Salario Jan/2024',
    valor=1000.0,
    categoria=categorias_receitas
)

cadastrar_transacao(
    descricao='Freelancer',
    valor=500.0,
    categoria=categorias_receitas
)

cadastrar_transacao(
    descricao='Ingresso Show',
    valor=-350.0,
    categoria=categoria_lazer
)

total = saldo_total()
print('Saldo Total:', total)