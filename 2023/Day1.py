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
myset = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()


# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=1, year=2023).splitlines()

# remove line feeds from the list


def get_first_and_last_digit(mixed_string):
    numbers = re.findall(r'\d',mixed_string)
    print(int(numbers[0] + numbers[-1]), numbers, mixed_string)
    return(int(numbers[0] + numbers[-1]))




#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)

# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()
total = 0
for x in myset:
    total += get_first_and_last_digit(x)
    print(get_first_and_last_digit(x))

print(f'P1: {total} in {time.time() - startime} seconds.')
