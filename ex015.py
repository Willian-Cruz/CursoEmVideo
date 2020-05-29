#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km foram oercorridos? "))
dias = int(input("Quantidade de dias de alocação: "))
preco = (km * 0.15) + (60 * dias)
print("O veículo foi alugado por {} dias e rodou {}km, portanto o valor a ser pago é de R${:.2f}".format(dias, km, preco))

