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
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that #
# looks more to you like a farm.                                                                                #
#                                                                                                               #
# "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any       #
# water.                                                                                                        #
#                                                                                                               #
# "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. #
# Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no."   #
# His face sinks into a look of horrified realization.                                                          #
#                                                                                                               #
# "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped        #
# getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than #
# your boat. Could you please go check it out?"                                                                 #
#                                                                                                               #
# You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe #
# you can help us with our food production problem. The latest Island Island Almanac just arrived and we're     #
# having trouble making sense of it."                                                                           #
#                                                                                                               #
# The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of    #
# soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of       #
# water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is       #
# identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123      #
# aren't necessarily related to each other.                                                                     #
#                                                                                                               #
# For example:                                                                                                  #
#                                                                                                               #
# seeds: 79 14 55 13                                                                                            #
#                                                                                                               #
# seed-to-soil map:                                                                                             #
# 50 98 2                                                                                                       #
# 52 50 48                                                                                                      #
#                                                                                                               #
# soil-to-fertilizer map:                                                                                       #
# 0 15 37                                                                                                       #
# 37 52 2                                                                                                       #
# 39 0 15                                                                                                       #
#                                                                                                               #
# fertilizer-to-water map:                                                                                      #
# 49 53 8                                                                                                       #
# 0 11 42                                                                                                       #
# 42 0 7                                                                                                        #
# 57 7 4                                                                                                        #
#                                                                                                               #
# water-to-light map:                                                                                           #
# 88 18 7                                                                                                       #
# 18 25 70                                                                                                      #
#                                                                                                               #
# light-to-temperature map:                                                                                     #
# 45 77 23                                                                                                      #
# 81 45 19                                                                                                      #
# 68 64 13                                                                                                      #
#                                                                                                               #
# temperature-to-humidity map:                                                                                  #
# 0 69 1                                                                                                        #
# 1 0 69                                                                                                        #
#                                                                                                               #
# humidity-to-location map:                                                                                     #
# 60 56 37                                                                                                      #
# 56 93 4                                                                                                       #
# The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.                       #
#                                                                                                               #
# The rest of the almanac contains a list of maps which describe how to convert numbers from a source category  #
# into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how #
# to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team #
# know which soil to use with which seeds, which water to use with which fertilizer, and so on.                 #
#                                                                                                               #
# Rather than list every source number and its corresponding destination number one by one, the maps describe   #
# entire ranges of numbers that can be converted. Each line within a map contains three numbers: the            #
# destination range start, the source range start, and the range length.                                        #
#                                                                                                               #
# Consider again the example seed-to-soil map:                                                                  #
#                                                                                                               #
# 50 98 2                                                                                                       #
# 52 50 48                                                                                                      #
# The first line has a destination range start of 50, a source range start of 98, and a range length of 2.      #
# This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range  #
# is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know     #
# that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.      #
#                                                                                                               #
# The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This    #
# corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So,     #
# seed number 53 corresponds to soil number 55.                                                                 #
#                                                                                                               #
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10           #
# corresponds to soil number 10.                                                                                #
#                                                                                                               #
# So, the entire list of seed numbers and their corresponding soil numbers looks like this:                     #
#                                                                                                               #
# seed  soil                                                                                                    #
# 0     0                                                                                                       #
# 1     1                                                                                                       #
# ...   ...                                                                                                     #
# 48    48                                                                                                      #
# 49    49                                                                                                      #
# 50    52                                                                                                      #
# 51    53                                                                                                      #
# ...   ...                                                                                                     #
# 96    98                                                                                                      #
# 97    99                                                                                                      #
# 98    50                                                                                                      #
# 99    51                                                                                                      #
# With this map, you can look up the soil number required for each initial seed number:                         #
#                                                                                                               #
# Seed number 79 corresponds to soil number 81.                                                                 #
# Seed number 14 corresponds to soil number 14.                                                                 #
# Seed number 55 corresponds to soil number 57.                                                                 #
# Seed number 13 corresponds to soil number 13.                                                                 #
# The gardener and his team want to get started as soon as possible, so they'd like to know the closest         #
# location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the  #
# initial seeds. To do this, you'll need to convert each seed number through other categories until you can     #
# find its corresponding location number. In this example, the corresponding types are:                         #
#                                                                                                               #
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.                #
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.                #
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.                #
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.                #
# So, the lowest location number in this example is 35.                                                         #
#                                                                                                               #
# What is the lowest location number that corresponds to any of the initial seed numbers?                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like    #
# the seeds: line actually describes ranges of seed numbers.                                                    #
#                                                                                                               #
# The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the    #
# range and the second value is the length of the range. So, in the first line of the example above:            #
#                                                                                                               #
# seeds: 79 14 55 13                                                                                            #
# This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed  #
# number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and        #
# contains 13 values: 55, 56, ..., 66, 67.                                                                      #
#                                                                                                               #
# Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.              #
#                                                                                                               #
# In the above example, the lowest location number can be obtained from seed number 82, which corresponds to    #
# soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest      #
# location number is 46.                                                                                        #
#                                                                                                               #
# Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the   #
# lowest location number that corresponds to any of the initial seed numbers?                                   #
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


def map_the_loc(l):
    hum = l
    for hl in humidity_location:
        if hl[0] <= l < (hl[0] + hl[2]):
            hum = l + hl[1] - hl[0]
    temp = hum
    for th in temperature_humidity:
        if th[0] <= hum < (th[0] + th[2]):
            temp = hum + th[1] - th[0]
    lig = temp
    for lt in light_temperature:
        if lt[0] <= temp < (lt[0] + lt[2]):
            lig = temp + lt[1] - lt[0]
    wat = lig
    for wl in water_light:
        if wl[0] <= lig < (wl[0] + wl[2]):
            wat = lig + wl[1] - wl[0]
    fert = wat
    for fw in fertilizer_water:
        if fw[0] <= wat < (fw[0] + fw[2]):
            fert = wat + fw[1] - fw[0]
    soil = fert
    for sf in soil_fertilizer:
        if sf[0] <= fert < (sf[0] + sf[2]):
            soil = fert + sf[1] - sf[0]
    seed = soil
    for ss in seed_soil:
        if ss[0] <= soil < (ss[0] + ss[2]):
            seed = soil + ss[1] - ss[0]
    return seed


for s in seeds:
    location = map_the_seed(s)

    if 0 == p1ans or p1ans > location:
        p1ans = location
x = 0
p2ans = 0
# Loc 35 = Seed 13
# 35 35 34 34 41 52 13 13

# Brute force starting at loc 0 until we get a valid seed

# convert seeds to ranges
seed_ranges = []

while x < len(seeds):
    seed_ranges.append([seeds[x], seeds[x] + seeds[x+1] - 1])
    x += 2
found_seed = False
x = 0
print(seed_ranges)
# for y in seed_ranges:
#     for s in range(y[0], y[1] + 1):
#         location = map_the_seed(s)
#         if 0 == p2ans or p2ans > location:
#             p2ans = location

#
while not found_seed:
    possible_Seed = map_the_loc(x)
    for r in seed_ranges:
        if r[0] <= possible_Seed <= r[1]:
            found_seed = True
            p2ans = x
            break
    x += 1

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
