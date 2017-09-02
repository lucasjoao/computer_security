class lcg:
    def __init__(self, multiplier, increment, seed, modulus):
        if 0 < modulus and 0 < multiplier < modulus and \
           0 <= increment < modulus and 0 <= seed < modulus:
            self.a = multiplier
            self.c = increment
            self.r0 = seed
            self.m = modulus
        else:
            raise Exception("Argumentos inválidos!")

    def generate(self, n):
        result = []
        for i in range(n):
            if i == 0:
                previous = self.r0
            else:
                previous = result[i-1]

            result.append((self.a * previous + self.c) % self.m)

        return result

if __name__ == '__main__':
    psng = lcg(1664525, 1013904223, 10, 2**32)
    print(psng.generate(1000))
