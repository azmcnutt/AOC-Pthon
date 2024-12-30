# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import math
import time


def main():
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --- Day 20: Infinite Elves and Infinite Houses ---  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = 36000000

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=0, year=2015).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    n = 0
    while not p1 or not p2:
        n += 1
        divisors = GetDivisors(n)
        if not p1:
            # print(f'House {n}: {sum(divisors) * 10}')
            if sum(divisors) * 10 >= aoc_input:
                p1 = n
        if not p2:
            if sum(d for d in divisors if n / d <= 50) * 11 >= aoc_input:
                p2 = n

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def GetDivisors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

if __name__ == '__main__':
    main()
 