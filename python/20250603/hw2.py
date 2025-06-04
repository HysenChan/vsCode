# hw1.py
# name + andrewId + section

import math


def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d2 - d1) < epsilon


def sumOfSquaresOfDigits(n):
    total = 0
    while n > 0:
        total += (n % 10) ** 2
        n = n // 10
    return total


def isSumOfSquaresOfDigits():
    assert sumOfSquaresOfDigits(5) == 25  # 5**2 = 25
    assert sumOfSquaresOfDigits(12) == 5  # 1**2 + 2**2 = 1+4 = 5
    assert sumOfSquaresOfDigits(234) == 29  # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29


def isHappyNumber(n):
    if n < 1:
        return False
    seen = set()
    while n != 1:
        total = 0
        num = n
        while num > 0:
            total = sumOfSquaresOfDigits(n)
            num //= 10
        if total in seen:
            return False

        seen.add(total)
        n = total
    return True


def isHappyNumbers():
    assert isHappyNumber(-7) == False
    assert isHappyNumber(7) == True
    assert isHappyNumber(1) == True
    assert isHappyNumber(2) == False
    assert isHappyNumber(97) == True
    assert isHappyNumber(98) == False
    assert isHappyNumber(404) == True
    assert isHappyNumber(405) == False


def nthHappyNumber(n):
    count = -1
    num = 0
    while count < n:
        num += 1
        if isHappyNumber(num):
            count += 1
    return num


def isNthHappyNum():
    assert nthHappyNumber(0) == 1
    assert nthHappyNumber(1) == 7
    assert nthHappyNumber(2) == 10
    assert nthHappyNumber(3) == 13
    assert nthHappyNumber(4) == 19
    assert nthHappyNumber(5) == 23
    assert nthHappyNumber(6) == 28
    assert nthHappyNumber(7) == 31


def nthHappyPrime(n):
    count = -1
    num = 1
    while count < n:
        num += 1
        if isHappyNumber(num):
            p = 0
            for i in range(2, num):
                if num % i == 0:
                    p += 1
            if p == 0:
                count += 1
    return num


def isNthHappyPrime():
    assert nthHappyPrime(0) == 7
    assert nthHappyPrime(1) == 13
    assert nthHappyPrime(2) == 19
    assert nthHappyPrime(3) == 23
    assert nthHappyPrime(4) == 31


def testAll():
    isSumOfSquaresOfDigits()
    isHappyNumbers()
    isNthHappyNum()
    isNthHappyPrime()


if __name__ == "__main__":
    testAll()
