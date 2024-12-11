# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
from functools import lru_cache


def main():
    # # # # # # # # # # # # # # # # # # # #
    # --- Day 11: Plutonian Pebbles  ---  #
    # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """125 17"""

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=11, year=2024)

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    stones = aoc_input.split()
    
    for s in stones:
        p1 += calc_stone(int(s), 25)
        
    for s in stones:
        p2 += calc_stone(int(s), 75)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

@lru_cache(maxsize=None)
def calc_stone(stone, steps_left):
    if not steps_left:
        return 1
    if stone == 0:
        return calc_stone(1, steps_left - 1)
    if len(str(stone)) % 2 == 0:
        ans = calc_stone(int(str(stone)[:len(str(stone))//2]), steps_left - 1)
        ans += calc_stone(int(str(stone)[len(str(stone))//2:]), steps_left - 1)
        return ans
    else:
        return calc_stone(stone * 2024, steps_left - 1)

if __name__ == '__main__':
    main()
