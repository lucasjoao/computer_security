# -*- coding: utf-8 -*-

import random
import sys
import primefac as pf


class lucas:

    def __init__(self, k, bottom, up):
        self.k = k
        self.bottom = bottom
        self.up = up

    def make_number(self):
        i = 2
        while i % 2 == 0:
            i = random.randint(self.bottom, self.up)
        return i

    def prime_factors(self, n):
        return list(pf.primefac(n))

    def primarility_test(self, n):
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
        while True:
            n = self.make_number()
            if not self.primarility_test(n):
                continue
            return n

if __name__ == '__main__':
    png = lucas(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
