from turtle import clear
from olga.constants import NEWTASK, STANDARD
from olga.task.task import Task

#Printando as lista de Tasks na tela
def draw_tasks(tasklist):
    if len(tasklist) > 0:
        print('='*30)
        for task in tasklist:
            print(f'|| {task["task"]} || {task["due"]} || {task["created"]} ||')
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

# STORAGING TASKS IN JSON FILE
def save_tasks(tasklist, user):
    if len(tasklist) > 0:
        tosave= []
        for task in tasklist:
            save = NEWTASK.replace('ntask', task['task'])
            save = save.replace('ndue', task['due'])
            save = save.replace('ncreated', task['created'])
            tosave.append(save)
        tosave = ','.join(tosave)
        uhand = open('user.json', 'w', encoding='utf-8')
        cont = STANDARD.replace('user', user)
        cont = cont.replace('<t>', tosave)
        uhand.write(cont)
        uhand.close()
    else:
        print('Não há Tasks à serem salvas.\n Sair?\n1-Sim\n2-Não')
        dec = input()
        if dec == 1:
            quit()
        else:
            from olga.handlers import user_action, clear_console
            clear_console()
            user_action(tasklist, user)
