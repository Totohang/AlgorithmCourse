def fdigit(n):
    digit = 1
    while n >= 10:
        n = n // 10
        digit += 1

    return digit

def fhalf(n):
    halfdg = int(fdigit(n) / 2)
    left = n // (10**(halfdg))
    right = n % (10**(halfdg))
    return left, right


def kmulti(x, y):
    dg = fdigit(x)

    l_half1, r_half1 = fhalf(x)
    l_half2, r_half2 = fhalf(y)

    a = kmulti(l_half1, l_half2)
    b = kmulti(r_half1, r_half2)
    c = kmulti((l_half1 + r_half1), (l_half2 + r_half2))
    d = c - b - a

    return a * (10 ** dg) + b + d * (10 ** int(dg / 2))


print(kmulti(12, 34))