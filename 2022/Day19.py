from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re
#import queue

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 19:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
# myset = get_data(day=19, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

starttime = time()

geods: int = 0

def getMaxGeods(c: list, rb: list, rs: list, t: int):
    global geods
    ORE = 0
    CLA = 1
    OBS = 2
    GEO = 3
    q = [] # Rather than use recursion, I am going to try using a queue list
    q.append([rb,rs,t])
    while q:
        rob, res, time = q.pop(0)
        time -= 1
        buildq = [0,0,0,0]
        # check to see if I can build a robot.  If so, add it to the build queue
        if res[ORE] >= c[GEO][ORE] and res[OBS] >= c[GEO][OBS]:
            buildq[GEO] = 1
        elif res[ORE] >= c[OBS][ORE] and res[CLA] >= c[OBS][CLA]:
            buildq[OBS] = 1
        else:
            if res[ORE] >= c[CLA][ORE]:
                buildq[CLA] = 1
            if res[ORE] >= c[ORE][ORE]:
                buildq[ORE] = 1
        # now collect resources
        res[ORE] += rob[ORE]
        res[CLA] += rob[CLA]
        res[OBS] += rob[OBS]
        res[GEO] += rob[GEO]
        if time > 0:
            #add stuff to the queue
            if buildq[GEO]: # if we can build a GEO robot, do it always
                robb = rob.copy()
                resb = res.copy()
                robb[GEO] += 1
                resb[ORE] -= c[GEO][ORE]
                resb[OBS] -= c[GEO][OBS]
                q.append([robb,resb,time])
            elif buildq[OBS]: # Ok, we can't build GEO, how about OBS
                robb = rob.copy()
                resb = res.copy()
                robb[OBS] += 1
                resb[ORE] -= c[OBS][ORE]
                resb[OBS] -= c[OBS][CLA]
                q.append([robb,resb,time])
            else: # lets so everything else
                #first do nothing
                q.append(rob,res,time)
                if buildq[CLA]: # Add a CLA to the queue
                    robb = rob.copy()
                    resb = res.copy()
                    robb[CLA] += 1
                    resb[ORE] -= c[CLA][ORE]
                    q.append([robb,resb,time])
                if buildq[ORE]: # Add a CLA to the queue
                    robb = rob.copy()
                    resb = res.copy()
                    robb[ORE] += 1
                    resb[ORE] -= c[ORE][ORE]
                    q.append([robb,resb,time])
        else: # Time has run out
            if res[GEO] > geods: geods = res[GEO]
            print(f'Rb: {rob}   Rs: {res}   MaxGeo: {geods}')




bp = list()

for x in myset:
    pattern = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    #b,ore_c_ore,cla_c_ore,obs_c_ore,obs_c_cla,geo_c_ore,geo_c_obs = re.search(pattern, x)
    y = re.search(pattern, x)
    #b,ore_c_ore,cla_c_ore,obs_c_ore,obs_c_cla,geo_c_ore,geo_c_obs = y.groups()
    #print(f'{b},{ore_c_ore},{cla_c_ore},{obs_c_ore},{obs_c_cla},{geo_c_ore},{geo_c_obs}')
    bp.append(y.groups())
print(bp)

# for i in range(0,1):
#     res = {
#         'ore': 0,
#         'cla': 0,
#         'obs': 0,
#         'geo': 0,
#     }

#     robot = {
#         'ore': {
#             'cost': {
#                 'ore': 0,
#                 'cla': 0,
#                 'obs': 0,
#                 'geo': 0,
#             },
#             'qty': 0,
#         },
#         'cla': {
#             'cost': {
#                 'ore': 0,
#                 'cla': 0,
#                 'obs': 0,
#                 'geo': 0,
#             },
#             'qty': 0,
#         },
#         'obs': {
#             'cost': {
#                 'ore': 0,
#                 'cla': 0,
#                 'obs': 0,
#                 'geo': 0,
#             },
#             'qty': 0,
#         },
#         'geo': {
#             'cost': {
#                 'ore': 0,
#                 'cla': 0,
#                 'obs': 0,
#                 'geo': 0,
#             },
#             'qty': 0,
#         },

#     }

#     robot['ore']['qty'] = 1
#     robot['ore']['cost']['ore'] = int(bp[i][1])
#     robot['cla']['cost']['ore'] = int(bp[i][2])
#     robot['obs']['cost']['ore'] = int(bp[i][3])
#     robot['obs']['cost']['cla'] = int(bp[i][4])
#     robot['geo']['cost']['ore'] = int(bp[i][5])
#     robot['geo']['cost']['obs'] = int(bp[i][6])
i = 0
costs = [
    [int(bp[i][1]),0,0,0],
    [int(bp[i][2]),0,0,0],
    [int(bp[i][3]),int(bp[i][4]),0,0],
    [int(bp[i][5]),0,int(bp[i][6]),0]
]
getMaxGeods(costs,[1,0,0,0],[0,0,0,0],24)
print(f'{bp[i][0]}: {geods}')








#print(f'Part 1 Answer is: {p1ans}   {time() - starttime}')

