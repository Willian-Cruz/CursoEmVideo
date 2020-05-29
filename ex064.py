# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''n = soma = cont = 0
n = int(input('Digite um valor: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor: '))
print('Você digitou {} números\nA soma é igual a {}'.format(cont, soma))
'''
contador = soma = num = 0
num = int(input('Digite um número: '))
while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite um número: '))
print('Foram mostrados {} números, e a soma foi {}'.format(contador, soma - 999))