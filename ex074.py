#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
listagem = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:')
for n in listagem:
    print(f'{n} ', end='')
print(f'\nO maior valor soteado foi: {max(listagem)}')
print(f'O menor valor soteado foi: {min(listagem)}')