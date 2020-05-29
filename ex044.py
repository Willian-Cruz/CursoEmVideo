# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Valor total do produto: R$ '))
print('-==-' * 10)
print('SIMULADOR DE LOJA')
print('-==-' * 10)
print('FORMAS DE PAGAMENTO:\n[1] - Á VISTA DINHEIRO/CHEQUE\n[2] - Á VISTA NO CARTÃO\n[3] - ATÉ 2X NO CARTÃO\n[4] - 3X OU MAIS NO CARTÃO
')
opcao = int(input('Escolha a opção desejada: '))
if opcao == 1:
    valNovo = valor - (valor * 0.1)
    print('O valor da compra com o desconto é R${:.2f}'.format(valNovo))
elif opcao == 2:
    valNovo = valor - (valor * 0.05)
    print('O valor da compra com o desconto é R${:.2f}'.format(valNovo))
elif opcao == 3:
    parcela = valor / 2
    print('O valor foi parcelado em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    prest = int(input('Quantas parcelas?'))
    juros = valor + (valor * 20 / 100)
    parcela = juros / prest
    print('O valor total é de R$ {:.2f},foi parcelado em {} vezes de R${:.2f}'.format(juros, prest, parcela))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')'''

valor = float(input('Qual o valor total da compra? R$ '))
print('Formas de pagamento: \n'
      '[1] - à vista dinheiro/cheque: 10% de desconto\n'
      '[2] - à vista no cartão: 5% de desconto\n'
      '[3] - em até 2x no cartão: preço formal\n'
      '[4] - 3x ou mais no cartão: 20% de juros')
opcao = int(input('Escolha a forma de pagamento: '))
if opcao not in [1, 2, 3, 4]:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
else:
    if opcao == 1:
        novoValor = valor - (valor * 0.1)
        print('O valor da compra: R${:.2f}\nCom o desconto ficou em R${:.2f}'.format(valor, novoValor))
    elif opcao == 2:
        novoValor = valor - (valor * 0.05)
        print('O valor da compra: R${:.2f}\nCom o desconto, o valor ficou R${:.2f}'.format(valor, novoValor))
    elif opcao == 3:
        parcela = valor / 2
        print('O valor da compra é de R${:.2f} foi parcelado em 2x de R${:.2f}'.format(valor, parcela))
    elif opcao == 4:
        novoValor = valor + (valor * 0.2)
        qtparcela = int(input('Deseja parcelar em quantas vezes? '))
        parcela = novoValor / qtparcela
        print('O valor total da compra é R${:.2f}, que foram parcelados em {}x de R${:.2f}'.format(novoValor, qtparcela, parcela))

    print('OBRIGADO E VOLTE SEMPRE!')