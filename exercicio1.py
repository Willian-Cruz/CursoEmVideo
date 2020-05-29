'''num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O maior número é o {}'.format(num1))
elif num1 < num2:
    print('O maior número é o {}'.format(num2))
else:
    print('OS números informados são iguais!!')'''
'''num = float(input('Informe o valor: '))
if num > 0:
    print('O valor informado é POSITIVO!')
else:
    print('O valor informado é NEGATIVO!')'''
'''sexo = str(input('Informe o SEXO [M/F]: '))
if sexo not in ('M','m','f','F'):
    print('Opção inválida! Digite novamente.')
elif sexo == 'M' or sexo == 'm':
    print('M - Masculino')
elif sexo == 'F' or sexo == 'f':
    print('F - Feminino')'''
'''letra = str(input('Digite uma letra para informar se ela é VOGAL ou CONSOANTE: '))
if letra not in ('a', 'A', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'):
    print('A letra informada é uma CONSOANTE!')
else:
    print('A letra informada é uma VOGAL!')'''
'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = ''
maior = ''
if n1 > n2 and n1 > n3 and n2 > n3:
    maior = 'PRIMEIRO'
    menor = 'TERCEIRO'
    if n1 > n2 and n1 > n3 and n3 > n2:
        maior = 'PRIMEIRO'
        menor = 'SEGUNDO'
elif n2 > n1 and n2 > n3 and n3 > n1:
    maior = 'SEGUNDO'
    menor = 'PRIMEIRO'
    if n2 > n1 and n2 > n3 and n3 > n1:
        maior = 'SEGUNDO'
        menor = 'TERCEIRO'
elif n3 > n1 and n3 > n2 and n1 > n2:
    maior = 'TERCEIRO'
    menor = 'SEGUNDO'
    if n1 > n2 and n1 > n3 and n2 > n3:
        maior = 'PRIMEIRO'
        menor = 'TERCEIRO'
print('O maior valor é o {}, e o menor é o {}'.format(maior, menor))'''
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Olá, mundo!')
        self.msg.pack ()
        pass
root = Tk()
Application(root)
root.mainloop()