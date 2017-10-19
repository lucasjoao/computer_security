# -*- coding: utf-8 -*-
"""Calculador de raízes positivas módulo n. Funciona somente para um n primo"""

import math
import sys
import primefac as pf


def phi(n):
    """Calcula o totiente de Euler (função phi)

    Args:
        n: numero que terá o totiente de Euler calculado

    Returns:
        valor do totiente de Euler
    """
    amount = 0

    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1

    return amount


def prime_factors(n):
    """Determina os fatores primos de um número

    Com o auxílio do módulo primefac gera-se os fatores primos do número
    passado como argumento, onde os fatores primos são os números primos
    que dividem o argumento de maneira exata

    Args:
        n: número do qual sera determinado os fatores primos

    Returns:
        Uma lista com os fatores primos
    """
    return list(pf.primefac(n))


def primitive_roots(n):
    """Determina as raízes primitivas de um número

    Determina as raízes primitivas módulo n do argumento conforme algoritmo
    que pode ser encontrado em
    https://en.wikipedia.org/wiki/Primitive_root_modulo_n#Finding_primitive_roots
    Funciona somente para números primos.

    Args:
        n: número do qual será determinado as raízes primitivas dele

    Returns:
        Uma lista com as raízes primitivas módulo n
    """
    result = []
    phi_n = phi(n)
    facs = prime_factors(phi_n)
    for i in range(2, n):
        right = 0
        for fac in facs:
            expo = phi_n / fac

            if (i**expo) % n == 1:
                break

            right += 1

            if fac == facs[-1] and i not in result and right == len(facs):
                result.append(i)
    return result


if __name__ == '__main__':
    n = int(sys.argv[1])
    results = primitive_roots(n)
    for result in results:
        print(result)
