from random import randint
from time import sleep

def sorteio(lista, valores):
    print(f'Sorteando {valores} valor(es) da lista: ', end= '')
    for c in range(0, valores):
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
    print(f'Somando os valores pares: {lista}, temos {soma}.')

while True:
    valores = input('Quantos numeros você quer sortear? ')
    if valores.isnumeric():
        valores = int(valores)
        break
    else:
        print('Por favor, digite um valor valido!')


numero = []
sorteio(numero, valores)
sortepar(numero) 