import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
import hashlib

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
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
myset = """turn on 0,0 through 0,0
toggle 0,0 through 9,9
turn off 4,4 through 5,5""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=6, year=2015).splitlines()

starttime = time.time()
lights_on = set()
brightness = {}
for a in myset:
    if a[:7] == 'turn on':
        f, t = a[8:].split(' through ')
        fx, fy = [int(x) for x in f.split(',')]
        tx, ty = [int(x) for x in t.split(',')]
        for x in range(fx,tx+1):
            for y in range(fy,ty+1):
                lights_on.add((x,y))
                if str(x)+','+str(y) in brightness.keys():
                    brightness[str(x)+','+str(y)] += 1
                else:
                    brightness[str(x)+','+str(y)] = 1
    elif a[:6] == 'toggle':
        f, t = a[7:].split(' through ')
        fx, fy = [int(x) for x in f.split(',')]
        tx, ty = [int(x) for x in t.split(',')]
        
        for x in range(fx,tx+1):
            for y in range(fy,ty+1):
                if str(x)+','+str(y) in brightness.keys():
                    brightness[str(x)+','+str(y)] += 2
                else:
                    brightness[str(x)+','+str(y)] = 2
                if (x,y) in lights_on:
                    lights_on.remove((x,y))
                else:
                    lights_on.add((x,y))
    elif a[:8] == 'turn off':
        f, t = a[9:].split(' through ')
        fx, fy = [int(x) for x in f.split(',')]
        tx, ty = [int(x) for x in t.split(',')]
        for x in range(fx,tx+1):
            for y in range(fy,ty+1):
                if str(x)+','+str(y) in brightness.keys():
                    if brightness[str(x)+','+str(y)] >= 1:
                        brightness[str(x)+','+str(y)] -= 1
                if (x,y) in lights_on:
                    lights_on.remove((x,y))
p2count = 0
for i in brightness.values():
    p2count += i

print(f'Part 1 Answer is {len(lights_on)}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {p2count}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
