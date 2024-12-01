# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # #
# --- Day 1: Historian Hysteria  ---  #
# # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.
# Each list item is one line of input
aoc_input = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()


# once the test data provides the right answer:
# replace test data with data from the puzzle input
aoc_input = get_data(day=1, year=2024).splitlines()

# Get the time to see how fast the solution runs.
# I get the time after the input has been downloaded to test
# the speed of my program, not the speed of my Internet connection.
start_time = time.time()

p1 = 0
p2 = 0

left_list = []
right_list = []

for x in aoc_input:
    l,r = x.split()
    left_list.append(int(l))
    right_list.append(int(r))

for x in left_list:
    p2 += (x * right_list.count(x))

while left_list and right_list:
    min_left = min(left_list)
    min_right = min(right_list)
    left_list.remove(min_left)
    right_list.remove(min_right)
    p1 += abs(min_left - min_right)

print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
