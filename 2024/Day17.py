# import os
# import sys
# import copy
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
    p2 = 1
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
    
    # part 2 brute force:
    # https://www.reddit.com/r/adventofcode/comments/1hgcuw8/2024_day_17_part_2_any_hints_folks/
    p2 = 0
    mylist = [
        # int('5322353701100', 8),
        # int('5322353701101', 8),
        # int('5322353701102', 8),
        # int('5322353701103', 8),
        # int('5322353701104', 8),
        # int('5322353701105', 8),
        # int('5322353701106', 8),
        # int('5322353701107', 8),

        # int('53223537011610', 8),
        # int('53223537011611', 8),
        # int('53223537011612', 8),
        # int('53223537011613', 8),
        # int('53223537011614', 8),
        # int('53223537011615', 8),
        # int('53223537011616', 8),
        # int('53223537011617', 8),
        
        int('5322353701236010', 8),
        int('5322353701236011', 8),
        int('5322353701236012', 8),
        int('5322353701236013', 8),
        int('5322353701236014', 8),
        int('5322353701236015', 8),
        int('5322353701236016', 8),
        int('5322353701236017', 8),

        int('5322353707236010', 8),
        int('5322353707236011', 8),
        int('5322353707236012', 8),
        int('5322353707236013', 8),
        int('5322353707236014', 8),
        int('5322353707236015', 8),
        int('5322353707236016', 8),
        int('5322353707236017', 8),
        
        # int('532235370723650', 8),
        # int('532235370723651', 8),
        # int('532235370723652', 8),
        # int('532235370723653', 8),
        # int('532235370723654', 8),
        # int('532235370723655', 8),
        # int('532235370723656', 8),
        # int('532235370723657', 8),
        
        int('5322353717236010', 8),
        int('5322353717236011', 8),
        int('5322353717236012', 8),
        int('5322353717236013', 8),
        int('5322353717236014', 8),
        int('5322353717236015', 8),
        int('5322353717236016', 8),
        int('5322353717236017', 8),

        # int('532235371723650', 8),
        # int('532235371723651', 8),
        # int('532235371723652', 8),
        # int('532235371723653', 8),
        # int('532235371723654', 8),
        # int('532235371723655', 8),
        # int('532235371723656', 8),
        # int('532235371723657', 8),
        

        # int('5322353717250', 8),
        # int('5322353717251', 8),
        # int('5322353717252', 8),
        # int('5322353717253', 8),
        # int('5322353717254', 8),
        # int('5322353717255', 8),
        # int('5322353717256', 8),
        # int('5322353717257', 8),
        
        # int('53223537372360', 8),
        # int('53223537372361', 8),
        # int('53223537372362', 8),
        # int('53223537372363', 8),
        # int('53223537372364', 8),
        # int('53223537372365', 8),
        # int('53223537372366', 8),
        # int('53223537372367', 8),

        # int('5322353737250', 8),
        # int('5322353737251', 8),
        # int('5322353737252', 8),
        # int('5322353737253', 8),
        # int('5322353737254', 8),
        # int('5322353737255', 8),
        # int('5322353737256', 8),
        # int('5322353737257', 8),

        # int('5322353737500', 8),
        # int('5322353737501', 8),
        # int('5322353737502', 8),
        # int('5322353737503', 8),
        # int('5322353737504', 8),
        # int('5322353737505', 8),
        # int('5322353737506', 8),
        # int('5322353737507', 8),

        # int('5322353737550', 8),
        # int('5322353737551', 8),
        # int('5322353737552', 8),
        # int('5322353737553', 8),
        # int('5322353737554', 8),
        # int('5322353737555', 8),
        # int('5322353737556', 8),
        # int('5322353737557', 8),

        # int('5322353737750', 8),
        # int('5322353737751', 8),
        # int('5322353737752', 8),
        # int('5322353737753', 8),
        # int('5322353737754', 8),
        # int('5322353737755', 8),
        # int('5322353737756', 8),
        # int('5322353737757', 8),
        
        # int('5722353701100', 8),
        # int('5722353701101', 8),
        # int('5722353701102', 8),
        # int('5722353701103', 8),
        # int('5722353701104', 8),
        # int('5722353701105', 8),
        # int('5722353701106', 8),
        # int('5722353701107', 8),

        # int('5722353701160', 8),
        # int('5722353701161', 8),
        # int('5722353701162', 8),
        # int('5722353701163', 8),
        # int('5722353701164', 8),
        # int('5722353701165', 8),
        # int('5722353701166', 8),
        # int('5722353701167', 8),

        int('5722353701236010', 8),
        int('5722353701236011', 8),
        int('5722353701236012', 8),
        int('5722353701236013', 8),
        int('5722353701236014', 8),
        int('5722353701236015', 8),
        int('5722353701236016', 8),
        int('5722353701236017', 8),

        # int('572235370123650', 8),
        # int('572235370123651', 8),
        # int('572235370123652', 8),
        # int('572235370123653', 8),
        # int('572235370123654', 8),
        # int('572235370123655', 8),
        # int('572235370123656', 8),
        # int('572235370123657', 8),
        
        int('5722353717236010', 8),
        int('5722353717236011', 8),
        int('5722353717236012', 8),
        int('5722353717236013', 8),
        int('5722353717236014', 8),
        int('5722353717236015', 8),
        int('5722353717236016', 8),
        int('5722353717236017', 8),

        # int('572235371723650', 8),
        # int('572235371723651', 8),
        # int('572235371723652', 8),
        # int('572235371723653', 8),
        # int('572235371723654', 8),
        # int('572235371723655', 8),
        # int('572235371723656', 8),
        # int('572235371723657', 8),

        # int('5722353717250', 8),
        # int('5722353717251', 8),
        # int('5722353717252', 8),
        # int('5722353717253', 8),
        # int('5722353717254', 8),
        # int('5722353717255', 8),
        # int('5722353717256', 8),
        # int('5722353717257', 8),
        
        int('5722353737236010', 8),
        int('5722353737236011', 8),
        int('5722353737236012', 8),
        int('5722353737236013', 8),
        int('5722353737236014', 8),
        int('5722353737236015', 8),
        int('5722353737236016', 8),
        int('5722353737236017', 8),

        # int('572235373723650', 8),
        # int('572235373723651', 8),
        # int('572235373723652', 8),
        # int('572235373723653', 8),
        # int('572235373723654', 8),
        # int('572235373723655', 8),
        # int('572235373723656', 8),
        # int('572235373723657', 8),

        # int('5722353737250', 8),
        # int('5722353737251', 8),
        # int('5722353737252', 8),
        # int('5722353737253', 8),
        # int('5722353737254', 8),
        # int('5722353737255', 8),
        # int('5722353737256', 8),
        # int('5722353737257', 8),

        # int('5722353737500', 8),
        # int('5722353737501', 8),
        # int('5722353737502', 8),
        # int('5722353737503', 8),
        # int('5722353737504', 8),
        # int('5722353737505', 8),
        # int('5722353737506', 8),
        # int('5722353737507', 8),

        # int('5722353737550', 8),
        # int('5722353737551', 8),
        # int('5722353737552', 8),
        # int('5722353737553', 8),
        # int('5722353737554', 8),
        # int('5722353737555', 8),
        # int('5722353737556', 8),
        # int('5722353737557', 8),

        # int('5722353737750', 8),
        # int('5722353737751', 8),
        # int('5722353737752', 8),
        # int('5722353737753', 8),
        # int('5722353737754', 8),
        # int('5722353737755', 8),
        # int('5722353737756', 8),
        # int('5722353737757', 8),
    ]
    for _ in mylist:
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
        print(f'{_}:{oct(_)}: {ans} ({original_program})')
        if ans == original_program:
            p2 = _
            break

    print(f'P1: {p1} - P2: {p2} in {time.time() - start_time} seconds.')

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
 