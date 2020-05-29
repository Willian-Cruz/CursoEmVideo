#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#Para calcular porcentagem: valor * QuantosPorCento / 100
nome = input("Qual o nome do funcionário? ")
sal = float(input("Qual o valor do seu salário? "))
aumento = float(input("Quanto de aumento? "))
novoSal = sal + (sal * aumento / 100)
print("O funcionário {} tem um salário de R${:.2f} e terá um reajuste de {:.2f}%, portanto, passará a ser de R${:.2f}".format(nome, sal, aumento, novoSal))
