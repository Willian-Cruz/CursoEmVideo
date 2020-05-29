# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do sistema')
    print('-==-' * 10)
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 +n2
        print('O produto de {} X {} é igual a {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opção inválida! Tente novamente.')
print('Fim do Programa. Volte sempre!')
'''
from time import sleep
opcao = ''
sair = ''
while opcao != 5 or sair == 'N':
    print('-----Menu-----')
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    print('__' * 10)
    print('[1] - SOMAR \n'
          '[2] - MULTIPLICAR \n'
          '[3] - MAIOR \n'
          '[4] - NOVOS NÚMEROS \n'
          '[5] - SAIR')
    opcao = int(input('Escolha a opção desejada: '))
    if opcao not in [1, 2, 3, 4, 5]:
        print('Opção inválida! Tente novamente.')
    else:
        if opcao == 1:
            soma = n1 + n2
            print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
        elif opcao == 2:
            produto = n1 * n2
            print('Produto de {} e {} é igual a {}'.format(n1, n2, produto))
        elif opcao == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
            else:
                print('{} é maior que {}'.format(n2, n1))
        elif opcao == 4:
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Primeiro valor: "))
        elif opcao == 5:
            sair = input('Deseja sair [S/N]? ').upper().strip()[0]
print('Finalizando..')
sleep(3)
print('Fim do Programa!')
