# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM 2011
# - Até 14 anos: INFANTIL 2006
# - Até 19 anos: JÚNIOR 2001
# - Até 25 anos: SÊNIOR 1995
# - Acima de 25 anos: MASTER 1994
from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Você nasceu em {} e tem {} anos'.format(nascimento, idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
elif idade > 25:
    print('Categoria: MASTER')
