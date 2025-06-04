import math


def digitCount(n):
    if n == 0:
        return 1
    total = 0
    num = abs(n)
    while num > 0:
        total += 1
        num = num // 10
    return total


def testDigitCount():
    print("Testing digitCount()...", end="")
    assert digitCount(3) == 1
    assert digitCount(33) == 2
    assert digitCount(3030) == 4
    assert digitCount(-3030) == 4
    assert digitCount(0) == 1
    print("Passed!")


testDigitCount()


def hasConsecutiveDigits(n):
    if n == 0:
        return False
    num = abs(n)
    pre = -1
    while num > 0:
        cur = num % 10
        if pre == cur:
            return True
        pre = cur
        num //= 10
    return False


def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert hasConsecutiveDigits(0) == False
    assert hasConsecutiveDigits(123456789) == False
    assert hasConsecutiveDigits(1212) == False
    assert hasConsecutiveDigits(1212111212) == True
    assert hasConsecutiveDigits(33) == True
    assert hasConsecutiveDigits(-1212111212) == True
    print("Passed!")


testHasConsecutiveDigits()


def nthPerfectNumber(n):
    if n < 0:
        return None
    count = 0
    num = 1
    while True:
        total = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                total += i

        if total == num:
            if count == n:
                return num
            count += 1
        num += 1


def testNthPerfectNumber():
    print("Testing nthPerfectNumber()...", end="")
    assert nthPerfectNumber(0) == 6
    assert nthPerfectNumber(1) == 28
    assert nthPerfectNumber(2) == 496  # this can be slow in Brython
    assert nthPerfectNumber(3) == 8128  # this can be slow even in Standard Python!
    print("Passed!")


testNthPerfectNumber()


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def testGcd():
    print("Testing gcd()...", end="")
    assert gcd(3, 3) == 3
    assert gcd(3**6, 3**6) == 3**6
    assert gcd(3**6, 2**6) == 1
    x = 1568160  # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448  # 2**3 * 3**6 *        7**2 * 11**1
    g = 7128  # 2**3 * 3**4 *               11**1
    assert gcd(x, y) == g
    print("Passed!")


testGcd()


def cosineError(x, k):
    approx = 0.0
    for n in range(k + 1):  # 计算前k+1项（从n=0到n=k）
        sign = (-1) ** n
        exponent = 2 * n
        term = sign * (x**exponent) / math.factorial(exponent)
        approx += term
    return abs(approx - math.cos(x))


def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon


def testCosineError():
    print("Testing cosineError()...", end="")
    assert almostEqual(cosineError(0, 0), abs(math.cos(0) - 1))
    assert almostEqual(cosineError(1, 0), abs(math.cos(1) - 1))
    x = 1.2
    guess = 1 - x**2 / 2 + x**4 / (4 * 3 * 2)
    error = abs(math.cos(x) - guess)
    assert almostEqual(cosineError(x, 2), error)
    x = 0.75
    guess = 1 - x**2 / 2 + x**4 / (4 * 3 * 2) - x**6 / (6 * 5 * 4 * 3 * 2)
    error = abs(math.cos(x) - guess)
    assert almostEqual(cosineError(x, 3), error)
    print("Passed!")


testCosineError()
