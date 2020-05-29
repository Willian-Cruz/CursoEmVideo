# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('As retas informadas formam um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é possível formar um triângulo')
