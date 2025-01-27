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
    # # # # # # # # # # # #
    # --- Day  19: TBD --- #
    # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO""".splitlines()
    # Sample Part 1 Answer: 4

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=19, year=2015).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    molc = set()
    replacement = []
    orig_molc = ''

    for a in aoc_input:
        if '=>' not in  a:
            break
        replacement.append(a.split(' => '))
    orig_molc = aoc_input[-1]

    for r in replacement:
        start = 0
        while True:
            index = orig_molc.find(r[0], start)
            if index == -1:
                break

            s = orig_molc[:index] + r[1] + orig_molc[index + len(r[0]):]
            molc.add(s)
            start = index + 1
    p1 = len(molc)
    
    # loop from:
    # https://github.com/hughcoleman/advent-of-code/blob/6d27c39a6ba300b46d62726a985b784fb0bb1db2/events/2015/19.py#L46
    # Does not work well on the sample input, but works on actual problem.
    while orig_molc != "e":
        for reactant, products in replacement:
            if "".join(products) in orig_molc:
                orig_molc = orig_molc.replace("".join(products), reactant, 1)
                p2 += 1

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 