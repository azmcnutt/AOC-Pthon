# import os
# import sys
# import copy
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # # # # #
    # --- Day 8: Resonant Collinearity  --- #
    # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=8, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    max_x = len(aoc_input)
    max_y = len(aoc_input[0])

    antenna_map = {}
    antinodes_p1 = set()
    antinodes_p2 = set()

    for indx, x in enumerate(aoc_input):
        for indy, y in enumerate(x):
            if y != '.':
                if y in antenna_map.keys():
                    antenna_map[y].add((indx,indy))
                else:
                    antenna_map[y] = set()
                    antenna_map[y].add((indx,indy))
    
    for ant in antenna_map:
        z = get_antinodes_p1(antenna_map[ant], max_x, max_y)
        if z and isinstance(z, set):
            antinodes_p1.update(z)
        z = get_antinodes_p2(antenna_map[ant], max_x, max_y)
        if z and isinstance(z, set):
            antinodes_p2.update(z)

    p1 = len(antinodes_p1)
    p2 = len(antinodes_p2)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def get_antinodes_p2(ant, max_x, max_y):
    anti_nodes = set()
    for a in ant:
        for b in ant:
            if a != b:
                x1 = a[0] - b[0]
                y1 = a[1] - b[1]
                x2 = x1 * -1
                y2 = y1 * -1

                an_x = a[0] + x1
                an_y = a[1] + y1

                while (an_x >= 0 and an_x < max_x and
                       an_y >= 0 and an_y < max_y):
                    anti_nodes.add((an_x, an_y))
                    an_x += x1
                    an_y += y1
                
                an_x = a[0] + x2
                an_y = a[1] + y2

                while (an_x >= 0 and an_x < max_x and
                       an_y >= 0 and an_y < max_y):
                    anti_nodes.add((an_x, an_y))
                    an_x += x2
                    an_y += y2
    return anti_nodes

def get_antinodes_p1(ant, max_x, max_y):
    anti_nodes = set()
    for a in ant:
        for b in ant:
            if a != b:
                x1 = a[0] - b[0]
                y1 = a[1] - b[1]
                x2 = x1 * -1
                y2 = y1 * -1
                anti_node_1 = (a[0] + x1, a[1] + y1)
                anti_node_2 = (b[0] + x2, b[1] + y2)
                if (anti_node_1[0] >= 0 and
                    anti_node_1[0] < max_x and
                    anti_node_1[1] >= 0 and
                    anti_node_1[1] < max_y):
                    anti_nodes.add(anti_node_1)
                if (anti_node_2[0] >= 0 and
                    anti_node_2[0] < max_x and
                    anti_node_2[1] >= 0 and
                    anti_node_2[1] < max_y):
                    anti_nodes.add(anti_node_2)
    return anti_nodes



if __name__ == '__main__':
    main()