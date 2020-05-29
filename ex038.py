# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro valor inteiro: '))
num2 = int(input('Segundo valor inteiro: '))

if num1 > num2:
    print('O primeiro é valor é maior!')
elif num1 < num2:
    print('O segundo é valor é maior!')
else:
    print('Os valores são iguais!')
