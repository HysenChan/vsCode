import string
import re


def sameChars(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return False

    if s1 == "" and s2 == "":
        return True

    return set(s1) == set(s2)


# 测试用例
print(sameChars("abc", "cba"))  # True（相同字符）
print(sameChars("abc", "ab"))  # False（缺少'c'）
print(sameChars("ABC", "abc"))  # False（大小写敏感）
print(sameChars("", ""))  # True（空字符串）
print(sameChars("a", 123))  # False（非字符串）
print(sameChars("aabbcc", "abc"))  # True（字符种类相同）


def wordWrap(text, width):
    # 初始化结果列表和当前行
    lines = []
    current_line = ""

    # 遍历每个字符
    for char in text:
        # 当达到宽度限制时换行
        if len(current_line) == width:
            # 移除首尾空格并替换中间空格为短横
            processed_line = current_line.strip().replace(" ", "-")
            lines.append(processed_line)
            current_line = char  # 新行以当前字符开始
        else:
            current_line += char

    # 处理最后一行
    if current_line:
        processed_line = current_line.strip().replace(" ", "-")
        lines.append(processed_line)

    # 用换行符连接所有行
    return "\n".join(lines)


assert (
    wordWrap("abcdefghij", 4)
    == """\
abcd
efgh
ij"""
)
assert (
    wordWrap("a b c de fg", 4)
    == """\
a-b
c-de
fg"""
)


def largestNumber(s):
    numbers = re.findall(r"\d+", s)

    if not numbers:
        return None
    return max(map(int, numbers))


assert largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17
assert largestNumber("One person ate two hot dogs!") == None


def longestSubpalindrome(s):
    if not s:
        return ""

    n = len(s)
    max_str = ""
    max_len = 0

    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        odd_pal = s[l + 1 : r]

        if i < n - 1:
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            even_pal = s[l + 1 : r]
        else:
            even_pal = ""

        for pal in [odd_pal, even_pal]:
            if len(pal) > max_len:
                max_len = len(pal)
                max_str = pal
            elif len(pal) == max_len and pal > max_str:
                max_str = pal

    return max_str


assert longestSubpalindrome("ab-4-be!!!") == "b-4-b"
assert longestSubpalindrome("abcbce") == "cbc"


def longestCommonSubstring(s1, s2):
    if not s1 or not s2:
        return ""

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    m, n = len(s1), len(s2)
    dp = [0] * (n + 1)
    max_len = 0
    result = ""

    for i in range(m):
        prev = 0
        for j in range(n):
            temp = dp[j + 1]
            if s1[i] == s2[j]:
                dp[j + 1] = prev + 1
                current_len = dp[j + 1]
                start_idx = i - current_len + 1
                current_sub = s1[start_idx : i + 1]

                if current_len > max_len:
                    max_len = current_len
                    result = current_sub
                elif current_len == max_len and current_sub < result:
                    result = current_sub
            else:
                dp[j + 1] = 0
            prev = temp
    return result


assert longestCommonSubstring("abcdef", "abqrcdest") == "cde"
assert longestCommonSubstring("abcdef", "ghi") == ""


def leastFrequentLetters(s):
    letters = [char.lower() for char in s if char.isalpha()]

    if not letters:  # 使用 not 检查空列表
        return ""

    count = {}
    for char in letters:
        count[char] = count.get(char, 0) + 1

    min_count = min(count.values())

    result_chars = sorted(char for char, freq in count.items() if freq == min_count)

    return "".join(result_chars)


assert leastFrequentLetters("aDq efQ? FB'daf!!!") == "be"
