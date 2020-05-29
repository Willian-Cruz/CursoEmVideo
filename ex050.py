# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
'''soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o valor {}: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} números PARES é igual a {}'.format(cont, soma))'''
'''soma = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números PARES '
      'é igual a {}!'.format(soma))
print('FIM')'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram {} números pares, e a soma foi {}'.format(cont, soma))
