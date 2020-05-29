# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''frase = str(input('Digite uma frase para ver seu palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1]     Sintaxe para ler a variável de trás para frente sem utilizar o 'FOR'
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndormo!')
else:
    print('A frase não é um palíndromo')
'''
frase = str(input('Digite uma frase: ')).strip().upper()    # strip() => remove os espaços | upper() => deixa em maiusculo
palavras = frase.split()    # as palavras da frase foram separadas
junto = ''.join(palavras)   # juntara as palavras sem os espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):     #  sintaxe para ler da última letra [len(junto)], até a primeira letra(-1), voltando de uma em uma casa(-1)
    inverso += junto[letra]
if inverso == junto:    # leia: Se a o inverso da frase foi igual a frase
    print('A frase É UM PALÍNDROMO!\n')
    print(junto, inverso)
else:
    print('A frase NÃO É UM PALÍNDROMO!\n')
    print(junto, inverso)