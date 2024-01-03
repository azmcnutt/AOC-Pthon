import os
import sys
import copy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 1: Calorie Counting ---                                                                               #
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



