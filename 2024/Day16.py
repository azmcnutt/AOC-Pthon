# import os
import sys
import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

sys.setrecursionlimit(6000)

walls = set()
maze = set()
paths = []
max_x = 0
max_y = 0
dirs = {
    (-1,0): [(-1,0),(0,-1),(0,1)],
    (1,0): [(1,0),(0,-1),(0,1)],
    (0,-1): [(0,-1),(1,0),(-1,0)],
    (0,1): [(0,1),(1,0),(-1,0)],
}
best_score = 0
path = {}


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 16: Reindeer Maze --- #
    # # # # # # # # # # # # # # # # #

    # Some code ideas from:
    # https://www.reddit.com/r/adventofcode/comments/1hfibxy/2024_day_16_help_pls/


    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()
    # 7036

    aoc_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()
    # 11048

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=16, year=2024).splitlines()
    # 328104 Too high

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    global max_x
    global max_y
    global path
    max_x = len(aoc_input[0])
    max_y = len(aoc_input)
    initial_dir = (1,0)
    

    for iy, y in enumerate(aoc_input):
        for ix, x in enumerate(y):
            path[(ix, iy)] = int(10e9)
            if x == '.':
                maze.add((ix, iy))
            elif x == '#':
                walls.add((ix, iy))
            elif x == 'S':
                maze.add((ix, iy))
                start = (ix, iy)
            elif x == 'E':
                maze.add((ix, iy))
                end = (ix, iy)

    p1 = find_trail(start, initial_dir, 0, set(), end)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def find_trail(pos, cur_dir, score, visited, end):
    global path

    if pos == end:
        path[pos] = min(path[pos],score)
        print(score)
        return path[end]
    
    if pos in visited:
        if path[pos] <= score:
            return path[end]
        path[pos] = score
    else:
        visited.add(pos)
        path[pos] = score

    for d in dirs[cur_dir]:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        s = score
        if cur_dir == d:
            s += 1
        else:
            s += 1001
        if next_pos in maze:
            new_visited = copy.deepcopy(visited)
            find_trail(next_pos,d,s,new_visited, end)
    return path[end]

if __name__ == '__main__':
    main()
 