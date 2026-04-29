# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
import os

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

array = []

# OBJETOS:
print('Pessoa 1')
pessoa1 = Pessoa(nome=input('Nome: ').capitalize(), idade=int(input('Idade: ')))
array.append(pessoa1)
os.system('cls' if os.name == 'nt' else 'clear')

print('Pessoa 2')
pessoa2 = Pessoa(nome=input('Nome: ').capitalize(), idade=int(input('Idade: ')))
array.append(pessoa2)
os.system('cls' if os.name == 'nt' else 'clear')

# Converter objetos para dicionário
dados = []
for pessoa in array:
    dados.append({
        "nome": pessoa.nome,
        "idade": pessoa.idade
    })

# Salvar JSON
caminho = 'Pessoa.json'
with open(caminho, 'w', encoding='utf8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    