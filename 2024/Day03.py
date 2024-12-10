# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import re


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 3: Mull It Over  ---  #
    # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # added some extra stuff for edge case testing for part 2
    # Each list item is one line of input
    aoc_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()shouldn\notbeheredo()shouldbeheredon't()stillnothere"""


    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=3, year=2024)

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    aoc_input = re.sub('\n|\r', '', aoc_input)

    # Used regex tester at https://regex101.com/
    patternp1 = r"(mul\(\d+,\d+\))" # returns all valid muls
    patternp2 = r"(don\'t\(\).*?do\(\))" # removes everything between don't() and do()
    # However patternp2 will leave the last don't() to the end of the string
    # see below for the hack to remove the last chunk of don'ts

    # Probably a more efficient way to perform the two regex's and multiplications

    mulsp1 = re.findall(patternp1, aoc_input)
    for m in mulsp1:
        # remove mul( amd ) and return a list with the two numbers
        m = m.replace('mul(','').replace(')','').split(',')
        p1 += int(m[0]) * int(m[1])
    
    mulsp2 = re.sub(patternp2, '', aoc_input)

    # A hacky way to get rid of everything after the last don't()
    mulsp2 = mulsp2[:mulsp2.rfind('don\'t()')]

    mulsp2 = re.findall(patternp1, mulsp2)
    for m in mulsp2:
        # remove mul( amd ) and return a list with the two numbers
        m = m.replace('mul(','').replace(')','').split(',')
        p2 += int(m[0]) * int(m[1])

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()