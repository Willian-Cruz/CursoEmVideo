# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if r not in 'SN':
        print('Opção inválida! Tente novamente.')
        r = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    elif r == 'N':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'LISTA COMPLETA: {numeros}')
print('#' * 30)
print(f'LISTA DE PARES: {pares}')
print('#' * 30)
print(f'LISTA DE ÍMPARES: {impares}')
