from copy import deepcopy
from pprint import pprint
from aocd import get_data
from operator import itemgetter
import sys
from time import time
import matplotlib.pyplot as plt

lis=[(101, 153), (255, 827), (361, 961)]






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 17:  ---                                                                        #
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
myset = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=17, year=2022).splitlines()




# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

starttime = time()
shapes = {
    1:{
        'next': 2,
        'coords': ((0,0),(1,0),(2,0),(3,0)),
    },
    2:{
        'next': 3,
        'coords': ((0,1),(1,0),(1,1),(1,2),(2,1)),
    },
    3:{
        'next': 4,
        'coords': ((0,0),(1,0),(2,0),(2,1),(2,2)),
    },
    4:{
        'next': 5,
        'coords': ((0,0),(0,1),(0,2),(0,3)),
    },
    5:{
        'next': 1,
        'coords': ((0,0),(1,0),(0,1),(1,1)),
    },
}
jets = myset[0]
maxjet = len(jets) - 1
curjet = 0
curshape = 1
tower = set()
tube = [0,0,0,0,0,0,0]





for _ in range(0,25000):
    s = []
    for x,y in shapes[curshape]['coords']:
        sx = x + 3
        sy = y + max(tube) + 5
        s.append((sx,sy))
    falling = True
    while falling:
        # first make the shape move down 1:
        for i,xy in enumerate(s):
            s[i] = (xy[0],xy[1] - 1)
        #attempt to move the shape to left or right
        if jets[curjet] == '>':
            if max(s,key=itemgetter(0))[0] <= len(tube) - 1:
                sm = []
                for j,xy in enumerate(s):
                    mx,my = xy
                    if (mx+1,my) not in tower:
                        sm.append((mx+1,my))
                if len(sm) == len(s): s = deepcopy(sm)
        else:
            if min(s,key=itemgetter(0))[0] > 1:
                sm = []
                for j,xy in enumerate(s):
                    mx,my = xy
                    if (mx-1,my) not in tower:
                        sm.append((mx-1,my))
                if len(sm) == len(s): s = deepcopy(sm)
        curjet = curjet + 1 if curjet < maxjet else 0
        # check to see if we are on something
        for i,xy in enumerate(s):
            if (xy[0],xy[1] -1) in tower or xy[1] -1 <= 0:
                falling = False
    for xy in s:
        tower.add(xy)
        #plt.scatter(xy[0],xy[1],color = 'black') #.scatter()
        if xy[1] > tube[xy[0]-1]:tube[xy[0]-1] = xy[1]
    if tube[0] == tube[1] == tube[2] == tube[3] == tube[4] == tube[5] == tube[6]:
        print('---------------------------------')
        print(_)
        print(tube)
        print(f'Cur Shape: {curshape}.  Next is: {shapes[curshape]["next"]}')
        print(f'next jet: {curjet}  Next 5:{jets[curjet:curjet+5]}')
    # next shape
    curshape = shapes[curshape]['next']
    #plt.show()


#plt.show()
print(len(jets))
print(tube)







print(f'Part 1 Answer is: {max(tube)}   {time() - starttime}')

