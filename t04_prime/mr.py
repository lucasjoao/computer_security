# -*- coding: utf-8 -*-

import random
import sys
import utils as u


class mr:

    def __init__(self, k, bottom, up):
        self.k = k
        self.bottom = bottom
        self.up = up

    # documentar sobre seguranca que nao eh impar
    def decomposite(self, n):
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
        while True:
            n = u.utils.make_number(self.bottom, self.up)
            s_d = self.decomposite(n-1)
            if not self.primality_test(n-1, s_d):
                continue
            return n

if __name__ == '__main__':
    png = mr(10, int(sys.argv[1]), int(sys.argv[2]))
    print(png.generate())
