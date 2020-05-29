# Calcular a média de duas notas do aluno
nome = input("Qual o nome do aluno? ")
n1 = float(input("Primeira nota : "))
n2 = float(input("Segunda nota : "))
media = (n1+n2)/2

print("O aluno {} teve a nédia de {} e suas notas foram: \n Nota 01: {} \n Nota 02: {}" .format(nome, media, n1, n2))
