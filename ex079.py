# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = list()
continuar = True
while True:
    num = int(input('Digite um valor para adicionar à lista: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor não será adicionado, pois já existe na lista.')
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')
'''
'''
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com êxito!')
    else:
        print('Valor duplicado, não adicionado.')
    r = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if r == 'N':
        break

print('-=' * 30)
num.sort()
print(f'Você digitou os valores {num}')
'''     # Solução do professor