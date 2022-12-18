from copy import deepcopy
from pprint import pprint
from aocd import get_data
import sys

# part two would not run on windows.  Had to run on linux and increase recursion size and resource limit.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 18:  ---                                                                        #
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
myset = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()



# once the test data provides the right answer: replace test data with data from the puzzle input
# myset = get_data(day=18, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')





cubes = []
space = []
maxx = 0
maxy = 0
maxz = 0
for i in myset:
    x,y,z = i.split(',')
    x,y,z = int(x),int(y),int(z)
    if x > maxx: maxx = x
    if y > maxy: maxy = y
    if z > maxz: maxz = z
    cubes.append((x,y,z))
sides = 0
adjacents = lambda x, y, z: [(x, y, z+1), (x, y+1, z), (x+1, y, z), (x, y, z-1), (x, y-1, z), (x-1, y, z)]
for i in cubes:
    x,y,z = i
    s = 6
    for p in adjacents(x, y, z):
        if p in cubes:
            s -= 1
    sides += s
print(f'Part 1 Answer is: {sides}')

print(maxx * maxy * maxz)
#part 2
# flood fill and trapped list ides from PHolder on Twit community forums:
# https://www.twit.community/t/advent-of-code-2022/13520/76
def floodFill(x, y, z):
    if x < 0 or y < 0 or z < 0: return
    if x > maxx + 1 or y > maxy + 1 or z > maxz + 1: return
    space.append((x, y, z))
    for p in adjacents(x,y,z):
        if p not in cubes and p not in space:
            floodFill(p[0],p[1],p[2])
floodFill(0,0,0)

# I don't know why I need to do this, but when I checked to see if a neighbor was in cubes or not in space it gave the wrong answer.
trapped = []
for x in range(0,maxx + 1):
    for y in range(0,maxy + 1):
        for z in range(0,maxz + 1):
            if (x,y,z) not in cubes and (x,y,z) not in space:
                trapped.append((x,y,z))

#print(trapped)

sides = 0
for i in cubes:
    x,y,z = i
    s = 6
    for p in adjacents(x, y, z):
        if p in cubes or p in trapped:
            s -= 1
    sides += s
print(f'Part 2 Answer is: {sides}')









