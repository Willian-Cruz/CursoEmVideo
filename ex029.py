#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h!')
    multa = (velocidade - 80) * 7
    print("Você foi multado em RS {:.2f}!! Pois estava a {}km/h.".format(multa, velocidade))
else:
    print('Tenha um bom dia! Dirija com segurança.')