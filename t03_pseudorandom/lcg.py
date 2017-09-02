# -*- coding: utf-8 -*-
"""Implementação do 'Linear congruential generator'"""


class lcg:
    """Classe que constrói o gerador de números pseudo-aleatórios

    Atributos:
        multiplier: número multiplicador da fórmula
        increment: número que faz a adição da fórmula
        seed: semente do gerador
        modulus: número que é feito o módulo da fórmula
    """

    def __init__(self, multiplier, increment, seed, modulus):
        """Construtor com todos os atributos obrigatórios

        Só constrói o gerador se os atributos são considerados válidos para a
        geração dos números

        Args:
            já especificado na classe

        Raises:
            Exception: quando os argumentos são considerados inválidos
        """
        if modulus > 0 and 0 < multiplier < modulus and \
           0 <= increment < modulus and 0 <= seed < modulus:
            self.a = multiplier
            self.c = increment
            self.r0 = seed
            self.m = modulus
        else:
            raise Exception("Argumentos inválidos!")

    def generate(self, n):
        """Gerador de números pseudo-aleatórios

        Gera uma lista com n números pseudo-aleatórios conforme o algoritmo lcg,
        ou seja, utiliza da seguinte relação:
            X_{n+1} = (a * X_n + c) mod m
                Quando n = 0, então X_n = semente do gerador

        Args:
            n: quantidade de números que serão gerados

        Returns:
            lista com os n números gerados
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
    psng = lcg(1664525, 1013904223, 10, 2**32)
    print(psng.generate(1000))
