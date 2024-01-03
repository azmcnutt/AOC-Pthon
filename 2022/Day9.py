import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 9:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

myset = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=9, year=2022).splitlines()

starttime = time.time()
dirs = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0),
    'u': (0,1),
    'd': (0,-1),
    'r': (1,0),
    'l': (-1,0),
}

h = (0,0)
t = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),]
last_h = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
tset = set()
tset.add(t[0])
t9set = set()
t9set.add(t[8])
for z in myset:
    d,m = z.split(' ')
    for i in range(0,int(m)):
        last_h[0] = h
        h = (h[0] + dirs[d][0],h[1] + dirs[d][1])
        # print(f'x:{abs(t[0]-h[0])},y:{abs(t[1]-h[1])}')
        if abs(t[0][0]-h[0]) > 1 or abs(t[0][1]-h[1]) > 1:
            # move tail
            if last_h[0][0] > t[0][0] and last_h[0][1] > t[0][1]: #move T up and right
                t[0] = (t[0][0] + dirs['u'][0] + dirs['r'][0],t[0][1] + dirs['u'][1] + dirs['r'][1])
            elif last_h[0][0] > t[0][0] and last_h[0][1] < t[0][1]: #move T dn and right
                t[0] = (t[0][0] + dirs['d'][0] + dirs['r'][0],t[0][1] + dirs['d'][1] + dirs['r'][1])
            elif last_h[0][0] < t[0][0] and last_h[0][1] > t[0][1]: #move T up and left
                t[0] = (t[0][0] + dirs['u'][0] + dirs['l'][0],t[0][1] + dirs['u'][1] + dirs['r'][1])
            elif last_h[0][0] < t[0][0] and last_h[0][1] < t[0][1]: #move T dn and left
                t[0] = (t[0][0] + dirs['d'][0] + dirs['l'][0],t[0][1] + dirs['d'][1] + dirs['r'][1])
            elif last_h[0][0] == t[0][0] and last_h[0][1] > t[0][1]: #move T up
                t[0] = (t[0][0] + dirs['u'][0],t[0][1] + dirs['u'][1])
            elif last_h[0][0] == t[0][0] and last_h[0][1] < t[0][1]: #move T dn
                t[0] = (t[0][0] + dirs['d'][0],t[0][1] + dirs['d'][1])
            elif last_h[0][0] > t[0][0] and last_h[0][1] == t[0][1]: #move T right
                t[0] = (t[0][0] + dirs['r'][0],t[0][1] + dirs['r'][1])
            elif last_h[0][0] < t[0][0] and last_h[0][1] == t[0][1]: #move T left
                t[0] = (t[0][0] + dirs['l'][0],t[0][1] + dirs['l'][1])
            tset.add(t[0])
            last_h[1] = t[0]
        for j in range(1,len(t)):
            if abs(t[j][0]-t[j-1][0]) > 1 or abs(t[j][1]-t[j-1][1]) > 1:
                # move tail
                if last_h[j][0] > t[j][0] and last_h[j][1] > t[j][1]: #move T up and right
                    t[j] = (t[j][0] + dirs['u'][0] + dirs['r'][0],t[j][1] + dirs['u'][1] + dirs['r'][1])
                elif last_h[j][0] > t[j][0] and last_h[j][1] < t[j][1]: #move T dn and right
                    t[j] = (t[j][0] + dirs['d'][0] + dirs['r'][0],t[j][1] + dirs['d'][1] + dirs['r'][1])
                elif last_h[j][0] < t[j][0] and last_h[j][1] > t[j][1]: #move T up and left
                    t[j] = (t[j][0] + dirs['u'][0] + dirs['l'][0],t[j][1] + dirs['u'][1] + dirs['r'][1])
                elif last_h[j][0] < t[j][0] and last_h[j][1] < t[j][1]: #move T dn and left
                    t[j] = (t[j][0] + dirs['d'][0] + dirs['l'][0],t[j][1] + dirs['d'][1] + dirs['r'][1])
                elif last_h[j][0] == t[j][0] and last_h[j][1] > t[j][1]: #move T up
                    t[j] = (t[j][0] + dirs['u'][0],t[j][1] + dirs['u'][1])
                elif last_h[j][0] == t[j][0] and last_h[j][1] < t[j][1]: #move T dn
                    t[j] = (t[j][0] + dirs['d'][0],t[j][1] + dirs['d'][1])
                elif last_h[j][0] > t[j][0] and last_h[j][1] == t[j][1]: #move T right
                    t[j] = (t[j][0] + dirs['r'][0],t[j][1] + dirs['r'][1])
                elif last_h[j][0] < t[j][0] and last_h[j][1] == t[j][1]: #move T left
                    t[j] = (t[j][0] + dirs['l'][0],t[j][1] + dirs['l'][1])
                last_h[j+1] = t[j]
        t9set.add(t[8])

            

print(f'Part 1 Answer is {len(tset)}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {len(t9set)}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
