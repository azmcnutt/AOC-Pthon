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
import itertools
import re
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 13:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=13, year=2015).splitlines()

people = {}

for x in myset:
    p1, ud, pts, p2 = re.split(r' would |ain |ose | happiness units by sitting next to ',x)
    if ud == 'g':
        pts = int(pts)
    else:
        pts = -1 * int(pts)
    if p1 in people.keys():
        people[p1][p2[:-1]] = int(pts)
    else:
        people[p1] = {p2[:-1]: int(pts)}
#pprint(people)

#part 2
people['me'] = {}

#now add me to people:
for x in people.keys():
    if 'me' in people.keys():
        people['me'][x] = 0
    else:
        people['me'] = {x: 0}
    people[x]['me'] = 0



p1ans = 0
p2ans = 0
for r in itertools.permutations(people.keys(), len(people)):
    points = 0
    # print(r)
    points += people[r[0]][r[-1]] + people[r[-1]][r[0]]
    for i in range(1,len(r)):
        #print(f'{r[i-1]} to {r[i]} = {people[r[i-1]][r[i]]}')
        points += people[r[i-1]][r[i]] + people[r[i]][r[i-1]]
    
    #print(f'Trip Total: {trip}')
    #if trip < p1ans or p1ans == 0: p1ans = trip
    if points > p1ans: p1ans = points

print(f'Part 1 Answer is {p1ans}')


#print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
