import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 5:  ---                                                                        #
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
myset = """12
14
1969
100756""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=1, year=2019).splitlines()

# remove line feeds from the list



#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()
total = 0
for x in myset:
    f = trunc(int(x) / 3) - 2
    total += f
print(f'P1: {total}')
total = 0
for x in myset:
    f = trunc(int(x) / 3) - 2
    
    while f > 0:
        total += f
        f = trunc(int(f) / 3) - 2
print(f'P2: {total}')