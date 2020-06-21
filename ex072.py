# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0, 21):
    num = int(input('Valor Inválido! Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num}, por extenso fica {contagem[num]}!')
'''

c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze',
     'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = True
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {c[num].upper()}')
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        print('FIM DO PROGRAMA!')
        break