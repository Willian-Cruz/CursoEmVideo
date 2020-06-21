# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
numeros = [[], [], [], [], [], []]
palpites = []
print('-=' * 30)
print(f'{"GERADOR DE JOGOS MEGA SENA":^56}')
print('-=' * 30)
jogos = int(input('Quantos jogos deseja sortear? '))
for sort in range(1, jogos):
    palpites = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    numeros.clear()
    numeros.append(palpites)

print(f'Os números sugeridos foram: {numeros}')
'''
'''
from random import randint
lista = []
jogos = []
print('-' * 50)
print(f'{"GERADOR DE JOGOS MEGASENA":^50}')
print('-' * 50)
quantidade = int(input('Quantos jogos deseja sortear? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os números sorteados foram: {lista}')
'''
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 50)
print(f'{"GERADOR DE JOGOS MEGASENA":^50}')
print('-' * 50)
quantidade = int(input('Quantos jogos deseja sortear? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=-' * 3, f'  SORTEANDO {quantidade} JOGOS  ', '-=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
