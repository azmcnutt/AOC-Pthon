import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 6: Wait For It ---                                                                                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

# myset = get_data(day=6, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()

race = []
record = []
ways_to_win = []
for idx, row in enumerate(myset):
    x = row.split()
    if x[0] == 'Time:':
        for y in range(1, len(x)):
            race.append(int(x[y]))
    if x[0] == 'Distance:':
        for y in range(1, len(x)):
            record.append(int(x[y]))
# print(race)
# print(record)
p1ans = 1
for idx, r in enumerate(race):
    count = 0
    for x in range(1, r):
        # movement = x
        # number of moves = r - x
        print(f'Race {r} - Hold: {x} - Distance: {(r - x) * x}')
        if ((r - x) * x) > record[idx]:
            count += 1
    ways_to_win.append(count)
    p1ans *= count



p2ans = 0

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
