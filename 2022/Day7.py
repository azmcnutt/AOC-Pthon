import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 7:  ---                                                                        #
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
myset = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=7, year=2022).splitlines()

starttime = time.time()
folders = {}
def getFolderSize(data,folder='total'):
    size = 0
    while len(data) > 0:
        x = data.pop(0)
        if x == '$ ls' or x[:3] == 'dir':
            pass
        elif x == '$ cd ..':
            folders[folder] = size
            return size
        elif x[:4] == '$ cd':
            if x[5:] == '/':
                y = 'root'
            else:
                y = x[5:]
            size += getFolderSize(data,folder+ ':' + y)
        else:
            y,_ = x.split(' ')
            size += int(y)
    folders[folder] = size
    return size

myset.pop(0)
getFolderSize(myset,'root')
p1ans = 0
p2ans = 0
extra_space_req = 30000000 - (70000000 - folders['root'])
for x in folders.values():
    if x <= 100000:
        p1ans += x
    if x >= extra_space_req and (p2ans == 0 or x < p2ans):
        p2ans = x
print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
