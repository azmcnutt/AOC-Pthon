from copy import deepcopy
from pprint import pprint
from aocd import get_data
import json
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 11:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
#myset = """abcdefgh
#ghijklmn
#cqjxxyzy
#cqjxjnds""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=12, year=2015)
def part1(d):
    if type(d) is int:
        return d
    elif type(d) is list:
        return sum(map(part1, d))
    elif type(d) is dict:
        vals = d.values()
        return sum(map(part1, vals))
    else:
        return 0
        
def part2(d):
    if type(d) is int:
        return d
    elif type(d) is list:
        return sum(map(part2, d))
    elif type(d) is dict:
        vals = d.values()
        if "red" in vals:
            return 0
        return sum(map(part2, vals))
    else:
        return 0


p1ans = part1(json.loads(myset))
p2ans = part2(json.loads(myset))


print(f'Part 1 Answer is {p1ans}')
print(f'Part 2 Answer is {p2ans}')
