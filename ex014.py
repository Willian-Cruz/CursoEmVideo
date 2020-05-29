#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
c = float(input("Temperatura em ºC: "))
f = ((9 * c) / 5) + 32
print("A temperatura de {}ºC corresponde a {}ºF" .format(c, f))