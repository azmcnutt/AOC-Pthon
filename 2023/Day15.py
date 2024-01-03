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
# --- Day 16: The Floor Will Be Lava ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=16, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

max_x = len(myset) - 1
max_y = len(myset[0]) - 1
dirs = {
    'e': {'x': 0, 'y': 1},
    'w': {'x': 0, 'y': -1},
    'n': {'x': -1, 'y': 0},
    's': {'x': 1, 'y': 0},
}
energized = set()
loops = set()


def beam(x=0, y=0, d='e'):
    while True:
        if x > max_x or y > max_y or x < 0 or y < 0:
            return
        if (x, y, d) in loops:
            # print('loop detected')
            return
        energized.add((x, y))
        loops.add((x, y, d))
        # print(x,y,d)
        if myset[x][y] == '/':
            if d == 'n':
                d = 'e'
            elif d == 's':
                d = 'w'
            elif d == 'e':
                d = 'n'
            elif d == 'w':
                d = 's'
        elif myset[x][y] == '\\':
            if d == 'n':
                d = 'w'
            elif d == 's':
                d = 'e'
            elif d == 'e':
                d = 's'
            elif d == 'w':
                d = 'n'
        elif myset[x][y] == '-' and d in ['n', 's']:
            if max_y > y > 0: # split the beam
                # print('split')
                beam(x, y + 1, 'e')
                # print('back')
                d = 'w'
            elif y == 0: # turn to e because we are on the w edge
                d = 'e'
            elif y >= max_y: # turn to w because we are on the e edge
                d = 'w'
            else:
                print(f'- split error at: {x},{y} going {d}')
        elif myset[x][y] == '|' and d in ['e', 'w']:
            if max_x > x > 0: # split the beam
                # print('split')
                beam(x + 1, y, 's')
                # print('back')
                d = 'n'
            elif x == 0: # turn to s because we are on the n edge
                d = 's'
            elif x >= max_y: # turn to n because we are on the s edge
                d = 'n'
            else:
                print(f'| split error at: {x},{y} going {d}')
        x += dirs[d]['x']
        y += dirs[d]['y']


    return


beam()
p1ans = len(energized)

# part 2, lets brute force this thing:
# lets process the top row
for i in range(0, len(myset[0])):
    energized = set()
    loops = set()
    beam(0, i, 's')
    if len(energized) > p2ans:
        p2ans = len(energized)

# bottom row
for i in range(0, len(myset[0])):
    energized = set()
    loops = set()
    beam(max_x, i, 'n')
    if len(energized) > p2ans:
        p2ans = len(energized)

# left row
for i in range(0, len(myset)):
    energized = set()
    loops = set()
    beam(i, 0, 'e')
    if len(energized) > p2ans:
        p2ans = len(energized)

# right row
for i in range(0, len(myset)):
    energized = set()
    loops = set()
    beam(i, max_y, 'w')
    if len(energized) > p2ans:
        p2ans = len(energized)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
