# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
num = (int(input('Digite o valor 1: ')), int(input('Digite o valor 2: ')), int(input('Digite o valor 3: ')), int(input('Digite o valor 4: ')))
print(f'Os valores digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'A posição em que o número 3 foi pela primeira vez foi a {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez!')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
