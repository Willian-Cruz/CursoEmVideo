# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('linux', 'dinheiro', 'namorada',
            'apartamento', 'interestadual', 'flexibilizar',
            'estabilidade', 'concurso', 'exercicios',
            'biblioteca', 'internazionale', 'inconstitucional')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')