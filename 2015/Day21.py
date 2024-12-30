# import os
# import sys
import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # # # #
    # --- Day 21: RPG Simulator 20XX ---  #
    # # # # # # # # # # # # # # # # # # # #

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    weps = {
        'dagger': [8, 4, 0,],
        'shortsword': [10, 5, 0,],
        'warhammer': [25, 6, 0,],
        'longsword': [40, 7, 0,],
        'greataxe': [74, 8, 0,],
    }

    armor = {
        'none': [0, 0, 0,],
        'leather': [13, 0, 1,],
        'chainmail': [31, 0, 2,],
        'splintmail': [53, 0, 3,],
        'bandedmail': [75, 0, 4,],
        'platemail': [102, 0, 5,],
    }

    rings = {
        'none1': [0, 0, 0,],
        'none2': [0, 0, 0,],
        'dam1': [25, 1, 0,],
        'dam2': [50, 2, 0,],
        'dam3': [100, 3, 0,],
        'def1': [20, 0, 1,],
        'def2': [40, 0, 2,],
        'def3': [80, 0, 3,],
    }

    boss = {
        'hp': 104,
        'dam': 8,
        'arm': 1,
    }

    player = {
        'hp': 100,
        'dam': 0,
        'arm': 0,
    }

    test_player = {
        'hp': 8,
        'dam': 5,
        'arm': 5,
    }

    test_boss = {
        'hp': 12,
        'dam': 7,
        'arm': 2,
    }

    p1 = 0
    p2 = 0

    for wn, w in weps.items():
        for an, a in armor.items():
            for rn1, r1 in rings.items():
                for rn2, r2 in rings.items():
                    if rn1 != rn2:
                        p = copy.deepcopy(player)
                        b = copy.deepcopy(boss)
                        p['dam'] = w[1] + r1[1] + r2[1]
                        p['arm'] = a[2] + r1[2] + r2[2]
                        cost = w[0] + a[0] + r1[0] + r2[0]
                        if does_player_win(p, b):
                            if p1 == 0 or cost < p1:
                                p1 = cost
                        else:
                            if p2 < cost:
                                p2 = cost


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def does_player_win(p: dict, b: dict) -> bool:
    while True:
        b['hp'] -= (p['dam'] - b['arm'])
        if b['hp'] <= 0:
            return True
        p['hp'] -= (b['dam'] - p['arm'])
        if p['hp'] <= 0:
            return False



if __name__ == '__main__':
    main()
 