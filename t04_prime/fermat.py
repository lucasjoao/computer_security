# -*- coding: utf-8 -*-

import random
import sys
import math


class fermat:

    def __init__(self, k, bottom, up):
        self.k = k
        self.bottom = bottom
        self.up = up

    def make_number(self):
        i = 2
        while i % 2 == 0:
            i = random.randint(self.bottom, self.up)
        return i

    def primarility_test(self, n):
        i = 0
        while i < self.k:
            i += 1
            a = random.randint(1, n)
            if math.gcd(a, n) != 1 or pow(a, n-1, n) != 1:
                return False

        return True

    def generate(self):
        while True:
            n = self.make_number()
            if not self.primarility_test(n):
                continue
            return n

if __name__ == '__main__':
    png = fermat(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
