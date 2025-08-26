
current_users = ['Luis', 'carlos', 'lucas', 'PEDRO', 'thiago']

new_users = ['pedro', 'luis', 'alves', 'matheus', 'paulo']

for user in new_users:
    if user in str(current_users).lower():
        print(f'Usuário {user.title()} usado')
    else:
        print(f'Usuário {user.title()} disponível')

numbers = range(1, 10)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    elif number == 4:
        print(f'{number}th')
    elif number == 5:
        print(f'{number}th')
    elif number == 6:
        print(f'{number}th')
    elif number == 7:
        print(f'{number}th')
    elif number == 8:
        print(f'{number}th')
    elif number == 9:
        print(f'{number}th')

