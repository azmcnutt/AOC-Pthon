import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 3: Rucksack Reorganization ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=4, year=2022).splitlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
# pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()
count = 0
for x in range(0,len(myset)):
    y,z, = myset[x].split(',')
    #a, b = tuple(int(x) for x in '1 2'.split())
    y1,y2 = tuple(int(a) for a in y.split('-'))
    z1,z2 = tuple(int(a) for a in z.split('-'))
    if (y1 in range(z1,z2+1) and y2 in range(z1,z2+1)) or (z1 in range(y1,y2+1) and z2 in range(y1,y2+1)):
        count += 1
print(f'Part 1: The number of inclusive zones is {count}.    {time.time() - startime}')
#submit(count, part='a', day = 4, year=2022)

# part 2
startime = time.time()
count = 0
for x in range(0,len(myset)):
    y,z, = myset[x].split(',')
    #a, b = tuple(int(x) for x in '1 2'.split())
    y1,y2 = tuple(int(a) for a in y.split('-'))
    z1,z2 = tuple(int(a) for a in z.split('-'))
    if y1 in range(z1,z2+1) or y2 in range(z1,z2+1) or z1 in range(y1,y2+1) or z2 in range(y1,y2+1):
        count += 1
print(f'Part 2: The number of overlapping zones is {count}.    {time.time() - startime}')
submit(count, part='b', day = 4, year=2022)