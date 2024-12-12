from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end= '')
    for c in range(0, 5):
        n = randint(0, 10)
        numero.append(n)
        print(n, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def sortepar(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    print(f'Somando os valores pares de {lista}, temos {soma}')


numero = []
sorteio(numero)
sortepar(numero) 