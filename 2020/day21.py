from email.policy import strict
import os
import sys
import copy

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

ingredientsPossibleAllergens={}



for x in myset:
    for ing in x[0]:
        if ing not in ingredientsPossibleAllergens:
            ingredientsPossibleAllergens[ing]=copy.deepcopy(x[1])
        else:
            for y in x[1]:
                if y not in ingredientsPossibleAllergens[ing]:
                    ingredientsPossibleAllergens[ing].append(y)

print(ingredientsPossibleAllergens)