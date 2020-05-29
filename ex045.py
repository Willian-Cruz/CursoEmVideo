# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('{:*^40}'.format('JOKENPÔ'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Escolha uma opção:\n'
                  '[0] - PEDRA\n'
                  '[1] - PAPEL\n'
                  '[2] - TESOURA')
jogador = int(input('Qual a sua jogada? '))
print('JO',end=' ')
sleep(1)
print('KEN',end=' ')
sleep(1)
print('PÔ!!!')

print('-' * 60)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[computador]))
print('-' * 60)
if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVALIDA \nJogue novamente')
else:
    if computador == 0:     # PEDRA(Computador)
        if jogador == 0:    # PEDRA(Jogador)
            print('EMPATE')
        elif jogador == 1:  # PAPEL(Jogador)
            print('JOGADOR GANHOU!')
        elif jogador == 2:  # TESOURA(Jogador)
            print('COMPUTADOR GANHOU')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1:   # PAPEL(Computador)
        if jogador == 0:    # PEDRA(Jogador)
            print('COMPUTADOR GANHOU!')
        elif jogador == 1:  # PAPEL(Jogador)
            print('EMPATE')
        elif jogador == 2:  # TESOURA(Jogador)
            print('JOGADOR GANHOU!')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2:   # TESOURA(Computador)
        if jogador == 0:    # PEDRA(Jogador)
            print('JOGADOR GANHOU!')
        elif jogador == 1:  # PAPEL(Jogador)
            print('COMPUTADOR GANHOU!')
        elif jogador == 2:  # TESOURA(Jogador)
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA!')
