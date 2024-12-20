# import os
import sys
import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

reg_a = 0
reg_b = 0
reg_c = 0
pointer = 0

def main():
    global reg_a
    global reg_b
    global reg_c
    global pointer
    # # # # # # # # # # # # # # # # # # # # #
    # --- Day 0: Chronospatial Computer --- #
    # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".splitlines()
    
    aoc_input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=17, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = ''
    p2 = []
    program = []
    original_program = ''

    for x in aoc_input:
        if x[0:12] == "Register A: ":
            print(f'Reg A: {x[12:]}')
            reg_a = int(x[12:])
        elif x[0:12] == "Register B: ":
            print(f'Reg B: {x[12:]}')
            reg_b = int(x[12:])
        elif x[0:12] == "Register C: ":
            print(f'Reg C: {x[12:]}')
            reg_c = int(x[12:])
        elif x[0:9] == "Program: ":
            print(f'Program: {x[9:]}')
            original_program = x[9:]
            temp = x[9:].split(',')
            program = [int(item) for item in temp]
    
    while pointer < len(program):
        ret = instructions(program[pointer], program[pointer + 1])
        if ret is not None:
            if not p1:
                p1 = str(ret)
            else:
                p1 += ',' + str(ret)
    
    # Part 2 Programmatically
    candidates = {
        int('0', 8),
        int('1', 8),
        int('2', 8),
        int('3', 8),
        int('4', 8),
        int('5', 8),
        int('6', 8),
        int('7', 8),
    }

    while not p2:
        new_candidates = []
        for _ in candidates:
            pointer = 0
            ans = ''
            reg_a = _
            reg_b = 0
            reg_c = 0
            program = [int(item) for item in temp]
            while pointer < len(program):
                ret = instructions(program[pointer], program[pointer + 1])
                if ret is not None:
                    if not ans:
                        ans = str(ret)
                    else:
                        ans += ',' + str(ret)
            if ans == original_program:
                p2.append(_)
            if ans == original_program[-len(ans):]:
                new_candidates.append(int(str(oct(_))[2:] + '0', 8))
                new_candidates.append(int(str(oct(_))[2:] + '1', 8))
                new_candidates.append(int(str(oct(_))[2:] + '2', 8))
                new_candidates.append(int(str(oct(_))[2:] + '3', 8))
                new_candidates.append(int(str(oct(_))[2:] + '4', 8))
                new_candidates.append(int(str(oct(_))[2:] + '5', 8))
                new_candidates.append(int(str(oct(_))[2:] + '6', 8))
                new_candidates.append(int(str(oct(_))[2:] + '7', 8))
        candidates = copy.deepcopy(new_candidates)



    
    print(f'P1: {p1} - P2: {min(p2)} in {time.time() - start_time} seconds.')

def instructions(opcode, operand):
    global reg_a
    global reg_b
    global reg_c
    global pointer
    if opcode == 0:
        operand = convert_combo(operand)
        operand = 2 ** operand
        reg_a = int(reg_a / operand)
        pointer += 2
        return
    if opcode == 1:
        reg_b = reg_b ^ operand
        pointer += 2
        return
    if opcode == 2:
        operand = convert_combo(operand)
        reg_b = operand % 8
        pointer += 2
        return
    if opcode == 3:
        if reg_a == 0:
            pointer += 2
            return
        else:
            pointer = operand
            return
    if opcode == 4:
        reg_b = reg_b ^ reg_c
        pointer += 2
        return
    if opcode == 5:
        operand = convert_combo(operand)
        pointer += 2
        return operand % 8
    if opcode == 6:
        operand = convert_combo(operand)
        operand = 2 ** operand
        reg_b = int(reg_a / operand)
        pointer += 2
        return
    if opcode == 7:
        operand = convert_combo(operand)
        operand = 2 ** operand
        reg_c = int(reg_a / operand)
        pointer += 2
        return

def convert_combo(o):
    if 0 <= o <= 3:
        return o
    elif o == 4:
        return reg_a
    elif o == 5:
        return reg_b
    elif o == 6:
        return reg_c
    return None

if __name__ == '__main__':
    main()
 