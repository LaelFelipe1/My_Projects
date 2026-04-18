import os
import time
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def lista_dinamica():
    todo = []
    refazer = []

    while True:
        limpar()
        print("Digite uma tarefa ou 'C' para comandos.")
        tarefa = input(">>> ")

        if tarefa.lower() == 'c':
            comandos(todo, refazer)
            continue

        todo.append(tarefa)
        refazer.clear()  # limpa o refazer quando adiciona algo novo

def comandos(todo, refazer):
    limpar()
    print("COMANDOS: (L)istar, (D)esfazer, (R)efazer")
    cmd = input(">>> ").lower()

    # LISTAR
    if cmd == 'l':
        print("Lista:", todo)
        time.sleep(2)

    # DESFAZER
    elif cmd == 'd':
        if not todo:
            print("Nada para desfazer.")
        else:
            item = todo.pop()
            refazer.append(item)
            print(f"Desfeito: {item}")
        time.sleep(2)

    # REFAZER
    elif cmd == 'r':
        if not refazer:
            print("Nada para refazer.")
        else:
            item = refazer.pop()
            todo.append(item)
            print(f"Refeito: {item}")
        time.sleep(2)

lista_dinamica()