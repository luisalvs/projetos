from modulo import *

print("Bem vindo ao LSV BANCO")
print("Como podemos te ajudar hoje?")

exit = True
while exit:
    print("""
1 - Cadastrar conta
2 - Realizar um depósito
3 - Realizar um saque
4 - Realizar um transferência
5 - Listar contas
6 - Sair           
""")
    
    opcoes = int(input('Escolha uma das opções acima: '))
    match opcoes:
        case 1:
            cadastrar_conta()
        case 2:
            depositar()
        case 3:
            saque()
        case 4:
            transferencia()
        case 5:
            listar_contas()
        case _:
            exit = False