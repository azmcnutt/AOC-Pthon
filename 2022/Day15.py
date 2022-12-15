from copy import deepcopy
from pprint import pprint
from aocd import get_data
import re
from time import time



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 15:  ---                                                                        #
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
y = 2000000

sensors = {}
beacons = set()
ycoverage = []

for d in myset:
    _,sx,sy,bx,by = re.split('Sensor at x=|, y=|: closest beacon is at x=',d)
    md = (abs(int(sx) - int(bx)) + abs(int(sy) - int(by)))
    sensors[(int(sx),int(sy))] = md
    beacons.add((int(bx),int(by)))

for s,md in sensors.items():
    if s[1] == y: #the sensor is on Y, so the md is in both directions
        # (0, 11): 3
        l = s[0] - md
        h = s[0] + md
        #print(f'{s}: y from: {l},{y} to {h},{y}')
    elif s[1] < y and s[1] + md >= y:
        # (16, 7): 5
        l = s[0] - (md - (y - s[1]))
        h = s[0] + (md - (y - s[1]))
        #print(f'{s}: y from: {l},{y} to {h},{y}')
    elif s[1] > y and s[1] - md <= y:
        # 20,14 8
        l = s[0] - (md - (s[1] - y))
        h = s[0] + (md - (s[1] - y))
        #print(f'{s}: y from: {l},{y} to {h},{y}')
    else:
        continue
    #
    # print(f'{s}: y from: {l},{y} to {h},{y}')
    ycoverage.extend(list(range(l,h+1)))
ycoverage = set(ycoverage)
#print(len(ycoverage))
#print(ycoverage)
for bx,by in beacons:
    if by == y and bx in ycoverage:
        ycoverage.remove(bx)
#print('-------------------')
#print(ycoverage)
#print(len(ycoverage))
p1ans = len(ycoverage)

print(f'Part 1 Answer is: {p1ans} {time() - starttime}')
#print(f'Part 2 Answer is: {p2ans}')

