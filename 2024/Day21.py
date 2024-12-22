# import os
# import sys
# import copy
# from pprint import pprint
from functools import cache
from aocd import get_data
# from aocd import submit
import time

num_key = {
    'a0': '<',
    'a1': '^<<',
    'a2': '<^',
    'a3': '^',
    'a4': '^^<<',
    'a5': '<^^',
    'a6': '^^',
    'a7': '^^^<<',
    'a8': '<^^^',
    'a9': '^^^',
    '0a': '>',
    '01': '^<',
    '02': '^',
    '03': '^>',
    '04': '^^<',
    '05': '^^',
    '06': '>^^',
    '07': '^^^<',
    '08': '^^^',
    '09': '>^^^',
    '1a': '>>v',
    '10': '>v',
    '12': '>',
    '13': '>>',
    '14': '^',
    '15': '^>',
    '16': '^>>',
    '17': '^^',
    '18': '>^^',
    '19': '^^>>',
    '2a': 'v>',
    '20': 'v',
    '21': '<',
    '23': '>',
    '24': '^<',
    '25': '^',
    '26': '^>',
    '27': '^^<',
    '28': '^^',
    '29': '^^>',
    '3a': 'v',
    '30': '<v',
    '31': '<<',
    '32': '<',
    '34': '^<<',
    '35': '^<',
    '36': '^',
    '37': '<<^^',
    '38': '<^^',
    '39': '^^',
    '4a': '>>vv',
    '40': '>vv',
    '41': 'v',
    '42': '>v',
    '43': '>>v',
    '45': '>',
    '46': '>>',
    '47': '^',
    '48': '>^',
    '49': '>>^',
    '5a': 'vv>',
    '50': 'vv',
    '51': 'v<',
    '52': 'v',
    '53': 'v>',
    '54': '<',
    '56': '>',
    '57': '^<',
    '58': '^',
    '59': '^>',
    '6a': 'vv',
    '60': 'vv<',
    '61': 'v<<',
    '62': 'v<',
    '63': 'v',
    '64': '<<',
    '65': '<',
    '67': '<<^',
    '68': '^<',
    '69': '^',
    '7a': '>>vvv',
    '70': '>vvv',
    '71': 'vv',
    '72': '>vv',
    '73': '>>vv',
    '74': 'v',
    '75': '>v',
    '76': '>>v',
    '78': '>',
    '79': '>>',
    '8a': 'vvv>',
    '80': 'vvv',
    '81': 'vv<',
    '82': 'vv',
    '83': '>vv',
    '84': '<v',
    '85': 'v',
    '86': '>v',
    '87': '<',
    '89': '>',
    '9a': 'vvv',
    '90': 'vvv<',
    '91': '<<vv',
    '92': '<vv',
    '93': 'vv',
    '94': 'v<<',
    '95': 'v<',
    '96': 'v',
    '97': '<<',
    '98': '<',
}

dir_key = {
    'a^': '<',
    'a<': 'v<<',
    'av': '<v',
    'a>': 'v',
    '^a': '>',
    '^<': 'v<',
    '^v': 'v',
    '^>': 'v>',
    '<a': '>>^',
    '<^': '>^',
    '<v': '>',
    '<>': '>>',
    'va': '^>',
    'v^': '^',
    'v<': '<',
    'v>': '>',
    '>a': '^',
    '>^': '<^',
    '><': '<<',
    '>v': '<',
}

def main():
    # # # # # # # # # # # # # # # # # # #
    # --- Day 21: Keypad Conundrum ---  #
    # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """029A
980A
179A
456A
379A""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=21, year=2024).splitlines()
    num_robots = 25
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    
    for a in aoc_input:
        x = push_keys('A', a, num_robots - 1)
        p1 += x * int(a[:-1])
    
    print(f'Ans: {p1} in {time.time() - start_time} seconds.')

def push_keys(start: str, code: str, count: int) -> int:
    moves = ''
    x = 0
    start = start.lower()
    for c in code.lower():
        if start != c:
            moves += num_key[start + c]
        moves += 'a'
        start = c
    x += push_dirs('A', moves, count)
    return x

@cache
def push_dirs(start: str, code: str, count: int) -> int:
    moves = ''
    x = 0
    start = start.lower()
    for c in code.lower():
        if start != c:
            moves += dir_key[start + c]
        moves += 'a'
        if count != 0:
            x += push_dirs('A', moves, count - 1)
            moves = ''
        start = c
    if count == 0:
        return (len(moves))
    return x


if __name__ == '__main__':
    main()
 