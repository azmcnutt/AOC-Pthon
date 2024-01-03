from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re
import sys

# 51232 too low
#115311 just right
#129149 too high
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
        
        while(x):

            nextdir = -1
            if curdir == E:
                d = (1,0)
            elif curdir == S:
                d = (0,1)
            elif curdir == W:
                d = (-1,0)
            elif curdir == N:
                d = (0,-1)
            nextpos = (curpos[0] + d[0],curpos[1] + d[1])
            if nextpos in walls:
                break
            elif nextpos in paths:
                curpos = nextpos
                x-=1
            else:
                #wrap
                # OMG, I hate 3D math.  I guess this is what I need to study before next year.
                if nextpos[1] == 0: #falling off the top
                    if nextpos[0] >= 51 and nextpos[0] <= 100: # falling off first grid
                        nextpos = (1, curpos[0] + 100)
                        nextdir = E
                    elif nextpos[0] >= 101 and nextpos[0] <= 150: # falling off second grid
                        nextpos = (curpos[0] - 100, 200)
                        nextdir = N
                elif nextpos[0] >= 151 and nextpos[1] >= 1 and nextpos[1] <= 50:
                    nextpos = (100, 151 - curpos[1])
                    nextdir = W
                elif nextpos[0] >= 101 and nextpos[0] <= 150 and nextpos[1] == 51:
                    nextpos = (100, curpos[0] - 50)
                    nextdir = W
                elif nextpos[0] == 101 and nextpos[1] >= 51 and nextpos[1] <= 100:
                    nextpos = (curpos[1] + 50, 50)
                    nextdir = N
                elif nextpos[0] == 101 and nextpos[1] >= 101 and nextpos[1] <= 150:
                    nextpos = (150, 151 - curpos[1])
                    nextdir = W
                elif nextpos[0] >= 51 and nextpos[0] <= 150 and nextpos[1] == 151:
                    nextpos = (50, curpos[0] + 100)
                    nextdir = W
                elif nextpos[0] == 51 and nextpos[1] >= 151 and nextpos[1] <= 200:
                    nextpos = (curpos[1] - 100, 150)
                    nextdir = N
                elif nextpos[0] >=1 and nextpos[0] <= 50 and nextpos[1] == 201:
                    nextpos = (curpos[0] + 100, 1)
                    nextdir = S
                elif nextpos[0] == 0 and nextpos[1] >= 151 and nextpos[1] <= 200:
                    nextpos = (curpos[1] - 100, 1)
                    nextdir = S
                elif nextpos[0] == 0 and nextpos[1] >= 101 and nextpos[1] <= 150:
                    nextpos = (51, 151 - curpos[1])
                    nextdir = E
                elif nextpos[0] >= 1 and nextpos[0] <= 50 and nextpos[1] == 100:
                    nextpos = (51, 50 + curpos[0])
                    nextdir = E
                elif nextpos[0] == 50 and nextpos[1] >= 51 and nextpos[1] <= 100:
                    nextpos = (curpos[1] - 50, 101)
                    nextdir = S
                elif nextpos[0] == 50 and nextpos[1] >= 1 and nextpos[1] <= 50:
                    nextpos = (1, 151 - curpos[1])
                    nextdir = E
                else:
                    print('missed one')
                    print(f'curpos: {curpos}')
                    print(f'curdir: {curdir}')
                    print(f'nextpos: {nextpos}')
                    sys.exit()
                



                if nextpos in walls:
                    break
                elif nextpos in paths:
                    print('------------------------')
                    print(f'curpos: {curpos}')
                    print(f'curdir: {curdir}')
                    print(f'nextpos: {nextpos}')
                    print(f'nextdir: {nextdir}')
                    curpos = nextpos
                    if nextdir >= 0:
                        curdir = nextdir
                    x-=1
                else:
                    print('gotlost')
                    print(f'curpos: {curpos}')
                    print(f'curdir: {curdir}')
                    print(f'nextpos: {nextpos}')
                    sys.exit()

        # print(f'to: {curpos}')
    else:
        # print(f'curdir is {curdir}, turn {x} to {dirs[curdir][x]}.')
        curdir = dirs[curdir][x]

# print('-------------------------------')
# print(f'Current Position: {curpos}, facing {curdir}.')

p1ans = (curpos[1] * 1000) + (4 * curpos[0]) + curdir

print(f'Part 1 Answer is: {p1ans}')
print(time() - starttime)

