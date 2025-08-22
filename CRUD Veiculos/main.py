import json

carros = []
filename = 'carros.json'

def criar_json():
    with open (filename, 'w') as arquivo:
        json.dump(carros, arquivo, indent=4)

def carregar_json():
    global carros
    with open(filename) as arquivo:
        carros = json.load(arquivo)
    
def cadastrar_veiculo():
    carregar_json() # carrega dados existentes antes de adicionar
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    cor = input('Cor: ')
    ano = int(input('Ano: '))
    placa = input('Placa: ').upper()

    carros.append({'Marca': marca, 'Modelo': modelo, 'Cor': cor, 'Ano': ano, 'Placa': placa })
    criar_json() # salva a lista atualizada de carros

def buscar_pela_placa():
    carregar_json()
    placa = input('Placa: ').upper()
    for carro in carros:
        if carro["Placa"] == placa:
            print(carro)
            return
    print('Carro não encontrado.')