"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


from statistics import mean


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    lista_cidade = []
    lista_veiculos = []
    lista_acidentes = []
    lista_cidade_pequena = []
    numero_acidentes = []
    dicionario = []

    for cidade, veiculos, acidentes in cidades:
        lista_cidade.append(cidade)
        lista_veiculos.append(veiculos)
        lista_acidentes.append(acidentes)
        numero_acidente = (acidentes/veiculos)*1000
        numero_acidentes.append(numero_acidente)
        if veiculos <= 150000:
            lista_cidade_pequena.append(acidentes)

    dicionario = {acidentes:cidade for cidade, acidentes in zip(lista_cidade, numero_acidentes)}

    maior_indice = max(dicionario)
    menor_indice = min(dicionario)
    mais_acidentes = dicionario[maior_indice]
    menos_acidentes = dicionario[menor_indice]
    media = mean(lista_veiculos)
    media_cidades_pequenas = mean(lista_cidade_pequena)

    print(f'O maior índice de acidentes é de {mais_acidentes}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {menos_acidentes}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_cidades_pequenas:.1f} acidentes.')