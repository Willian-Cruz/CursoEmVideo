# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar,
# Se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade == 18:
    print('Você tem 18 anos, deverá se alistar esse ano!')
elif idade > 18:
    alistar = atual - (nascimento + 18)
    print('Você tem {} anos, deveria ter se alistado há {} anos!'.format(idade, alistar))
elif idade < 18:
    alistar = (nascimento + 18) - atual
    print('Você tem {} anos, ainda faltam {} anos para seu alistamento!'.format(idade, alistar))
