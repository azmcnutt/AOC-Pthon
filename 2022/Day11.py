from copy import deepcopy
from pprint import pprint
from aocd import get_data
import time
import re
from math import lcm


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 11:  ---                                                                        #
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
myset = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=11, year=2022).splitlines()

starttime = time.time()
tests = []
mon=dict()
x=0
while x < len(myset):
    mon_num = int(myset[x][-2])
    mon[mon_num] = dict()
    mon[mon_num]['counter'] = 0
    x += 1
    items = re.split(': |,',myset[x])
    items.pop(0)
    mon[mon_num]['items'] = [int(_) for _ in items]
    x += 1
    if myset[x][23] == '+':
        mon[mon_num]['op'] = 'add'
    else:
        mon[mon_num]['op'] = 'mul'
    if myset[x][25:] == 'old':
        mon[mon_num]['val'] = -1
    else:
        mon[mon_num]['val'] = int(myset[x][25:])
    x += 1
    mon[mon_num]['test'] = int(myset[x][21:])
    tests.append(int(myset[x][21:]))
    x += 1
    mon[mon_num]['t'] = int(myset[x][-1])
    x += 1
    mon[mon_num]['f'] = int(myset[x][-1])
    x += 2
#pprint(mon)

lcm_div = lcm(*tests)

for _ in range(0,10000):
    for m in mon.keys():
        for x in range(0,len(mon[m]['items'])):
            mon[m]['counter'] += 1
            i = mon[m]['items'].pop(0)
            if mon[m]['op'] == 'add':
                i += mon[m]['val']
            elif mon[m]['op'] == 'mul' and mon[m]['val'] == -1:
                i *= i
            else:
                i *= mon[m]['val']
            # A little bit of help from https://github.com/MuhammadSaadSiddique/AdventofCode/blob/main/2022/11/code.py
            # using the lowest common multiple of the test divisors, allows us to keep the worry int low enough
            # to now cause an overflow.  This also allows the code to run in a reasonable amount of time.
            i %= lcm_div
            # for part 1, floor divide by 3
            # i //= 3
            if i % mon[m]['test'] == 0:
                mon[mon[m]['t']]['items'].append(i)
            else:
                mon[mon[m]['f']]['items'].append(i)

counters=[]
for _ in mon:
    counters.append(mon[_]['counter'])
p1ans = max(counters)
counters.remove(p1ans)
p1ans *= max(counters)



print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
#print(f'Part 2 Answer is:')

