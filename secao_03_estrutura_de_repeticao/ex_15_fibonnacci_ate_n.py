"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""


def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    a, b, c = 1, 1, 0
    while a <= n:
        print("{}.".format(c), end="")
        c = a + b
        a = b
        b = c
       


    # if n==1:
    #     return '1'
    # elif n==2: 
    #     return '1, 1'
    # else:
    #     for i in range(1,n+1):

    #         i += 1
    #     print(i)
    






            # numero_atual = num_anterior + numero_atual
            # num_anterior = numero_atual - num_anterior
    # ultimo=1
    # penultimo=1

    # if (n==1) or (n==2):
    #     print("1")
    # else:
    #     for count in range(2,n):
    #         termo = ultimo + penultimo
    #         penultimo = ultimo
    #         ultimo = termo
    #         count += 1
    #     print(termo)