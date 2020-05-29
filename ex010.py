#Leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considera US$ 1,00 = R$3,27)
real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = float(input("Cotação do dólar? US$ "))
dol = real / dolar
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real, dol))