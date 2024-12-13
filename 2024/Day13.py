# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time
import re


def main():
    # # # # # # # # # # # # # # # # # # #
    # --- Day 13: Claw Contraption ---  #
    # # # # # # # # # # # # # # # # # # #
    # Credit to Reddit user u/ThunderChaser for the math explanation
    # https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=13, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    add = 10000000000000
    i = 0
    digit_re = r'\d+'
    a_x_list = []
    b_x_list = []
    a_y_list = []
    b_y_list = []
    p_x_list = []
    p_y_list = []

    while i < len(aoc_input):
        a_x, a_y = [int(re.findall(digit_re, d)[0]) for d in aoc_input[i].split(',')]
        i += 1
        b_x, b_y = [int(re.findall(digit_re, d)[0]) for d in aoc_input[i].split(',')]
        i += 1
        p_x, p_y = [int(re.findall(digit_re, d)[0]) for d in aoc_input[i].split(',')]
        i += 2
        a_x_list.append(a_x)
        a_y_list.append(a_y)
        b_x_list.append(b_x)
        b_y_list.append(b_y)
        p_x_list.append(p_x)
        p_y_list.append(p_y)


    

    for i in range(len(a_x_list)):
        presses = solve_the_claw(a_x_list[i],a_y_list[i],b_x_list[i],b_y_list[i],p_x_list[i],p_y_list[i])
        if presses:
            p1 += int((presses[0] * 3) + (presses[1]))
        presses = solve_the_claw(a_x_list[i],a_y_list[i],b_x_list[i],b_y_list[i],p_x_list[i] + add,p_y_list[i] + add)
        if presses:
            p2 += int((presses[0] * 3) + (presses[1]))



    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def solve_the_claw(ax, ay, bx, by, px, py):
    a = (px * by - py * bx) / (ax * by - ay *bx)
    b = (ax * py - ay * px) / (ax * by - ay * bx)
    if (a == int(a) and b == int(b)):
        return [int(a),int(b)]
    else:
        return None

if __name__ == '__main__':
    main()
 