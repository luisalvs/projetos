import json
import os

# Cadastro de contas → cada conta com número, titular e saldo.

banco = []
filename = 'banco.json'

def criar_json():
    with open(filename, 'w') as file:
        json.dump(banco, file, indent=4)

def carregar_json():
    global banco
    if os.path.exists(filename):
        with open(filename) as file:
            banco = json.load(file)
    else:
        banco = []

def cadastrar_conta():
    carregar_json()
    numero = int(input('Número da conta: '))
    titular = input('Titular da conta: ')
    saldo = float(input('Saldo da conta: '))

    banco.append({'Numero': numero, 'Titular': titular, 'Saldo': saldo})
    criar_json()

# Depósito → adicionar valor a uma conta.
def depositar():
    carregar_json()
    numero_conta = int(input('Digite o número da conta: '))
    for conta in banco:
        if conta['Numero'] == numero_conta:
            deposito = float(input('Digite o valor do deposito: '))
            conta['Saldo'] += deposito
            criar_json()
            return
    print('Conta não encontrada')       
    

# Saque → retirar valor, se houver saldo suficiente.

# Transferência → passar valor de uma conta para outra.

# Listar contas → ver todas as contas e saldos.


