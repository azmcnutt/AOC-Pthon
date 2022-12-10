import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
from functools import cache
from string import hexdigits
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
\"\\x27\"
\"g\\\\k\\x27qsl\\x34hwfglcdxqbeclt\\xca\\\\\"""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=8, year=2015).splitlines()

starttime = time.time()
len_code = 0
len_char = 0

for x in myset:
    len_code += len(x)
    #print(f'{x} : {len(x)}')
    if x[0] == '"':
        x= x[1:]
    if x[-1] == '"':
        x = x[:-1]
    y = 0
    tempstr = ''
    while y < len(x):
        #for y in range(0,len(x)):
        if len(x) - y >= 4  and x[y] == '\\' and x[y+1] == 'x' and all(c in hexdigits for c in x[y+2:y+4]):
            tempstr += 'X'
            y += 4
        elif x[y:y+1] == '\\' or x[y:y+1] == '\"':
            tempstr += 'V'
            y += 2
        else:
            tempstr += x[y]
            y += 1
    len_char += len(tempstr)
    #print(f'{tempstr} : {len(tempstr)}')
print(f'Part 1 Answer is {len_code - len_char}    {time.time() - starttime}')
starttime = time.time()
len_code = 0
len_char = 0
for x in myset:
    extra_codes = 0
    len_code += len(x)
    print(f'{x} : {len(x)}')
    if x[0] == '"':
        x= x[1:]
        extra_codes += 3
    if x[-1] == '"':
        x = x[:-1]
        extra_codes += 3
    y = 0
    tempstr = ''
    while y < len(x):
        #for y in range(0,len(x)):
        if len(x) - y >= 4  and x[y] == '\\' and x[y+1] == 'x' and all(c in hexdigits for c in x[y+2:y+4]):
            #tempstr += 'X'
            extra_codes += 1
            y += 4
        elif x[y:y+1] == '\\' or x[y:y+1] == '\"':
            #tempstr += 'V'
            extra_codes += 2
            y += 2
        else:
            # tempstr += x[y]
            y += 1
    len_char += len(x) + extra_codes
    print(f'"{x}" : {len(x) + extra_codes}')
    
#print(f'{len_code - len_char}')

# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {len_char - len_code}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
