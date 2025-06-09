import string


def vowelCount(s):
    s = s.lower()
    count = 0
    for i in ("a", "e", "i", "o", "u"):
        if s.count(i):
            count += s.count(i)
    return count


def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert vowelCount("abcdefg") == 2
    assert vowelCount("ABCDEFG") == 2
    assert vowelCount("") == 0
    assert vowelCount("This is a test.  12345.") == 4
    assert vowelCount(string.ascii_lowercase) == 5
    assert vowelCount(string.ascii_lowercase * 100) == 500
    assert vowelCount(string.ascii_uppercase) == 5
    assert vowelCount(string.punctuation) == 0
    assert vowelCount(string.whitespace) == 0
    print("Passed!")


testVowelCount()


def interleave(s1, s2):
    # 初始化结果字符串和两个指针
    result = ""
    i, j = 0, 0

    # 循环交替添加字符
    while i < len(s1) and j < len(s2):
        result += s1[i] + s2[j]  # 先添加s1字符，再添加s2字符
        i += 1
        j += 1

    # 添加剩余字符
    if i < len(s1):
        result += s1[i:]
    if j < len(s2):
        result += s2[j:]

    return result


def testInterleave():
    print("Testing interleave()...", end="")
    assert interleave("abcdefg", "abcdefg") == "aabbccddeeffgg"
    assert interleave("abcde", "abcdefgh") == "aabbccddeefgh"
    assert interleave("abcdefgh", "abcde") == "aabbccddeefgh"
    assert (
        interleave("Smlksgeneg n a!", "a ie re gsadhm")
        == "Sam likes green eggs and ham!"
    )
    assert interleave("", "") == ""
    print("Passed!")


testInterleave()

import string


def mostFrequentLetters(s):
    letters = [char.upper() for char in s if char.isalpha()]
    if not letters:  # 使用 not 检查空列表
        return ""
    freq = {char: 0 for char in string.ascii_uppercase}

    for char in s:
        upper_char = char.upper()
        if upper_char in freq:
            freq[upper_char] += 1

    max_freq = 0
    for count in freq.values():
        if count > max_freq:
            max_freq = count

    result_chars = []
    for letter, count in freq.items():
        if count == max_freq:
            result_chars.append(letter)

    result_chars.sort()
    return "".join(result_chars)


def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert mostFrequentLetters("Cat") == "ACT"
    assert mostFrequentLetters("A cat") == "A"
    assert mostFrequentLetters("A cat in the hat") == "AT"
    assert mostFrequentLetters("This is a test") == "ST"
    assert mostFrequentLetters("This is an I test?") == "IST"
    assert mostFrequentLetters("") == ""
    print("Passed!")


testMostFrequentLetters()


def hasBalancedParentheses(s):
    total = 0
    for i in range(len(s)):
        if s[i] == "(":
            total += 1
        elif s[i] == ")":
            total -= 1
        if total < 0:
            return False
    return total == 0


def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert hasBalancedParentheses("()") == True
    assert hasBalancedParentheses("") == True
    assert hasBalancedParentheses("())") == False
    assert hasBalancedParentheses("()(") == False
    assert hasBalancedParentheses(")(") == False
    assert hasBalancedParentheses("(()())") == True
    assert hasBalancedParentheses("((()())(()(()())))") == True
    assert hasBalancedParentheses("((()())(()((()())))") == False
    assert hasBalancedParentheses("((()())(((()())))") == False
    print("Passed!")


testHasBalancedParentheses()

import string


def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_lower = s1.lower()
    s2_lower = s2.lower()

    for char in string.ascii_lowercase:
        if s1_lower.count(char) != s2_lower.count(char):
            return False

    return True


def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert areAnagrams("", "") == True
    assert areAnagrams("abCdabCd", "abcdabcd") == True
    assert areAnagrams("abcdaBcD", "AAbbcddc") == True
    assert areAnagrams("abcdaabcd", "aabbcddcb") == False
    print("Passed!")


testAreAnagrams()


def rotateStringLeft(s, k):
    n = len(s)
    if n == 0:
        return s
    k = k % n

    if k == 0:  # 如果k为0，则不需要旋转
        return s

    lst = list(s)

    def reverse(l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    reverse(lst, 0, k - 1)
    reverse(lst, k, n - 1)
    reverse(lst, 0, n - 1)
    return "".join(lst)

    # return "".join(s[(i + k) % n] for i in range(n))


def testRotateStringLeft():
    print("Testing rotateStringLeft()...", end="")
    assert rotateStringLeft("abcde", 0) == "abcde"
    assert rotateStringLeft("abcde", 1) == "bcdea"
    assert rotateStringLeft("abcde", 2) == "cdeab"
    assert rotateStringLeft("abcde", 3) == "deabc"
    assert rotateStringLeft("abcde", 4) == "eabcd"
    assert rotateStringLeft("abcde", 5) == "abcde"
    assert rotateStringLeft("abcde", 25) == "abcde"
    assert rotateStringLeft("abcde", 28) == "deabc"
    print("Passed!")


testRotateStringLeft()


def collapseWhitespace(s):
    result = []
    in_whitespace = False

    for char in s:
        print(char, char.isspace())
        if char.isspace():
            if not in_whitespace:
                result.append(" ")
                in_whitespace = True
        else:
            result.append(char)
            in_whitespace = False

    return "".join(result)


def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert collapseWhitespace("a\n\n\nb") == "a b"
    assert collapseWhitespace("a\n   \t    b") == "a b"
    assert collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c "
    print("Passed!")


testCollapseWhitespace()
