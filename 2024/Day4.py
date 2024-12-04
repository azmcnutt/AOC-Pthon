# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 4: Ceres Search  ---  #
    # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()


    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=4, year=2024).splitlines()
    # Not right 2492

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    for x in range(len(aoc_input)):
        for y in range(len(aoc_input[x])):
            # Check for xmas forward
            if aoc_input[x][y:y+4] == 'XMAS':
                p1 += 1
            # Check for xmas backwards
            if aoc_input[x][y:y-4:-1] == 'XMAS':
                p1 += 1
            # Check for xmas down
            if x + 3 <= len(aoc_input) - 1:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x+1][y] == 'M' and
                    aoc_input[x+2][y] == 'A' and
                    aoc_input[x+3][y] == 'S'
                ):
                    p1 += 1
            # Check for xmas up
            if x - 3 >= 0:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x-1][y] == 'M' and
                    aoc_input[x-2][y] == 'A' and
                    aoc_input[x-3][y] == 'S'
                ):
                    p1 += 1
            # Check for xmas down to the right
            if x + 3 <= len(aoc_input) - 1 and y + 3 <= len(aoc_input[x]) - 1:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x+1][y+1] == 'M' and
                    aoc_input[x+2][y+2] == 'A' and
                    aoc_input[x+3][y+3] == 'S'
                ):
                    p1 += 1
            # Check for xmas down to the left
            if x + 3 <= len(aoc_input) - 1 and y - 3 >= 0:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x+1][y-1] == 'M' and
                    aoc_input[x+2][y-2] == 'A' and
                    aoc_input[x+3][y-3] == 'S'
                ):
                    p1 += 1
            # Check for xmas up to the right
            if x - 3 >= 0 and y + 3 <= len(aoc_input[x]) - 1:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x-1][y+1] == 'M' and
                    aoc_input[x-2][y+2] == 'A' and
                    aoc_input[x-3][y+3] == 'S'
                ):
                    p1 += 1
            # Check for xmas up to the left
            if x - 3 >= 0 and y - 3 >= 0:
                if (aoc_input[x][y] == 'X' and
                    aoc_input[x-1][y-1] == 'M' and
                    aoc_input[x-2][y-2] == 'A' and
                    aoc_input[x-3][y-3] == 'S'
                ):
                    p1 += 1


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()