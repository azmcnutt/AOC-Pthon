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
# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in #
# the closest gondola, finally ready to ascend to the water source.                                             #
#                                                                                                               #
# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a  #
# phone labeled "help", so you pick it up and the engineer answers.                                             #
#                                                                                                               #
# Before you can explain the situation, she suggests that you look out the window. There stands the engineer,   #
# holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the  #
# station. You exit the gondola.                                                                                #
#                                                                                                               #
# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that #
# is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers        #
# together.                                                                                                     #
#                                                                                                               #
# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure  #
# out which gear needs to be replaced.                                                                          #
#                                                                                                               #
# Consider the same engine schematic again:                                                                     #
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
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its  #
# gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617  #
# is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces      #
# 467835.                                                                                                       #
#                                                                                                               #
# What is the sum of all of the gear ratios in your engine schematic?                                           #
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

myset = get_data(day=3, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
discovered = []
partnumbers = []
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
            test_numbers.add(int(number))

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
            pn_found = False
            # check before:
            if idx_y > 0:
                before = myset[idx_x][idx_y - 1]
                if before != '.':
                    pn_found = True
                    partnumbers.append([int(number), idx_x, idx_y, z - 1,])
                    # partnumbers[int(number)] = [idx_x, idx_y, z - 1]
            # Check after:
            if z < len(row):
                after = myset[idx_x][z]
                if after != '.' and not pn_found:
                    pn_found = True
                    partnumbers.append([int(number), idx_x, idx_y, z - 1,])
                    # partnumbers[int(number)] = [idx_x, idx_y, z - 1]
            # check row above
            # set start and end points for row above and below
            if idx_y > 0:
                s = idx_y - 1
            else:
                s = idx_y
            if z < len(row):
                e = z
            else:
                e = z - 1
            if idx_x > 0:
                above = myset[idx_x - 1][s:e + 1]
                above = above.replace('.','')
                if above and not pn_found:
                    pn_found = True
                    partnumbers.append([int(number), idx_x, idx_y, z - 1,])
                    # partnumbers[int(number)] = [idx_x, idx_y, z - 1]
            if idx_x < len(myset) - 1:
                below = myset[idx_x + 1][s:e + 1]
                below = below.replace('.','')
                if below and not pn_found:
                    pn_found = True
                    partnumbers.append([int(number), idx_x, idx_y, z - 1,])
                    # partnumbers[int(number)] = [idx_x, idx_y, z - 1]
# Now for part 2 (very brute force)
# check for a '*' in the grid, and then see if there are exactly two part numbers next to it.
gear_ratios = []
for idx_x, row in enumerate(myset):
    for idx_y, x in enumerate(row):
        if x == '*':
            # found a gear, not check around for two part numbers
            # make a list of the coordinates around the gear
            pn_found = set()
            search = list()
            search.append([idx_x - 1, idx_y - 1])
            search.append([idx_x - 1, idx_y])
            search.append([idx_x - 1, idx_y + 1])
            search.append([idx_x, idx_y - 1])
            search.append([idx_x, idx_y + 1])
            search.append([idx_x + 1, idx_y + 1])
            search.append([idx_x + 1, idx_y])
            search.append([idx_x + 1, idx_y - 1])

            for s in search:
                for p in partnumbers:
                    if p[1] == s[0] and p[2] <= s[1] <= p[3]:
                        pn_found.add(p[0])
            if len(pn_found) == 2:
                print(pn_found)
                gr = 1
                for p in pn_found:
                    gr *= p
                gear_ratios.append(gr)



# print(discovered)
# print(partnumbers)
# print(test_numbers)
#pprint(partnumbers)

p1 = 0
for p in partnumbers:
    p1 += p[0]
p2 = 0
for g in gear_ratios:
    p2 += g


print(f'P1: {p1} and P2: {p2} in {time.time() - start_time} seconds.')
