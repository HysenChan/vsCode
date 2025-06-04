# single-quoted or double-quoted strings are the most common
print("single-quotes")
print("double-quotes")

# triple-qouted strings are less common (though see next section for a typical use)
print("""triple single-quotes""")
print("""triple double-quotes""")

print("abc\ndef")  # \n is a single newline character
print(
    """abc
def"""
)

print(
    """\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
"""
)

print('Double-quote: "')
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")

s = 'a\\b"c\td'
print("s =", s)
print("len(s) =", len(s))

s = "abc" "def"  # ok (but "abc" + "def" is preferred)
print(s)
# s = s "def" # error (only works with string literals, not variables)

"""
Python does not have multiline comments, but you can do something similar
by using a top-level multiline string, such as this. Technically, this is
not a comment, and Python will evaluate this string, but then ignore it
and garbage collect it!
"""
print("wow!")

import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print("-----------")
print(string.punctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)  # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)  # space + tab + linefeed + return + ...

print("abc" + "def")
print("abc" * 3)
# print("abc" + 3)  # error

print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")

s = "abcdefgh"
print(s)
print(s[0])
print(s[1])
print(s[2])

print("-----------")
print(s[len(s) - 1])
# print(s[len(s)])  # crashes (string index out of range)

s = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])

s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3])

s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])

print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])

s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")


def reverseString(s):
    return s[::-1]


print(reverseString(s))  # crystal clear!

s = "abcd"
for i in range(len(s)):
    print(i, s[i])

s = "abcd"
for c in s:
    print(c)

names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)

# quotes from brainyquote.com
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if line.startswith("Knuth"):
        print(line)
