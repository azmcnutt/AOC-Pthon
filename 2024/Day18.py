# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import heapq


def main():
    # # # # # # # # # # # # # #
    # --- Day 18: RAM Run --- #
    # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=18, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    start = (0,0)
    initial_range = 1024
    end = (70, 70)
    # initial_range = 12
    # end = (6, 6)

    maze = set()

    for i in range(initial_range):
        loc = aoc_input.pop(0)
        loc = loc.split(',')
        maze.add((int(loc[0]), int(loc[1])))
    
    p1 = len(a_star(maze, start, end))

    while not p2:
        loc = aoc_input.pop(0)
        loc = loc.split(',')
        maze.add((int(loc[0]), int(loc[1])))
        if not a_star(maze, start, end):
            p2 = f'{loc[0]},{loc[1]}'
        
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
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
            if 0 <= x <= end[0] and 0 <= y <= end[1] and (x, y) not in maze:
                tentative_g_score = g_score[current] + 1
                if (x, y) not in g_score or tentative_g_score < g_score[(x, y)]:
                    came_from[(x, y)] = current
                    g_score[(x, y)] = tentative_g_score
                    f_score[(x, y)] = tentative_g_score + heuristic((x, y), end)
                    heapq.heappush(open_set, (f_score[(x, y)], (x, y)))

    return None

if __name__ == '__main__':
    main()
 