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
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island.   #
# This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang #
# glider behind.                                                                                                #
#                                                                                                               #
# You wander around for a while, but you don't find any people or animals. However, you do occasionally find    #
# signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at   #
# the hot springs and ask them where the desert-machine parts are made.                                         #
#                                                                                                               #
# The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal   #
# grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It       #
# didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.      #
#                                                                                                               #
# Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was #
# hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch #
# of all of the surface pipes you can see (your puzzle input).                                                  #
#                                                                                                               #
# The pipes are arranged in a two-dimensional grid of tiles:                                                    #
#                                                                                                               #
# | is a vertical pipe connecting north and south.                                                              #
# - is a horizontal pipe connecting east and west.                                                              #
# L is a 90-degree bend connecting north and east.                                                              #
# J is a 90-degree bend connecting north and west.                                                              #
# 7 is a 90-degree bend connecting south and west.                                                              #
# F is a 90-degree bend connecting south and east.                                                              #
# . is ground; there is no pipe in this tile.                                                                   #
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what     #
# shape the pipe has.                                                                                           #
# Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one   #
# large, continuous loop.                                                                                       #
#                                                                                                               #
# For example, here is a square loop of pipe:                                                                   #
#                                                                                                               #
# .....                                                                                                         #
# .F-7.                                                                                                         #
# .|.|.                                                                                                         #
# .L-J.                                                                                                         #
# .....                                                                                                         #
# If the animal had entered this loop in the northwest corner, the sketch would instead look like this:         #
#                                                                                                               #
# .....                                                                                                         #
# .S-7.                                                                                                         #
# .|.|.                                                                                                         #
# .L-J.                                                                                                         #
# .....                                                                                                         #
# In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes  #
# connect to it.                                                                                                #
#                                                                                                               #
# Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop   #
# as above:                                                                                                     #
#                                                                                                               #
# -L|F7                                                                                                         #
# 7S-7|                                                                                                         #
# L|7||                                                                                                         #
# -L-J|                                                                                                         #
# L|-JF                                                                                                         #
# In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to  #
# S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop         #
# connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is  #
# assumed to connect back to those two pipes).                                                                  #
#                                                                                                               #
# Here is a sketch that contains a slightly more complex main loop:                                             #
#                                                                                                               #
# ..F7.                                                                                                         #
# .FJ|.                                                                                                         #
# SJ.L7                                                                                                         #
# |F--J                                                                                                         #
# LJ...                                                                                                         #
# Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:                           #
#                                                                                                               #
# 7-F7-                                                                                                         #
# .FJ|7                                                                                                         #
# SJLL7                                                                                                         #
# |F--J                                                                                                         #
# LJ.LJ                                                                                                         #
# If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the    #
# starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct         #
# distance. Instead, you need to find the tile that would take the longest number of steps along the loop to    #
# reach from the starting point - regardless of which way around the loop the animal went.                      #
#                                                                                                               #
# In the first example with the square loop:                                                                    #
#                                                                                                               #
# .....                                                                                                         #
# .S-7.                                                                                                         #
# .|.|.                                                                                                         #
# .L-J.                                                                                                         #
# .....                                                                                                         #
# You can count the distance each tile in the loop is from the starting point like this:                        #
#                                                                                                               #
# .....                                                                                                         #
# .012.                                                                                                         #
# .1.3.                                                                                                         #
# .234.                                                                                                         #
# .....                                                                                                         #
# In this example, the farthest point from the start is 4 steps away.                                           #
#                                                                                                               #
# Here's the more complex loop again:                                                                           #
#                                                                                                               #
# ..F7.                                                                                                         #
# .FJ|.                                                                                                         #
# SJ.L7                                                                                                         #
# |F--J                                                                                                         #
# LJ...                                                                                                         #
# Here are the distances for each tile on that loop:                                                            #
#                                                                                                               #
# ..45.                                                                                                         #
# .236.                                                                                                         #
# 01.78                                                                                                         #
# 14567                                                                                                         #
# 23...                                                                                                         #
# Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting #
# position to the point farthest from the starting position?                                                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the  #
# area enclosed by the loop?                                                                                    #
#                                                                                                               #
# To determine whether it's even worth taking the time to search for such a nest, you should calculate how many #
# tiles are contained within the loop. For example:                                                             #
#                                                                                                               #
# ...........                                                                                                   #
# .S-------7.                                                                                                   #
# .|F-----7|.                                                                                                   #
# .||.....||.                                                                                                   #
# .||.....||.                                                                                                   #
# .|L-7.F-J|.                                                                                                   #
# .|..|.|..|.                                                                                                   #
# .L--J.L--J.                                                                                                   #
# ...........                                                                                                   #
# The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I       #
# below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those       #
# regions marked:                                                                                               #
#                                                                                                               #
# ...........                                                                                                   #
# .S-------7.                                                                                                   #
# .|F-----7|.                                                                                                   #
# .||OOOOO||.                                                                                                   #
# .||OOOOO||.                                                                                                   #
# .|L-7OF-J|.                                                                                                   #
# .|II|O|II|.                                                                                                   #
# .L--JOL--J.                                                                                                   #
# .....O.....                                                                                                   #
# In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop #
# - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:  #
#                                                                                                               #
# ..........                                                                                                    #
# .S------7.                                                                                                    #
# .|F----7|.                                                                                                    #
# .||OOOO||.                                                                                                    #
# .||OOOO||.                                                                                                    #
# .|L-7F-J|.                                                                                                    #
# .|II||II|.                                                                                                    #
# .L--JL--J.                                                                                                    #
# ..........                                                                                                    #
# In both of the above examples, 4 tiles are enclosed by the loop.                                              #
#                                                                                                               #
# Here's a larger example:                                                                                      #
#                                                                                                               #
# .F----7F7F7F7F-7....                                                                                          #
# .|F--7||||||||FJ....                                                                                          #
# .||.FJ||||||||L7....                                                                                          #
# FJL7L7LJLJ||LJ.L-7..                                                                                          #
# L--J.L7...LJS7F-7L7.                                                                                          #
# ....F-J..F7FJ|L7L7L7                                                                                          #
# ....L7.F7||L7|.L7L7|                                                                                          #
# .....|FJLJ|FJ|F7|.LJ                                                                                          #
# ....FJL-7.||.||||...                                                                                          #
# ....L---J.LJ.LJLJ...                                                                                          #
# The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are      #
# outside it (O):                                                                                               #
#                                                                                                               #
# OF----7F7F7F7F-7OOOO                                                                                          #
# O|F--7||||||||FJOOOO                                                                                          #
# O||OFJ||||||||L7OOOO                                                                                          #
# FJL7L7LJLJ||LJIL-7OO                                                                                          #
# L--JOL7IIILJS7F-7L7O                                                                                          #
# OOOOF-JIIF7FJ|L7L7L7                                                                                          #
# OOOOL7IF7||L7|IL7L7|                                                                                          #
# OOOOO|FJLJ|FJ|F7|OLJ                                                                                          #
# OOOOFJL-7O||O||||OOO                                                                                          #
# OOOOL---JOLJOLJLJOOO                                                                                          #
# In this larger example, 8 tiles are enclosed by the loop.                                                     #
#                                                                                                               #
# Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example     #
# with many bits of junk pipe lying around that aren't connected to the main loop at all:                       #
#                                                                                                               #
# FF7FSF7F7F7F7F7F---7                                                                                          #
# L|LJ||||||||||||F--J                                                                                          #
# FL-7LJLJ||||||LJL-77                                                                                          #
# F--JF--7||LJLJ7F7FJ-                                                                                          #
# L---JF-JLJ.||-FJLJJ7                                                                                          #
# |F|F-JF---7F7-L7L|7|                                                                                          #
# |FFJF7L7F-JF7|JL---7                                                                                          #
# 7-L-JL7||F7|L7F-7F7|                                                                                          #
# L.L7LFJ|||||FJL7||LJ                                                                                          #
# L7JLJL-JLJLJL--JLJ.L                                                                                          #
# Here are just the tiles that are enclosed by the loop marked with I:                                          #
#                                                                                                               #
# FF7FSF7F7F7F7F7F---7                                                                                          #
# L|LJ||||||||||||F--J                                                                                          #
# FL-7LJLJ||||||LJL-77                                                                                          #
# F--JF--7||LJLJIF7FJ-                                                                                          #
# L---JF-JLJIIIIFJLJJ7                                                                                          #
# |F|F-JF---7IIIL7L|7|                                                                                          #
# |FFJF7L7F-JF7IIL---7                                                                                          #
# 7-L-JL7||F7|L7F-7F7|                                                                                          #
# L.L7LFJ|||||FJL7||LJ                                                                                          #
# L7JLJL-JLJLJL--JLJ.L                                                                                          #
# In this last example, 10 tiles are enclosed by the loop.                                                      #
#                                                                                                               #
# Figure out whether you have time to search for the nest by calculating the area within the loop. How many     #
# tiles are enclosed by the loop?                                                                               #
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
