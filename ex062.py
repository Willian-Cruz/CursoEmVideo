# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos

num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        cont += 1
        print('{} ->'.format(cont), end=' ')
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))

print('FIM')
