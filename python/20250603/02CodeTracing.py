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
    num = abs(n)


def testNthPerfectNumber():
    print("Testing nthPerfectNumber()...", end="")
    assert nthPerfectNumber(0) == 6
    assert nthPerfectNumber(1) == 28
    # assert(nthPerfectNumber(2) == 496)  # this can be slow in Brython
    # assert(nthPerfectNumber(3) == 8128) # this can be slow even in Standard Python!
    print("Passed!")


testNthPerfectNumber()
