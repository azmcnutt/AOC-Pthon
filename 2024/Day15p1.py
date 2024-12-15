# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

# load sample data, copied and pasted from the site into list.
# Each list item is one line of input
aoc_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".splitlines()
# 10092

#Smaller Test Input 
# aoc_input = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<""".splitlines()
# 2028

r = []
moves = []
walls = set()
boxes = []
dirs = {
    '^': [0, -1],
    '>': [1, 0],
    'v': [0, 1],
    '<': [-1, 0],
}

# once the test data provides the right answer:
# replace test data with data from the puzzle input
aoc_input = get_data(day=15, year=2024).splitlines()

def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 15: Warehouse Woes  --- #
    # # # # # # # # # # # # # # # # # #

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0

    for iy, y in enumerate(aoc_input):
        for ix, x in enumerate(y):
            if x == '#':
                walls.add((ix, iy))
            elif x == 'O':
                boxes.append((ix, iy))
            elif x == '@':
                r.append(ix)
                r.append(iy)
            elif x in dirs.keys():
                moves.append(x)
    
    while moves:
        m = moves.pop(0)
        if safe_to_move(r[0], r[1], m):
            move_it(r[0], r[1], m, 'r')
    
    for b in boxes:
        p1 += (b[1] * 100) + b[0]
        


    print(f'P1: {p1} in {time.time() - start_time} seconds.')

def safe_to_move(x, y, d):
    dx = x + dirs[d][0]
    dy = y + dirs[d][1]
    if (dx,dy) in walls:
        return False
    if (dx, dy) in boxes:
        return safe_to_move(dx, dy, d)
    return True

def move_it(x, y, d, t = 'b'):
    # if t = 'b' then we are moving a box
    dx = x + dirs[d][0]
    dy = y + dirs[d][1]
    if (dx, dy) in boxes:
        move_it(dx, dy, d)
    if t =='b':
        i = boxes.index((x, y))
        boxes[i] = ((dx, dy))
    elif t == 'r':
        r[0] = dx
        r[1] = dy


if __name__ == '__main__':
    main()
 