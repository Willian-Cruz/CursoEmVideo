print('{:=^40}'.format('LOJA TESTE'))
preco = float(input('Qual o valor das compras? R$ '))

print('OPÇÕES DE PAGAMENTO:\n'
      '[1] - à vista no dinheiro ou cheque(Desconto de 10%)\n'
      '[2] - à vista no cartão(Desconto de 5%)\n'
      '[3] - 2x no cartão\n'
      '[4] - 3x ou mais no cartão(20% de juros no valor final da compra)')
opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)  # valor com juros
    totparc = int(input('Quantas parcelas?'))   # ler a quantidade de parcelas
    parcela = total / totparc   # valor da parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('Opção de pagamento inválida! Tente novamente')
print('Sua compra de R${:.2f} terá o valor final de R%{:.2f}.'.format(preco, total))
