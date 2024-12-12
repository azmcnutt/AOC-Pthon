# import os
# import sys
# import copy
from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

dirs=[(-1,0),(0,1),(1,0),(0,-1)]

def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 12: Garden Groups --- #
    # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """AAAA
BBCD
BBCC
EEEC""".splitlines()
    # 140

    aoc_input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""".splitlines()
    # 368

#     aoc_input = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO""".splitlines()
    # 772
    
    
    aoc_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()
    # 1930

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=12, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    gardens = {}

    for x, a in enumerate(aoc_input):
        for y, b in enumerate(a):
            if b in gardens.keys():
                gardens[b].append((x,y))
            else:
                gardens[b] = [(x,y)]

    # group(gardens['I'])

    for k, v in gardens.items():
        groups = group(v)
        for g in groups:
            # print(f'G {k}: {calc_garden_p1(g)}')
            # print(k)
            one, two = calc_garden_p1(g)
            p1 += one
            p2 += two


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def calc_garden_p1(garden):
    area = 0
    perimeter = 0
    sides = 0

    for z in range(len(garden) - 1):
        pass

    for g in garden:
        area += 1
        for d in dirs:
            t = (g[0]+d[0],g[1]+d[1])
            if t not in garden:
                perimeter += 1
            
        # trying to count sides/corners
        # top left corner:
        if ((g[0] - 1,g[1]) not in garden and
            (g[0], g[1] - 1) not in garden and
            (g[0], g[1] + 1) in garden and
            (g[0] +1, g[1]) in garden
        ):
            sides += 1
        # top right corner
        elif ((g[0] - 1,g[1]) not in garden and
            (g[0], g[1] - 1) in garden and
            (g[0], g[1] + 1) not in garden and
            (g[0] +1, g[1]) in garden
        ):
            sides += 1
        # bot left corner:
        elif ((g[0] - 1,g[1]) in garden and
            (g[0], g[1] - 1) not in garden and
            (g[0], g[1] + 1) in garden and
            (g[0] +1, g[1]) not in garden
        ):
            sides += 1
        # bot right corner
        elif ((g[0] - 1,g[1]) in garden and
            (g[0], g[1] - 1) in garden and
            (g[0], g[1] + 1) not in garden and
            (g[0] +1, g[1]) not in garden
        ):
            sides += 1
        # single
        elif len(garden) == 1:
            sides = 4
        # right end
        elif ((g[0] - 1,g[1]) not in garden and
            (g[0], g[1] - 1) in garden and
            (g[0], g[1] + 1) not in garden and
            (g[0] +1, g[1]) not in garden
        ):
            sides += 2
        # left end
        elif ((g[0] - 1,g[1]) not in garden and
            (g[0], g[1] - 1) not in garden and
            (g[0], g[1] + 1) in garden and
            (g[0] +1, g[1]) not in garden
        ):
            sides += 2
        # up end
        elif ((g[0] - 1,g[1]) not in garden and
            (g[0], g[1] - 1) not in garden and
            (g[0], g[1] + 1) not in garden and
            (g[0] +1, g[1]) in garden
        ):
            sides += 2
        # down end
        elif ((g[0] - 1,g[1]) in garden and
            (g[0], g[1] - 1) not in garden and
            (g[0], g[1] + 1) not in garden and
            (g[0] +1, g[1]) not in garden
        ):
            sides += 2
        # top left inside corner:
        if ((g[0], g[1] + 1) in garden and
            (g[0] +1, g[1]) in garden and
            (g[0] +1, g[1] + 1) not in garden
        ):
            sides += 1
        # top right inside corner
        if ((g[0], g[1] - 1) in garden and
            (g[0] +1, g[1]) in garden and
            (g[0] +1, g[1] - 1) not in garden
        ):
            sides += 1
        # bot left inside corner:
        if ((g[0], g[1] + 1) in garden and
            (g[0] -1, g[1]) in garden and
            (g[0] -1, g[1] + 1) not in garden
        ):
            sides += 1
        # bot right inside corner
        if ((g[0], g[1] - 1) in garden and
            (g[0] -1, g[1]) in garden and
            (g[0] -1, g[1] - 1) not in garden
        ):
            sides += 1
        
        # # Up U:
        # if ((g[0] - 1, g[1]) not in garden and
        #     (g[0], g[1] - 1) in garden and
        #     (g[0], g[1] + 1) in garden and
        #     (g[0] - 1, g[1] - 1) in garden and
        #     (g[0] - 1, g[1] + 1) in garden
        # ):
        #     sides += 1
        # # Right U
        # elif ((g[0], g[1] + 1) not in garden and
        #     (g[0] - 1, g[1]) in garden and
        #     (g[0] + 1, g[1]) in garden and
        #     (g[0] - 1, g[1] + 1) in garden and
        #     (g[0] + 1, g[1] + 1) in garden
        # ):
        #     sides += 1
        # # Down U:
        # if ((g[0] + 1, g[1]) not in garden and
        #     (g[0], g[1] - 1) in garden and
        #     (g[0], g[1] + 1) in garden and
        #     (g[0] + 1, g[1] - 1) in garden and
        #     (g[0] + 1, g[1] + 1) in garden
        # ):
        #     sides += 1
        #  # Left U
        # elif ((g[0], g[1] - 1) not in garden and
        #     (g[0] - 1, g[1]) in garden and
        #     (g[0] + 1, g[1]) in garden and
        #     (g[0] - 1, g[1] - 1) in garden and
        #     (g[0] + 1, g[1] - 1) in garden
        # ):
        #     sides += 1
            
    # print(area, sides)

    return [area * perimeter, area * sides]

def group(points):
    groups = []
    searched = set()
    def find_group(start):
        if start in searched:
            return
        searched.add(start)
        for d in dirs:
            if (start[0]+d[0],start[1] + d[1]) in points:
                find_group((start[0]+d[0],start[1] + d[1]))
    
    while points:
        find_group(points[0])
        groups.append(list(searched))
        points = [x for x in points if x not in list(searched)]
        searched = set()
    return groups

if __name__ == '__main__':
    main()
