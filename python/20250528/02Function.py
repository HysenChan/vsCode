x = 5


def f(y, z):
    result = x + y + z
    return result


print(f(1, 2))
print(f(2, 3))


def isPositive(x):
    return x > 0


print(isPositive(5))
print(isPositive(-5))
print(isPositive(0))


def f(x):
    return x + 42


print(f(5))


def cubed(x):
    return x**3


cubed(2)
print(cubed(3))
print(2 * cubed(2))


def hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


print(hypotenuse(3, 4))
print("---------------")


def xor(b1, b2):
    return b1 != b2


print(xor(True, True))
print(xor(True, False))
print(xor(False, True))
print(xor(False, False))
print("---------------")


def isPositive(n):
    return n > 0


print(isPositive(5))
print(isPositive(-1.2))


def f(w):
    return 10 * w


def g(x, y):
    return f(3 * x) + y


def h(z):
    return f(g(z, f(z + 1)))


print(h(1))


def onesDigit(n):
    return n % 10


def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))


print("largerOnesDigit", largerOnesDigit(123, 456))
print("largerOnesDigit1", largerOnesDigit(123, 4562))


def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert onesDigit(0) == 0
    assert onesDigit(1) == 1
    assert onesDigit(9) == 9
    assert onesDigit(100) == 0
    print("Passed")


testOnesDigit()


def f(x):
    print("In f, x = ", x)
    x += 5
    return x


def g(x):
    return f(x * 2) + f(x * 3)


print(g(2))


def f(x):
    print("In f, x = ", x)
    x += 7
    result = round(x / 3)
    print("result:", result)
    return result


def g(x):
    x *= 10
    return 2 * f(x)


def h(x):
    x += 3
    return f(x + 4) + g(x)


print(h(f(1)))

g = 100


def f(x):
    global g
    g += 1
    print(x, g)
    return x + g


print(f(1))
print(f(2))
print(g)
