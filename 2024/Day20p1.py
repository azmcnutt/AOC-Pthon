# import os
# import sys
import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import heapq


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 20: Race Condition ---  #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=20, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    maze = set()
    max_x = len(aoc_input[0])
    max_y = len(aoc_input)
    no_cheat = 0
    for iy, y in enumerate(aoc_input):
        for ix, x in enumerate(y):
            if x == '#':
                maze.add((ix, iy))
            elif x == 'S':
                start = (ix, iy)
            elif x == 'E':
                end = (ix, iy)

    no_cheat = len(a_star(maze, start, end, max_x, max_y))
    print(no_cheat)
    for i in maze:
        cheat_maze = copy.deepcopy(maze)
        cheat_maze.remove(i)
        cheat_time = len(a_star(cheat_maze, start, end, max_x, max_y))
        if cheat_time <= no_cheat - 100:
            p1 += 1
            # 44

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end, mx, my):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x <= mx and 0 <= y <= my and (x, y) not in maze:
                tentative_g_score = g_score[current] + 1
                if (x, y) not in g_score or tentative_g_score < g_score[(x, y)]:
                    came_from[(x, y)] = current
                    g_score[(x, y)] = tentative_g_score
                    f_score[(x, y)] = tentative_g_score + heuristic((x, y), end)
                    heapq.heappush(open_set, (f_score[(x, y)], (x, y)))

    return None

if __name__ == '__main__':
    main()
 