def isFactor(f, n):
    if n == 0:
        return True
    if f == 0:
        return False
    if n % f == 0:
        return True


def testIsFactor():
    print("Testing isFactor()...", end="")
    assert isFactor(2, 2)
    assert isFactor(2, 4)
    assert not isFactor(2, 5)
    assert not isFactor(0, 6)
    assert isFactor(6, 0)
    assert isFactor(0, 0)
    assert isFactor(-2, 4)
    print("Passed!")


testIsFactor()

import math


def kthDigit(n, k):
    positiveN = abs(n)
    numK = (positiveN // (10**k)) % 10
    if positiveN < 10**k:
        return 0
    return numK


def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert kthDigit(0, 0) == 0
    assert kthDigit(789, 0) == 9
    assert kthDigit(789, 1) == 8
    assert kthDigit(789, 2) == 7
    assert kthDigit(789, 3) == 0
    assert kthDigit(-1234, 3) == 1
    assert kthDigit(-3, 1) == 0
    print("Passed!")


testKthDigit()


def isAlmostInteger(n):
    n = abs(n)
    epsilon = 0.0001
    return abs(n - 5) < epsilon


def testIsAlmostInteger():
    print("Testing isAlmostInteger()...", end="")
    assert isAlmostInteger(5) == True
    assert isAlmostInteger(5.0001) == True
    assert isAlmostInteger(4.9999) == True
    assert isAlmostInteger(5.00011) == False
    assert isAlmostInteger(4.99989) == False
    assert isAlmostInteger(-4.9999) == True
    assert isAlmostInteger(-5.00011) == False
    print("Passed.")


testIsAlmostInteger()


def isPerfectSquare(n):
    if n < 0:
        return False
    return math.sqrt(n) % 2 == 0


def testIsPerfectSquare():
    print("Testing isPerfectSquare...", end="")
    assert isPerfectSquare(16) == True
    assert isPerfectSquare(32) == False
    assert isPerfectSquare(0) == True
    assert isPerfectSquare(15) == False
    assert isPerfectSquare(-16) == False
    print("Passed!")


testIsPerfectSquare()

import math


def fabricExcess(fabricInches):
    yards = math.ceil(fabricInches / 36)
    excess = yards * 36 - fabricInches
    return excess


def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1 - d2) <= epsilon


def testFabricExcess():
    print("Testing fabricExcess()...", end="")
    assert fabricExcess(0) == 0
    assert fabricExcess(1) == 35
    assert fabricExcess(35) == 1
    assert fabricExcess(36) == 0
    assert fabricExcess(37) == 35
    # use almostEqual when comparing floats
    assert almostEqual(fabricExcess(35.5), 0.5)
    assert almostEqual(fabricExcess(36.5), 35.5)
    print("Passed.")


testFabricExcess()


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# 海伦公式
def triangleArea(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1 - d2) <= epsilon


def testTriangleArea():
    print("Testing triangleArea...", end="")
    assert almostEqual(triangleArea(0, 0, 0, 2, 2, 0), 2.0)
    assert almostEqual(triangleArea(0, 0, 4, 0, 2, 6), 12.0)
    assert almostEqual(triangleArea(0, 0, -4, 0, -2, -6), 12.0)
    print("Passed!")


testTriangleArea()
