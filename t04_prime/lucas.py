# -*- coding: utf-8 -*-
"""Gerador de numeros primos com base no 'Lucas primality test'"""

import random
import sys
import primefac as pf
import utils as u


class lucas:
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

    def prime_factors(self, n):
        """Determina os fatores primos de um numero

        Com o auxilio do modulo primefac gera-se os fatores primos do numero
        passado como argumento, onde os fatores primos sao os numeros primos
        que dividem o argumento de maneira exata

        Args:
            n: numero do qual sera determinado os fatores primos

        Returns:
            Uma lista com os fatores primos
        """
        return list(pf.primefac(n))

    def primality_test(self, n):
        """Determina se um numero e primo de maneira probabilistica

        Atraves do teste de lucas define se o numero passado como argumento
        e um provavel primo ou nao. O argumento recebido e asseguradamente
        impar devido a forma que ele foi gerado

        Args:
            n: numero impar no qual o teste sera aplicado

        Returns:
            True se n e um provavel primo, senao False
        """
        i = 0
        prime_factors = self.prime_factors(n-1)
        while i < self.k:
            i += 1
            a = random.randint(2, n-1)
            if pow(a, n-1, n) != 1:
                return False

            for q in prime_factors:
                if pow(a, (n-1)//q, n) != 1:
                    if q == prime_factors[-1]:
                        return True
                    else:
                        continue
                else:
                    break

        return False

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
    png = lucas(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
