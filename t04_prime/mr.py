# -*- coding: utf-8 -*-
"""Gerador de numeros primos com base no 'Miller–Rabin primality test'"""

import random
import sys
import utils as u


class mr:
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

    def decomposite(self, n):
        """Escreve um numero par no formato 2^s * d

        Determina s e d provenientes da transformacao do numero par recebido
        para o formato 2^s * d. O argumento recebido e asseguradamente par,
        pois trata-se do valor do qual se deseja determinar a primalidade menos
        um, e, esse valor e par devido a forma que ele foi gerado

        Args:
            n: numero par que sera decomposto

        Returns:
            tupla com os valores de s e d no formato (s, d)
        """
        s, d = (0, 0)
        while True:
            x, y = divmod(n, 2)
            if y == 0:
                s += 1
                n = x
                continue
            else:
                d = n
                break

        return (s, d)

    def primality_test(self, n, s_d):
        """Determina se um numero e primo de maneira probabilistica

        Atraves do teste de miller-rabin define se o numero mais um passado
        como argumento e um provavel primo ou nao. O argumento recebido e
        asseguradamente par, pois trata-se do valor do qual se deseja
        determinar a primalidade menos um, e, esse valor e par devido a forma
        que ele foi gerado

        Args:
            n: numero par no qual o teste sera aplicado
            s_d: tupla que representa a decomposicao de n em 2^s * d, onde d e
            impar

        Returns:
            True se n+1 e um provavel primo, senao False
        """
        s, d = s_d
        i = 0
        while i < self.k:
            i += 1
            a = random.randint(2, n-1)
            x = pow(a, d, n+1)
            if x == 1 or x == n:
                continue

            r = 0
            while r <= s-1:
                r += 1
                x = pow(x, 2, n+1)
                if x == 1:
                    return False
                if x == n:
                    break

            if x == n:
                continue

            return False

        return True

    def generate(self):
        """Gera um numero possivelmente primo entre a faixa [bottom, up]

        Returns:
            numero possivelmente primo gerado
        """
        while True:
            n = u.utils.make_number(self.bottom, self.up)
            s_d = self.decomposite(n-1)
            if not self.primality_test(n-1, s_d):
                continue
            return n

if __name__ == '__main__':
    png = mr(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
