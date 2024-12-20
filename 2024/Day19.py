# import os
# import sys
# import copy
# from pprint import pprint
from functools import cache
from aocd import get_data
# from aocd import submit
import time

patterns = []
designs = []



def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 19: Linen Layout ---  #
    # # # # # # # # # # # # # # # # #

    # A little help with part two from:
    # https://github.com/sanvirk99/adventcode/blob/main/day19.py

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=19, year=2024).splitlines()
    # 530276499894300 Too Low
    # 530276499894300

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()
    global patterns
    global designs

    p1 = 0
    p2 = 0

    for i in aoc_input:
        if not patterns:
            patterns = i.split(',')
            patterns = [item.strip() for item in patterns]
        elif i:
            designs.append(i)

    for d in designs:
        i = check_design(d)
        if i:
            p1 += 1
            p2 += i

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

@cache
def check_design(design):
    if not design:
        return 1
    global patterns
    counter = 0
    original_design = design
    for p in patterns:
        design = original_design
        if design.startswith(p):
            design = design.replace(p, '', 1)
            counter += check_design(design)
    return counter
        

if __name__ == '__main__':
    main()
 