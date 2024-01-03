import math
import os
import sys
import copy
from pprint import pprint
from aocd import get_data, submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 15: Lens Library ---                                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".splitlines()
# myset = """HASH""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

myset = get_data(day=15, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

myset = myset[0].split(',')


def get_hash(x):
    z = 0
    for y in x:
        z += ord(y)
        z *= 17
        z %= 256
    return z


boxes = {}
focal_lengths = {}
for i in range(0, 256):
    boxes[i] = []
for w in myset:
    p1ans += get_hash(w)
    if w[-1] == '-':
        a = w[:-1]
        c = get_hash(a)
        if a in boxes[c]:
            boxes[c].remove(a)
            del focal_lengths[a]
    elif w[-2] == '=':
        # add to a box
        a, b = w.split('=')
        c = get_hash(a)
        if a in boxes[c]:
            # code to update the focal length
            focal_lengths[a] = int(b)
        else:
            boxes[c].append(a)
            focal_lengths[a] = int(b)
    else:
        print('error')
for b in boxes.keys():
    if len(boxes[b]) > 0:
        # print(f'Box: {b}:')
        for i, a in enumerate(boxes[b]):
            p2ans += (b + 1) * (i + 1) * focal_lengths[a]
            # print(f'Lens {a} - Focal Length: {focal_lengths[a]}')
        # print()

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
