# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import re
import time
import itertools


def main():
    # # # # # # # # # # # # # # # # # # # # # # # #
    # --- Day  15: Science for Hungry People ---  #
    # # # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".splitlines()
    # Sample Score P1: 62842880
    # Sample Score P2: 57600000

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=15, year=2015).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()
    
    p1 = 0
    p2 = 0

    ing = []
    for a in aoc_input:
        ing.append([int(num) for num in re.findall(r'-?\d+', a)])
    
    for m in tqdm(mixtures(len(ing), 100)):
        rs = 0
        c = 0
        d = 0
        f = 0
        t = 0
        cal = 0
        for x, i in enumerate(ing):
            c += i[0] * m[x]
            d += i[1] * m[x]
            f += i[2] * m[x]
            t += i[3] * m[x]
            cal += i[4] * m[x]
        if c <= 0:
            c = 0
        if d <= 0:
            d = 0
        if f <= 0:
            f = 0
        if t <= 0:
            t = 0
        rs = c * d * f * t
        if rs > p1:
            p1 = rs
        if cal == 500 and rs > p2:
            p2 = rs

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total+1):
        left = total - i
        if n-1:
            for y in mixtures(n-1, left):
                yield [i] + y
        else:
            yield [i]

if __name__ == '__main__':
    main()
 