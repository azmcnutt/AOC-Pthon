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
# --- Day 11: Cosmic Expansion ---                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within      #
# turns out to be a researcher studying cosmic expansion using the giant telescope here.                        #
#                                                                                                               #
# He doesn't know anything about the missing machine parts; he's only visiting for this research project.       #
# However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take    #
# you straight there once he's done with today's observation analysis.                                          #
#                                                                                                               #
# Maybe you can help him with the analysis to speed things up?                                                  #
#                                                                                                               #
# The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle     #
# input). The image includes empty space (.) and galaxies (#). For example:                                     #
#                                                                                                               #
# ...#......                                                                                                    #
# .......#..                                                                                                    #
# #.........                                                                                                    #
# ..........                                                                                                    #
# ......#...                                                                                                    #
# .#........                                                                                                    #
# .........#                                                                                                    #
# ..........                                                                                                    #
# .......#..                                                                                                    #
# #...#.....                                                                                                    #
# The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of      #
# galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies   #
# to reach the observatory.                                                                                     #
#                                                                                                               #
# Due to something involving gravitational effects, only some space expands. In fact, the result is that any    #
# rows or columns that contain no galaxies should all actually be twice as big.                                 #
#                                                                                                               #
# In the above example, three columns and two rows contain no galaxies:                                         #
#                                                                                                               #
#    v  v  v                                                                                                    #
#  ...#......                                                                                                   #
#  .......#..                                                                                                   #
#  #.........                                                                                                   #
# >..........<                                                                                                  #
#  ......#...                                                                                                   #
#  .#........                                                                                                   #
#  .........#                                                                                                   #
# >..........<                                                                                                  #
#  .......#..                                                                                                   #
#  #...#.....                                                                                                   #
#    ^  ^  ^                                                                                                    #
# These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:     #
#                                                                                                               #
# ....#........                                                                                                 #
# .........#...                                                                                                 #
# #............                                                                                                 #
# .............                                                                                                 #
# .............                                                                                                 #
# ........#....                                                                                                 #
# .#...........                                                                                                 #
# ............#                                                                                                 #
# .............                                                                                                 #
# .............                                                                                                 #
# .........#...                                                                                                 #
# #....#.......                                                                                                 #
# Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can   #
# help to assign every galaxy a unique number:                                                                  #
#                                                                                                               #
# ....1........                                                                                                 #
# .........2...                                                                                                 #
# 3............                                                                                                 #
# .............                                                                                                 #
# .............                                                                                                 #
# ........4....                                                                                                 #
# .5...........                                                                                                 #
# ............6                                                                                                 #
# .............                                                                                                 #
# .............                                                                                                 #
# .........7...                                                                                                 #
# 8....9.......                                                                                                 #
# In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For #
# each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or      #
# right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through        #
# another galaxy.)                                                                                              #
#                                                                                                               #
# For example, here is one of the shortest paths between galaxies 5 and 9:                                      #
#                                                                                                               #
# ....1........                                                                                                 #
# .........2...                                                                                                 #
# 3............                                                                                                 #
# .............                                                                                                 #
# .............                                                                                                 #
# ........4....                                                                                                 #
# .5...........                                                                                                 #
# .##.........6                                                                                                 #
# ..##.........                                                                                                 #
# ...##........                                                                                                 #
# ....##...7...                                                                                                 #
# 8....9.......                                                                                                 #
# This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight   #
# locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:    #
#                                                                                                               #
# Between galaxy 1 and galaxy 7: 15                                                                             #
# Between galaxy 3 and galaxy 6: 17                                                                             #
# Between galaxy 8 and galaxy 9: 5                                                                              #
# In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies  #
# is 374.                                                                                                       #
#                                                                                                               #
# Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the    #
# sum of these lengths?                                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The galaxies are much older (and thus much farther apart) than the researcher initially estimated.            #
#                                                                                                               #
# Now, instead of the expansion you did before, make each empty row or column one million times larger. That    #
# is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with  #
# 1000000 empty columns.                                                                                        #
#                                                                                                               #
# (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths #
# between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the   #
# sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to   #
# expand far beyond these values.)                                                                              #
#                                                                                                               #
# Starting with the same initial image, expand the universe according to these new rules, then find the length  #
# of the shortest path between every pair of galaxies. What is the sum of these lengths?                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=11, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

all_x = set()
all_y = set()
max_x = len(myset) - 1
max_y = len(myset[0]) - 1
galaxies = []

for x, r in enumerate(myset):
    for y, z in enumerate(r):
        if z == '#':
            all_x.add(x)
            all_y.add(y)
            galaxies.append((x, y))

# print(all_x, all_y)
# print(galaxies)
# print(max_x, max_y)


def distance(point1, point2, expansion=1):
    x1, y1 = point1
    x2, y2 = point2
    d = abs(x1 - x2) + abs(y1 - y2)
    if x1 > x2:
        x2, x1 = x1, x2
    if y1 > y2:
        y2, y1 = y1, y2

    for z in range(x1, x2 + 1):
        if z not in all_x:
            d += expansion
    for z in range(y1, y2 + 1):
        if z not in all_y:
            d += expansion
    return d


# Part 1
for i1, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies):
        if i1 < i2:
            p1ans += distance(g1, g2)

# Part 2
for i1, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies):
        if i1 < i2:
            p2ans += distance(g1, g2, 999999)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
