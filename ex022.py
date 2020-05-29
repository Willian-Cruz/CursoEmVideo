'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo (sem considerar espaços);
– Quantas letras tem o primeiro nome.'''
nome = str(input("Digite seu nome completo: ")).strip()#.strip() elimina os espaços antes e depois da frase
print("Analisando seu nome...")
print("Seu nome completo em maiúsculo: {}".format(nome.upper()))
print("Seu nome completo em minúscolo: {}".format(nome.lower()))
print("Seu nome tem {} letras ".format(len(nome)-nome.count(' ')))
#print("Seu nome primeiro nome tem {} letras".format(nome.find(' ')))
""".find() indica o índice do primeiro espaço, 
portanto ele vai considerar os indices anteriores para contar a quantidade de letras do primeiro nome"""
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))