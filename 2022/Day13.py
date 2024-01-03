from copy import deepcopy
from pprint import pprint
from aocd import get_data
import ast



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 12:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=13, year=2022).splitlines()

x = 0
pack = []
all_pack = []
while x < len(myset):
    r = []
    l = []
    l = ast.literal_eval(myset[x])
    x += 1
    r = ast.literal_eval(myset[x])
    x +=2 #skip blank line
    pack.append([l,r])
    all_pack.append(l)
    all_pack.append(r)
all_pack.append([[2]])
all_pack.append([[6]])


def orderPackets(l,r):
    # returns a list:  Element 0 is status, 1 is the current index
    # status 0 means values were equal, continue
    # status 1 means l was lower than r return index
    # status -1 means r was low than left, return -1
    
    count = len(l) if len(l) >= len(r) else len(r)
    for x in range(0,count):
        if len(l) <= x: return 1 #left ran out, return index plus one because problem start at index 1
        if len(r) <= x: return 0 #right ran out, return -1 for out of order packet

        if type(l[x]) == list and type(r[x]) == list:
            y = orderPackets(l[x],r[x])
            if y != None: return y
        elif type(l[x]) == int and type(r[x]) == list:
            y = orderPackets([l[x]],r[x])
            if y != None: return y
        elif type(l[x]) == list and type(r[x]) == int:
            y = orderPackets(l[x],[r[x]])
            if y != None: return y
        elif type(l[x]) == int and type(r[x]) == int:
            if l[x] == r[x]:
                pass # keep going
            elif l[x] < r[x]:
                return 1
            elif l[x] > r[x]:
                return 0

def sorter(p):
    # https://www.geeksforgeeks.org/python-program-for-bubble-sort/
    all_sorted = True
    for x in range(len(p)-1):
        for y in range(0, len(p)-x-1):
            if orderPackets(p[y+1],p[y]):
                all_sorted = False
                p[y] , p[y + 1] = p[y + 1], p[y]
        if all_sorted: return
    return(p)


p1ans = 0
for x in range(0,len(pack)):
    if orderPackets(pack[x][0],pack[x][1]):
        p1ans += x + 1
sorter(all_pack)
print(f'Part 1 Answer is {p1ans}')
p2ans = (all_pack.index([[2]]) + 1) * (all_pack.index([[6]]) + 1)
print(f'Part 2 Answer is: {p2ans}')

