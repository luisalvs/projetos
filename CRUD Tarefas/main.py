import json

tasks = []
filename = 'task.json'

def create_json():
    with open (filename, 'w') as arquivo:
        json.dump(tasks, arquivo, indent=4)

def load_json():
    with open (filename, 'r') as arquivo:
        x = json.load(arquivo)
        print(x)

def create_task():
    task_id = int(input('ID: '))
    task_name = input('Tarefa: ')
    tasks.append({'ID': task_id, 'Tarefa': task_name})

def load_tasks():
    for task in tasks:
        return task
    load_json()

def update_taks():
    ...
    
