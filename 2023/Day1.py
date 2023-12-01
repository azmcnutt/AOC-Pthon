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
# --- Day 1: Trebuchet?!  ---                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even  #
# given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having       #
# problems.                                                                                                     #
#                                                                                                               #
# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars #
# by December 25th.                                                                                             #
#                                                                                                               #
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the  #
# second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!                #
#                                                                                                               #
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even       #
# sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on   #
# did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves    #
# are already loading you into a trebuchet ("please hold still, we need to strap you in").                      #
#                                                                                                               #
# As they're making the final adjustments, they discover that their calibration document (your puzzle input)    #
# has been amended by a very young Elf who was apparently just excited to show off her art skills.              #
# Consequently, the Elves are having trouble reading the values on the document.                                #
#                                                                                                               #
# The newly-improved calibration document consists of lines of text; each line originally contained a specific  #
# calibration value that the Elves now need to recover. On each line, the calibration value can be found by     #
# combining the first digit and the last digit (in that order) to form a single two-digit number.               #
#                                                                                                               #
# For example:                                                                                                  #
#                                                                                                               #
# 1abc2                                                                                                         #
# pqr3stu8vwx                                                                                                   #
# a1b2c3d4e5f                                                                                                   #
# treb7uchet                                                                                                    #
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together     #
# produces 142.                                                                                                 #
#                                                                                                               #
# Consider your entire calibration document. What is the sum of all of the calibration values?                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:   #
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".                        #
#                                                                                                               #
# Equipped with this new information, you now need to find the real first and last digit on each line. For      #
# example:                                                                                                      #
#                                                                                                               #
# two1nine                                                                                                      #
# eightwothree                                                                                                  #
# abcone2threexyz                                                                                               #
# xtwone3four                                                                                                   #
# 4nineeightseven2                                                                                              #
# zoneight234                                                                                                   #
# 7pqrstsixteen                                                                                                 #
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces    #
# 281.                                                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
# myset = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".splitlines()

myset = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
# myset = get_data(day=1, year=2023).splitlines()

# remove line feeds from the list

def get_first_and_last_digit(mixed_string):
    numbers = re.findall(r'\d',mixed_string)
    print(int(numbers[0] + numbers[-1]), numbers, mixed_string)
    return(int(numbers[0] + numbers[-1]))




#for x in range(0,len(myset)):
#    myset[x] = myset[x].strip()
#pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()
total = 0
# for x in myset:
#     total += get_first_and_last_digit(x)
#     # print(get_first_and_last_digit(x))

#print(f'P1: {total} in {time.time() - startime} seconds.')
startime = time.time()
total = 0
num_replace = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
for x in myset:
    for word, digit in num_replace.items():
        x = x.replace(word, digit)
    total += get_first_and_last_digit(x)
    # print(get_first_and_last_digit(x))
print(f'P2: {total} in {time.time() - startime} seconds.')
