import os

from olga.constants import STANDARD
from olga.task import handlers

def clear_console():
    os.system('cls')

def user_verify():
    try:
        user_hand = open('user.csv')
        cont = user_hand.read()
        user = cont[2:cont.find(';')]
        tasklist = [(1, 2, 3), ('abc', 3, 'yeepee')]
        user_hand.close()
        clear_console()
        print(f'Bem vindo, {user}!\n')
        return tasklist
    except:
        user_hand = open('user.csv', 'w')
        tasklist = []
        user = input('Você é novo por aqui... Qual o seu nome? ')
        cont = STANDARD.replace('user', user)
        user_hand.write(cont)
        clear_console()
        print(f'Bem vindo, {user}!')
        return tasklist

def user_action():
    print('O que deseja fazer?\n\n1-Adicionar uma nova tarefa\n2-Sair')
    dec = input()
    if dec == '1':
        handlers.create_task()
        handlers.draw_tasks()
        user_action()
    else: 
        pass

def run():
    print('Olá! Aqui é Olga.\nBem vindx ao teste da Assistente Olga')
    tasklist = user_verify()
    handlers.draw_tasks(tasklist)
    user_action()
    
