# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = ''
c = soma = 0
while resposta != 'N':
    if resposta not in 'SN':
        print('Opção inválida! Tente novamente')
        resposta = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    else:
        num = int(input('Digite um valor: '))
        soma += num
        c += 1
        if c == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        resposta = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
media = soma / c
print('Você digitou {} números, a soma foi {} e a média é igual a {:.2f}'.format(c, soma, media))
print('O maior número foi {} e o menor {}.'.format(maior, menor))
print('FIM')
