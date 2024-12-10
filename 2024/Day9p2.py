# import os
# import sys
# import copy
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 9: Disk Fragmenter  --- #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """2333133121414131402"""
    # P1: 1928
    # P2: 2858

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=9, year=2024)

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p2 = 0
    counter = 0
    fs = []

    for indx, x in enumerate(aoc_input):
        if indx % 2 == 0:
            fs.append((counter, int(x)))
            counter += 1
        elif int(x) != 0:
            fs.append(('.',int(x)))
    counter = 0

    end_ptr = len(fs) - 1
    a = len(fs) - 1
    b = 0
    while a > 0:
        b = 0
        if fs[a][0] == '.':
            a -= 1
            continue
        while b < len(fs):
            if b >= a:
                break
            elif fs[b][0] != '.':
                b += 1
                continue
            elif fs[a][1] == fs[b][1]:
                fs[b] = fs[a]
                fs[a] = ('.',fs[a][1])
                b += 1
                break
            elif fs[a][1] < fs[b][1]:
                fs.insert(b + 1,('.',fs[b][1] - fs[a][1]))
                a += 1
                fs[b] = fs[a]
                fs[a] = ('.',fs[a][1])
                b += 1
                break
            else:
                b += 1
        a -= 1
    
    for a in fs:
        if a[0] == '.':
            counter += a[1]
        else:
            for b in range(a[1]):
                p2 += counter * a[0]
                counter += 1

    print(f'P2: {p2} in {time.time() - start_time} seconds.')




if __name__ == '__main__':
    main()