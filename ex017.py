#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
from math import hypot #hypot -> calula a hipotenusa
oposto = float(input("Qual o comprimentoi do cateto oposto? "))
adjacente = float(input("Qual o comprimentoi do cateto adjacente? "))
#hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2) <- Solução matemática
hipotenusa = hypot(oposto, adjacente)
print("A hipotenusa vai medir {:.2f} ".format(hipotenusa))