import random


class lfg:
    def __init__(self, lags, exponent):
        self.j = lags[0]
        self.k = lags[1]
        self.m = 2**exponent
        self.seed = []

    def make_seed(self):
        for i in range(self.k):
            # explicar isso
            self.seed.append((int(random.random() * 10000)))

    def alfg_generate(self, n):
        if not self.valid_amount(n):
            raise Exception("Valores inválidos!")

        result = []
        # n is amount of numbers
        self.make_seed()
        for i in range(n):
            for j in range(self.k):
                if j == 0:
                    x = self.seed[n - self.j] + self.seed[n - self.k]
                    number = x % self.m
                elif 0 < j < self.k - 1:
                    self.seed[j] = self.seed[j + 1]
                else:
                    self.seed[j] = number
                    result.append(number)

        return result

    def valid_amount(self, n):
        return True if n - self.j < self.k and self.j < self.k else False

if __name__ == '__main__':
    psng = lfg((70, 100), 4)
    print(psng.alfg_generate(150))
