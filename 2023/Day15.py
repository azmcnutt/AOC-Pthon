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
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava        #
# Production Facility. At some point, you realize that the steel facility walls have been replaced with cave,   #
# and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant   #
# cave.                                                                                                         #
#                                                                                                               #
# Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. #
# There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest  #
# to the facility and pouring all of its energy into a contraption on the opposite side.                        #
#                                                                                                               #
# Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty    #
# space (.), mirrors (/ and \), and splitters (| and -).                                                        #
#                                                                                                               #
# The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid        #
# converts some of the beam's light into heat to melt the rock in the cavern.                                   #
#                                                                                                               #
# You note the layout of the contraption (your puzzle input). For example:                                      #
#                                                                                                               #
# .|...\....                                                                                                    #
# |.-.\.....                                                                                                    #
# .....|-...                                                                                                    #
# ........|.                                                                                                    #
# ..........                                                                                                    #
# .........\                                                                                                    #
# ..../.\\..                                                                                                    #
# .-.-/..|..                                                                                                    #
# .|....-|.\                                                                                                    #
# ..//.|....                                                                                                    #
# The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on  #
# what it encounters as it moves:                                                                               #
#                                                                                                               #
# If the beam encounters empty space (.), it continues in the same direction.                                   #
# If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the      #
# mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the         #
# mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the    #
# mirror's column.                                                                                              #
# If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the  #
# splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue  #
# in the same direction.                                                                                        #
# If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each   #
# of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that     #
# encounters a | splitter would split into two beams: one that continues upward from the splitter's column and  #
# one that continues downward from the splitter's column.                                                       #
# Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A     #
# tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.          #
#                                                                                                               #
# In the above example, here is how the beam of light bounces around the contraption:                           #
#                                                                                                               #
# >|<<<\....                                                                                                    #
# |v-.\^....                                                                                                    #
# .v...|->>>                                                                                                    #
# .v...v^.|.                                                                                                    #
# .v...v^...                                                                                                    #
# .v...v^..\                                                                                                    #
# .v../2\\..                                                                                                    #
# <->-/vv|..                                                                                                    #
# .|<<<2-|.\                                                                                                    #
# .v//.|.v..                                                                                                    #
# Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams     #
# moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram   #
# but instead only showing whether a tile is energized (#) or not (.):                                          #
#                                                                                                               #
# ######....                                                                                                    #
# .#...#....                                                                                                    #
# .#...#####                                                                                                    #
# .#...##...                                                                                                    #
# .#...##...                                                                                                    #
# .#...##...                                                                                                    #
# .#..####..                                                                                                    #
# ########..                                                                                                    #
# .#######..                                                                                                    #
# .#...#.#..                                                                                                    #
# Ultimately, in this example, 46 tiles become energized.                                                       #
#                                                                                                               #
# The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by       #
# analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up  #
# being energized?                                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control #
# panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge    #
# tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a #
# corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or      #
# upward.)                                                                                                      #
#                                                                                                               #
# So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading   #
# upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). #
# To produce lava, you need to find the configuration that energizes as many tiles as possible.                 #
#                                                                                                               #
# In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top   #
# row:                                                                                                          #
#                                                                                                               #
# .|<2<\....                                                                                                    #
# |v-v\^....                                                                                                    #
# .v.v.|->>>                                                                                                    #
# .v.v.v^.|.                                                                                                    #
# .v.v.v^...                                                                                                    #
# .v.v.v^..\                                                                                                    #
# .v.v/2\\..                                                                                                    #
# <-2-/vv|..                                                                                                    #
# .|<<<2-|.\                                                                                                    #
# .v//.|.v..                                                                                                    #
# Using this configuration, 51 tiles are energized:                                                             #
#                                                                                                               #
# .#####....                                                                                                    #
# .#.#.#....                                                                                                    #
# .#.#.#####                                                                                                    #
# .#.#.##...                                                                                                    #
# .#.#.##...                                                                                                    #
# .#.#.##...                                                                                                    #
# .#.#####..                                                                                                    #
# ########..                                                                                                    #
# .#######..                                                                                                    #
# .#...#.#..                                                                                                    #
# Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized  #
# in that configuration?                                                                                        #
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
