from copy import deepcopy
from pprint import pprint
from aocd import get_data
import re
from time import time
import sys
from functools import cache



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 15:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=15, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')
starttime = time()
# y = 10

maxxy = 4000000

sensors = {}



for d in myset:
    _,sx,sy,bx,by = re.split('Sensor at x=|, y=|: closest beacon is at x=',d)
    md = (abs(int(sx) - int(bx)) + abs(int(sy) - int(by)))
    sensors[(int(sx),int(sy))] = md

@cache
def check_point(x,y):
    # get the manhatan distance between (x,y) and s, if less than or = md then false
    for s,md in sensors.items():
        if (abs(s[0] - x) + abs(s[1] - y)) <= md:
            return False
    return True



def search_edges():# get edge of sensor md + 1
    for s,md in sensors.items():
        md += 1
        for i in range(0,md + 1):
            edges = lambda: [(s[0]-i,s[1]-(md-i)), (s[0]-i,s[1]+(md-i)), (s[0]+i,s[1]-(md-i)), (s[0]+i,s[1]-(md-i))]
            #u/l:
            for p in edges():
            # now check each edge point to see if one of the other areas intersects
                if p[0] >= 0 and p[0] <= maxxy and p[1] >=0 and p[1] <= maxxy:
                    if check_point(p[0],p[1]): return p

x,y = search_edges()
print(f'Part 2 Answer is: {(x * 4000000) + y}   {time() - starttime}')

