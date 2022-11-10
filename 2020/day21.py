import os
import sys
import copy
from pprint import pprint

# AOC 2020 Day 21 Part 1: Determine the number of ingredients for each items and total where ingredients do not contain allergens.  Sample data = 5

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n','trh fvjkl sbzzf mxmxvkd (contains dairy)\n',
    'sqjhc fvjkl (contains soy)\n','sqjhc mxmxvkd sbzzf (contains fish)\n',]
# replace test data with data from the puzzle input
# myset = open(os.path.join(sys.path[0], 'input21.txt')).readlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()

# Split the data into a list of two lists'.
# each list item will contain a list with two items: 
#   A list of ingredients
#   A list of allergens
for x in range(0,len(myset)):
    myset[x] = myset[x].split(' (contains ')
    myset[x][1] = myset[x][1].strip(')')
    myset[x][0]=copy.deepcopy(myset[x][0].split(' '))
    myset[x][1]=copy.deepcopy(myset[x][1].split(', '))

tested_ing=[]
noallergen_ing=[]
ing_alg={}
int_algremove=[]

# Create a dictionary (ing_alg) of each menu ingredient and all possible allergens
# probably an easy way to do this, but this works.  Besides, I like spaghetti.
for menuidx in range(0,len(myset)):
    pprint(f'{myset[menuidx]}')
    for ingidx in range(0,len(myset[menuidx][0])):
        print(f'    {myset[menuidx][0][ingidx]}')
        if myset[menuidx][0][ingidx] not in tested_ing:
            tested_ing.append(copy.deepcopy(myset[menuidx][0][ingidx]))
            ing_alg[myset[menuidx][0][ingidx]] = copy.deepcopy(myset[menuidx][1])
        else:
            for alg in myset[menuidx][1]:
                if alg not in ing_alg[myset[menuidx][0][ingidx]]:
                    ing_alg[myset[menuidx][0][ingidx]].append(copy.deepcopy(alg))


# Now iterate through each ingredient and if the it exists without one of the allergens, remove the allergen


pprint(ing_alg)
