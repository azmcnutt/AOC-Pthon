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

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    letter_x = []
    letter_m = []
    letter_a = []
    letter_s = []

    # build a table of XMAS locations:
    for x, row in enumerate(aoc_input):
        for y, letter in enumerate(row):
            if letter == 'X':
                letter_x.append((x,y))
            elif letter == 'M':
                letter_m.append((x,y))
            elif letter == 'A':
                letter_a.append((x,y))
            elif letter == 'S':
                letter_s.append((x,y))
            else:
                print('didnt match')

    dirs = [
        (1,1),
        (0,1),
        (1,0),
        (-1,1),
        (1,-1),
        (-1,0),
        (0,-1),
        (-1,-1),
    ]
    mas_dirs = [
        [
            [(-1,-1),(1,1)],
            [(-1,1),(1,-1)]
        ],[
            [(-1,-1),(1,1)],
            [(1,-1),(-1,1)]
        ],[
            [(-1,1),(1,-1)],
            [(1,1),(-1,-1)]
        ],[
            [(1,-1),(-1,1)],
            [(1,1),(-1,-1)]
        ],
    ]

    for z in letter_x:
        x = z[0]
        y = z[1]
        for d in dirs:
            if (((x + d[0]),(y + d[1])) in letter_m and
                ((x + (d[0] * 2)),(y + (d[1] * 2))) in letter_a and
                ((x + (d[0] * 3)),(y + (d[1] * 3))) in letter_s
            ):
                p1 += 1
    
    for z in letter_a:
        x = z[0]
        y = z[1]
        for d in mas_dirs:
            m1 = (x + d[0][0][0],y + d[0][0][1])
            s1 = (x + d[0][1][0],y + d[0][1][1])
            m2 = (x + d[1][0][0],y + d[1][0][1])
            s2 = (x + d[1][1][0],y + d[1][1][1])
            
            
            if (m1 in letter_m and m2 in letter_m and
                s1 in letter_s and s2 in letter_s
            ):
                p2 += 1

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()