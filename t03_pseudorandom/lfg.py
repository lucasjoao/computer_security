import random


class lfg:
    def __init__(self, lags, exponent):
        self.j = lags[0]
        self.k = lags[1]
        self.m = 10
        self.seed = [8675309]

    def make_seed(self):
        for i in range(self.k):
            # explicar isso
            self.seed.append((int(random.random() * 100)))

    def alfg_generate(self, n):
        result = []
        # n is amount of numbers
        # dúvida implementação aqui, perguntar
        for i in range(n):
            x = self.seed[n - self.j] + self.seed[n - self.k]
            number = x % self.m
            result.append(number)

        return result

if __name__ == '__main__':
    psng = lfg((3, 7), 0)
    print(psng.alfg_generate(10))
