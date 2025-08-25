from main import *

while True:

    print('\n🚗🚗🚗 Sistema de cadastro de veículo 🚗🚗🚗')
    print('\n1 - Cadastrar veículo\n2 - Buscar veículo\n3 - Listar veículos\n4 - Remover veículo\n')

    opcoes = int(input('Digite uma opção acima: '))

    if opcoes == 1:
        criar_json()
        cadastrar_veiculo()
    elif opcoes == 2:
        buscar_pela_placa()
    elif opcoes == 3:
        listar_veiculos()
    else:
        remover_veiculo()

    