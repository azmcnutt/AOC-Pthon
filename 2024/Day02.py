# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # # #
    # --- Day 2: Red-Nosed Reports  --- #
    # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9""".splitlines()


    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=2, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    for report in aoc_input:
        if is_report_safe(report.split()):
            p1 += 1
            p2 += 1
        else:
            # This report is not safe with dampening, lets see if it
            # is safe with dampening
            if is_report_safe(report.split(), True):
                p2 += 1
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def is_report_safe(r: list, d: bool = False) -> bool:
    """Returns true if a provided report is safe.
    r: a list of numbers to process as the report
    d: a True/False to allow report dampening.
        False does not permit one unsafe condition
        True will allow one unsafe condition.
    """

    # r = r.split()
    r = [int(item) for item in r]
    # first lets determine if we are increasing or decreasing
    if r[1] > r[0]:
        direction = -1
    else:
        direction = 1
    for x in range(len(r) - 1):
        if (r[x] != (r[x+1] + (1 * direction))
            and r[x] != (r[x+1] + (2 * direction))
            and r[x] != (r[x+1] + (3 * direction))
        ):
            if d:
                # Report is not safe, but we can check to see if 
                # dampening helps
                # Eliminate Current Level
                if is_report_safe(r[:x] + r[x+1:]):
                    return True
                # Eliminate Next Level
                elif is_report_safe(r[:x+1] + r[x+2:]):
                    return True
                # Eliminate Previous Level
                elif is_report_safe(r[:x-1] + r[x:]):
                    return True
                else:
                    return False
            else:
                return False
    return True

if __name__ == '__main__':
    main()