# -*- coding: utf-8 -*-

import random
import sys
import math
import utils as u


class fermat:

    def __init__(self, k, bottom, up):
        self.k = k
        self.bottom = bottom
        self.up = up

    def primality_test(self, n):
        i = 0
        while i < self.k:
            i += 1
            a = random.randint(1, n)
            if math.gcd(a, n) != 1 or pow(a, n-1, n) != 1:
                return False

        return True

    def generate(self):
        while True:
            n = u.utils.make_number(self.bottom, self.up)
            if not self.primality_test(n):
                continue
            return n

if __name__ == '__main__':
    png = fermat(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
