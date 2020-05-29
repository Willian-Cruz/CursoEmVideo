# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''t = int(input('Termo inicial: '))
r = int(input('Qual a razão? '))
decimo = t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('FIM!')
'''

t = int(input('Informe o termo inicial da PA: '))
r = int(input('A razão: '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print("{}".format(c), end=' -> ')
print('FIM')
