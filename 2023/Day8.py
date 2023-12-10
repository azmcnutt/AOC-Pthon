import math
import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8: Haunted Wasteland ---                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn #
# to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts  #
# a few minutes ago.                                                                                            #
#                                                                                                               #
# One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about  #
# how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains  #
# a list of left/right instructions, and the rest of the documents seem to describe some kind of network of     #
# labeled nodes.                                                                                                #
#                                                                                                               #
# It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have    #
# the camel follow the same instructions, you can escape the haunted wasteland!                                 #
#                                                                                                               #
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, #
# and you have to follow the left/right instructions until you reach ZZZ.                                       #
#                                                                                                               #
# This format defines each node of the network individually. For example:                                       #
#                                                                                                               #
# RL                                                                                                            #
#                                                                                                               #
# AAA = (BBB, CCC)                                                                                              #
# BBB = (DDD, EEE)                                                                                              #
# CCC = (ZZZ, GGG)                                                                                              #
# DDD = (DDD, DDD)                                                                                              #
# EEE = (EEE, EEE)                                                                                              #
# GGG = (GGG, GGG)                                                                                              #
# ZZZ = (ZZZ, ZZZ)                                                                                              #
# Starting with AAA, you need to look up the next element based on the next left/right instruction in your      #
# input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L    #
# means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2    #
# steps.                                                                                                        #
#                                                                                                               #
# Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole     #
# sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a  #
# situation that takes 6 steps to reach ZZZ:                                                                    #
#                                                                                                               #
# LLR                                                                                                           #
#                                                                                                               #
# AAA = (BBB, BBB)                                                                                              #
# BBB = (AAA, ZZZ)                                                                                              #
# ZZZ = (ZZZ, ZZZ)                                                                                              #
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the   #
# instructions, but you've barely left your starting position. It's going to take significantly more steps to   #
# escape!                                                                                                       #
#                                                                                                               #
# What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of        #
# spacetime? Only one way to find out.                                                                          #
#                                                                                                               #
# After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with    #
# names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every #
# node that ends with A and follow all of the paths at the same time until they all simultaneously end up at    #
# nodes that end with Z.                                                                                        #
#                                                                                                               #
# For example:                                                                                                  #
#                                                                                                               #
# LR                                                                                                            #
#                                                                                                               #
# 11A = (11B, XXX)                                                                                              #
# 11B = (XXX, 11Z)                                                                                              #
# 11Z = (11B, XXX)                                                                                              #
# 22A = (22B, XXX)                                                                                              #
# 22B = (22C, 22C)                                                                                              #
# 22C = (22Z, 22Z)                                                                                              #
# 22Z = (22B, 22B)                                                                                              #
# XXX = (XXX, XXX)                                                                                              #
# Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right #
# instruction, use that instruction to simultaneously navigate away from both nodes you're currently on.        #
# Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're  #
# on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed   #
# as follows:                                                                                                   #
#                                                                                                               #
# Step 0: You are at 11A and 22A.                                                                               #
# Step 1: You choose all of the left paths, leading you to 11B and 22B.                                         #
# Step 2: You choose all of the right paths, leading you to 11Z and 22C.                                        #
# Step 3: You choose all of the left paths, leading you to 11B and 22Z.                                         #
# Step 4: You choose all of the right paths, leading you to 11Z and 22B.                                        #
# Step 5: You choose all of the left paths, leading you to 11B and 22C.                                         #
# Step 6: You choose all of the right paths, leading you to 11Z and 22Z.                                        #
# So, in this example, you end up entirely on nodes that end in Z after 6 steps.                                #
#                                                                                                               #
# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes  #
# that end with Z?                                                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

myset = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=8, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 1

map = {}
inst = myset[0]
for x in range(2, len(myset)):
    y = myset[x].split(' = ')
    y[1] = y[1].replace('(', '')
    y[1] = y[1].replace(')', '')
    y[1] = y[1].split(', ')
    map[y[0]] = y[1]
#pprint(map)
end = False
x = 0
count = 1
next_loc = 'AAA'
while not end:
    if inst[x] == 'L':
        next_loc = map[next_loc][0]
    elif inst[x] == 'R':
        next_loc = map[next_loc][1]
    else:
        # we should never get here
        print('error')
        sys.exit()
    if next_loc == 'ZZZ':
        end = True
        p1ans = count
    else:
        count += 1
        x += 1
        if x >= len(inst):
            x = 0
next_loc = []
for x in map.keys():
    if x[-1] == 'A':
        next_loc.append(x)
end = False
x = 0
count = 1
guess = []
for n in next_loc:
    start = n
    end = False
    x = 0
    count = 1
    while not end:
        if inst[x] == 'L':
            n = map[n][0]
        elif inst[x] == 'R':
            n = map[n][1]
        else:
            # we should never get here
            print('error')
            sys.exit()
        if n[-1] == 'Z':
            end = True
            guess.append(count)
        else:
            count += 1
            x += 1
            if x >= len(inst):
                x = 0
# https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
for i in guess:
    p2ans = p2ans*i//math.gcd(p2ans, i)

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
