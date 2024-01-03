from copy import deepcopy
from pprint import pprint
from aocd import get_data
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 11:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """abcdefgh
ghijklmn
cqjxxyzy
cqjxjnds""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=11, year=2015).splitlines()

def checkforDoubles(p):
    first = ''
    for i in range(1,len(p)):
        if p[i] == p[i-1] and first == '':
            first = p[i]
        elif p[i] != first and p[i] == p[i-1]:
            return True
    return False
def checkforThree(p):
    for i in range(2,len((p))):
        if p[i] == l[p[i-1]] and p[i-1] == l[p[i-2]]:
            return True
    return False
# letters for testing three letters in a row
l = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'i',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'o',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'z',
    'x': 'y',
    'y': 'z',
    'z': '.',
}

#letters for going to the next while skipping bad letters.
letters = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'j',
    'i': 'j',
    'j': 'k',
    'k': 'm',
    'l': 'm',
    'm': 'n',
    'n': 'p',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
    'z': 'a',
}

badletters = ['i','o','l']

def getNextPassword(p):
    p = list(p)
    for b in badletters:
        if b in p:
            i = p.index(b)
            
            i += 1
            while i <= 7:
                p[i] = letters['y']
                i += 1
            break
    nextpass = ''
    newpass = False
    while not newpass:
        if p[-1] == 'z':
            if p[-2] == 'z':
                if p[-3] == 'z':
                    if p[-4] == 'z':
                        if p[-5] == 'z':
                            if p[-6] == 'z':
                                if p[-7] == 'z':
                                    p[-8] = letters[p[-8]]
                                p[-7] = letters[p[-7]]
                            p[-6] = letters[p[-6]]
                        p[-5] = letters[p[-5]]
                    p[-4] = letters[p[-4]]
                p[-3] = letters[p[-3]]
            p[-2] = letters[p[-2]]
        p[-1] = letters[p[-1]]
        if checkforDoubles(p) and checkforThree(p):
            newpass = True
            nextpass = ''.join(p)
            break
    return nextpass

p1ans = getNextPassword(myset[0])
print(f'Part 1 Answer is {p1ans}')
p2ans = getNextPassword(p1ans)
print(f'Part 2 Answer is {p2ans}')
