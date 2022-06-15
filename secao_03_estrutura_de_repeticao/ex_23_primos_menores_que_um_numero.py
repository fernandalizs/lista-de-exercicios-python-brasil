"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    primos = imprime_apenas_os_primos(n)
    divisoes = nro_divisoes(n)
    return (primos, divisoes)


def imprime_apenas_os_primos(numero):
    primos = []
    for num in range(2, numero + 1):
        if is_prime(num):
            primos.append(str(num))

    return ", ".join(primos)


def is_prime(numero):

    prime = True
    for num in range(2, numero):
        resto_divisao = numero % num
        if resto_divisao == 0:
            prime = False
            break
    return prime


def nro_divisoes(numero):
    """retorna se o número é primo"""
    divisoes = 0
    for num in range(2, numero):
        divisoes += 1

    return divisoes