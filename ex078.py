# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
menor = maior = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {v}: ')))
    if v == 0:
        menor = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {maior}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
