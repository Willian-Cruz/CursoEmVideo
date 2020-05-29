#Leia o preço de um produto e mostre seu novo preço com 5% de desconto
#Para calcular porcentagem: valor * QuantosPorCento / 100
valor = float(input("Qual o valor do produto? R$ "))
desc = float(input("Quantos % de desconto? "))
promo = valor - (valor * desc / 100)
print("O produto custa R${:.2f}, na promoção com o desconto de {:.2f}% custará R${:.2f}!".format(valor, desc, promo))


