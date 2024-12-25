# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 25: Code Chronicle ---  #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=25, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    
    aoc_input.append([])
    locks = []
    keys = []
    temp = []
    max_height = 0
    for a in aoc_input:
        if a:
            temp.append(a)
        else:
            if not max_height:
                max_height = len(temp)
            b = [0] * len(temp[0])
            for c in temp:
                for i, d in enumerate(c):
                    if d == '#':
                        b[i] += 1
            if temp[0].startswith('#'):
                locks.append(b)
            elif temp[-1].startswith('#'):
                keys.append(b)
            temp = []
    
    for k in keys:
        for l in locks:
            possible_match = True
            for i, _ in enumerate(k):
                if max_height - k[i] < l[i]:
                    possible_match = False
                    break
            if possible_match:
                p1 += 1



    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 