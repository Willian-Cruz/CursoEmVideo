# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Dados inválidos! Por favor digite seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
'''
sexo = str(input('Digite o sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    print('Opção inválida! Tente novamente.')
    sexo = str(input('Digite o sexo [M/F]: ')).upper()[0].strip()
if sexo == 'M':
    print('Você é homem.')
if sexo == 'F':
    print('Você é mulher.')
print('FIM')
