# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
'''
c = 0
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    c += 1
    r = str(input('Deseja continuar [S/N]]? ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Foram digitados {c} números')
print(f'Os valores digitados forma: {lista}')
lista.sort()
print(f'Valores em ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'Valores em ordem crescente: {lista}')
if 5 in lista:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')
'''
'''
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if r == 'N':
        break
print('-' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
'''     # Solução do professor