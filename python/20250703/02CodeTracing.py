def onesDigit(n):
    return n % 10


def ct1(L):
    for i in range(len(L)):
        L[i] += sum(L) + max(L)
    return sorted(L, key=onesDigit)


a = [2, 1, 0]

print(ct1(a))
print(a)


# Code Tracing #2 of 2
def ct2(a, b):
    a += [3]
    a = a + [4]
    for c in a:
        for i in range(len(b)):
            if b[i] not in a:
                print("A", end="")
                b[i] += c
            elif c % 2 == 1:
                print("B", end="")
                b += [c]
            elif b[-1] != c:
                print("C", end="")
                b = b + [c]
    return (a, b)


a = [4]
b = [2, 3]
print(ct2(a, b))
print(a, b)


def areaOfPolygon(L):
    n = len(L)
    area = 0.0

    for i in range(n):
        x1, y1 = L[i]
        x2, y2 = L[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area / 2.0)


def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon


def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert almostEqual(areaOfPolygon([(4, 10), (9, 7), (11, 2), (2, 2)]), 45.5)
    assert almostEqual(areaOfPolygon([(9, 7), (11, 2), (2, 2), (4, 10)]), 45.5)
    assert almostEqual(areaOfPolygon([(0, 0), (0.5, 1), (1, 0)]), 0.5)
    assert almostEqual(areaOfPolygon([(0, 10), (0.5, 11), (1, 10)]), 0.5)
    assert almostEqual(areaOfPolygon([(-0.5, 10), (0, -11), (0.5, 10)]), 10.5)
    print("Passed!")


testAreaOfPolygon()


# 霍纳法则将多项式转化为嵌套形式，避免直接计算高次幂
def evalPolynomial(coeffs, x):
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
    return result


def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert evalPolynomial([2, 3, 0, 4], 4) == 180
    # f(x) = 6, f(42) = 6
    assert evalPolynomial([6], 42) == 6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert evalPolynomial([6, -2, -20], -1) == -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert evalPolynomial([6, 0, -8, 0, -8, 0], 2) == 112
    assert evalPolynomial([6, 0, -8, 0, -8, 0], 1) == -10
    assert evalPolynomial([6, 0, -8, 0, -8, 0], 0) == 0
    print("Passed!")


testEvalPolynomial()


def multiplyPolynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)

    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result


def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert multiplyPolynomials([2], [3]) == [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert multiplyPolynomials([2, -4], [3, 5]) == [6, -2, -20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert multiplyPolynomials([2, 0, -4], [3, 0, 2, 0]) == [6, 0, -8, 0, -8, 0]
    print("Passed!")


testMultiplyPolynomials()


def repeatingPattern(L):
    n = len(L)
    # 如果列表长度小于2，无法形成重复模式
    if n < 2:
        return None

    # 遍历可能的模式长度（从1到n//2）
    for pattern_len in range(1, n // 2 + 1):
        # 检查n是否能被当前模式长度整除
        if n % pattern_len != 0:
            continue

        # 计算重复次数
        k = n // pattern_len
        # 检查每一段是否都等于第一段
        found = True
        for i in range(1, k):
            # 比较第i段与第一段
            start_index = i * pattern_len
            for j in range(pattern_len):
                if L[j] != L[start_index + j]:
                    found = False
                    break
            if not found:
                break

        # 如果找到，返回模式（第一段）和重复次数
        if found:
            return (L[:pattern_len], k)

    # 没有找到任何模式
    return None


def testRepeatingPattern():
    print("Testing repeatingPattern()...", end="")
    assert repeatingPattern([]) == None
    assert repeatingPattern([42]) == None
    assert repeatingPattern([1, 2]) == None
    assert repeatingPattern([1, 1]) == ([1], 2)
    assert repeatingPattern([1, 2, 1]) == None
    assert repeatingPattern([1, 2, 3, 1, 2, 3]) == ([1, 2, 3], 2)
    assert repeatingPattern([1, 2, 3, 1, 2]) == None
    assert repeatingPattern([1, 2, 3, 1, 2, 3, 1]) == None
    L = list(range(10))
    assert repeatingPattern(L * 20) == (L, 20)
    print("Passed!")


testRepeatingPattern()


def isNearlySorted(L):
    n = len(L)
    if n < 2:  # 长度小于2的列表无法交换
        return False

    # 检查是否已有序（非严格升序）
    isOrdered = True
    for i in range(n - 1):
        if L[i] > L[i + 1]:
            isOrdered = False
            break
    if isOrdered:  # 已有序无需交换
        return False

    # 寻找第一个逆序位置i
    i = 0
    while i < n - 1 and L[i] <= L[i + 1]:
        i += 1

    # 寻找最后一个逆序位置j
    j = n - 2
    while j >= 0 and L[j] <= L[j + 1]:
        j -= 1

    # 交换位置i和j+1的元素
    L2 = L[:]  # 创建副本避免修改原列表
    L2[i], L2[j + 1] = L2[j + 1], L2[i]

    # 检查交换后是否有序
    for k in range(len(L2) - 1):
        if L2[k] > L2[k + 1]:
            return False
    return True


def testIsNearlySorted():
    print("Testing isNearlySorted()...", end="")
    assert isNearlySorted([0, 1, 2, 3]) == False
    assert isNearlySorted([]) == False
    assert isNearlySorted([42]) == False
    assert isNearlySorted([3, 2]) == True
    assert isNearlySorted([2, 2]) == False
    assert isNearlySorted([5, 2, 3, 4, 1, 6]) == True
    assert isNearlySorted([1, 2, 3, 5, 4]) == True
    print("Passed!")


testIsNearlySorted()
