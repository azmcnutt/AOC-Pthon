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

myset = get_data(day=6, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()

race = 0
record = 0
first_winner = 0
last_winner = 0
for idx, row in enumerate(myset):
    x = row.split(':')
    if x[0] == 'Time':
        race = int(x[1].replace(' ', ''))
    if x[0] == 'Distance':
        record = int(x[1].replace(' ', ''))
# print(race)
# print(record)
p1ans = 0
# find the first winner
x = 0
while not first_winner:
    # movement = x
    # number of moves = race - x
    # print(f'Race {race} - Hold: {x} - Distance: {(race - x) * x}')
    if ((race - x) * x) > record:
        first_winner = x
    x += 1

# find the last winner
x = race
while not last_winner:
    # movement = x
    # number of moves = race - x
    # print(f'Race {race} - Hold: {x} - Distance: {(race - x) * x}')
    if ((race - x) * x) > record:
        last_winner = x
    x -= 1
p2ans = last_winner - first_winner + 1
#
#
#

print(f'P2: {p2ans} in {time.time() - start_time} seconds.')
