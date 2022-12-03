import os
import sys
import copy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 2: Rock Paper Scissors ---                                                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a  #
# giant Rock Paper Scissors tournament is already in progress.                                                  #
#                                                                                                               #
# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players #
# each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round  #
# is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose    #
# the same shape, the round instead ends in a draw.                                                             #
#                                                                                                               #
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that   #
# they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock,  #
# B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's #
# tent.                                                                                                         #
#                                                                                                               #
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for   #
# Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.           #
#                                                                                                               #
# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your  #
# scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2    #
# for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was #
# a draw, and 6 if you won).                                                                                    #
#                                                                                                               #
# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you     #
# would get if you were to follow the strategy guide.                                                           #
#                                                                                                               #
# For example, suppose you were given the following strategy guide:                                             #
#                                                                                                               #
# A Y                                                                                                           #
# B X                                                                                                           #
# C Z                                                                                                           #
# This strategy guide predicts and recommends the following:                                                    #
#                                                                                                               #
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win   #
#   for you with a score of 8 (2 because you chose Paper + 6 because you won).                                  #
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss #
#   for you with a score of 1 (1 + 0).                                                                          #
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.               #
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).     #
#                                                                                                               #
# What would your total score be if everything goes exactly according to your strategy guide?                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2                                                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the   #
# round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you    #
# need to win. Good luck!"                                                                                      #
#                                                                                                               # 
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so   #
# the round ends as indicated. The example above now goes like this:                                            #
#                                                                                                               #
# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you   #
#   also choose Rock. This gives you a score of 1 + 3 = 4.                                                      #
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of #
#   1 + 0 = 1.                                                                                                  #
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.              #
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.  #
#                                                                                                               #
# Following the Elf's instructions for the second column, what would your total score be if everything goes     #
# exactly according to your strategy guide?                                                                     #
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
