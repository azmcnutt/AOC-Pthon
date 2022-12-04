import os
import sys
import copy
import time
from aocd import get_data
from aocd import submit
from pprint import pprint

# AOC 2020 Day 21 Part 1: Determine the number of ingredients for each items and total where ingredients do not contain allergens.  Sample data = 5

myset = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=21, year=2020).splitlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
# pprint(myset)
starttime = time.time()
all_ingredients = []
all_allergens = {}

for x in range(0,len(myset)):
    myset[x] = myset[x].split(' (contains ')
    myset[x][1] = myset[x][1].strip(')')
    myset[x][0]=copy.deepcopy(myset[x][0].split(' '))
    myset[x][1]=copy.deepcopy(myset[x][1].split(', '))
    all_ingredients += copy.deepcopy(myset[x][0])
    for allergen in myset[x][1]:
        if allergen in all_allergens:
            all_allergens[allergen] &= set(copy.deepcopy(myset[x][0]))
        else:
            all_allergens[allergen] = set(copy.deepcopy(myset[x][0]))
allergen_ingredient = set([x for val in all_allergens.values() for x in val])
safe_ingredient = [ing for ing in all_ingredients if ing not in allergen_ingredient]
print(f'Part 1:  There are {len(safe_ingredient)} ingredients without allergens.    {time.time() - starttime}')

allergen_dict = {}

#print(all_allergens)
while all_allergens:
    for a,b in all_allergens.items():
        if len(b) == 1:
            allergen_dict[a] = list(b)[0]
            del all_allergens[a]
            for x in all_allergens:
                if list(b)[0] in all_allergens[x]:
                    all_allergens[x].remove(list(b)[0])
            
            break;
p2answer = ''
for a,b in sorted(allergen_dict.items()):
    if len(p2answer) > 1:
        p2answer += ','
    p2answer += b
print(f'Part 2:  The allergens, sorted are {p2answer}.    {time.time() - starttime}')
submit(p2answer, part='b', day=21, year=2020)
