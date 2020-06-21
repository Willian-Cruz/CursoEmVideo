# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
'''
pessoas = list()
dados = list()
c = pesado = leve = 0
while True:
    c += 1
    dados.append(str(input(f'Nome da pessoa {c}: ').title()))
    dados.append(float(input(f'Peso da pessoa {c}: ')))
    pessoas.append(dados[:])
    dados.clear()

    for p in pessoas:
        if p[1] > 90:
            pesado += 1
        elif p[1] < 70:
            leve += 1
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida, informe se deseja continuar [S/N]? ')).upper().strip()[0]
        if resp == 'N':
            break
print(f'Ao todo foram cadastradas {c} pessoas')
print(f'Foram informadas {pesado} pessoas pesadas e {leve} leves')
'''

principal = []
temporario = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os dados foram {principal}')
print(f'Ao todo foram cadastradas {len(principal)} pessoas')
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')
