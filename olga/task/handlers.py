from olga.task.task import Task

#Recupera as tasks do arquivo .csv
def get_tasks(handle):
    pass

#Printando as lista de Tasks na tela
def draw_tasks(tasklist):
    if len(tasklist) > 0:
        print('='*30)
        for task in tasklist:
            print(f'|| {task[0]} || {task[1]} || {task[2]} ||')
            print('='*30)
    else:
        print('\nNão há tarefas ativas')
    print('')

#Criando uma nova Task
def create_task(tasklist):
    task = input('Insira o nome da Tarefa: ')
    due = input('Insira para quando é a tarefa: ')
    new_task = Task(name=task, due=due)
    return new_task