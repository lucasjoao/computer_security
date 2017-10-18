import math
import sys
import primefac as pf


def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1

    return amount


def prime_factors(n):
    return list(pf.primefac(n))


def primitive_roots(n):
    result = []
    phi_n = phi(n)
    factors = prime_factors(phi_n)
    for i in range(2, n):
        for factor in factors:
            expo = phi_n / factor
            wrong = False
            if (i**expo) % n == 1:
                wrong = True
                break
            elif factor == factors[-1] and i not in result:
                result.append(i)
    return result


if __name__ == '__main__':
    n = int(sys.argv[1])
    # n = 4
    results = primitive_roots(n)
    for result in results:
        print(result)
