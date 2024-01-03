import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """>
^>v<
^v^v^v^v^v""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=3, year=2015).splitlines()

starttime = time.time()
moves = {
    "^": (1,0),
    "v": (-1,0),
    "<": (0,1),
    ">": (0,-1),
}

s_loc = (0,0)
rs_loc = (0,0)
total = 0
for x in myset:
    houses = set()
    houses.add(s_loc)
    for y in x:
        s_loc = (s_loc[0] + moves[y][0], s_loc[1] + moves[y][1])
        houses.add(s_loc)
    total += len(houses)
    s_loc = (0,0)
print(f'Part 1 Answer is {total}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)

# part 2
s_loc = (0,0)
rs_loc = (0,0)
total = 0
for x in myset:
    houses = set()
    houses.add(s_loc)
    for y in range(0, len(x)):
        if y % 2 == 0:
            #santa
            s_loc = (s_loc[0] + moves[x[y]][0], s_loc[1] + moves[x[y]][1])
            houses.add(s_loc)
        else:
            # robot santa
            rs_loc = (rs_loc[0] + moves[x[y]][0], rs_loc[1] + moves[x[y]][1])
            houses.add(rs_loc)
    total += len(houses)
    s_loc = (0,0)
    rs_loc = (0,0)



print(f'Part 2 Answer is {total}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
