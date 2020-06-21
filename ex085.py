# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente
'''
numeros = list()
pares = []
impares = []
for n in range(0, 8):
    num = int(input(f'Digite o {n + 1}º valor: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
print(f'Os número digitados foram: {numeros}')
numeros.sort()  # Coloca os números da lista em ordem.
print(f'Os números pares foram: {pares}')
print(f'Os números pares foram: {impares}')
'''
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
print(f'Os valores pares são: {num[0]}')
num[1].sort()
print(f'Os valores ímpares são: {num[1]}')
