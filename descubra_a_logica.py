def elemento_a():
    sequencia = [1, 3, 5, 7]
    proximo = sequencia[-1] + 2
    return proximo


def elemento_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo = sequencia[-1] * 2
    return proximo


def elemento_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo = (len(sequencia)) ** 2
    return proximo


def elemento_d():
    sequencia = [4, 16, 36, 64]
    proximo = (len(sequencia)* 2 + 2 ) ** 2
    return proximo


def elemento_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo = sequencia[-1] + sequencia[-2]
    return proximo


def elemento_e():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1
    return proximo
