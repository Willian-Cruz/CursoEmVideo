# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''somaidade = 0
midade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('***** {}ª Pessoa *****'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

midade = somaidade / 4
print('A média de idade do grupo é {} anos'.format(midade))
print('O homem mais velho é o {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''
'''somaIdade = somaF = 0
for p in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(p))).title()
    idade = int(input('Idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Sexo da {}ª pessoa[M/F]: '.format(p))).upper()
    somaIdade += idade
    if sexo == 'F' and idade < 20:
        somaF += 1
media = somaIdade / 4

print('A média de idade é de {} anos'.format(media))

'''
somaIdade = mediaIdade = maiorIdade = somaF = 0
maisVelho = ''
for p in range(1, 5):
    print('---- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    somaIdade += idade
    if p == 1 and sexo == 'M':
        maiorIdade = idade
        maisVelho = nome
    if sexo == 'M' and idade > maiorIdade:
        maisVelho = nome
        maiorIdade = idade
    if sexo == 'F' and idade < 20:
        somaF += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho é o {} e tem {} anos'.format(maisVelho.title(), maiorIdade))
print(print('Ao todo são {} mulheres que tem menos de 20 anos'.format(somaF)))
