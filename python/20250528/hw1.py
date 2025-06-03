# hw1.py
# name + andrewId + section

import math


def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d2 - d1) < epsilon


def nearestBusStop(street):
    base_stop = (street // 8) * 8
    next_stop = base_stop + 8

    left_dist = street - base_stop
    right_dist = next_stop - street

    if left_dist <= right_dist:
        return base_stop
    else:
        return next_stop


def setKthDigit(n, k, d):
    low = n % (10**k)
    high = n // (10 ** (k + 1))
    return high * (10 ** (k + 1)) + d * (10**k) + low


def cosineZerosCount(r):
    if r < 0:
        return 0
    k_max = math.floor(r / math.pi - 0.5 + 1e-10)
    count = k_max + 1

    return max(0, count)


def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    halfDistance = totalDistance / 2
    a = totalTime
    b = -totalDistance
    c = -2 * totalTime * riverCurrent
    judge = (b * b) - (4 * a * c)
    if judge < 0:
        return -1
    tempA = -b
    tempB = math.sqrt(judge)
    tempC = 2 * a
    x1 = (tempA + tempB) / tempC
    x2 = (tempA - tempB) / tempC
    if x1 > 0:
        return halfDistance / (x1 - riverCurrent)
    else:
        return halfDistance / (x2 - riverCurrent)


def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
    right1 = left1 + width1
    bottom1 = top1 + height1
    right2 = left2 + width2
    bottom2 = top2 + height2

    if left1 <= right2 and left2 <= right1 and top1 <= bottom2 and top2 <= bottom1:
        return True
    else:
        return False


# y=mx+b
# m1*x+b1=m2*x+b2
def lineIntersection(m1, b1, m2, b2):
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def triangleArea(s1, s2, s3):
    p = (s1 + s2 + s3) / 2
    return math.sqrt(p * (p - s1) * (p - s2) * (p - s3))


def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1, b1, m2, b2)
    y1 = m1 * x1 + b1
    x2 = lineIntersection(m2, b2, m3, b3)
    y2 = m2 * x2 + b2
    x3 = lineIntersection(m3, b3, m1, b1)
    y3 = m3 * x3 + b3

    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x3, y3, x1, y1)
    return triangleArea(s1, s2, s3)


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################


def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert nearestBusStop(0) == 0
    assert nearestBusStop(4) == 0
    assert nearestBusStop(5) == 8
    assert nearestBusStop(12) == 8
    assert nearestBusStop(13) == 16
    assert nearestBusStop(20) == 16
    assert nearestBusStop(21) == 24
    print("Passed. (Add more tests to be more sure!)")


def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert setKthDigit(468, 0, 1) == 461
    assert setKthDigit(468, 1, 1) == 418
    assert setKthDigit(468, 2, 1) == 168
    assert setKthDigit(468, 3, 1) == 1468
    print("Passed. (Add more tests to be more sure!)")


def testCosineZerosCount():
    print("Testing cosineZerosCount()...", end="")
    assert type(cosineZerosCount(0)) == int
    assert cosineZerosCount(0) == 0
    assert cosineZerosCount(math.pi / 2 - 0.0001) == 0
    assert cosineZerosCount(math.pi / 2 + 0.0001) == 1
    assert cosineZerosCount(3 * math.pi / 2 - 0.0001) == 1
    assert cosineZerosCount(3 * math.pi / 2 + 0.0001) == 2
    assert cosineZerosCount(5 * math.pi / 2 - 0.0001) == 2
    assert cosineZerosCount(5 * math.pi / 2 + 0.0001) == 3
    assert cosineZerosCount(-math.pi / 2 - 0.0001) == 0
    assert cosineZerosCount(-math.pi / 2 + 0.0001) == 0
    print("Passed. (Add more tests to be more sure!)")


def testRiverCruiseUpstreamTime():
    print("Testing riverCruiseUpstreamTime()...", end="")
    # example from the source notes:
    totalTime = 3  # hours
    totalDistance = 30  # 15km up, 15km back down
    riverCurrent = 2  # km/hour
    assert almostEqual(
        riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent),
        1.7888736053508778,
    )  # 1.79 in notes
    # another simple example
    totalTime = 3  # hours
    totalDistance = 30  # 15km up, 15km back down
    riverCurrent = 0  # km/hour
    assert almostEqual(
        riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent), 1.5
    )
    print("Passed. (Add more tests to be more sure!)")


def testRectanglesOverlap():
    print("Testing rectanglesOverlap()...", end="")
    assert type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool
    assert rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True
    assert rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True
    assert rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True
    assert rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False
    assert rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False
    assert rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True
    print("Passed. (Add more tests to be more sure!)")


def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert lineIntersection(2.5, 3, 2.5, 11) == None
    assert lineIntersection(25, 3, 25, 11) == None
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert almostEqual(lineIntersection(3, -5, 1, 5), 5)
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert almostEqual(lineIntersection(10, 0, -4, 35), 2.5)
    print("Passed. (Add more tests to be more sure!)")


def testDistance():
    print("Testing distance()...", end="")
    assert almostEqual(distance(0, 0, 1, 1), 2**0.5)
    assert almostEqual(distance(3, 3, -3, -3), 6 * 2**0.5)
    assert almostEqual(distance(20, 20, 23, 24), 5)
    print("Passed. (Add more tests to be more sure!)")


def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert almostEqual(triangleArea(3, 4, 5), 6)
    assert almostEqual(triangleArea(2**0.5, 1, 1), 0.5)
    assert almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1)
    print("Passed. (Add more tests to be more sure!)")


def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0)
    assert almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36)
    assert almostEqual(threeLinesArea(0, 3, -0.5, -5, 1, 3), 42.66666666666)
    assert almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25)
    assert almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21)
    print("Passed. (Add more tests to be more sure!)")


def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e, f, g = root1, root2, root3
    return k, -k * (e + f + g), k * (e * f + f * g + e * g), -k * e * f * g


def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a, b, c, d = getCubicCoeffs(k, z1, z2, z3)
    observed = findIntRootsOfCubic(a, b, c, d)
    actual = tuple(sorted([z1, z2, z3]))
    assert observed == actual


def testBonusFindIntRootsOfCubic():
    # only test the bonus if they tried it...
    if "findIntRootsOfCubic" not in globals():
        return
    print("Testing findIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3, 2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed. (Add more tests to be more sure!)")


def testAll():
    testNearestBusStop()
    testSetKthDigit()
    testCosineZerosCount()
    testRiverCruiseUpstreamTime()
    testRectanglesOverlap()
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()


if __name__ == "__main__":
    testAll()
