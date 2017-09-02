# -*- coding: utf-8 -*-
"""Implementacao do 'Lagged Fibonacci generator'"""
import random


class lfg:
    """Classe que constroi o gerador de numeros pseudo-aleatorios

    Atributos:
        lags: tupla de dois valores que irao representar os 'lags' da formula
        exponent: expoente que ira na potencia de 2 que e feita de modulo da
        formula
    """

    def __init__(self, lags, exponent):
        """Construtor com todos os atributos obrigatorios

        Args:
            seed: lista vazia que ira conter a semente do gerador
            alem dos ja especificados na classe
        """
        self.j = lags[0]
        self.k = lags[1]
        self.m = 2**exponent
        self.seed = []

    def make_seed(self):
        """Monta a lista de numeros que sera utilizada como semente no gerador

        Para o funcionamento correto do algoritmo e necessario que k valores
        aleatorios sejam utilizados como semente. Nessa implementacao isso e
        feito da seguinte forma:
            Utiliza-se o modulo random do python para gerar um numero entre 0 e
            1, para assim multiplicar esse valor por 10000
            (um valor arbitrario) e por fim pegar a parte inteira desse
            resultado e adicionar na lista de sementes
        """
        i = 0
        while i < self.k:
            self.seed.append((int(random.random() * 10000)))
            i += 1

    def valid_amount(self, n):
        """Verifica a validade dos argumentos utilizados na geracao dos numeros

        Argumentos serao validos quando:
            j < k
            n - j < k
            n - k < k

        Args:
            n: quantidade de numeros que serao gerados

        Returns:
            True se os argumentos sao validos, senao False
        """
        return True if n - self.j < self.k and self.j < self.k else False

    def alfg_generate(self, n):
        """Gerador de numeros pseudo-aleatorios com a operacao de adicao

        Gera uma lista com n numeros pseudo-aleatorios conforme o algoritmo
        alfg (additive lagged fibonacci generator), ou seja, ha outras versoes
        que ao inves da adicao para montar o p do algoritmo utilizam da:
            subtracao
            multiplicacao
            xor
        O algoritmo utiliza da seguinte relacao:
            Para cada numero que sera gerado a lista de sementes e iterada:
                Quando e o primeiro elemento da lista de sementes:
                    Calcula-se o pseudo-aleatorio p:
                        p  = (seed_{n - j} + seed_{n - k}) mod m
                            Onde seed e a lista de sementes
                Quando e o ultimo elemento da lista de sementes:
                    A posicao recebe o pseudo-aleatorio calculado
                Nos outros casos:
                    O elemento a direita da lista vem para a posicao atual

        Args:
            n: quantidade de numeros que serao gerados

        Returns:
            lista com os n numeros gerados

        Raises:
            Exception: quando os argumentos sao considerados invalidos
        """
        if not self.valid_amount(n):
            raise Exception("Valores invalidos!")

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
