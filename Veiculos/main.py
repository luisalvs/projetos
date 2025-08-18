import json

veiculos = []
filename = 'veiculos.json'

def criar_json():
    with open(filename, 'w') as arquivo: 
        json.dump(veiculos, arquivo, indent=4)

def carregar_json():
    with open(filename, 'r') as arquivo:
        v = json.load(arquivo)
        print(v)
        
def cadastrar_veiculos():
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    ano = int(input('Ano: '))
    placa = input('Placa: ')
    cor = input('Cor: ')

    veiculos.append({'Marca': marca, 'Modelo': modelo, 'Ano': ano, 'Placa': placa, 'Cor': cor})

def listar_veiculos():
    for veiculo in veiculos:
        print(veiculo)

def buscar_por_placa():
    placa = input('Placa: ')
    for veiculo in veiculos:
        if veiculo['Placa'] == placa:
            print(veiculo)
    print('Veículo não encontrado')

def remover_por_placa():
    placa = input('Placa: ')
    for veiculo in veiculos:
        if veiculo['Placa'] == placa:
            veiculos.remove(veiculo)
            print('Veículo removido com sucesso.')
            return
    print('Veículo não encontrado.')


while True:
    print('\n🚗 SISTEMA DE CONTROLE DE VEÍCULOS 🚗\n')
    
    print('1. Cadastrar veículo\n2. Listar veículos\n3. Buscar por placa\n4. Remover veículo\n5. Sair\n')
            
    opcoes = int(input('Digite um número: '))

    if opcoes == 1:
        cadastrar_veiculos()
        criar_json()
    elif opcoes == 2:
        listar_veiculos()
        carregar_json()
    elif opcoes == 3:
        buscar_por_placa()
        carregar_json()
    elif opcoes == 4:
        remover_por_placa()
        criar_json()
    else:
        break