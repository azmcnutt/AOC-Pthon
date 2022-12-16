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
# myset = get_data(day=14, year=2015).splitlines()

rd = {}

for x in myset:
    #create a dict of dict's where n is reindeer name, s is speed, t is time, and r is rest (d is distance and p is points to be calculated later)
    n,s,t,_,r,_ = re.split(' can fly | km/s for |seconds|,| but then must rest for | seconds.',x)
    rd[n] = {
        's': int(s),
        't': int(t),
        'r': int(r),
        'd': 0,
        'p': 0,
    }

# pprint(rd)

secs = 1000
p2ans = 0
c = 0
for i in range(1,secs + 1):
    c += 1
    leadscore = 0
    for r in rd.items():
        # take the mod to determine if the rd is flying or resting
        x = i % (r[1]['t'] + r[1]['r'])
        if x <= r[1]['t']: #rd flies for this second, add the distance
            rd[r[0]]['d'] += rd[r[0]]['s']
        #if rd[r[0]]['d'] > leadscore: leadscore = rd[r[0]]['d']
    #for r in rd.items():
    #    if rd[r[0]]['d'] == leadscore:
    #        rd[r[0]]['p'] += 1


pprint(rd)
print(c)

print(f'Part 1 Answer is {p2ans}')


#print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
