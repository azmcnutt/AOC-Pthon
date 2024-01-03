import math
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
# --- Day 8: Haunted Wasteland ---                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

myset = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=8, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 1

map = {}
inst = myset[0]
for x in range(2, len(myset)):
    y = myset[x].split(' = ')
    y[1] = y[1].replace('(', '')
    y[1] = y[1].replace(')', '')
    y[1] = y[1].split(', ')
    map[y[0]] = y[1]
#pprint(map)
end = False
x = 0
count = 1
next_loc = 'AAA'
while not end:
    if inst[x] == 'L':
        next_loc = map[next_loc][0]
    elif inst[x] == 'R':
        next_loc = map[next_loc][1]
    else:
        # we should never get here
        print('error')
        sys.exit()
    if next_loc == 'ZZZ':
        end = True
        p1ans = count
    else:
        count += 1
        x += 1
        if x >= len(inst):
            x = 0
next_loc = []
for x in map.keys():
    if x[-1] == 'A':
        next_loc.append(x)
end = False
x = 0
count = 1
guess = []
for n in next_loc:
    start = n
    end = False
    x = 0
    count = 1
    while not end:
        if inst[x] == 'L':
            n = map[n][0]
        elif inst[x] == 'R':
            n = map[n][1]
        else:
            # we should never get here
            print('error')
            sys.exit()
        if n[-1] == 'Z':
            end = True
            guess.append(count)
        else:
            count += 1
            x += 1
            if x >= len(inst):
                x = 0
# https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
for i in guess:
    p2ans = p2ans*i//math.gcd(p2ans, i)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
