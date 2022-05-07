import os
import json

from olga.constants import STANDARD
from olga.task import handlers


# CONSOLE MANIPULATION FUNCTIONALITY
def clear_console():
    os.system('cls')


# USER RELATED FUNCTIONALITY
def user_verify():
    try:
        user_hand = open('user.json', encoding='utf-8')
        cont = json.loads(user_hand.read())
        user = cont["name"]
        tasklist = cont["tasks"]
        user_hand.close()
        clear_console()
        print(f'Bem vindo, {user}!\n')
        return tasklist, user
    except:
        tasklist = []
        user = input('Você é novo por aqui... Qual o seu nome? ')
        clear_console()
        print(f'Bem vindo, {user}!')
        return tasklist, user

def user_action(tasklist, user):
    print('O que deseja fazer?\n\n1-Adicionar uma nova tarefa\n2-Salvar e sair')
    dec = input()
    if dec == '1':
        handlers.create_task(tasklist)
        clear_console()
        handlers.draw_tasks(tasklist)
        user_action(tasklist, user)
    else: 
        handlers.save_tasks(tasklist, user)


# MAIN APP RUN
def run():
    print('Olá! Aqui é Olga.\nBem vindx ao teste da Assistente Olga')
    tasklist, user = user_verify()
    handlers.draw_tasks(tasklist)
    user_action(tasklist, user)
    
