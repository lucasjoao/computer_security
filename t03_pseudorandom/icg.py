class icg:
    def __init__(self, seed, q, a, c):
        self.seed = seed
        self.q = q
        self.a = a
        self.c = c

    def generate(self, n):
        result = [self.seed]
        # n is amount of numbers - 1
        for i in range(n):
            number = 0
            if result[i] == 0:
                number = self.c
            else:
                x = (self.a * self.modular_inverse(result[i]) + self.c)
                number = x % self.q

            result.append(number)

        return result

    # naive
    def modular_inverse(self, x):
        for i in range(self.q):
            result = (x * i) % self.q
            if result == 1:
                return i

        raise Exception("Não foi possível calcular a 'inversa modular'")

if __name__ == '__main__':
    psng = icg(1, 5, 2, 3)
    print(psng.generate(30))
