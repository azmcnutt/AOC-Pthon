from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time
import re
from sympy import Symbol, sympify
from sympy.solvers import solve


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
r1: str = ''
r2: str = ''

def monkey_business(k: str):
    if k == 'humn': return k
    if type(m[k]) == int:
        return int(m[k])
    else:
        a = monkey_business(m[k][0])
        b = monkey_business(m[k][2])
        if type(a) != str and type(b) != str:
            if m[k][1] == '+':
                return a + b
            if m[k][1] == '-':
                return a - b
            if m[k][1] == '*':
                return a * b
            if m[k][1] == '/':
                return a / b
        else:
            return (f'({a} {m[k][1]} {b})')

        


for x in myset:
    x = re.split(': | ',x)
    if len(x) == 2:
        if x[0] != 'humn': m[x[0]] = int(x[1])
    else:
        if x[0] == 'root':
            r1 = x[1]
            r2 = x[3]
        else:
            m[x[0]] = x[1:]



x = monkey_business(r1)
y = monkey_business(r2)

if type(x) == int:
    #print(f'x:{x}')
    z = (f'{y} - {x}')
else:
    #print(f'y:{y}')
    z = (f'{x} - {y}')

humn = Symbol('humn')
# z = '((4 + (2 * (humn - 3))) / 4) - 150'

p2ans = solve(z,humn)



print(f'Part 2 Answer is: {p2ans}')
print(time() - starttime)

