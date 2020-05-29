#Escreva um programa em Python que leia um número inteiro qualquer
# Peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Informe um valor: '))
print('-=-' * 10)
print('ESCOLHA A OPÇÃO PARA CONVERTER:\n[1] - BINARIO\n[2] - OCTAL\n[3] - HEXADECIMAL')

opcao = int(input('Opção desejada: '))

if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:].upper()))
else:
    print('Opção inválida! Escolha novamente.')