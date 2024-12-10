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

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=9, year=2024)

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    data_map = {}
    data_index = 0

    for indx, x in enumerate(aoc_input):
        if indx % 2 == 0:
            data_map[data_index] = int(x)
            data_index += 1
        
    # pprint(data_map)
    data_index = 0
    for indx, x in enumerate(aoc_input):
        x = int(x)
        if indx % 2 == 0:
            #print(f'Index: {indx} - Number: {x}')
            for _ in range(x):
                # print(f'{p1} += {data_index} * {indx}')
                # p1 += data_index * indx
                # data_index += 1
                # print(f'{p1} += {data_index} * {list(data_map.keys())[0]}')
                p1 += data_index * list(data_map.keys())[0]
                data_index += 1
            del data_map[list(data_map.keys())[0]]
            if not data_map:
                break
        else:
            if not data_map:
                break
            if len(data_map) == 1:
                for _ in range(data_map[list(data_map.keys())[-1]]):
                    # print(f'{p1} += {data_index} * {list(data_map.keys())[-1]}')
                    p1 += data_index * list(data_map.keys())[-1]
                    data_index += 1
                del data_map[list(data_map.keys())[-1]]
                break
            for _ in range(x):
                z = 0
                while z == 0:
                    if data_map[list(data_map.keys())[-1]] <= 0:
                        del data_map[list(data_map.keys())[-1]]
                    else:
                        z = list(data_map.keys())[-1]
                        data_map[list(data_map.keys())[-1]] -= 1
                # print(f'{p1} += {data_index} * {z}')
                p1 += data_index * z
                data_index += 1
                if not data_map:
                    break  


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')




if __name__ == '__main__':
    main()