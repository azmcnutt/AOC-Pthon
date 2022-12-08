import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time
import hashlib

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """ugknbfddgicrmopn
aaa
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=5, year=2015).splitlines()

starttime = time.time()
def countVowels(s):
    count = 0
    vowel = set('aeiou')
    for x in s:
        if x in vowel: count += 1
    return count

def hasDoubleLetter(s):
    for x in range(1,len(s)):
        if s[x] == s[x-1]: return True
    return False

def hasNoBadStr(s):
    bad_string = {'ab','cd','pq','xy',}
    for b in bad_string:
        if b in s: return False
    return True

def hasTwoPair(s):
    #print(s)
    for x in range(1,len(s)):
        #print(f'{s[x-1:x+1]} : {s[x+1:]}')
        if s[x-1:x+1] in s[x+1:]: return True
    return False

def hasTwoLettersSep(s):
    for x in range(2,len(s)):
        if s[x] == s[x-2]: return True
    return False

p1count = 0
p2count = 0
for x in myset:
    if countVowels(x) >= 3 and hasDoubleLetter(x) and hasNoBadStr(x):
        p1count += 1
    if hasTwoPair(x) and hasTwoLettersSep(x):
        #print(x)
        p2count += 1
print(f'Part 1 Answer is {p1count}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {p2count}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
