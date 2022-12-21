from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 21:  ---                                                                        #
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
myset = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=21, year=2022).splitlines()
starttime = time()
# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

m: dict = {}

def monkey_business(k: str = 'root') -> int:
    if type(m[k]) == int:
        return m[k]
    else:
        a = monkey_business(m[k][0])
        b = monkey_business(m[k][2])
        if m[k][1] == '+':
            return a + b
        if m[k][1] == '-':
            return a - b
        if m[k][1] == '*':
            return a * b
        if m[k][1] == '/':
            return a / b

        


for x in myset:
    x = re.split(': | ',x)
    if len(x) == 2:
        m[x[0]] = int(x[1])
    else:
        m[x[0]] = x[1:]

print(f'Part 1 Answer is: {monkey_business()}')
print(time() - starttime)

