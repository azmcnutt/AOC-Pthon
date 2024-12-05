# import os
import sys
# import copy
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

# Increase recursion limit
sys.setrecursionlimit(2500)

def main():
    # # # # # # # # # # # # # # # #
    # --- Day 5: Print Queue  --- #
    # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=5, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    rules = {}
    pages = []
    switch = False
    for line in aoc_input:
        if not switch:
            # We are still in the rules section
            if not line:
                switch = True
                continue
            x,y = line.split('|')
            if x in rules.keys():
                rules[x].append(y)
            else:
                rules[x] = [y,]
        else:
            pages.append(line.split(','))
    
    for line in pages:
        x, y = is_line_valid(line, rules)
        if x:
            p1 += y
        else:
            #print(f'y: {y}')
            p2 += y

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def is_line_valid(l, r):
    for indx,p in enumerate(l):
        if p in r.keys():
            for x in r[p]:
                if x in l[:indx]:
                    # if the line violates a rule, move the violator
                    # and run the is line valid again
                    l.pop(l.index(x))
                    l.insert(indx,x)
                    _,y = is_line_valid(l, r)
                    # once the line is valid, return the middle number
                    return [False, int(l[int((len(l) - 1)/2)]),]
    return [True, int(l[int((len(l) - 1)/2)]),]

if __name__ == '__main__':
    main()