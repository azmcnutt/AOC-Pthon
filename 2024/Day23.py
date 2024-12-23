# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # #
    # --- Day 23: LAN Party --- #
    # # # # # # # # # # # # # # # 

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=23, year=2024).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = ''

    net_map = {}

    for a in tqdm(aoc_input):
        a,b = a.split('-')
        if a in net_map.keys():
            if b not in net_map[a]:
                net_map[a].append(b)
        else:
            net_map[a] = [b]
        if b in net_map.keys():
            if a not in net_map[b]:
                net_map[b].append(a)
        else:
            net_map[b] = [a]
    tset = set()
    for k,v in tqdm(net_map.items()):
        if k.startswith('t'):
            for c in v:
                for cv in net_map[c]:
                    if k in net_map[cv]:
                        tlist = [k, c, cv]
                        tlist.sort()
                        tset.add(tuple(tlist))
    p1 = len(tset)

    largest_network = set()
    for k, v in tqdm(net_map.items()):
        for c in range(0, len(v)):
            net = set()
            net.add(k)
            net.add(v[c])
            for cv in range(c + 1, len(v)):
                included = True
                for s in net:
                    if v[cv] not in net_map[s]:
                        included = False
                        break
                if included:
                    net.add(v[cv])
            if len(net) > len(largest_network):
                largest_network = net
    p2 = ",".join(sorted(largest_network))
                



    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 