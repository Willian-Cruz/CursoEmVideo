# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Corinthians', 'Atético-MG', 'Grêmio', 'São Paulo', 'Internacional', 'Sport', 'Santos', 'Cruzeiro', 'Palmeiras', 'Athetico-PR',
         'Ponte Preta', 'Flamengo', 'Fluminense', 'Chapecoense', 'Coritiba', 'Figueirense', 'Avaí', 'Vasco', 'Goiás', 'Joinville')
top5 = tabela[0:5]
rebaixados = tabela[-4:]
print(f'Classificados para a Libertadores: {top5}')
print('-=' * 140)
print(f'Zona de rebaixamento: {rebaixados}')
print('-=' * 140)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 40)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição!')