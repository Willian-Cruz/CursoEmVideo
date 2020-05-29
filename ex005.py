#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor
numero = int(input("Informe o valor: "))
sucessor = numero + 1
antecessor = numero - 1
print("O antecessor de {} é {} e o sucessor é {}".format(numero, antecessor, sucessor))