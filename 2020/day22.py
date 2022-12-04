import os
import sys
import copy
import time
from aocd import get_data
from aocd import submit
from pprint import pprint

# AOC 2020 --- Day 22: Crab Combat ---

def PlayCrabCombatPart1(p1c, p2c):
    while len(p1c) > 0 and len(p2c) > 0:
        p1 = p1c.pop(0)
        p2 = p2c.pop(0)
        if p1 > p2:
            # p1 wins
            p1c.append(p1)
            p1c.append(p2)
        elif p2 > p1:
            p2c.append(p2)
            p2c.append(p1)
        else:
            print(f'Error:  {p1}:{p2}')
            pprint(p1c)
            print('----------------------')
            pprint(p2c)
    if len(p1c) != 0:
        return(1)
    elif len(p2c) != 0:
        return(2)

def PlayCrabCombatPart2(p1c, p2c):
    p1h = []
    p2h = []
    while len(p1c) > 0 and len(p2c) > 0:
        p1 = p1c.pop(0) 
        p2 = p2c.pop(0)
        
        if len(p1c) >= p1 and len(p2c) >= p2:
            # print('subgame')
            if PlayCrabCombatPart2(copy.deepcopy(p1c[:p1]), copy.deepcopy(p2c[:p2])) == 1:
                # p1 wins
                p1c.append(p1)
                p1c.append(p2)
            else:
                p2c.append(p2)
                p2c.append(p1)
        elif p1 > p2:
            # p1 wins
            p1c.append(p1)
            p1c.append(p2)
        elif p2 > p1:
            p2c.append(p2)
            p2c.append(p1)
        else:
            print(f'Error:  {p1}:{p2}')
            pprint(p1c)
            print('----------------------')
            pprint(p2c)
        if p1c in p1h and p2c in p2h:
            return 1
        else:
            p1h.append(copy.deepcopy(p1c))
            p2h.append(copy.deepcopy(p2c))
    if len(p1c) != 0:
        return(1)
    elif len(p2c) != 0:
        return(2)

myset = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".splitlines()

#myset = """Player 1:
#43
#19
#
#Player 2:
#2
#29
#14""".splitlines()



# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=22, year=2020).splitlines()

# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
#print(myset)
starttime = time.time()

p1idx = 0
p2idx = 0
mididx = 0

for x in range(0,len(myset)):
    if myset[x] == 'Player 1:':
        p1idx = x
    elif myset[x] == 'Player 2:':
        p2idx = x
    elif myset[x] == '':
        mididx = x

# Part 1
p1cards = list(map(int, copy.deepcopy(myset[p1idx+1:mididx])))
p2cards = list(map(int, copy.deepcopy(myset[p2idx+1:])))

#pprint(p1cards)
#print('-------------------------')
#pprint(p2cards)

#PlayCrabCombatPart1(p1cards,p2cards)

#pprint(p1cards)
#print('----------------------')
#pprint(p2cards)

winning_hand = []

if len(p1cards) != 0:
    winning_hand = copy.deepcopy(p1cards)
elif len(p2cards) != 0:
    winning_hand = copy.deepcopy(p2cards)

#score the hand:
score = 0
count = 1
for x in reversed(winning_hand):
    score += (count * x)
    count += 1

print(f'Part 1: The winning hand score is: {score}.  {time.time() - starttime}')
#submit(score, part='a', day=22, year=2020)

# Part 2
p1cards = list(map(int, copy.deepcopy(myset[p1idx+1:mididx])))
p2cards = list(map(int, copy.deepcopy(myset[p2idx+1:])))

#pprint(p1cards)
#print('-------------------------')
#pprint(p2cards)

PlayCrabCombatPart2(p1cards,p2cards)
winning_hand = []

if len(p1cards) != 0:
    winning_hand = copy.deepcopy(p1cards)
elif len(p2cards) != 0:
    winning_hand = copy.deepcopy(p2cards)

#score the hand:
score = 0
count = 1
for x in reversed(winning_hand):
    score += (count * x)
    count += 1

print(f'Part 2: The winning hand score is: {score}.  {time.time() - starttime}')
#submit(score, part='b', day=22, year=2020)

