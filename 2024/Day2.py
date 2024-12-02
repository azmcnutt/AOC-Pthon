# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

# # # # # # # # # # # # # # # # # # #
# --- Day 2: Red-Nosed Reports  --- #
# # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.
# Each list item is one line of input
aoc_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()


# once the test data provides the right answer:
# replace test data with data from the puzzle input
# aoc_input = get_data(day=2, year=2024).splitlines()

# Get the time to see how fast the solution runs.
# I get the time after the input has been downloaded to test
# the speed of my program, not the speed of my Internet connection.
start_time = time.time()

p1 = 0
p2 = 0

for report in aoc_input:
    safe_report = True
    report = report.split()
    report = [int(item) for item in report]
    # first lets determine if we are increasing or degreasing
    if report[1] > report[0]:
        direction = -1
    else:
        direction = 1
    for x in range(len(report) - 1):
        if (report[x] != (report[x+1] + (1 * direction))
            and report[x] != (report[x+1] + (2 * direction))
            and report[x] != (report[x+1] + (3 * direction))
        ):
            safe_report = False
    if safe_report:
        p1 += 1

print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
