#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(dist))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print("O valor da passagem será de R$ {:.2f}".format(preco))



