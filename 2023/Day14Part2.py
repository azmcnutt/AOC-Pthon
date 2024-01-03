import math
import os
import sys
import copy
from pprint import pprint
from aocd import get_data, submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 14: Parabolic Reflector Dish ---                                                                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=14, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

for i, _ in enumerate(myset):
    myset[i] = list(_)

max_x = len(myset) - 1
max_y = len(myset[0]) - 1
max_load = len(myset)

loop_check = []

# for i in myset:
#     print(i)
# print()
for _ in range(0, 999999999):
    # north
    for ix, x in enumerate(myset):
        for iy, y in enumerate(x):
            if 'O' != y != '#':
                # look down the row to see if there is a rock we can slide up
                for ic in range(ix + 1, len(myset)):
                    if myset[ic][iy] == '#':
                        # solid rock found, we're done with this one
                        break
                    elif myset[ic][iy] == 'O':
                        myset[ic][iy] = '.'
                        myset[ix][iy] = 'O'
                        break

    # west
    for ix, x in enumerate(myset):
        for iy, y in enumerate(x):
            if 'O' != y != '#':
                # look east the row to see if there is a rock we can slide up
                for ic in range(iy + 1, len(myset[0])):
                    if myset[ix][ic] == '#':
                        # solid rock found, we're done with this one
                        break
                    elif myset[ix][ic] == 'O':
                        myset[ix][ic] = '.'
                        myset[ix][iy] = 'O'
                        break

    # south
    for ix in range(len(myset) - 1, -1, -1):
        for iy in range(len(myset[0]) - 1, -1, -1):
            if 'O' != myset[ix][iy] != '#':
                # look up the row to see if there is a rock we can slide up
                for ic in range(ix - 1, -1, -1):
                    if myset[ic][iy] == '#':
                        # solid rock found, we're done with this one
                        break
                    elif myset[ic][iy] == 'O':
                        myset[ic][iy] = '.'
                        myset[ix][iy] = 'O'
                        break

    # east
    for ix in range(len(myset) - 1, -1, -1):
        for iy in range(len(myset[0]) - 1, -1, -1):
            if 'O' != myset[ix][iy] != '#':
                # look east the row to see if there is a rock we can slide up
                for ic in range(iy - 1, -1, -1):
                    if myset[ix][ic] == '#':
                        # solid rock found, we're done with this one
                        break
                    elif myset[ix][ic] == 'O':
                        myset[ix][ic] = '.'
                        myset[ix][iy] = 'O'
                        break
    if myset in loop_check:
        # found a look at _
        # once we find the loop, we do the following to find the 1 000 000 000 loop:
        # subtract the loop count from 1 000 000 000 minus 1 (because our loop count starts at 0) to get the number
        #   of loops left
        # subtract the loop count from the first occurrence where the loop started to get our loop size
        # do loops left MOD loop size.  This tells us how far before the end the last loop starts
        # ass in the index of the first occurrence of the loop to get the index of where the rocks will be
        #   on the 1 000 000 000 loop
        one_mil_loop = ((999999999 - _) % (_ - loop_check.index(myset))) + loop_check.index(myset)
        break
    else:
        loop_check.append(copy.deepcopy(myset))
    # for i in myset:
    #     print(i)
    # print()

# now get the load of the one millionth loop
for ix, x in enumerate(loop_check[one_mil_loop]):
# for ix, x in enumerate(loop_check[5]):
    for iy, y in enumerate(x):
        if y == 'O':
            p2ans += max_load - ix


print(f'P2: {p2ans} in {time.time() - start_time} seconds.')
