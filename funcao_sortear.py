from random import randint
from time import sleep

def sorteio(lista, valor):
    if valor == 1:
        print(f'Sorteando {valor} valor da lista: ', end= '')
    else:
        print(f'Sorteando {valor} valor(es) da lista: ', end= '')
    for c in range(0, valor):
        n = randint(0, 10)
        numero.append(n)
        print(n, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def sortepar(lista):
    soma = 0
    pares = []
    for item in lista:
        if item % 2 == 0:
            soma += item
            pares.append(item)
    print(f'Somando os valores pares temos: {soma}. Que são: ', end='')
    for j in pares:
        print(j, end=' ')
    print('')


def sorteimpar(lista):
    soma = 0
    impares = []
    for item in lista:
        if item % 2 == 1:
            soma += item
            impares.append(item)
    print(f'Somando os valores impares temos: {soma}. Que são: ', end='')
    for j in impares:
        print(j, end=' ')
    print('')



while True:
    valores = input('Quantos numeros você quer sortear? ')

    if valores.isnumeric():
        valores = int(valores)
        if valores == 0:
            print('Por favor, digite um valor maior que 0!')
        else:
            break
    else:
        print('Por favor, digite um valor valido!')


numero = []
sorteio(numero, valores)
sortepar(numero) 
sorteimpar(numero)