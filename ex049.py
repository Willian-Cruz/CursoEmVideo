# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

('''
num = int(input("Digite um número: "))
cont = -1
for c in range(0, 11):
    cont += 1
    res = num * cont
    print("{} x {:2} = {:2} ".format(num, cont, res))
''')    # Minha resposta
'''
num = int(input("Digite um número: "))
for c in range(0, 11):
    print("{} x {:2} = {:2} ".format(num, c, num*c))    # Resposta do Professor
'''

num = int(input('Informe um número: '))
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, c, (num * c)))
print('FIM!')