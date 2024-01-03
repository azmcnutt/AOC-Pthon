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
# --- Day 11: Cosmic Expansion ---                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=11, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

all_x = set()
all_y = set()
max_x = len(myset) - 1
max_y = len(myset[0]) - 1
galaxies = []

for x, r in enumerate(myset):
    for y, z in enumerate(r):
        if z == '#':
            all_x.add(x)
            all_y.add(y)
            galaxies.append((x, y))

# print(all_x, all_y)
# print(galaxies)
# print(max_x, max_y)


def distance(point1, point2, expansion=1):
    x1, y1 = point1
    x2, y2 = point2
    d = abs(x1 - x2) + abs(y1 - y2)
    if x1 > x2:
        x2, x1 = x1, x2
    if y1 > y2:
        y2, y1 = y1, y2

    for z in range(x1, x2 + 1):
        if z not in all_x:
            d += expansion
    for z in range(y1, y2 + 1):
        if z not in all_y:
            d += expansion
    return d


# Part 1
for i1, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies):
        if i1 < i2:
            p1ans += distance(g1, g2)

# Part 2
for i1, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies):
        if i1 < i2:
            p2ans += distance(g1, g2, 999999)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
