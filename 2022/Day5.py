import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 5:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=5, year=2022).splitlines()

# remove line feeds from the list



#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()
ship = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [],}

for x in myset:
    if x == '': pass
    elif x[1] != '1' and x[0] != 'm':
        y = 1
        z = 1
        temp = []
        while y < len(x):
            if (x[y]) != ' ':ship[z].append(x[y])
            y += 4
            z += 1
    elif x[0] == 'm':
        _, q, _, f, _, t = x.split(' ')
        q = int(q)
        f = int(f)
        t = int(t)
        temp=[]
        for _ in range (0,q):
            temp.append(ship[f].pop(0))
        for _ in temp:
            ship[t].insert(0,_)

p1ans = ''
for s,c in ship.items():
    if len(c) > 0:
        p1ans += c[0]
print(f'Part 1 Answer is {p1ans}    {time.time() - startime}')
# submit(p1ans, part='a', day = 5, year=2022)

# Part 2
startime = time.time()
ship = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [],}

for x in myset:
    if x == '': pass
    elif x[1] != '1' and x[0] != 'm':
        y = 1
        z = 1
        temp = []
        while y < len(x):
            if (x[y]) != ' ':ship[z].append(x[y])
            y += 4
            z += 1
    elif x[0] == 'm':
        _, q, _, f, _, t = x.split(' ')
        q = int(q)
        f = int(f)
        t = int(t)
        temp=[]
        for _ in range (0,q):
            temp.append(ship[f].pop(0))
        for _ in reversed(temp):
            ship[t].insert(0,_)

p2ans = ''
for s,c in ship.items():
    if len(c) > 0:
        p2ans += c[0]
print(f'Part 2 Answer is {p2ans}    {time.time() - startime}')
# submit(p2ans, part='b', day = 5, year=2022)