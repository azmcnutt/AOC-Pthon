from copy import deepcopy
from pprint import pprint
from aocd import get_data



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 14:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=14, year=2022).splitlines()

walls = set()
sand = set()
maxy = 0
for a in myset:
    b = a.split(' -> ')
    c = 1
    while c < len(b):
        x1, y1 = b[c-1].split(',')
        x2, y2 = b[c].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if y1 > maxy: maxy = y1
        if y2 > maxy: maxy = y2
        if x1 != x2: #build a wall along x axis
            if x1 > x2: x1, x2 = x2, x1 #if x1 is larger, swap
            for x in range(x1, x2+1):
                if (x,y1) not in walls:
                    walls.add((x,y1))
        else:
            if y1 > y2: y1, y2 = y2, y1 #if y1 is larger, swap
            for y in range(y1, y2+1):
                if (x1,y) not in walls:
                    walls.add((x1,y))
        c+=1

c = 0
while True:
    sx = 500
    sy = 0
    still_falling = True
    while still_falling:
        if sy > maxy:
            still_falling = False
        elif (sx, sy+1) not in walls and (sx, sy+1) not in sand: # space below is not a wall or sand
            sy += 1
        elif (sx-1, sy+1) not in walls and (sx-1, sy+1) not in sand: # space below and left is not a wall or sand
            sx -= 1
            sy += 1
        elif (sx+1, sy+1) not in walls and (sx+1, sy+1) not in sand: # space below and right is not a wall or sand
            sx += 1
            sy += 1
        else: #build a pile
            sand.add((sx,sy))
            still_falling = False
    if sy > maxy: break
    p1ans = len(sand)    
# now part 2
sand.clear()
for x in range(0,1001):
    walls.add((x,maxy+2))


while (500,0) not in sand:
    sx = 500
    sy = 0
    still_falling = True
    while still_falling:
        if (sx, sy+1) not in walls and (sx, sy+1) not in sand: # space below is not a wall or sand
            sy += 1
        elif (sx-1, sy+1) not in walls and (sx-1, sy+1) not in sand: # space below and left is not a wall or sand
            sx -= 1
            sy += 1
        elif (sx+1, sy+1) not in walls and (sx+1, sy+1) not in sand: # space below and right is not a wall or sand
            sx += 1
            sy += 1
        else: #build a pile
            sand.add((sx,sy))
            still_falling = False
    p2ans = len(sand)    

print(f'Part 1 Answer is: {p1ans}')
print(f'Part 2 Answer is: {p2ans}')

