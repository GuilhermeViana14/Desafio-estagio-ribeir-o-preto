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


def elemento_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1
    return proximo


print(f"a) proximo numero", elemento_a())
print(f"b) proximo numero", elemento_b())
print(f"c) proximo numero", elemento_c())
print(f"d) proximo numero", elemento_d())
print(f"e) proximo numero", elemento_e())
print(f"f) proximo numero", elemento_f())

