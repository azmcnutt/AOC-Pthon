import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 2: 1202 Program Alarm  ---                                                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """1,9,10,3,2,3,11,0,99,30,40,50""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=2, year=2019).splitlines()

# remove line feeds from the list

def my_initcode(init_code):
    init_code = [int(i) for i in init_code]
    # print(init_code)
    for x in range(0, len(init_code), 4):
        if init_code[x] == 1:
            # print(f'Add x: {x} - OpCode: {init_code[x]} First: {init_code[init_code[x + 1]]} Second: {init_code[init_code[x + 2]]} Write {init_code[init_code[x + 1]] + init_code[init_code[x + 2]]} to: ({init_code[x + 3]}){init_code[init_code[x + 3]]}')
            init_code[init_code[x + 3]] = init_code[init_code[x + 1]] + init_code[init_code[x + 2]]
        elif init_code[x] == 2:
            # print(f'Mul x: {x} - OpCode: {init_code[x]} First: {init_code[init_code[x + 1]]} Second: {init_code[init_code[x + 2]]} Write {init_code[init_code[x + 1]] * init_code[init_code[x + 2]]} to: ({init_code[x + 3]}){init_code[init_code[x + 3]]}')
            init_code[init_code[x + 3]] = init_code[init_code[x + 1]] * init_code[init_code[x + 2]]
        elif init_code[x] == 99:
            return init_code[0]
        else:
            print('Initcode error')
            print(f'x: {x} - OpCode: {init_code[x]} First: {init_code[x + 1]} Second: {init_code[x + 2]} Write to: {init_code[x + 3]}')
            sys.exit()
        # print(init_code)



myset = myset[0].split(',')
#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()

# Substitute the 1202 error
myset[1] = 12
myset[2] = 2

print(f'P1: {my_initcode(copy.deepcopy(myset))} in {time.time() - startime} seconds.')
startime = time.time()
for noun in range(0,99):
    for verb in range(0,99):
        # Substitute for noun and verb
        myset[1] = noun
        myset[2] = verb
        if my_initcode(copy.deepcopy(myset)) == 19690720:
            print(f'P2: {(noun * 100) + verb} in {time.time() - startime} seconds.')
            sys.exit()
