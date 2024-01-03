import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 5: If You Give A Seed A Fertilizer  ---                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=5, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()

# Let's get the organized. Each record in the dict, will contain an index with the game ID and a list of lists wtih
# each draw with the digits representing the number of Red, Green, and Blue
seeds = []
seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temperature = []
temperature_humidity = []
humidity_location = []
mapped_seeds = []

temp = myset[0].split(': ')
seeds = temp[1].split()
seeds = [int(i.strip()) for i in seeds]
x = 3 # Seed to soil map start
for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # soil to fertilizer map start
        break
    seed_soil.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # fertilizer to water map start
        break
    soil_fertilizer.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # water to light map start
        break
    fertilizer_water.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # light to temp map start
        break
    water_light.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # temp to humidity map start
        break
    light_temperature.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        x = y + 2  # humidity to map start
        break
    temperature_humidity.append([int(i.strip()) for i in myset[y].split()])

for y in range(x, len(myset)):
    if not myset[y]:
        break
    humidity_location.append([int(i.strip()) for i in myset[y].split()])

# print(seeds)
# print(seed_soil)
# print(soil_fertilizer)
# print(fertilizer_water)
# print(water_light)
# print(light_temperature)
# print(temperature_humidity)
# print(humidity_location)
p1ans = 0

@lru_cache()
def map_the_seed(s):
    # first map the seed to soil
    # let the soil = the seed in case there is no match
    soil = s
    for ss in seed_soil:
        if ss[1] <= s < (ss[1] + ss[2]):
            soil = s + ss[0] - ss[1]
    fert = soil
    for sf in soil_fertilizer:
        if sf[1] <= soil < (sf[1] + sf[2]):
            fert = soil + sf[0] - sf[1]
    wat = fert
    for fw in fertilizer_water:
        if fw[1] <= fert < (fw[1] + fw[2]):
            wat = fert + fw[0] - fw[1]
    lig = wat
    for wl in water_light:
        if wl[1] <= wat < (wl[1] + wl[2]):
            lig = wat + wl[0] - wl[1]
    temp = lig
    for lt in light_temperature:
        if lt[1] <= lig < (lt[1] + lt[2]):
            temp = lig + lt[0] - lt[1]
    hum = temp
    for th in temperature_humidity:
        if th[1] <= temp < (th[1] + th[2]):
            hum = temp + th[0] - th[1]
    loc = hum
    for hl in humidity_location:
        if hl[1] <= hum < (hl[1] + hl[2]):
            loc = hum + hl[0] - hl[1]
    # print(s, soil, fert, wat, lig, temp, hum, loc)
    return loc


for s in seeds:
    location = map_the_seed(s)
    if 0 == p1ans or p1ans > location:
        p1ans = location
x = 0
p2ans = 0
while x < len(seeds):
    for y in range(seeds[0], seeds[0] + seeds[1]):
        location = map_the_seed(y)
        if 0 == p2ans or p2ans > location:
            p2ans = location
    x += 2



print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
