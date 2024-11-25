# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

# # # # # # # # # # # # # # # #
# --- Day 1: TBD  ---         #
# # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.
# Each list item is one line of input
aoc_input = """Sample
Data""".splitlines()


# once the test data provides the right answer:
# replace test data with data from the puzzle input
# aoc_input = get_data(day=1, year=2024).splitlines()

# Get the time to see how fast the solution runs.
# I get the time after the input has been downloaded to test
# the speed of my program, not the speed of my Internet connection.
star_time = time.time()

p1=0


print(f'P1: {p1} in {time.time() - star_time} seconds.')
