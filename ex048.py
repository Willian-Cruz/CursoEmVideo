# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1   # contagem de números ímpares & múltiplos de 3
        soma += c
print('A soma dos {} valores somados é {}'.format(cont, soma))
'''
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        contador += 1
print('A soma dos {} valores é {}.'.format(contador, soma))
print('FIM!')