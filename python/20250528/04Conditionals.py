def f(x):
    print("A", end="")
    if x == 0:
        print("B", end="")
        print("C", end="")
    print("D")


f(0)
f(1)


def abs1(n):
    if n < 0:
        n = -n
    return n


print("abs1(-10) = ", abs1(-10))


def f(x):
    print("A", end="")
    if x == 0:
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if x == 1:
            print("E", end="")
        else:
            print("F", end="")
    print("G", end="")


f(0)
print()
f(1)
print()
f(2)
print()


def numberOfRoots(a, b, c):
    # Returns number of roots (zeros) of y = a*x**2 + b*x + c
    d = b**2 - 4 * a * c
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0


print("y = 4*x**2 + 5*x + 1 has", numberOfRoots(4, 5, 1), "root(s).")
print("y = 4*x**2 + 4*x + 1 has", numberOfRoots(4, 4, 1), "root(s).")
print("y = 4*x**2 + 3*x + 1 has", numberOfRoots(4, 3, 1), "root(s).")


def getGrade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))
