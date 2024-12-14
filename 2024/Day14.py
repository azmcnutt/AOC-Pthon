# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import re


def main():
    # # # # # # # # # # # # # # # # # # #
    # --- Day 14: Restroom Redoubt ---  #
    # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()
    max_x, max_y = [11,7]

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=14, year=2024).splitlines()
    max_x, max_y = [101,103]

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    seconds = 100
    robots = []
    gq1 = [0, 0, (max_x - 1) / 2 - 1, (max_y - 1) / 2 - 1]
    gq2 = [(max_x + 1) / 2, 0, max_x - 1, (max_y - 1) / 2 - 1]
    gq3 = [0, (max_y + 1) / 2, (max_x - 1) / 2 - 1, max_y - 1]
    gq4 = [(max_x + 1) / 2, (max_y + 1) / 2, max_x - 1, max_y - 1]
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    

    for line in aoc_input:
        line = line.replace('p=', '')
        line = line.replace('v=', '')
        p, v = line.split(' ')
        p = [int(d) for d in p.split(',')]
        v = [int(d) for d in v.split(',')]
        robots.append([p, v,])
    

    
    for r in robots:
        p = move_robot(r, seconds, max_x, max_y)
        if (gq1[0] <= p[0] <= gq1[2] and gq1[1] <= p[1] <= gq1[3]):
            q1.append(p)
        elif (gq2[0] <= p[0] <= gq2[2] and gq2[1] <= p[1] <= gq2[3]):
            q2.append(p)
        elif (gq3[0] <= p[0] <= gq3[2] and gq3[1] <= p[1] <= gq3[3]):
            q3.append(p)
        elif (gq4[0] <= p[0] <= gq4[2] and gq4[1] <= p[1] <= gq4[3]):
            q4.append(p)
    
    # hacky solution for part 2 thanks to a tip from Phaul on Club TWiT Discord
    # If none of the points overlap, assume its a tree
    while True:
        p2 += 1
        tree = []
        for r in robots:
            p = move_robot(r, p2, max_x, max_y)
            if p in tree:
                break
            else:
                tree.append(p)
        if len(tree) == len(aoc_input):
            break

    
    p1 = len(q1) * len(q2) * len(q3) * len(q4)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def move_robot(r, s, mx, my):
    p_x, p_y = r[0]
    v_x, v_y = r[1]
    p_x += v_x * s
    p_y += v_y * s
    f_x = p_x % mx
    f_y = p_y % my
    return [f_x, f_y]

    

if __name__ == '__main__':
    main()
 