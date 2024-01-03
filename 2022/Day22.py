from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 22:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=22, year=2022).splitlines()
starttime = time()
# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

E = 0
S = 1
W = 2
N = 3
walls = set()
paths = set()
curpos = ()
curdir = E
inst = ''
moves = []
dirs = {
    E: {
        'R': S,
        'L': N,
    },
    S: {
        'R': W,
        'L': E,
    },
    W: {
        'R': N,
        'L': S,
    },
    N: {
        'R': E,
        'L': W,
    },
}

for i,y in enumerate(myset):
    if y == '':
        inst = myset[i+1]
        break
    for j,x in enumerate(y):
        if curpos == () and i == 0 and x == '.':
            curpos = (j+1,i+1)
        if x == '.':
            paths.add((j+1,i+1))
        elif x == '#':
            walls.add((j+1,i+1))
# print(curpos)
# print('-----------------------------')
# print(walls)
# print('-----------------------------')
# print(paths)
# print('-----------------------------')
# print(inst)

temp_move = ''
while inst:
    if inst[0].isnumeric():
        temp_move += inst[0]
        inst = inst[1:]
    else:
        moves.append(int(temp_move))
        temp_move = ''
        moves.append(inst[0])
        inst = inst[1:]
if len(temp_move) > 0 and temp_move.isnumeric():
    moves.append(int(temp_move))
del temp_move
del inst

# pprint(dirs)

# print(moves)

for x in moves:
    if type(x) == int:
        # print(f'try to move {x} spaces.')
        # print(f'from: {curpos}')
        # I know there is a better way to determine direction, but.....  I'm lazy
        if curdir == E:
            d = (1,0)
        elif curdir == S:
            d = (0,1)
        elif curdir == W:
            d = (-1,0)
        elif curdir == N:
            d = (0,-1)
        while(x):
            nextpos = (curpos[0] + d[0],curpos[1] + d[1])
            if nextpos in walls:
                break
            elif nextpos in paths:
                curpos = nextpos
                x-=1
            else:
                #wrap
                if curdir == E: #find the space on the left side of the board
                    # again, I know there is a better way.....
                    minx = 0
                    for z in walls.union(paths):
                        if z[1] == curpos[1] and (z[0] < minx or minx == 0):
                            minx = z[0]
                    nextpos = (minx, curpos[1])
                elif curdir == S: #find the space on the left side of the board
                    # again, I know there is a better way.....
                    miny = 0
                    for z in walls.union(paths):
                        if z[0] == curpos[0] and (z[1] < miny or miny == 0):
                            miny = z[1]
                    nextpos = (curpos[0], miny)
                elif curdir == W: #find the space on the left side of the board
                    # again, I know there is a better way.....
                    maxx = 0
                    for z in walls.union(paths):
                        if z[1] == curpos[1] and z[0] > maxx:
                            maxx = z[0]
                    nextpos = (maxx, curpos[1])
                elif curdir == N: #find the space on the left side of the board
                    # again, I know there is a better way.....
                    maxy = 0
                    for z in walls.union(paths):
                        if z[0] == curpos[0] and z[1] > maxy:
                            maxy = z[1]
                    nextpos = (curpos[0], maxy)
                if nextpos in walls:
                    break
                elif nextpos in paths:
                    curpos = nextpos
                    x-=1
        # print(f'to: {curpos}')
    else:
        # print(f'curdir is {curdir}, turn {x} to {dirs[curdir][x]}.')
        curdir = dirs[curdir][x]

# print('-------------------------------')
# print(f'Current Position: {curpos}, facing {curdir}.')

p1ans = (curpos[1] * 1000) + (4 * curpos[0]) + curdir

print(f'Part 1 Answer is: {p1ans}')
print(time() - starttime)

