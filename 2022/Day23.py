from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re
import sys

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 23:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=23, year=2022).splitlines()
starttime = time()
# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

e = set()
adjacents = lambda x, y: [(x, y+1), (x+1, y), (x, y-1), (x-1, y), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
check_n = lambda x, y: [(x+1, y-1), (x, y-1), (x-1, y-1)]
check_s = lambda x, y: [(x+1, y+1), (x, y+1), (x-1, y+1)]
check_w = lambda x, y: [(x-1, y+1), (x-1, y), (x-1, y-1)]
check_e = lambda x, y: [(x+1, y+1), (x+1, y), (x+1, y-1)]
nextdirs = {
    'N': 'S',
    'S': 'W',
    'W': 'E',
    'E': 'N',
}
curdir = 'N'

def printmap(s):
    miny = 1000000000
    minx = 1000000000
    maxx = 0
    maxy = 0
    for x,y in s:
        if x > maxx: maxx = x
        if x < minx: minx = x
        if y > maxy: maxy = y
        if y < miny: miny = y
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in s:
                print('#', end = '')
            else:
                print('.', end = '')
        print()

def checkprogress(s):
    miny = 1000000000
    minx = 1000000000
    maxx = 0
    maxy = 0
    for x,y in s:
        if x > maxx: maxx = x
        if x < minx: minx = x
        if y > maxy: maxy = y
        if y < miny: miny = y
    
    #print(f'X Width = {maxx - minx + 1}')
    #print(f'Y Width = {maxy - miny + 1}')
    #print(f'Area = {(maxx - minx + 1) * (maxy - miny + 1)}')
    #print(f'Num Elves = {len(s)}')
    #print(f'Empty Ground = {((maxx - minx + 1) * (maxy - miny + 1)) - len(s)}')
    return ((maxx - minx + 1) * (maxy - miny + 1)) - len(s)


for y, i in enumerate(myset):
    for x, j in enumerate(i):
        if j == '#':
            e.add((x,y))
        else:
            pass
#printmap(e)
i = 1
while True:
    ep = []
    moves = []
    for x,y in e:
        moving = False
        for p in adjacents(x,y):
            if p in e:
                moving = True
                break
        if moving:
            looking = curdir
            for _ in range(0,4):
                empty = True
                if looking == 'N':
                    for p in check_n(x,y):
                        if p in e:
                            empty = False
                            break
                elif looking == 'S':
                    for p in check_s(x,y):
                        if p in e:
                            empty = False
                            break
                elif looking == 'W':
                    for p in check_w(x,y):
                        if p in e:
                            empty = False
                            break
                elif looking == 'E':
                    for p in check_e(x,y):
                        if p in e:
                            empty = False
                            break
                if empty:
                    if looking == 'N':
                        ep.append((x,y-1))
                        moves.append([(x,y),(x,y-1)])
                        break
                    if looking == 'S':
                        ep.append((x,y+1))
                        moves.append([(x,y),(x,y+1)])
                        break
                    if looking == 'W':
                        ep.append((x-1,y))
                        moves.append([(x,y),(x-1,y)])
                        break
                    if looking == 'E':
                        ep.append((x+1,y))
                        moves.append([(x,y),(x+1,y)])
                        break
                else:
                    looking = nextdirs[looking]
    if len(moves) == 0:
        print(f'Part 2 Answer is: {i}')
        print(time() - starttime)
        sys.exit()
    for f,t in moves:
        if ep.count(t) == 1:
            e.remove(f)
            e.add(t)
    curdir = nextdirs[curdir]
    if i == 10:
        print(f'Part 1 Answer is: {checkprogress(e)}')
        print(time() - starttime)
    i += 1
    #print('--------------------------')
    #printmap(e)

p1ans = checkprogress(e)

print(f'Part 1 Answer is: {p1ans}')
print(time() - starttime)

