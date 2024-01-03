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
# --- Day 9: Mirage Maintenance ---                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=9, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

# first convert all lines to a list of ints
for i, m in enumerate(myset):
    m = m.split()
    m = list([[int(x) for x in m]])
    while not all([x == 0 for x in m[-1]]):
        temp = []
        for x in range(1, len(m[-1])):
            temp.append(m[-1][x] - m[-1][x-1])
        m.append(temp)
    temp = 0

    for x in reversed(m):
        p1ans += x[-1]
        temp = x[0] - temp
    p2ans += temp
print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
