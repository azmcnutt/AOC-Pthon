import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
import hashlib

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """abcdef
pqrstuv""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=4, year=2015).splitlines()

starttime = time.time()
for x in myset:
    y = 0
    while True:
        result = hashlib.md5((x + str(y)).encode()).hexdigest()
        if result[:6] == '000000':
            print(f'Part 1 Answer is {y}    {time.time() - starttime}')
            break
        y += 1


#print(f'Part 1 Answer is {total}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)

#print(f'Part 2 Answer is {total}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
