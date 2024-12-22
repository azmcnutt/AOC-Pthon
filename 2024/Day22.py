# import os
# import sys
# import copy
# from pprint import pprint
from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # #
    # --- Day Monkey Market: ---  #
    # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """1
2
3
2024""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=22, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    x = 123
    prices = {}
    change = {}
    sequence = {}
    unique_sequences = set()
    scores = {}

    for a in tqdm(aoc_input, desc='Process File'):
        prices[a] = []
        change[a] = []
        sequence[a] = []
        x = int(a)
        last_price = x % 10
        prices[a].append(last_price)
        change[a].append(None)
        sequence[a].append(None)
        for _ in range(2000 - 1):
            x = secret_num_gen(x)
            cur_price = x % 10
            prices[a].append(cur_price)
            change[a].append(cur_price - last_price)
            last_price = cur_price
            if _ <= 2:
                sequence[a].append(None)
            else:
                sequence[a].append((
                    change[a][-4],
                    change[a][-3],
                    change[a][-2],
                    change[a][-1],
                ))
                unique_sequences.add(sequence[a][-1])
        p1 += x
    for u in tqdm(unique_sequences, desc='Finding Price'):
        score = 0
        for s in sequence:
            try:
                x = sequence[s].index(u)
                score += prices[s][x]
            except ValueError:
                pass
        scores[u] = score
    max_key = max(scores, key=scores.get)
    p2 = scores[max_key]


    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
@cache
def secret_num_gen(x):
    # Step one
    x = int((x * 64) ^ x)
    x = int(x % 16777216)
    # Step two
    x = int(int((x / 32)) ^ x)
    x = int(x % 16777216)
    # Step three
    x = int((x * 2048) ^ x)
    x = int(x % 16777216)
    return int(x)



if __name__ == '__main__':
    main()
 