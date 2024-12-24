# import os
# import sys
import copy
from tqdm import tqdm
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import heapq


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 20: Race Condition ---  #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=20, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    maze = set()
    route = {}
    cheats = set()
    dirs = {
        (0, 1): [(1, 0), (-1, 0), (0, 1)],
        (1, 0): [(0, 1), (1, 0), (0, -1)],
        (0, -1): [(1, 0), (-1, 0), (0, -1)],
        (-1, 0): [(0, 1), (-1, 0), (0, -1)],
    }
    for iy, y in tqdm(enumerate(aoc_input)):
        for ix, x in enumerate(y):
            if x == '#':
                maze.add((ix, iy))
            elif x == 'S':
                start = (ix, iy)
            elif x == 'E':
                end = (ix, iy)
    
    cur_pos = end
    # get cur direction
    if (end[0], end[1] + 1) not in maze:
        cur_dir = (0, 1)
    elif (end[0], end[1] - 1) not in maze:
        cur_dir = (0, -1)
    elif (end[0] + 1, end[1]) not in maze:
        cur_dir = (1, 0)
    elif (end[0] - 1, end[1]) not in maze:
        cur_dir = (-1, 0)
    counter = 0
    route[counter] = end
    counter += 1
    while True:
        for d in dirs[cur_dir]:
            if (cur_pos[0] + d[0], cur_pos[1] + d[1]) not in maze:
                cur_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])
                cur_dir = d
                route[counter] = cur_pos
                counter += 1
                break
        if cur_pos == start:
            break
    
    # find part 1 (Sample 44)
    cheat_psec = 2
    cheat_min = 2
    for a in tqdm(range(cheat_psec, len(route))):
        for b in range(a - cheat_psec, -1, -1):
            if a == 66 and b == 0:
                pass
            md = abs(route[a][0] - route[b][0]) + abs(route[a][1] - route[b][1])
            if md <= cheat_psec:
                cheat_savings = a - b - md
                if cheat_savings >= cheat_min:
                    cheats.add((
                        a, route[a],
                        b, route[b],
                        md, cheat_savings
                    ))
    p1 = len(cheats)
    cheats = set()
    # find part 2 (Sample 285)
    cheat_psec = 20
    cheat_min = 100
    for a in tqdm(range(cheat_psec, len(route))):
        for b in range(a - cheat_psec, -1, -1):
            if a == 66 and b == 0:
                pass
            md = abs(route[a][0] - route[b][0]) + abs(route[a][1] - route[b][1])
            if md <= cheat_psec:
                cheat_savings = a - b - md
                if cheat_savings >= cheat_min:
                    cheats.add((
                        a, route[a],
                        b, route[b],
                        md, cheat_savings
                    ))
    p2 = len(cheats)
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 