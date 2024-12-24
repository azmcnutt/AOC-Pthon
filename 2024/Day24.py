# import os
# import sys
# import copy
from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time

rules = {}
gates = {}
zs = {}


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 24: Crossed Wires --- #
    # # # # # # # # # # # # # # # # # 

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=24, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    global rules, gates, zs

    
    for a in tqdm(aoc_input):
        if ':' in a:  # This is an initial value
            g,v = a.split(': ')
            gates[g] = int(v)
        elif '->' in a: # This is a rule
            a = a.split(' ')
            rules[a[4]] = [a[0], a[1], a[2]]
            if a[4] not in gates.keys():
                gates[a[4]] = None
            if a[4].startswith('z') and a[4] not in zs.keys():
                zs[a[4]] = None

    
    for a in tqdm(zs.keys()):
        zs[a] = solve_gate(a)

    zs = dict(sorted(zs.items(), reverse=True))
    binary = ''
    for _, z in tqdm(zs.items()):
        binary += str(z)
    p1 = int(binary, 2)
    p2 = part_two()

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def solve_gate(g):
    global rules, gates, zs

    if gates[g] is not None:
        return gates[g]
    elif g in rules.keys():
        a, f, b = rules[g]
        a = solve_gate(a)
        b = solve_gate(b)
        if f == 'AND':
            gates[g] = a and b
        elif f == 'OR':
            gates[g] = a or b
        elif f == 'XOR':
            gates[g] = a ^ b
        else:
            print(f' error on gate {g} with {a} {f} {b}')
        return gates[g]

def part_two():
    # process modified from:
    # https://github.com/michaeljgallagher/Advent-of-Code/blob/master/2024/24.py
    global rules, gates, zs
    return ",".join(
        sorted(
            c
            for c, (a, op, b) in rules.items()
            if (
                (c.startswith("z") and op != "XOR" and c != "z45")
                or (
                    op == "XOR"
                    and all(not x.startswith(("x", "y", "z")) for x in (a, b, c))
                )
                or (
                    op == "AND"
                    and "x00" not in (a, b)
                    and any(
                        c in (aa, bb) and op2 != "OR"
                        for (aa, op2, bb) in rules.values()
                    )
                )
                or (
                    op == "XOR"
                    and any(
                        c in (aa, bb) and op2 == "OR"
                        for (aa, op2, bb) in rules.values()
                    )
                )
            )
        )
    )

if __name__ == '__main__':
    main()
 