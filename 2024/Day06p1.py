# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 6: Guard Gallivant  --- #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=6, year=2024).splitlines()
    # too low 4579

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    
    obstructions = set()
    empties = set()
    cur_dir = 'n'
    cur_pos = (0,0,'n')
    


    for ix, x in enumerate(aoc_input):
        for iy, y in enumerate(x):
            if y == '.':
                empties.add((ix, iy))
            elif y == '#':
                obstructions.add((ix, iy))
            elif y == '^':
                cur_pos = (ix, iy)

    
    
    p1 = guard_path_length(cur_pos, cur_dir, obstructions, len(aoc_input), len(aoc_input[0]))

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def guard_path_length(s, d, o, max_x, max_y):
    min_x = 0
    min_y = 0
    # max_x = len(aoc_input)
    #max_y = len(aoc_input[0])
    visited = set()
    next_dirs = {
        'n': 'e',
        'e': 's',
        's': 'w',
        'w': 'n',
    }
    
    dirs = {
        'n': (-1, 0),
        'e': (0, 1),
        's': (1,0),
        'w': (0,-1),
    }
    while(s[0] >= min_x and
          s[0] < max_x and
          s[1] >= min_y and
          s[1] < max_y
          ):
        visited.add(s)
        while True:
            n = (s[0] + dirs[d][0],
                 s[1] + dirs[d][1],
                 )
            if n not in o:
                s = n
                break
            else:
                d = next_dirs[d]
    return(len(visited))

if __name__ == '__main__':
    main()