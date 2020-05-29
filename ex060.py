# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial
num = int(input('Digite um valor para mostrar seu faforial: '))
fatorial = factorial(num)
print('O resultado é {}! = {}'.format(num, fatorial))
'''
'''from time import sleep
num = int(input('Esolha um número para calcular o fatorial: '))
cont = num
fatorial = 1
print('Calculando...')
sleep(3.5)
print('{}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
'''

num = int(input('Digite o número para calcular seu fatorial: '))
contador = num
fatorial = 1
print('Calculando {}!\n'.format(num), end='')
# for contador in range( num, 1, -1): Sintaxe par usar com o 'FOR'
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial), end='')


