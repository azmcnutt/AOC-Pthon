import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc
import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 4: Scratchcards  ---                                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=4, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()

# Let's get the organized. Each record in the dict, will contain an index with the game ID and a list of lists wtih
# each draw with the digits representing the number of Red, Green, and Blue
games = {}
for x in myset:
    x = x.replace('Card ','')
    x = x.split(': ')
    c, w = x[1].strip().split(' | ')
    c = c.split()
    w = w.split()
    c = [int(i.strip()) for i in c]
    w = [int(i.strip()) for i in w]
    games[int(x[0])] = [c, w, 1, ]
p1ans = 0
for game_num, g in games.items():
    x = 0
    # get the number of matches (n), then double 1 n-1 times:
    n = set(g[0]) & set(g[1])
    if n:
        # lets make some copies for part 2
        for y in range(1, len(n) + 1):
            games[game_num + y][2] += g[2]
            # print(f'Game {game_num}: y = {y}')
        x = 1 * 2 ** (len(n) - 1)
        p1ans += x
    # print(f'Game {game_num} Matches: {set(g[0]) & set(g[1])} = score: {x}')

p2ans = 0
for t in games.items():
    p2ans += t[-1][-1]


print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
