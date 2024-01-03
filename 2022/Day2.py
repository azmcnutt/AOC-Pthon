import os
import sys
import copy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 2: Rock Paper Scissors ---                                                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = ['A Y\n','B X\n','C Z\n',]

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=2, year=2022).splitlines()
# remove line feeds from the list
for x in range(0,len(myset)):
    myset[x] = myset[x].strip()
# pprint(myset)
# get the time we start running our solution: even though I'm running in debug mode
startime = time.time()

total_score = 0

# Dict to convert ABC, XYZ to Rock Paper Scissor.
rps = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

# Dict for the score if you used R, P, or S
score = {
    'R': 1,
    'P': 2,
    'S': 3,
}

# loop through the games to determine score if X Y Z is played as R, P, S
for game in myset:
    opp, me = game.split(' ')
    opp = rps[opp]
    me = rps[me]
    #print(f'Opponent: {opp} - Me: {me}')
    # score for the roll I made
    total_score += score[me]

    # Used if statements because I could not quickly figure out how to make match do what I wanted.
    if opp == me: #draw score 3 points
        total_score += 3
    elif opp == 'R' and me == 'P': # I win, score 6 points
        total_score += 6
    elif opp == 'P' and me == 'S': # I win, score 6 points
        total_score += 6
    elif opp == 'S' and me == 'R': # I win, score 6 points
        total_score += 6
    # I do not need to do losses because 0 points does not need to be added
    # I could have put the elif all on one line, but left is separate for readability
print(f'Part 1: Me score: {total_score}.  {time.time() - startime}')

# part 2
startime = time.time()
total_score = 0

# loop through the games using X, Y, Z, as Win, Lie, Lose.
for game in myset:
    opp, me = game.split(' ')
    opp = rps[opp]
    if me == 'Y':  # must be draw
        total_score += 3 # for the draw
        total_score += score[opp] # the score for my play ( since it is a draw, my play is the same as the opp)
    elif me == 'X':  # I need to loose
        if opp == 'R': # get the score for playing S
            total_score += score['S']
        elif opp == 'P':  # get the score for playing R
            total_score += score['R']
        elif opp == 'S': # I get to score for playing P
            total_score += score['P']
    elif me == 'Z':  # I need to win
        total_score += 6
        if opp == 'R': # get the score for playing P
            total_score += score['P']
        elif opp == 'P':  # get the score for playing S
            total_score += score['S']
        elif opp == 'S': # I get to score for playing R
            total_score += score['R']
print(f'Part 2: Me score: {total_score}.  {time.time() - startime}')
