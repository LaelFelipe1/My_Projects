# Leia um valor inteiro. A seguir, calcule o menor número de notas 
#possíveis (cédulas) no qual o valor pode ser decomposto. 
#As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
#A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas 
# de cada tipo necessárias, conforme o exemplo fornecido.
#Não esqueça de imprimir o fim de linha após cada linha, 
#caso contrário seu programa apresentará a mensagem: 
# “Presentation Error”.


def decompor():
    n1 = int(input('>>> '))
    notas = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
    }
    
    
    for nota in notas:
        notas[nota] = n1 // nota
        n1 = n1 % nota
    for nota in notas:
        print(f'{notas[nota]} nota(s) de R$ {nota},00')
        
decompor()
