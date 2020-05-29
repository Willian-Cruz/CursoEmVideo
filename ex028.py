#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Tente adivinhar qual número pensei...')
print('-=-' * 20)
jogador = int(input('Escolha um número entre 0 e 10: '))
print('PROCESSANDO...')
sleep(3)
if jogador > 10:
    print('Você deve escolher um número entre 0 e 10! Tente novamente.')
elif jogador == computador:
    print('Muito bem! Você ganhou =)')
else:
    print('Você perdeu =( Pensei no número {} e não no número {}'.format(computador, jogador))