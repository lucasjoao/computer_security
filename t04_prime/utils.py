# -*- coding: utf-8 -*-
"""Funcoes uteis para a geracao de numeros primos"""

import random


class utils:
    """Classe que possui as funcoes uteis"""

    @staticmethod
    def make_number(bottom, up):
        """Retorna um inteiro aleatorio impar entre a faixa [bottom, up]

        Args:
            bottom: menor valor da faixa de valores
            up: maior valor da faixa de valores

        Returns:
            Inteiro impar
        """
        i = 2
        while i % 2 == 0:
            i = random.randint(bottom, up)
        return i
