import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc
import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 2: Cube Conundrum  ---                                                                                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=2, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()

# Let's get the organized. Each record in the dict, will contain an index with the game ID and a list of lists wtih
# each draw with the digits representing the number of Red, Green, and Blue
games = {}
for x in myset:
    rgb=[]
    game_id, draws = x.split(':')
    game_id = re.search(r'\d+', game_id).group()
    draws = draws.strip().split(';')
    for d in draws:
        red = 0
        green = 0
        blue = 0
        all_cubes = d.strip().split(', ')
        for c in all_cubes:
            cube = c.split(' ')
            if cube[1] == 'red':
                red = int(cube[0])
            if cube[1] == 'green':
                green = int(cube[0])
            if cube[1] == 'blue':
                blue = int(cube[0])
        rgb.append([red, green, blue])
    games[game_id] = rgb
# pprint(games)


max_red = 12
max_green = 13
max_blue = 14
possible_game_id_total = 0
total_cube_power = 0
for g, d in games.items():
    min_red = 0
    min_green = 0
    min_blue = 0
    game_possible = True
    for _ in d:
        if _[0] > max_red:
            # print(f'Game: {g} Impossible Red: {_[0]} is greater than {max_red}')
            game_possible = False
        elif _[1] > max_green:
            # print(f'Game: {g} Impossible Green: {_[1]} is greater than {max_green}')
            game_possible = False
        elif _[2] > max_blue:
            # print(f'Game: {g} Impossible Green: {_[2]} is greater than {max_blue}')
            game_possible = False
        if _[0] > min_red:
            min_red = _[0]
        if _[1] > min_green:
            min_green = _[1]
        if _[2] > min_blue:
            min_blue = _[2]
    if game_possible:
        possible_game_id_total += int(g)
    total_cube_power += (min_red * min_blue * min_green)



print(f'P1: {possible_game_id_total} and P2: {total_cube_power} in {time.time() - start_time} seconds.')
