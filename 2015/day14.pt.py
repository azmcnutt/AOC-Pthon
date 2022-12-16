import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
import re
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 14:  ---                                                                        #
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
myset = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=14, year=2015).splitlines()

rd = {}

for x in myset:
    #create a dict of dict's where n is reindeer name, s is speed, t is time, and r is rest (d is distance to be calculated later)
    n,s,t,_,r,_ = re.split(' can fly | km/s for |seconds|,| but then must rest for | seconds.',x)
    rd[n] = {
        's': int(s),
        't': int(t),
        'r': int(r),
        'd': 0
    }

# pprint(rd)

secs = 2503
p1ans = 0
for r in rd.items():
    # How many complete fly/rest cycles do we get?
    x = secs // (r[1]['t'] + r[1]['r'])
    # how many secs are left in the last cycle before time is up:
    secs_left = secs % (r[1]['t'] + r[1]['r'])
    # is there are more seconds left than the rd flies for, then add one the number of cylces
    # because the rd gets a complete flying cycle
    if secs_left >= r[1]['t']:
        x += 1
        rd[r[0]]['d'] = x * r[1]['s'] * r[1]['t']
    else:
        rd[r[0]]['d'] = (x * r[1]['s'] * r[1]['t']) + (r[1]['s'] * secs_left)
    if rd[r[0]]['d'] > p1ans: p1ans = rd[r[0]]['d']
# pprint(rd)


print(f'Part 1 Answer is {p1ans}')


#print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
