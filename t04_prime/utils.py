import random


class utils:
    @staticmethod
    def make_number(bottom, up):
        i = 2
        while i % 2 == 0:
            i = random.randint(bottom, up)
        return i
