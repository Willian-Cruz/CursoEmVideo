# Refaça o DESAFIO 051,
# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = num
cont = 1
while cont <= 10:
    cont += 1
    print('{} ->'.format(cont), end=' ')
print('FIM')
'''
'''
termo = int(input('Informe o termo inicial da PA: '))
razao = int(input('A razão: '))
cont = 10
while cont > 0:
    print("{}".format(termo), end=' -> ')
    termo += razao
    cont -= 1

print('FIM')
'''
'''
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
'''