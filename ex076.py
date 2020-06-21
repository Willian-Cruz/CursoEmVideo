# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 45)
print(f'{"Listagem de preços":^45}')
print('-' * 45)
listagem = ('Joystick - Dualshock 3', 99.50,
            'HeadSet', 87.00,
            'Monitor LED 4k', 1.800,
            'Teclado Gamer', 119.80,
            'Mouse Gamer', 180.00,
            'Playstation 4 500 GB', 1140.00,
            'XBox One 500 GB', 999.94,
            'Mouse pad', 14.50,
            'Cabo HDMI', 49.90,)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>10.2f}')
print('-' * 45)
