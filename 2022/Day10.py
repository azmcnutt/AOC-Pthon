from copy import deepcopy
from pprint import pprint
from aocd import get_data
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 10: Cathode-Ray Tube ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=10, year=2022).splitlines()

starttime = time.time()
crt = ''
cycles = 0
X = 1
signal = 0

def calcSignal():
    global crt
    global signal
    if cycles == 20 or (cycles > 40 and (cycles - 20) % 40 == 0):
        # print(f'Signal: {sig} += Cycle: {cycles} * X:{X} = {cycles * X}')
        signal += (cycles * X)
    crt_pos = 40 if cycles % 40 == 0 else cycles % 40
    if crt_pos >= X and crt_pos <= X + 2:
        crt += b'\xdb'.decode('cp437')
    else:
        crt += ' '
    if cycles % 40 == 0:
        #print(crt)
        crt += '\r\n'



for i in myset:
    if i == 'noop':
        cycles += 1
        calcSignal()
    else:
        _,y = i.split(' ')
        for _ in (1,2):
            cycles += 1
            calcSignal()
        X += int(y)

print(f'Part 1 Answer is {signal}    {time.time() - starttime}')
print(f'Part 2 Answer is:')
print(crt)
