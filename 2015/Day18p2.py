# import os
# import sys
import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time

lights = {}
dirs = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]
mx = 0
my = 0

def main():
    # # # # # # # # # # # # # # # # # # # # # # #
    # --- Day 18: Like a GIF For Your Yard ---  #
    # # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """.#.#.#
...##.
#....#
..#...
#.#..#
####..""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=18, year=2015).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p2 = 0
    steps = 100
    global mx, my

    mx = len(aoc_input[0]) - 1
    my = len(aoc_input) -1

    for iy, y in enumerate(aoc_input):
        for ix, x in enumerate(y):
            if x == '#':
                lights[(ix, iy)] = True
            elif ((ix == 0 and iy == 0) or
                  (ix == 0 and iy == my) or
                  (ix == mx and iy == 0) or
                  (ix == mx and iy == my)
            ):
                lights[(ix, iy)] = True
            else:
                lights[(ix, iy)] = False
    animate_lights(steps)
    p2 = sum(lights.values())
    print(f'P2: {p2} in {time.time() - start_time} seconds.')

def animate_lights(s):
    global lights, mx, my
    for a in tqdm(range(s)):
        new_lights = copy.deepcopy(lights)
        for x, y in lights.keys():
            counter = 0
            for d in dirs:
                if (x + d[0], y + d[1]) in lights.keys():
                    if lights[(x + d[0], y + d[1])]:
                        counter += 1
            if ((x == 0 and y == 0) or
                  (x == 0 and y == my) or
                  (x == mx and y == 0) or
                  (x == mx and y == my)
            ):
                new_lights[(x, y)] = True
            elif lights[(x, y)] and (counter < 2 or counter > 3):
                new_lights[(x, y)] = False
            elif not lights[(x, y)] and counter == 3:
                new_lights[(x, y)] = True
        lights = copy.deepcopy(new_lights)


if __name__ == '__main__':
    main()
 