#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digte um número: '))
result = num % 2
if result == 0:
    print('O número escolhido {}, é PAR!'.format(num))
else:
    print('O número escolhido {}, é ÍMPAR!'.format(num))