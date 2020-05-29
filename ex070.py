# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = maior = barato = contador = 0
maisbarato = ' '
print("#" * 50)
print('{: ^50}'.format('LOJA BARATEIRO'))
print("#" * 50)
while True:
    produto = str(input('Informe o Nome do produto: '))
    preco = float(input('Informe o Preço do produto:R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        maior += 1
    if contador == 1:
        barato = preco
        maisbarato = produto
    else:
        if preco < barato:
            barato = preco
            maisbarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja prosseguir [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total das compras foi de R${total:.2f}')
print(f'Ao todo {maior} produtos custam acima de R$ 1.000,00.')
print(f'O produto mais barato é {maisbarato} e custa R${barato:.2f}')
