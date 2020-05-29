#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
num = int(input("Digite um numero: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
#print("O dobro de {} é {}, \no triplo é igual a {} e sua raiz quadrada é {:.2f}" .format(num, dobro, triplo, raiz))
print("O dobro de {} vale {}. \nO triplo vale {} \nA sua raiz é igual a {:.2f}" .format(num, (num*2), (num*3), (num**(1/2)))) #pow(base, expoente)
