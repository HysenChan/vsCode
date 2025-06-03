import math


def helloWorld():
    print("Hello World")


helloWorld()

print("Carpe", "diem")

print()

a = 3
b = 4
c = ((a**2) + (b**2)) ** 0.5
print("size a = ", a)
print("size b = ", b)
print("size c = ", c)

# name = input("Enter your name: ")
# print("Your name is:", name)

# x = int(input("Enter a number: "))
# print("One half of", x, "=", x / 2)
print(math.factorial(20))
print(dir(math))
print(math.pi)

import webbrowser

print(dir(webbrowser))
print("Hit enter to see the online docs for the math module")
webbrowser.open("https://docs.python.org/3/library/math.html")
