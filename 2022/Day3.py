import os
import sys
import copy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 3: Rucksack Reorganization ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=3, year=2022).splitlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
# pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()

pri={
    'a': 1, 'b': 2,  'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30,
    'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'Y': 47, 'V': 48, 'W': 49, 'X': 50,
    'Y': 51, 'Z': 52,
}

pri_total=0

for rucksack in myset:
    comp1 = rucksack[:int(len(rucksack)/2)]
    comp2 = rucksack[int(len(rucksack)/2):]
    for x in comp1:
        if x in comp2:
            pri_total += pri[x]
            break
print(f'Part 1: Sum of priorities: {pri_total}.  {time.time() - startime}')

startime = time.time()
pri_total = 0
for i in range(0, len(myset), 3) :
    for x in myset[i]:
        if x in myset[i+1] and x in myset[i+2]:
            pri_total += pri[x]
            break
print(f'Part 2: Sum of priorities: {pri_total}.  {time.time() - startime}')