import os
import sys
import copy
from pprint import pprint
from aocd import get_data
from aocd import submit
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 5:  ---                                                                        #
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
myset = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=6, year=2022).splitlines()

# remove line feeds from the list
starttime = time.time()
def findStartOfPacket(data):
    # after seeing some solutions on-line, I'm going to change this up a bit
    for x in range(0, len(data)):
        # print(f'{data[x]} : {data[x-3:x]} - {data[x-1]} : {data[x-3:x-1]} - {data[x-2]} : {data[x-3:x-2]}')
        # if data[x] not in data[x-3:x] and data[x-1] not in data[x-3:x-1] and data[x-2] not in data[x-3:x-2]:
        if len(set(data[x:x+4])) == 4:
            return x+4
    return 0

def findStartOfPacket2(data):
    for x in range(13, len(data)):
        #print(f'{data[x]} : {data[x-3:x]} - {data[x-1]} : {data[x-3:x-1]} - {data[x-2]} : {data[x-3:x-2]}')
        #if (data[x] not in data[x-13:x] and data[x-1] not in data[x-13:x-1] and data[x-2] not in data[x-13:x-2]
        #    and data[x-3] not in data[x-13:x-3] and data[x-4] not in data[x-13:x-4] and data[x-5] not in data[x-13:x-5]
        #    and data[x-6] not in data[x-13:x-6] and data[x-7] not in data[x-13:x-7] and data[x-8] not in data[x-13:x-8]
        #    and data[x-9] not in data[x-13:x-9] and data[x-10] not in data[x-13:x-10] and data[x-11] not in data[x-13:x-11]
        #    and data[x-12] not in data[x-13:x-12]):
        if len(set(data[x:x+14])) == 14:
            return x+14
    return 0


#for x in myset:
#    p1ans = findStartOfPacket(x)
#    print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
p1ans = findStartOfPacket(myset[0])
print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 6, year=2022)
starttime = time.time()
#for x in myset:
#    p1ans = findStartOfPacket2(x)
#    print(f'Part 2 Answer is {p1ans}    {time.time() - starttime}')
p2ans = findStartOfPacket2(myset[0])
print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
#submit(p2ans, part='b', day = 6, year=2022)