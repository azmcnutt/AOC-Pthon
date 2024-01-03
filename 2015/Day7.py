import os
import sys
from copy import deepcopy
from pprint import pprint
from aocd import get_data
from aocd import submit
from functools import cache
import time
import hashlib
import ctypes

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 8:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=7, year=2015).splitlines()

starttime = time.time()

ins = {}

for x in myset:
    v,k = x.split(' -> ')
    ins[k]=v



@cache
def getWireValue(w):
    
    if w.isdigit():
        return int(w)
    temp=w+':'+ins[w]
    if ins[w].isdigit():
        return int(ins[w])
    elif 'AND' in ins[w]:
        a,b = ins[w].split(' AND ')
        a = getWireValue(a)
        b = getWireValue(b)
        return a & b
    elif 'OR' in ins[w]:
        a,b = ins[w].split(' OR ')
        a = getWireValue(a)
        b = getWireValue(b)
        return a | b
    elif 'NOT' in ins[w]:
        _,a = ins[w].split(' ')
        a = getWireValue(a)
        return ctypes.c_uint32(~a).value
    elif 'RSHIFT' in ins[w]:
        a,b = ins[w].split(' RSHIFT ')
        a = getWireValue(a)
        return a >> int(b)
    elif 'LSHIFT' in ins[w]:
        a,b = ins[w].split(' LSHIFT ')
        a = getWireValue(a)
        return a << int(b)
    return getWireValue(ins[w])

#pprint(ins)
#print(f'X: {getWireValue("x")}')
#print(f'E: {getWireValue("e")}')
#print(f'F: {getWireValue("f")}')
#print(f'G: {getWireValue("g")}')
#print(f'H: {getWireValue("h")}')
#print(f'I: {getWireValue("i")}')
#print(f'X: {getWireValue("x")}')
#print(f'Y: {getWireValue("y")}')
# print(ins['a'])
 
p1ans = getWireValue("a")

print(f'Part 1 Answer is {p1ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
ins['b'] = str(p1ans)
getWireValue.cache_clear()
p2ans = getWireValue("a")
print(f'Part 2 Answer is {p2ans}    {time.time() - starttime}')
# submit(p1ans, part='a', day = 7, year=2022)
