# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano nasceu a {}ª pessoa? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todos {} pessoas são maiores de idade\nAo todo {} pessoas são menores de idade'.format(maior, menor))
'''
from datetime import date
atual = date.today().year
maior = menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} são menores de idade'.format(maior, menor))