# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

dirs = [
        (-1,0),
        (0,1),
        (1,0),
        (0,-1),
    ]

# load sample data, copied and pasted from the site into list.
# Each list item is one line of input
aoc_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()

# once the test data provides the right answer:
# replace test data with data from the puzzle input
aoc_input = get_data(day=10, year=2024).splitlines()

def main():
    # # # # # # # # # # # # # # #
    # --- Day 10: Hoof It  ---  #
    # # # # # # # # # # # # # # #

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.

    start_time = time.time()

    p1 = 0
    p2 = 0
    starts = []
    ends = 0
    

    for indx, x in enumerate(aoc_input):
        for indy, y in enumerate(x):
            if int(y) == 0:
                starts.append((indx,indy))    

    for s in starts:
        found = []
        p1 += find_trail(s, 0, found)
        p2 += find_trail(s, 0, found, True)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def find_trail(pos, ends, found, find_all = False):
    cur_elevation = int(aoc_input[pos[0]][pos[1]])
    if cur_elevation == 9:
        if pos not in found:
            found.append(pos)
            ends += 1
        elif find_all:
            ends += 1
        return ends
    for d in dirs:
        next_pos = (
            pos[0] + d[0],
            pos[1] + d[1],
        )
        if (next_pos[0] >= 0 and next_pos[0] < len(aoc_input) and
            next_pos[1] >= 0 and next_pos[1] < len(aoc_input[0]) and
            cur_elevation + 1 == int(aoc_input[next_pos[0]][next_pos[1]])):
            ends = find_trail(next_pos, ends, found, find_all)
    return ends

if __name__ == '__main__':
    main()
