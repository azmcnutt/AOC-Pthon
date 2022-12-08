import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """30373
25512
65332
33549
35390""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=8, year=2022).splitlines()

starttime = time.time()

# we need to turn lines of text into a 2D array of ints.

for x in range(0, len(myset)):
    row = []
    for y in myset[x]:
        row.append(int(y))
    myset[x] = row

# I now would like a list of columns to make checking N S Trees easy
cols = []
for y in range(0, len(myset[0])):
    col = []
    for x in range(0, len(myset)):
        col.append(myset[x][y])
    cols.append(col)


hidden = 0
tree_score = []
for x in range(1, len(myset) - 1):
    for y in range(1, len(myset[x]) - 1):
        # now, lets look at all trees E, W, N, S and see if each direction has a taller tree:
        # N
        z = min([
            max(cols[y][:x]),
            max(cols[y][x+1:]),
            max(myset[x][:y]),
            max(myset[x][y+1:])
        ])
        if (myset[x][y]) <= z:
            hidden += 1
        
        # print(myset[x][y])
        u = 0
        d = 0
        r = 0
        l = 0
        trees_u = cols[y][:x][::-1]
        trees_d = cols[y][x+1:]
        trees_l = myset[x][:y][::-1]
        trees_r = myset[x][y+1:]
        for _ in trees_u:
            u += 1
            if _ >= myset[x][y]: break
        for _ in trees_d:
            d += 1
            if _ >= myset[x][y]: break
        for _ in trees_l:
            l += 1
            if _ >= myset[x][y]: break
        for _ in trees_r:
            r += 1
            if _ >= myset[x][y]: break
        # print(f'U:{u} L:{l}, R:{r}, D:{d}')
        tree_score.append(u * d * l * r)
        





print(f'Part 1 Answer is {(len(myset) * len(myset[0])) - hidden}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {max(tree_score)}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
