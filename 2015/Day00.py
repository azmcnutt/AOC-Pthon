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
    # --- Day  0: TBD --- #
    # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """Sample
    Data""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=0, year=2015).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 