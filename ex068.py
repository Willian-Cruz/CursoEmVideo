# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    tot = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par[P] ou Ímpar[I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jopgou {computador}. Total: {tot}')
    print('RESULTADO: PAR' if tot % 2 == 0 else 'RESULTADO: ÍMPAR')
    if opcao == 'P':
        if jogador % 2 == 0:
            print('Jogador GANHOU! =)')
            vitorias += 1
        else:
            print('Computador GANHOU! =(')
            break
    elif opcao == 'I':
        if jogador % 2 == 1:
            print('Jogador GANHOU! =)')
            vitorias += 1
        else:
            print('Computador GANHOU! =(')
            break
    print('Próxima rodada...')
print(f'GAME OVER! Você ganhou {vitorias} vezes')
'''
from random import randint
vit = 0
while True:
    jogador = int(input('Digite o valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' 10'
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} tanto e o computador {computador}. Total de {total}')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU! =)')
            vit += 1
        else:
            print('Você PERDEU! =(')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU! =)')
            vit += 1
        else:
            print('Você PERDEU! =(')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vit} vezes')
'''