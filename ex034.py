''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''    # ENUNCIADO
sal = float(input('Qual o valor do seu salário? R$ '))
if sal > 1250:
    novo = sal + (sal * 0.1)    # outra p/ calcular é novo = (sal * 10 / 100) + sal
elif sal <= 1250:
    novo = sal + (sal * 0.15)   # outra p/ calcular é novo = (sal * 15 / 100) + sal
print('Seu salário era de R${:.2f}, seu novo salário será R${:.2f}'.format(sal, novo))
