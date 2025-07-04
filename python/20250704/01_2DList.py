a = [[2, 3, 4], [5, 6, 7]]

print(a)

# Try, and FAIL, to create a variable-sized 2d list
rows = 3
cols = 2

a = [[0] * cols] * rows  # Error: creates shallow copy
# Creates one unique row, the rest are aliases!

print("This SEEMS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("   a =", a)

# Create a variable-sized 2d list
rows = 3
cols = 2

a = []
for row in range(rows):
    a += [[0] * cols]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)


def make2dList(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a


rows = 3
cols = 2

a = make2dList(rows, cols)

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)

rows = 3
cols = 2

a = [([0] * cols) for row in range(rows)]

print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)

# Create an "arbitrary" 2d List
a = [[2, 3, 5], [1, 4, 7]]
print("a = ", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])
print("rows =", rows)
print("cols =", cols)

# Create an "arbitrary" 2d List
a = [[2, 3, 5], [1, 4, 7]]
print("Before: a =", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])

# And now loop over every element
# Here, we'll add one to each element,
# just to make a change we can easily see
for row in range(rows):
    for col in range(cols):
        # This code will be run rows*cols times, once for each
        # element in the 2d list
        a[row][col] += 1

# Finally, print the results
print("After:  a =", a)

import copy

# Create a 2d list
a = [[1, 2, 3], [4, 5, 6]]

# Try to copy it
b = copy.copy(a)  # Error:  creates shallow copy

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("But after a[0][0] = 9")
print("   a =", a)
print("   b =", b)

import copy

# Create a 2d list
a = [[1, 2, 3], [4, 5, 6]]

# Try to copy it
b = copy.deepcopy(a)  # Correct!

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("And after a[0][0] = 9")
print("   a =", a)
print("   b =", b)

a = [[0] * 2] * 3  # makes 3 shallow copies of (aliases of) the same row
a[0][0] = 42  # appears to modify all 3 rows
print(a)  # prints [[42, 0], [42, 0], [42, 0]]

# now do it again with a deepcopy

import copy

a = [[0] * 2] * 3  # makes 3 shallow copies of the same row
a = copy.deepcopy(a)  # meant to make each row distinct
a[0][0] = 42  # so we hope this only modifies first row
print(a)  # STILL prints [[42, 0], [42, 0], [42, 0]]

# now one more time with a simple deepcopy alternative that does
# what we thought deepcopy did...


def myDeepCopy(a):
    if isinstance(a, list) or isinstance(a, tuple):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)


a = [[0] * 2] * 3  # makes 3 shallow copies of the same row
a = myDeepCopy(a)  # once again, meant to make each row distinct
a[0][0] = 42  # so we hope this only modifies first row
print(a)  # finally, prints [[42, 0], [0, 0], [0, 0]]

# what's going on with deepcopy? Answer: if the original list has aliases,
# the deepcopied list will have aliases (of a single copy, not the original).
# So copy.deepcopy preserves alias structure!


# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen


# Because Python prints 2d lists on one row,
# we might want to write our own function
# that prints 2d lists a bit nicer.
def print2dList(a):
    if a == []:
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if row > 0:
            print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if col > 0:
                print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]")


# Let's give the new function a try!
a = [[1, 2, 3], [4, 5, 67]]
print2dList(a)

# alias (not a copy!); cheap (no new list created)
a = [[1, 2, 3], [4, 5, 6]]
row = 1
rowList = a[row]
print(rowList)

# copy (not an alias!); expensive (new list created)
a = [[1, 2, 3], [4, 5, 6]]
col = 1
colList = []
for i in range(len(a)):
    colList += [a[i][col]]
print(colList)

# still a copy, still expensive, but cheaper and cleaner with a list comprehension!
a = [[1, 2, 3], [4, 5, 6]]
col = 1
colList = [a[i][col] for i in range(len(a))]
print(colList)

# 2d lists do not have to be rectangular
a = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]

rows = len(a)
for row in range(rows):
    cols = len(a[row])  # now cols depends on each row
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(a[row][col], " ", end="")
    print()

# 2d lists do not really exist in Python.
# They are just lists that happen to contain other lists as elements.
# And so this can be done for "3d lists", or even "4d" or higher-dimensional lists.
# And these can also be non-rectangular, of course!

a = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9]], [[10]]]

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print("a[%d][%d][%d] = %d" % (i, j, k, a[i][j][k]))
