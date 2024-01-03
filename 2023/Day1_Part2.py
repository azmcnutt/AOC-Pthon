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
# --- Day 1: Trebuchet?!  ---                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
# myset = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".splitlines()

myset = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=1, year=2023).splitlines()

# remove line feeds from the list


def get_first_and_last_digit(mixed_string):
    index_first = (0, 0)
    index_last = (0, 0)
    num_replace = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
    }
    searches = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'zero',
    ]
    # print(mixed_string)
    for s in searches:
        regex_first = r'' + re.escape(s)
        regex_last = r'' + re.escape(s) + '(?!.*' + re.escape(s) + ')'

        # Look for the regex match starting at the beginning of string
        # If it finds a number earlier than the others, set it as start.
        # If it finds a number later than the others, set it as end.
        match = re.search(regex_first, mixed_string)
        if match:
            if match.start() <= index_first[0] or index_first == (0,0):
                index_first = (match.start(), match.end())
            if match.start() >= index_last[0] or index_last == (0, 0):
                index_last = (match.start(), match.end())
        match = re.search(regex_last, mixed_string)

        # Now for an edge case where my regex doesn't so what I want
        # see if there is a match starting at the end.
        if match:
            if match.start() >= index_last[0] or index_last == (0, 0):
                index_last = (match.start(), match.end())
    first = mixed_string[index_first[0]:index_first[1]]
    last = mixed_string[index_last[0]:index_last[1]]

    # Replace word numbers with digit strings
    if first in num_replace.keys():
        first = num_replace[first]
    if last in num_replace.keys():
        last = num_replace[last]

    # return the integer value with the first digit in the tens spot
    # and the last digit in the ones spot
    return int(first + last)

# get the time we start running our solution: even though I'm running in debug mode


start_time = time.time()
total = 0

for x in myset:
    total += get_first_and_last_digit(x)
print(f'P2: {total} in {time.time() - start_time} seconds.')
