# -*- coding: utf-8 -*-
"""Implementação do 'Inversive congruential generator'"""


class icg:
    """Classe que constrói o gerador de números pseudo-aleatórios

    Atributos:
        seed: semente do gerador
        q: número que é feito o módulo da fórmula
        a: número multiplicador da fórmula
        c: número que faz a adição da fórmula, ou, pode ser utilizado como um
           resultado
    """

    def __init__(self, seed, q, a, c):
        """Construtor com todos os atributos obrigatórios

        Args:
            já especificado na classe
        """
        self.seed = seed
        self.q = q
        self.a = a
        self.c = c

    def generate(self, n):
        """Gerador de números pseudo-aleatórios

        Gera uma lista com n-1 números pseudo-aleatórios conforme o algoritmo
        icg ou seja, utiliza da seguinte relação:
            x_0 = seed
            x_{i+1} = (a * x^{-1}_i + c) mod q  if x_i != 0
            x_{i+1} = c                         if x_i == 0
                Onde x^{-1}_i é a função modular inversa

        Args:
            n: valor representa quantidade de números que serão gerados - 1

        Returns:
            lista com os n + 1 números gerados
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
        """Função que calcula a modular inversa de um número

        Forma 'naive' de se calcular a modular inversa de um número x mod q,
        onde q é informado na construção do gerador. Considerada 'naive' por não
        usar do algoritmo de euclides estendido. Funciona da seguinte maneira:
            Calcula x * i mod q para todo i entre 0 e q - 1, o i que gerar o
            resultado 1 será a modular inversa

        Args:
            x: número do qual se quer saber a modular inversa com q

        Returns:
            a modular inversa de um número x mod q

        Raises:
            Exception: quando não existe modular inversa
        """
        for i in range(self.q):
            result = (x * i) % self.q
            if result == 1:
                return i

        raise Exception("Não foi possível calcular a 'inversa modular'")

if __name__ == '__main__':
    psng = icg(1, 5, 2, 3)
    print(psng.generate(30))
