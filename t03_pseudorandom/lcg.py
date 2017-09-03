# -*- coding: utf-8 -*-
"""Implementacao do 'Linear congruential generator'"""

import sys


class lcg:
    """Classe que constroi o gerador de numeros pseudo-aleatorios

    Atributos:
        multiplier: numero multiplicador da formula
        increment: numero que faz a adicao da formula
        seed: semente do gerador
        modulus: numero que e feito o modulo da formula
    """

    def __init__(self, multiplier, increment, seed, modulus):
        """Construtor com todos os atributos obrigatorios

        So constroi o gerador se os atributos sao considerados validos para a
        geracao dos numeros

        Args:
            ja especificado na classe

        Raises:
            Exception: quando os argumentos sao considerados invalidos
        """
        if modulus > 0 and 0 < multiplier < modulus and \
           0 <= increment < modulus and 0 <= seed < modulus:
            self.a = multiplier
            self.c = increment
            self.r0 = seed
            self.m = modulus
        else:
            raise Exception("Argumentos invalidos!")

    def generate(self, n):
        """Gerador de numeros pseudo-aleatorios

        Gera uma lista com n numeros pseudo-aleatorios conforme o algoritmo lcg,
        ou seja, utiliza da seguinte relacao:
            X_{n+1} = (a * X_n + c) mod m
                Quando n = 0, entao X_n = semente do gerador

        Args:
            n: quantidade de numeros que serao gerados

        Returns:
            lista com os n numeros gerados
        """
        result = []
        for i in range(n):
            if i == 0:
                previous = self.r0
            else:
                previous = result[i-1]

            result.append((self.a * previous + self.c) % self.m)

        return result

if __name__ == '__main__':
    psng = lcg(1664525, 1013904223, int(sys.argv[1]), 2**int(sys.argv[2]))
    print(psng.generate(5))
