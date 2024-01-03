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
# --- Day 10: Pipe Maze ---                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=10, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

dirs = {
    'n': [-1, 0],
    's': [1, 0],
    'w': [0, -1],
    'e': [0, 1],
}

trav = {
    '|': {'n': 'n', 's': 's',},
    '-': {'w': 'w', 'e': 'e',},
    'J': {'s': 'w', 'e': 'n',},
    'L': {'s': 'e', 'w': 'n',},
    '7': {'n': 'w', 'e': 's',},
    'F': {'n': 'e', 'w': 's',},
}

steps = 0

max_x = len(myset) - 1
max_y = len(myset[0]) - 1

visited = []
s = []  # Start
cur_loc = []

cur_dir = ''
# find the start
for x, m in enumerate(myset):
    for y, z in enumerate(m):
        if z == 'S':
            s = [x, y]
# print(s)

# find the first exit point from start
# if start x is not 0, then look north
if s[0] != 0:
    x = s[0] + dirs['n'][0]
    y = s[1] + dirs['n'][1]
    a = myset[x][y]
    if a in trav.keys():
        if 'n' in trav[a].keys():
            cur_dir = 'n'

# if we don't have a cur dir, check south
if s[0] < max_x and not cur_dir:
    x = s[0] + dirs['s'][0]
    y = s[1] + dirs['s'][1]
    a = myset[x][y]
    if a in trav.keys():
        if 's' in trav[a].keys():
            cur_dir = 's'

# if we don't have a cur dir, check west
if s[1] != 0 and not cur_dir:
    x = s[0] + dirs['w'][0]
    y = s[1] + dirs['w'][1]
    a = myset[x][y]
    if a in trav.keys():
        if 'w' in trav[a].keys():
            cur_dir = 'w'

# if we don't have a cur dir, check east
if s[1] < max_y and not cur_dir:
    x = s[0] + dirs['e'][0]
    y = s[1] + dirs['e'][1]
    a = myset[x][y]
    if a in trav.keys():
        if 'e' in trav[a].keys():
            cur_dir = 'e'
loop_complete = False
cur_loc = s
while not loop_complete:
    visited.append((cur_loc[0], cur_loc[1]))
    next_loc = [cur_loc[0] + dirs[cur_dir][0], cur_loc[1] + dirs[cur_dir][1]]
    if myset[next_loc[0]][next_loc[1]] == 'S':
        loop_complete = True
        steps += 1
    else:
        # print(cur_loc, cur_dir, next_loc)
        cur_loc = copy.deepcopy(next_loc)
        cur_dir = trav[myset[next_loc[0]][next_loc[1]]][cur_dir]
        steps += 1
p1ans = int(steps / 2)

# https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/kcso138/?utm_source=share&utm_medium=web2x&context=3

for i in range(len(visited)):
    n_1 = visited[i]
    n_2 = visited[(i+1)%len(visited)]
    x_1, y_1 = n_1
    x_2, y_2 = n_2
    p2ans += x_1 * y_2 - y_1 * x_2

p2ans = abs(p2ans/2)

p2ans = int(p2ans-len(visited)/2+1)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
