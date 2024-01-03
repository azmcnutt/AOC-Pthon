from copy import deepcopy
from pprint import pprint
from aocd import get_data
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 9:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """1""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=10, year=2015).splitlines()
game = myset[0]
for _ in range(0,50):
    last_z = ''
    count = 0
    newgame = ''
    for z in game:
        if z != last_z and count != 0:
            newgame += str(count) + last_z
            count = 0
        if z != last_z: #start counting
            last_z = z
            count += 1
        else:
            count += 1
    newgame += str(count) + last_z
    count = 0
    game = newgame
    #print(game)


print(f'Part 1 Answer is {len(game)}')
# submit(p1ans, part='a', day = 7, year=2022)
# print(f'Part 2 Answer is {p2ans}')
# submit(p1ans, part='a', day = 7, year=2022)
