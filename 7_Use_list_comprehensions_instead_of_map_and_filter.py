# Item 7: Use List Comprehensions Instead of map and filter
# ------------------------------------------------------------------------

from random import randint

matrix = [[1,2,3],[4,5,6],[7,8,9]]
empty = []
flat = [x for row in matrix for x in row]
flat2 = [[x for x in row] for row in matrix]

for row in matrix:
    for x in row:
        empty.append(x)

squared = [[x**2 for x in row] for row in matrix]
print(empty)