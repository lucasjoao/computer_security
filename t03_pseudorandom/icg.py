# -*- coding: utf-8 -*-
"""Implementacao do 'Inversive congruential generator'"""


class icg:
    """Classe que constroi o gerador de numeros pseudo-aleatorios

    Atributos:
        seed: semente do gerador
        q: numero que e feito o modulo da formula
        a: numero multiplicador da formula
        c: numero que faz a adicao da formula, ou, pode ser utilizado como um
           resultado
    """

    def __init__(self, seed, q, a, c):
        """Construtor com todos os atributos obrigatorios

        Args:
            ja especificado na classe
        """
        self.seed = seed
        self.q = q
        self.a = a
        self.c = c

    def generate(self, n):
        """Gerador de numeros pseudo-aleatorios

        Gera uma lista com n-1 numeros pseudo-aleatorios conforme o algoritmo
        icg ou seja, utiliza da seguinte relacao:
            x_0 = seed
            x_{i+1} = (a * x^{-1}_i + c) mod q  if x_i != 0
            x_{i+1} = c                         if x_i == 0
                Onde x^{-1}_i e a funcao modular inversa

        Args:
            n: valor representa quantidade de numeros que serao gerados - 1

        Returns:
            lista com os n + 1 numeros gerados
        """
        result = [self.seed]
        for i in range(n):
            number = 0
            if result[i] == 0:
                number = self.c
            else:
                x = (self.a * self.modular_inverse(result[i]) + self.c)
                number = x % self.q

            result.append(number)

        return result

    def modular_inverse(self, x):
        """Funcao que calcula a modular inversa de um numero

        Forma 'naive' de se calcular a modular inversa de um numero x mod q,
        onde q e informado na construcao do gerador. Considerada 'naive' por nao
        usar do algoritmo de euclides estendido. Funciona da seguinte maneira:
            Calcula x * i mod q para todo i entre 0 e q - 1, o i que gerar o
            resultado 1 sera a modular inversa

        Args:
            x: numero do qual se quer saber a modular inversa com q

        Returns:
            a modular inversa de um numero x mod q

        Raises:
            Exception: quando nao existe modular inversa
        """
        for i in range(self.q):
            result = (x * i) % self.q
            if result == 1:
                return i

        raise Exception("Nao foi possivel calcular a 'inversa modular'")

if __name__ == '__main__':
    psng = icg(1, 5, 2, 3)
    print(psng.generate(30))
