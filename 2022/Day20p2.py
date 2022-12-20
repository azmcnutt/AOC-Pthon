from copy import deepcopy
from pprint import pprint
from aocd import get_data
from time import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 20:  ---                                                                        #
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
myset = """1
2
-3
3
-2
0
4""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=20, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')

starttime = time()

d = {}
zeroidx = -1
for i,v in enumerate(myset):
    if int(v) == 0: zeroidx = i
    n = i + 1 if i + 1 != len(myset) else 0
    p = i - 1 if i != 0 else len(myset) - 1
    d[i] = {
        'n': n,
        'p': p,
        'v': int(v) * 811589153
    }

#pprint(d)
#z = 0
#for y in range(0,len(d)):
#    print(f'{d[z]["v"]},',end='')
#    z = d[z]['n']
#print()
#pprint(d)
#print('------------------')
for _ in range(0,10):
    for i in range(0,len(d)):
        #
        moves = abs(d[i]['v']) % (len(d) - 1)
        #moves = abs(d[i]['v'])
        for j in range(0,abs(moves)):
            if d[i]['v'] >= 0: #move right d[i] right
                mn = d[i]['n']
                mp = d[i]['p']
                nn = d[mn]['n']
                d[mp]['n'] = mn
                d[mn]['p'] = mp
                d[mn]['n'] = i
                d[nn]['p'] = i
                d[i]['p'] = d[i]['n']
                d[i]['n'] = nn
            else:
                mn = d[i]['n']
                mp = d[i]['p']
                np = d[mp]['p']
                d[mn]['p'] = mp
                d[mp]['n'] = mn
                d[mp]['p'] = i
                d[np]['n'] = i
                d[i]['n'] = d[i]['p']
                d[i]['p'] = np
        #z = 0
        #print(i)
        #for z in range(0,len(d)):
        #    print(f'{d[z]["v"]},',end='')
        #    z = d[z]['n']
        #print()
        #print('------------------')
    #z = 0
    #if _ % 1000 == 0 or _ == 1:
    #    print(_)
    #    for y in range(0,len(d)):
    #        print(f'{d[z]["v"]},',end='')
    #        z = d[z]['n']
    #    print()
        #pprint(d)
    #    print('------------------')
#pprint(d)
#print(zeroidx)
z = zeroidx

mix = []

for y in range(0,len(d)):
    mix.append(d[z]["v"])
    #print(f'{d[z]["v"]},',end='')
    z = d[z]['n']
#print(mix)
#print(mix[(1000 % len(mix) - 1) + 1])
#print(mix[(2000 % len(mix) - 1) + 1])
#print(mix[(3000 % len(mix) - 1) + 1])
p1ans = mix[(1000 % len(mix) - 1) + 1] + mix[(2000 % len(mix) - 1) + 1] + mix[(3000 % len(mix) - 1) + 1]



print(f'Part 2 Answer is: {p1ans}   {time() - starttime}')

