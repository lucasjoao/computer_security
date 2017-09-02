# -*- coding: utf-8 -*-
"""Implementação do 'Lagged Fibonacci generator'"""
import random


class lfg:
    """Classe que constrói o gerador de números pseudo-aleatórios

    Atributos:
        lags: tupla de dois valores que irão representar os 'lags' da fórmula
        exponent: expoente que irá na potência de 2 que é feita de módulo da
        fórmula
    """

    def __init__(self, lags, exponent):
        """Construtor com todos os atributos obrigatórios

        Args:
            seed: lista vazia que irá conter a semente do gerador
            além dos já especificados na classe
        """
        self.j = lags[0]
        self.k = lags[1]
        self.m = 2**exponent
        self.seed = []

    def make_seed(self):
        """Monta a lista de números que será utilizada como semente no gerador

        Para o funcionamento correto do algoritmo é necessário que k valores
        aleatórios sejam utilizados como semente. Nessa implementação isso é
        feito da seguinte forma:
            Utiliza-se o módulo random do python para gerar um número entre 0 e
            1, para assim multiplicar esse valor por 10000
            (um valor arbitrário) e por fim pegar a parte inteira desse
            resultado e adicionar na lista de sementes
        """
        i = 0
        while i < self.k:
            self.seed.append((int(random.random() * 10000)))
            i += 1

    def valid_amount(self, n):
        """Verifica a validade dos argumentos utilizados na geração dos números

        Argumentos serão válidos quando:
            j < k
            n - j < k
            n - k < k

        Args:
            n: quantidade de números que serão gerados

        Returns:
            True se os argumentos são validos, senão False
        """
        return True if n - self.j < self.k and self.j < self.k else False

    def alfg_generate(self, n):
        """Gerador de números pseudo-aleatórios com a operação de adição

        Gera uma lista com n números pseudo-aleatórios conforme o algoritmo
        alfg (additive lagged fibonacci generator), ou seja, há outras versões
        que ao invés da adição para montar o p do algoritmo utilizam da:
            subtração
            multiplicação
            xor
        O algoritmo utiliza da seguinte relação:
            Para cada número que será gerado a lista de sementes é iterada:
                Quando é o primeiro elemento da lista de sementes:
                    Calcula-se o pseudo-aleatório p:
                        p  = (seed_{n - j} + seed_{n - k}) mod m
                            Onde seed é a lista de sementes
                Quando é o último elemento da lista de sementes:
                    A posição recebe o pseudo-aleatório calculado
                Nos outros casos:
                    O elemento à direita da lista vem para a posição atual

        Args:
            n: quantidade de números que serão gerados

        Returns:
            lista com os n números gerados

        Raises:
            Exception: quando os argumentos são considerados inválidos
        """
        if not self.valid_amount(n):
            raise Exception("Valores inválidos!")

        result = []
        self.make_seed()
        i = 0
        while i < n:
            for j in range(self.k):
                if j == 0:
                    x = self.seed[n - self.j] + self.seed[n - self.k]
                    number = x % self.m
                elif 0 < j < self.k - 1:
                    self.seed[j] = self.seed[j + 1]
                else:
                    self.seed[j] = number
                    result.append(number)
            i += 1

        return result

if __name__ == '__main__':
    psng = lfg((70, 100), 4)
    print(psng.alfg_generate(150))
