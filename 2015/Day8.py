import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
from functools import cache
import time
import hashlib
import ctypes

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
myset = """\"\"
\"abc\"
\"aaa\\\"aaa\"
\"\\x27\"""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=8, year=2015).splitlines()

starttime = time.time()
len_code = 0
len_char = 0

for x in myset:
    len_code += len(x)
    if x[0] == '"':
        x= x[1:]
    if x[-1] == '"':
        x = x[:-1]
    madeChanges = True
    while madeChanges:
        madeChanges = False
        for y in range(0,len(x)):
            if x[y] == '\\' and x[y+1] == 'x' and x[y+2:y+4].isnumeric():
                x = x[:y] + 'x' + x[y+5:]
                madeChanges = True
                break
            elif x[y] == '\\':
                x = x[:y] + x[y+1:]
                madeChanges = True
                break          
    len_char += len(x) 
    
#print(f'{len_code - len_char}')
print(f'Part 1 Answer is {len_code - len_char}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
# print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
