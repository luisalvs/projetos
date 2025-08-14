import json
import os
from datetime import datetime

# ==== Funções de utilidade ====
def carregar_dados(arquivo, default):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ==== Cadastro de produtos ====
def cadastrar_produto():
    produtos = carregar_dados("produtos.json", [])
    codigo = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))

    # Verifica se já existe
    for p in produtos:
        if p["codigo"] == codigo:
            print("❌ Código já cadastrado!")
            return

    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "estoque": estoque})
    salvar_dados("produtos.json", produtos)
    print("✅ Produto cadastrado com sucesso!")

# ==== Listar produtos ====
def listar_produtos():
    produtos = carregar_dados("produtos.json", [])
    if not produtos:
        print("📦 Nenhum produto cadastrado.")
        return
    print("\n=== Lista de Produtos ===")
    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} | R${p['preco']:.2f} | Estoque: {p['estoque']}")

# ==== Buscar produto ====
def buscar_produto():
    produtos = carregar_dados("produtos.json", [])
    termo = input("Digite nome ou código: ").lower()
    encontrados = [p for p in produtos if termo in p["nome"].lower() or termo == str(p["codigo"])]
    
    if encontrados:
        for p in encontrados:
            print(f"{p['codigo']} - {p['nome']} | R${p['preco']:.2f} | Estoque: {p['estoque']}")
    else:
        print("❌ Produto não encontrado.")

# ==== Registrar venda ====
def registrar_venda():
    produtos = carregar_dados("produtos.json", [])
    vendas = carregar_dados("vendas.json", [])

    carrinho = []
    while True:
        codigo = input("Código do produto (ou ENTER para finalizar): ")
        if codigo == "":
            break

        codigo = int(codigo)
        produto = next((p for p in produtos if p["codigo"] == codigo), None)
        if not produto:
            print("❌ Produto não encontrado.")
            continue

        quantidade = int(input("Quantidade: "))
        if quantidade > produto["estoque"]:
            print("⚠ Estoque insuficiente.")
            continue

        carrinho.append({
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "quantidade": quantidade,
            "preco_unit": produto["preco"]
        })

        produto["estoque"] -= quantidade

    if not carrinho:
        print("🛒 Nenhum item no carrinho.")
        return

    total = sum(item["quantidade"] * item["preco_unit"] for item in carrinho)
    vendas.append({
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "itens": carrinho,
        "total": total
    })

    salvar_dados("produtos.json", produtos)
    salvar_dados("vendas.json", vendas)

    print(f"✅ Venda registrada! Total: R${total:.2f}")

# ==== Relatórios ====
def relatorios():
    vendas = carregar_dados("vendas.json", [])
    if not vendas:
        print("📄 Nenhuma venda registrada.")
        return

    total_dia = sum(v["total"] for v in vendas)
    print(f"💰 Total vendido: R${total_dia:.2f}")

    # Produtos mais vendidos
    contador = {}
    for venda in vendas:
        for item in venda["itens"]:
            contador[item["nome"]] = contador.get(item["nome"], 0) + item["quantidade"]

    mais_vendidos = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    print("\n🏆 Produtos mais vendidos:")
    for nome, qtd in mais_vendidos:
        print(f"{nome}: {qtd} un.")

# ==== Menu principal ====
def menu():
    while True:
        print("\n=== MERCEARIA DO SEU JOÃO ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Buscar produto")
        print("4. Registrar venda")
        print("5. Relatórios")
        print("0. Sair")

        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            registrar_venda()
        elif opcao == "5":
            relatorios()
        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
