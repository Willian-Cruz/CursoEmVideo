# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maior18 = homem = menos20 = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        print('#' * 35)
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?  [S/N]: ')).strip().upper()[0]
        print('~' * 35)
    if resp == 'N':
        break
print(f'Ao todo {maior18} pessoas são maiores de 18 anos.')
print('^' * 35)
print(f'Foram cadastrados {homem} homens.')
print('^' * 35)
print(f'Foram cadastradas {menos20} mulheres com menos de 20 anos.')
print('^' * 35)
print('FIM DO PROGRAMA!')
