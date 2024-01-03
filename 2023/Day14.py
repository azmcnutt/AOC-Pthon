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

# for i in myset:
#     print(i)
# print()

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

# for i in myset:
#     print(i)
# print()

for ix, x in enumerate(myset):
    for iy, y in enumerate(x):
        if y == 'O':
            p1ans += max_load - ix


print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
