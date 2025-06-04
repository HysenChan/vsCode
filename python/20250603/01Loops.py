def sumFromMToN(m, n):
    total = 0
    # range(x,y)包含x但不包含y
    for i in range(m, n + 1):
        total = total + i
    return total


print(sumFromMToN(1, 10) == 55)

print(sum(range(1, 10 + 1)))


def sumEveryKthFromMToN(m, n, k):
    total = 0
    for i in range(m, n + 1, k):
        total = total + i
    return total


print(sumEveryKthFromMToN(1, 10, 8) == 10)


def sumOfOddsFromMToN(m, n):
    total = 0
    for i in range(m, n + 1):
        if i % 2 == 1:
            total += i
    return total


print(sumOfOddsFromMToN(1, 5) == 9)


def sumOfOddsFromMToN(m, n):
    if m % 2 == 0:
        m += 1
    total = 0
    for i in range(m, n + 1, 2):
        total += i
    return total


print(sumOfOddsFromMToN(4, 10) == 21)


def printCoordinates(xMax, yMax):
    for x in range(xMax + 1):
        for y in range(yMax + 1):
            print("(", x, ",", y, ")")
        print()


printCoordinates(3, 3)


def printStarRectangle(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


printStarRectangle(5)

# What would this do? Be careful and be precise!


def printMysteryStarShape(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()


printMysteryStarShape(5)

# use while loops when there is an indeterminate number of iterations


def leftmostDigit(n):
    n = abs(n)
    while n >= 10:
        n = n // 10
    return n


print(leftmostDigit(72658489290098) == 7)


def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)


def nthMultipleOf4or7(n):
    count = 0
    x = 0
    while count <= n:
        x = x + 1
        if isMultipleOf4or7(x):
            count = count + 1
    return x


print("Multiples of  4 or 7:", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
    print()


def buggySumToN(n):
    # note: this not only uses a "while" instead of a "for" loop,
    # but it also contains a bug. Ugh.
    total = 0
    counter = 0
    while counter < n:
        counter += 1
        total += counter
    return total


print(buggySumToN(5) == 1 + 2 + 3 + 4 + 5)

for n in range(200):
    if n % 3 == 0:
        continue  # skips rest of this pass (rarely a good idea to use "continue")
    elif n == 8:
        break  # skips rest of entire loop
    print(n, end=" ")
print()


def readUntilDone():
    linesEntered = 0
    while True:
        response = input("Enter a string (or 'done' to quit): ")
        if response == "done":
            break
        print("  You entered: ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered


# linesEntered = readUntilDone()
# print("You entered", linesEntered, "lines (not counting 'done').")


# Note: there are faster/better ways.  We're just going for clarity and simplicity here.
def isPrime(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


# And take it for a spin
for n in range(100):
    if isPrime(n):
        print(n, end=" ")
print()


# Note: this is still not the fastest way, but it's a nice improvement.
def fasterIsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor + 1, 2):
        if n % factor == 0:
            return False
    return True


# And try out this version:
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()


def isPrime(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def fasterIsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor + 1, 2):
        if n % factor == 0:
            return False
    return True


# Verify these are the same
for n in range(100):
    assert isPrime(n) == fasterIsPrime(n)
print("They seem to work the same!")

# Now let's see if we really sped things up
import time

bigPrime = 499  # Try 1010809, or 10101023, or 102030407
print("Timing isPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1 - time0) * 1000, "ms")

print("Timing fasterIsPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1 - time0) * 1000, "ms")
