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

# Split the input into a left and right list.
# left_list and right_list are used to keep it consistent with the 
# AOC problem.
for x in aoc_input:
    l,r = x.split()
    left_list.append(int(l))
    right_list.append(int(r))

# Because of how I solve for part one, it is easier to do part two first
# Iterate through left_list and count the number of times the number
# and count the number of times the number (x) appears in right_list.
# The multiply the left_list number by the number of times it appears in
# right_list.  Add the product to p2.
for x in left_list:
    p2 += (x * right_list.count(x))

# Now solve for part one.  Find the smallest number in left_ and right_list
# and get the difference between them.  Add to p1 and then remove those
# two numbers from the list.
while left_list and right_list:
    min_left = min(left_list)
    min_right = min(right_list)
    left_list.remove(min_left)
    right_list.remove(min_right)
    p1 += abs(min_left - min_right)

print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
