# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')