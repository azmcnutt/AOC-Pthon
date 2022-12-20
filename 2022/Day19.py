from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 19:  ---                                                                        #
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
myset = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
# myset = get_data(day=19, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

starttime = time()

geods: int = 0

def getMaxGeods(rb: dict, rs: list, t: int):
    global geods
    # create new rs
    new_rs = {
        'ore': rs['ore'] + rb['ore']['qty'],
        'cla': rs['cla'] + rb['cla']['qty'],
        'obs': rs['obs'] + rb['obs']['qty'],
        'geo': rs['geo'] + rb['geo']['qty'],
    }
    
    t = t - 1
    if t <= 0:
        print(rs)
        if rs['geo'] > geods:
            geods = rs['geo'] 
        return rs
    while t >= 1:
        # IF we can buy a geode robot, then do it
        if rs['obs'] >= rb['geo']['cost']['obs'] and rs['ore'] >= rb['geo']['cost']['ore']:
            new_rs['obs'] -= rb['geo']['cost']['obs']
            new_rs['ore'] -= rb['geo']['cost']['ore']
            rb['geo']['qty'] += 1
            rs = getMaxGeods(rb.copy(),new_rs.copy(), t)
            # reset to make sure we get all combinations
            new_rs['obs'] += rb['geo']['cost']['obs']
            new_rs['ore'] += rb['geo']['cost']['ore']
            rb['geo']['qty'] -= 1
        # if we can buy an obsidian robot, then do it
        elif rs['cla'] >= rb['obs']['cost']['cla'] and rs['ore'] >= rb['obs']['cost']['ore']:
            new_rs['cla'] -= rb['obs']['cost']['cla']
            new_rs['ore'] -= rb['obs']['cost']['ore']
            rb['obs']['qty'] += 1
            rs = getMaxGeods(rb.copy(),new_rs.copy(), t)
            # reset to make sure we get all combinations
            new_rs['cla'] += rb['obs']['cost']['cla']
            new_rs['ore'] += rb['obs']['cost']['ore']
            rb['obs']['qty'] -= 1
        else:
            # see what happens when we do nothing, or try to purchase one of the other robots
            # do nothing
            rs = getMaxGeods(rb.copy(),new_rs.copy(), t)

            #try to buy a cla robot:
            if rs['ore'] >= rb['cla']['cost']['ore']:
                new_rs['ore'] -= rb['cla']['cost']['ore']
                rb['cla']['qty'] += 1
                rs = getMaxGeods(rb.copy(),new_rs.copy(), t)
                # reset to make sure we get all combinations
                new_rs['ore'] += rb['cla']['cost']['ore']
                rb['cla']['qty'] -= 1
            
            #try to buy a ore robot:
            if rs['ore'] >= rb['ore']['cost']['ore']:
                new_rs['ore'] -= rb['ore']['cost']['ore']
                rb['ore']['qty'] += 1
                rs = getMaxGeods(rb.copy(),new_rs.copy(), t)
                # reset to make sure we get all combinations
                new_rs['ore'] += rb['cla']['cost']['ore']
                rb['ore']['qty'] -= 1
            
            
    return rs

bp = list()

for x in myset:
    pattern = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    #b,ore_c_ore,cla_c_ore,obs_c_ore,obs_c_cla,geo_c_ore,geo_c_obs = re.search(pattern, x)
    y = re.search(pattern, x)
    #b,ore_c_ore,cla_c_ore,obs_c_ore,obs_c_cla,geo_c_ore,geo_c_obs = y.groups()
    #print(f'{b},{ore_c_ore},{cla_c_ore},{obs_c_ore},{obs_c_cla},{geo_c_ore},{geo_c_obs}')
    bp.append(y.groups())
print(bp)

for i in range(0,1):
    res = {
        'ore': 0,
        'cla': 0,
        'obs': 0,
        'geo': 0,
    }

    robot = {
        'ore': {
            'cost': {
                'ore': 0,
                'cla': 0,
                'obs': 0,
                'geo': 0,
            },
            'qty': 0,
        },
        'cla': {
            'cost': {
                'ore': 0,
                'cla': 0,
                'obs': 0,
                'geo': 0,
            },
            'qty': 0,
        },
        'obs': {
            'cost': {
                'ore': 0,
                'cla': 0,
                'obs': 0,
                'geo': 0,
            },
            'qty': 0,
        },
        'geo': {
            'cost': {
                'ore': 0,
                'cla': 0,
                'obs': 0,
                'geo': 0,
            },
            'qty': 0,
        },

    }

    robot['ore']['qty'] = 1
    robot['ore']['cost']['ore'] = int(bp[i][1])
    robot['cla']['cost']['ore'] = int(bp[i][2])
    robot['obs']['cost']['ore'] = int(bp[i][3])
    robot['obs']['cost']['cla'] = int(bp[i][4])
    robot['geo']['cost']['ore'] = int(bp[i][5])
    robot['geo']['cost']['obs'] = int(bp[i][6])

    getMaxGeods(robot,res,24)
    print(f'{bp[i][0]}: {geods}')








#print(f'Part 1 Answer is: {p1ans}   {time() - starttime}')

