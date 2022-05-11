import json

from olga.constants import STANDARD
from olga.task.task import Task

#Printando as lista de Tasks na tela
def draw_tasks(tasklist):
    if len(tasklist) > 0:
        print('='*30)
        for index, task in enumerate(tasklist):
            print(f'|| {index+1} || {task["task"]} || {task["due"]} || {task["created"]} ||')
            print('='*30)
    else:
        print('\nNão há tarefas ativas')
    print('')
    pass

# CREATING A NEW TASK
def create_task(tasklist):
    task = input('Insira o nome da Tarefa: ')
    due = input('Insira para quando é a tarefa: ')
    new_task = Task(name=task, due=due)
    new_task.add(tasklist)

# DELETE TASK
def delete_task(tasklist, taskid):
    tasklist.pop(taskid-1)
    return tasklist

# STORAGING TASKS IN JSON FILE
def save_tasks(tasklist, user):
    if len(tasklist) > 0:
        with open('user.json', 'w', encoding='utf-8') as uhand:
            cont = STANDARD.replace('user', user)
            cont = STANDARD.replace('<t>', json.dumps(tasklist, indent=4, ensure_ascii=False))
            uhand.write(cont)
    else:
        print('Não há Tasks à serem salvas.\n Sair?\n1-Sim\n2-Não')
        dec = input()
        if dec == 1:
            print("Até logo!")
        else:
            from olga.handlers import user_action, clear_console
            clear_console()
            user_action(tasklist, user)
