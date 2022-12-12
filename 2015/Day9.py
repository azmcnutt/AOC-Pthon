import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
from functools import cache
from string import hexdigits
import time
import hashlib
import ctypes
import itertools
import re
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 9:  ---                                                                        #
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
myset = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=9, year=2015).splitlines()

cities = {}

starttime = time.time()
for x in myset:
    c1, c2, d = re.split(r' to | = ',x)
    if c1 in cities.keys():
        cities[c1][c2] = int(d)
    else:
        cities[c1] = {c2: int(d)}
    if c2 in cities.keys():
        cities[c2][c1] = int(d)
    else:
        cities[c2] = {c1: int(d)}
    

# pprint(cities)
p1ans = 0
p2ans = 0
for r in itertools.permutations(cities.keys(), len(cities)):
    trip = 0
    # print(r)
    for i in range(1,len(r)):
        #print(f'{r[i-1]} to {r[i]} = {cities[r[i-1]][r[i]]}')
        trip += cities[r[i-1]][r[i]]
    #print(f'Trip Total: {trip}')
    if trip < p1ans or p1ans == 0: p1ans = trip
    if trip > p2ans: p2ans = trip

print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
