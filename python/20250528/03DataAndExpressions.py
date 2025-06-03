import math


def f():
    print("This is a user-defined function")
    return 42


print("Some basic types in Python:")
print(type(2))
print(type(2.2))
print(type("Hello"))
print(type(True))
print(type(math))
print(type(math.tan))
print(type(f))
print(type(type(42)))

print(
    "#################################################################################"
)

print(type(Exception()))
print(type(range(5)))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({1: 42}))
print(type(2 + 3j))

print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
import math

print(math.pi)
print(math.e)

print("Type conversion functions:")
print(bool(0))
print(float(42))
print(int(2.2))

print("And some basic math functions:")
print(abs(-5))
print(max(2, 3))
print(min(1, 2))
print(pow(2, 3))  # 2的3次方
print(round(2.345, 1))  #  四舍五入

print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
# print(3 + "def")

print("The / operator does 'normal' float division:")
print(" 5/3  =", (5 / 3))
print()
print("The // operator does integer division:")
print(" 5//3 =", (5 // 3))
print(" 2//3 =", (2 // 3))
print("-1//3 =", (-1 // 3))
print("-4//3 =", (-4 // 3))

print("-------------------------------------------------------------------------------")
print(" 6%3 =", (6 % 3))
print(" 5%3 =", (5 % 3))
print(" 2%3 =", (2 % 3))
print(" 0%3 =", (0 % 3))
print("-4%3 =", (-4 % 3))
# print(" 3%0 =", (3 % 0))


def mod(a, b):
    return a - (a // b) * b


print(41 % 14, mod(41, 14))

print("Precedence:")
print(2 + 3 * 4)
print(5 + 4 % 3)
print(2**3 * 4)

print(0.1 + 0.1 == 0.2)  # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)  # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3)  # prints 5.55111512313e-17 (tiny, but non-zero!)

print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)  # False (never use == with floats!)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True!

print()
print("Once again, using a useful helper function, almostEqual:")


def almostEqual(d1, d2):
    epsilon = 10**-10
    return abs(d2 - d1) < epsilon


d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)  # still False, of course
print(almostEqual(d1, d2))  # True, and now packaged in a handy reusable function!


def isPositive(n):
    result = n > 0
    print("isPositive(", n, ") =", result)
    return result


def isEven(n):
    result = n % 2 == 0
    print("isEven(", n, ") =", result)
    return result


print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4))  # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(
    isEven(-3) and isPositive(-3)
)  # Calls only one function!（一假就返回，不需要判断后面的函数了）
