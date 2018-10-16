def gcd(m: int, n: int) -> int:
    """
    Реализация бинарного алгоритма вычисления наибольшего общего делителя

    :param m:
    :param n:
    :return:
    """
    if m == 0 and n != 0:
        return n
    
    elif n == 0 and m != 0:
        return m
    
    elif m == n:
        return m
    
    elif n == 1 or m == 1:
        return 1

    elif m % 2 == 0 and n % 2 == 0:
        return 2 * gcd(m // 2, n // 2)

    elif m % 2 == 0 and n % 2 == 1:
        return gcd(m // 2, n)

    elif m % 2 == 1 and n % 2 == 0:
        return gcd(m, n // 2)

    elif m % 2 == 1 and n % 2 == 1:
        m, n = max(m, n), min(m, n)
        return gcd((m - n) // 2, n)
