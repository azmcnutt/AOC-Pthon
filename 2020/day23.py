import os
import sys
import copy
import time
from aocd import get_data
from aocd import submit
from pprint import pprint

# AOC 2020 --- Day 23: Crab Cups ---


myset = """389125467""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
#myset = get_data(day=23, year=2020).splitlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
#print(myset)
starttime = time.time()

cups = []
for x in myset[0]:
    cups.append(int(x))

# pprint(cups)

for x in range(100):
    temp_list = copy.deepcopy(cups[1:4])
    for y in temp_list:
        cups.remove(y)
    z = cups[0]
    while True:
        if z == 1:
            z = 9
        else:
            z -= 1
        if z in cups:
            z = cups.index(z) + 1
            break
    for y in reversed(temp_list):
        cups.insert(z,y)
    cups.append(cups.pop(0))
    
while cups[0] != 1:
    cups.append(cups.pop(0))
p1ans = ''
for x in cups[1:]:
    p1ans += str(x)
print(f'Part 1: Cup order is {p1ans}.    {time.time() - starttime}')
submit(p1ans, part='a', day=23, year=2020)

