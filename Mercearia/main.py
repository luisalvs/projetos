
produtos = []

### Cadastrar produtos


def cadastrar_produto():
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    produtos.append({"nome": nome, "preço": preco, "quantidade": quantidade})


def listar_produtos():
    for p in produtos:
        print(p)


cadastrar_produto()
