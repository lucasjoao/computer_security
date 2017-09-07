# -*- coding: utf-8 -*-

import random
import sys
import primefac as pf
import utils as u


class lucas:

    def __init__(self, k, bottom, up):
        self.k = k
        self.bottom = bottom
        self.up = up

    def prime_factors(self, n):
        return list(pf.primefac(n))

    def primality_test(self, n):
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
            n = u.utils.make_number(self.bottom, self.up)
            if not self.primality_test(n):
                continue
            return n

if __name__ == '__main__':
    png = lucas(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
