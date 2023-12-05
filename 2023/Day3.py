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
# --- Day 3: Gear Ratios  ---                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the     #
# water source, but this is as far as he can bring you. You go inside.                                          #
#                                                                                                               #
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.               #
#                                                                                                               #
# "Aaah!"                                                                                                       #
#                                                                                                               #
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting #
# anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to   #
# help.                                                                                                         #
#                                                                                                               #
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out      #
# which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out      #
# which part is missing.                                                                                        #
#                                                                                                               #
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of #
# numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even         #
# diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)    #
#                                                                                                               #
# Here is an example engine schematic:                                                                          #
#                                                                                                               #
# 467..114..                                                                                                    #
# ...*......                                                                                                    #
# ..35..633.                                                                                                    #
# ......#...                                                                                                    #
# 617*......                                                                                                    #
# .....+.58.                                                                                                    #
# ..592.....                                                                                                    #
# ......755.                                                                                                    #
# ...$.*....                                                                                                    #
# .664.598..                                                                                                    #
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top       #
# right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum   #
# is 4361.                                                                                                      #
#                                                                                                               #
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the      #
# engine schematic?                                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

# myset = get_data(day=3, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
discovered = []
partnumbers = set()
test_numbers = set()
pn_totals = 0
for idx_x, row in enumerate(myset):
    for idx_y, x in enumerate(row):
        if x.isnumeric() and [idx_x,idx_y] not in discovered:
            # We have a number, lets get the entire number
            number = x
            discovered.append([idx_x, idx_y])
            z = idx_y + 1
            while row[z].isnumeric() and z < len(row):
                number += row[z]
                discovered.append([idx_x, z])
                z += 1
                if z == 10:
                    print('********************************************;')
                if z >= len(row):
                    break
            print(f'Start: ({idx_x}, {idx_y})')
            print(f'End: ({idx_x}, {z - 1})')
            print(f'Number: {number}')
            # min_x = idx_x - 1 if idx_x > 0 else 0
            # max_x = idx_x + 1 if idx_x < len(myset) - 1 else len(myset) - 1
            # min_y = idx_y - 1 if idx_y > 0 else 0
            # max_y = z if z < len(row) - 1 else len(row) - 1
            # print(f'Min({min_x}, {min_y}) Max:({max_x}, {max_y})')
            # for a in range(min_x, max_x + 1):
            #     for b in range(min_y, max_y + 1):
            #         if myset[a][b] != '.':
            #             print(number)
            #             partnumbers.add(int(number))

print(discovered)
print(partnumbers)


print(f'P1: {sum(partnumbers)} and P2:  in {time.time() - start_time} seconds.')
