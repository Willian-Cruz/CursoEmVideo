# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente!')
        else:
            print('Menos...Tente novamente!')
print('Parabens! Acertou após {} tentativas.'.format(palpites))

'''
from random import randint
from time import sleep
computador = randint(0, 10)
c = 0
print('Tente adivinhar qual número pensei...')
jogador = int(input('Escolha um número entre 0 e 10: '))
print('PROCESSANDO...')
sleep(1.5)
if jogador > 10:
    print('Você deve escolher um número entre 0 e 10! Tente novamente.')
else:
    while jogador != computador:
        c += 1
        print('Você perdeu =( Pensei no número {} e não no número {}'.format(computador, jogador))
        jogador = int(input('Escolha um número entre 0 e 10: '))
        print('PROCESSANDO...')
        sleep(1.5)
        if jogador > computador:
            print('Menos... Tente novamente!')
        else:
            print('Mais... Tente novamente!')

print('Muito bem! =) Você acertou Após {} tentativas!'.format(c))
'''