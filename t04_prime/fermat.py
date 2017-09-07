# -*- coding: utf-8 -*-
"""Gerador de numeros primos com base no 'Fermat primality test'"""

import random
import sys
import math
import utils as u


class fermat:
    """Constroi o gerador de numeros primos"""

    def __init__(self, k, bottom, up):
        """Construtor com todos os atributos obrigatorios

        Args:
            k: acuracia da determinacao se o numero gerado e primo
            bottom: valor qual o numero primo gerado deve ser maior
            up: valor qual o numero primo gerado deve ser menor
        """
        self.k = k
        self.bottom = bottom
        self.up = up

    def primality_test(self, n):
        """Determina se um numero e primo de maneira probabilistica

        Atraves do teste de fermat define se o numero passado como argumento
        e um provavel primo ou nao. O argumento recebido e asseguradamente
        impar devido a forma que ele foi gerado

        Args:
            n: numero impar no qual o teste sera aplicado

        Returns:
            True se n e um provavel primo, senao False
        """
        i = 0
        while i < self.k:
            i += 1
            a = random.randint(1, n)
            if math.gcd(a, n) != 1 or pow(a, n-1, n) != 1:
                return False

        return True

    def generate(self):
        """Gera um numero possivelmente primo entre a faixa [bottom, up]

        Returns:
            numero possivelmente primo gerado
        """
        while True:
            n = u.utils.make_number(self.bottom, self.up)
            if not self.primality_test(n):
                continue
            return n

if __name__ == '__main__':
    png = fermat(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
