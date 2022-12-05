import os
import sys
import copy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 1: Calorie Counting ---                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves'     #
# expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their #
# supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying    #
# (your puzzle input).                                                                                          #
#                                                                                                               #
# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations,     #
# etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the       #
# previous Elf's inventory (if any) by a blank line.                                                            #
#                                                                                                               #
# For example, suppose the Elves finish writing their items' Calories and end up with the following list:       #
#                                                                                                               #
# 1000                                                                                                          #
# 2000                                                                                                          #
# 3000                                                                                                          #
#                                                                                                               #
# 4000                                                                                                          #
#                                                                                                               #
# 5000                                                                                                          #
# 6000                                                                                                          #
#                                                                                                               #
# 7000                                                                                                          #
# 8000                                                                                                          #
# 9000                                                                                                          #
#                                                                                                               #
# 10000                                                                                                         #
#                                                                                                               #
# This list represents the Calories of the food carried by five Elves:                                          #
#                                                                                                               #
# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.                  #
# The second Elf is carrying one food item with 4000 Calories.                                                  #
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.                        #
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.                #
# The fifth Elf is carrying one food item with 10000 Calories.                                                  #
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know   #
# how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is      #
# 24000 (carried by the fourth Elf).                                                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying   #
# the most Calories of food might eventually run out of snacks.                                                 #
# 
# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the  #
# top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they     #
# still have two backups.                                                                                       #
#                                                                                                               #
# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with  #
# 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three     #
# elves is 45000.                                                                                               #
#                                                                                                               #
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = ['1000\n','2000\n','3000\n','\n','4000\n','\n','5000\n',\
    '6000\n','\n','7000\n','8000\n','9000\n','\n','10000\n',]

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=1, year=2022).splitlines()

# add an extra LF to my set so the final elf will be calculated
myset.append('\n')
startime = time.time()

# remove line feeds from the list
myset = [_.strip() for _ in myset]
#for x in range(0,len(myset)):
#   myset[x] = myset[x].strip()

#print(myset)

# get the time we start running our solution: even though I'm running in debug mode

elf_cal = []    # list with the total calories each elf has
count_cal = 0   # a count variable we will use in the loops

# loop through each line of the input.  If there is a number, add it to the count variable.
# if the line is blank, then add this total to the elf_cal list
for x in myset:
    if x != '':
        count_cal += int(x)
    else:
        elf_cal.append(int(count_cal))
        count_cal = 0

# part two: Find the total number of calories of the top three elves

# pprint(elf_cal)
count_cal = 0

# make a copy of the elf_cal list so we do not modify it.
temp_list = copy.deepcopy(elf_cal)

# find and total the top three calorie carrying elves
for _ in range(3):
    count_cal += max(temp_list)
    temp_list.remove(max(temp_list))

# now we can print our results
print(f'Part 1: The elf with the most calories has {max(elf_cal)} calories.\r\nPart 2: The top three elf\'s have {count_cal} calories.  {time.time() - startime}')



