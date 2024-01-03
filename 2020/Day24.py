import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 24:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=24, year=2020).splitlines()

# remove line feeds from the list



#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()

    


dirs = {
    "e": [1, -1, 0],
    "se": [0, -1, 1],
    "sw": [-1, 0, 1],
    "w": [-1, 1, 0],
    "nw": [0, 1, -1],
    "ne": [1, 0, -1],
}

flipped = set()

for x in myset:
    location = (0,0,0)
    while len(x) > 0:
        if x[0:2] == 'se':
            x = x[2:]
            location = ((location[0] + dirs['se'][0]),(location[1] + dirs['se'][1]),(location[2] + dirs['se'][2]))
        elif x[0:2] == 'sw':
            x = x[2:]
            location = ((location[0] + dirs['sw'][0]),(location[1] + dirs['sw'][1]),(location[2] + dirs['sw'][2]))
        elif x[0:2] == 'ne':
            x = x[2:]
            location = ((location[0] + dirs['ne'][0]),(location[1] + dirs['ne'][1]),(location[2] + dirs['ne'][2]))
        elif x[0:2] == 'nw':
            x = x[2:]
            location = ((location[0] + dirs['nw'][0]),(location[1] + dirs['nw'][1]),(location[2] + dirs['nw'][2]))
        elif x[0] == 'e':
            x=x[1:]
            location = ((location[0] + dirs['e'][0]),(location[1] + dirs['e'][1]),(location[2] + dirs['e'][2]))
        elif x[0] == 'w':
            x=x[1:]
            location = ((location[0] + dirs['w'][0]),(location[1] + dirs['w'][1]),(location[2] + dirs['w'][2]))
    if location in flipped:
        flipped.remove(location)
    else:
        flipped.add(location)
print(f'Part 1: {len(flipped)} tiles are black.    {time.time() - startime}')

for x in range(100):
    night_unflip = set()
    night_flip = set()
    checked = set()
    for location in flipped:
        not_flipped = set()
        checked.add(location)
        y = 0
        for d in dirs.values():
            if ((location[0] + d[0]),(location[1] + d[1]),(location[2] + d[2])) in flipped:
                y += 1
            elif ((location[0] + d[0]),(location[1] + d[1]),(location[2] + d[2])) not in checked:
                not_flipped.add(((location[0] + d[0]),(location[1] + d[1]),(location[2] + d[2])))
        if y == 0 or y > 2:
            night_unflip.add(location)
        for z in not_flipped:
            y = 0
            checked.add(z)
            for d in dirs.values():
                if ((z[0] + d[0]),(z[1] + d[1]),(z[2] + d[2])) in flipped:
                    y += 1
            if y == 2: night_flip.add(z)
    for unflip in night_unflip:
        flipped.remove(unflip)
    for flip in night_flip:
        flipped.add(flip)
print(f'Part 2: {len(flipped)} tiles are black.    {time.time() - startime}')    


    
        

