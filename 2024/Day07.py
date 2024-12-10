# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 7: Bridge Repair  --- #
    # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=7, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    
    for l in aoc_input:
        t,n = l.split(':')
        t = int(t)
        n = n.split()
        n = [int(item) for item in n]
        if test_equation(0, n, 0, t, 1):
            p1 += t
        if test_equation(0, n, 0, t, 2):
            p2 += t

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def test_equation(indx, nums, val, test, p):
    operations = ['+', '*',]
    if p == 2:
        operations.append('||')
    if indx == len(nums) and val == test:
        return True
    elif indx == len(nums):
        return False
    
    for o in operations:
        if o == '+':
            x = test_equation(indx + 1, nums, val + nums[indx], test, p)
            if x:
                return True
        if o == '*':
            x = test_equation(indx + 1, nums, val * nums[indx], test, p)
            if x:
                return True
    if o == '||':
            x = test_equation(indx + 1, nums, int(str(val) + str(nums[indx])), test, p)
            if x:
                return True
    return False

if __name__ == '__main__':
    main()