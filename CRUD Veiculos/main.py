import json
import os

carros = []
filename = 'carros.json'

def criar_json():
    with open (filename, 'w') as arquivo:
        json.dump(carros, arquivo, indent=4)

def carregar_json():
    global carros
    if os.path.exists(filename): # se o arquivo existir
        with open(filename) as arquivo:
            carros = json.load(arquivo)
    else:
        carros = []

def cadastrar_veiculo():
    carregar_json() # carrega dados existentes antes de adicionar
    marca = input('\nMarca: ')
    modelo = input('Modelo: ')
    cor = input('Cor: ')
    ano = int(input('Ano: '))
    placa = input('Placa: ').upper()

    carros.append({'Marca': marca, 'Modelo': modelo, 'Cor': cor, 'Ano': ano, 'Placa': placa })
    criar_json() # salva a lista atualizada de carros

def listar_veiculos():
    carregar_json()
    for i, carro in enumerate(carros, 1):
        print(f'\nVeículo {i}\n')
        for chave, valor in carro.items():
            print(f"{chave}: {valor}")

def buscar_pela_placa():
    carregar_json()
    placa = input('Placa: ').upper()
    for carro in carros:
        if carro["Placa"] == placa:
            print(carro)
            return
    print('Carro não encontrado.')

def remover_veiculo():
    carregar_json()
    placa = input('Digite a placa: ').upper()
    for carro in carros:
        if carro['Placa'] == placa:
            carros.remove(carro)
            criar_json()  # salva a lista atualizada
            print('Carro removido com sucesso.')
            return
    print('Carro não encontrado')

