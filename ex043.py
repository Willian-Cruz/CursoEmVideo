# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Informe o peso(Kg): '))
altura = float(input('Informe a altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f}, você está com '.format(imc), end='')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 24.9:
    print('Peso normal')
elif 25 < imc < 29.9:
    print('Sobrepeso')
elif 30 < imc < 34.9:
    print('Obesidade grau 1')
elif 35 < imc < 39.9:
    print('Obesidade grau 2')
elif imc >= 40:
    print('Obesidade grau 3')
