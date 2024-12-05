# import os
# import sys
# import copy
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # #
    # --- Day 5: TBD  --- #
    # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """Sample
    Data""".splitlines()


    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=5, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    rules = {}
    pages = []
    switch = False
    for line in aoc_input:
        if not switch:
            # We are still in the rules section
            if not line:
                switch = True
                continue
            x,y = line.split('|')
            if x in rules.keys():
                rules[x].append(y)
            else:
                rules[x] = [y,]
        else:
            pages.append(line.split(','))
    
    pprint(rules)
    print()
    pprint(pages)


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()