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
# --- Day 7: Camel Cards ---                                                                                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

# myset = get_data(day=7, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

hands = []
five = []
four = []
full = []
three = []
two = []
one = []
high = []

for x in myset:
    x = x.split()
    c = x[0]
    # change the letter cards (T, J, Q, K ,A) to hex charachters (A, B, C, D, E)
    c = c.replace('A', 'E')
    c = c.replace('K', 'D')
    c = c.replace('Q', 'C')
    c = c.replace('J', 'B')
    c = c.replace('T', 'A')
    count = {}
    for y in x[0]:
        if y in count:
            count[y] += 1
        else:
            count[y] = 1
    count = sorted(count.values(), reverse=True)
    if count[0] == 5:
        c = '6' + c
    elif count[0] == 4:
        c = '5' + c
    elif count[0] == 3 and count[1] == 2:
        c = '4' + c
    elif count[0] == 3:
        c = '3' + c
    elif count[0] == 2 and count[1] == 2:
        c = '2' + c
    elif count[0] == 2:
        c = '1' + c
    else:
        c = '0' + c
    x.append(c)
    hands.append(x)
# print(hands)
# print()
hands.sort(key=lambda y: y[2], reverse=False)
pprint(hands)
for idx, h in enumerate(hands):
    p1ans += (idx + 1) * int(h[1])
print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
