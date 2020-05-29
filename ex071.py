print('#' * 50)
print('{:^50}'.format('BANCO DE TESTE'))
print('#' * 50)

valor = int(input('Valor a ser sacado:R$ '))
total = valor
cedula = 50
tCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        tCedulas += 1
    else:
        if tCedulas > 0:
            print(f'Total de {tCedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tCedulas = 0
        if total == 0:
            break
