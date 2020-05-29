# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor do imóvel:R$ '))
salario = float(input('Salário:R$ '))
anos = (int(input('Tempo do empréstimo(Em Anos): ')))
meses = anos * 12
prestacao = valorCasa / meses

if prestacao > ((salario * 30) / 100):
    print('NEGADO! Valor excederá a margem de 30% do seu salário!')
else:
    print('APROVADO!'.format(prestacao))
    print('O valor do imóvel é R${:.2f} a serem pagos em {} parcelas de R${:.2f}!'.format(valorCasa, meses, prestacao))
