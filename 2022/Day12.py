from copy import deepcopy
from pprint import pprint
from aocd import get_data
import sys
from typing import Dict, List



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 12:  ---                                                                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load sample data, copied and pasted from the site into list.  Each list item is one line of input
myset = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=12, year=2022).splitlines()


w = len(myset[0])
h = len(myset)

#lambda's borrowed from https://github.com/floyduk/Advent-Of-Code-2022/blob/master/day12/d12p1.py
adjacents = lambda x, y: [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
is_valid_coordinate = lambda p: (0 <= p[0] < w and 0 <= p[1] < h)

g = {}
s = ()
e = ()
all_a = []
all_a_dist = []
for y in range(0,len(myset)):
    for x in range(0,len(myset[y])):
        if  myset[y][x] == 'a':
            all_a.append((x,y))
        if myset[y][x] == 'S':
            s=(x,y)
        if myset[y][x] == 'E':
            e=(x,y)
        g[(x,y)] = []
        c = myset[y][x]
        if c == 'S': c ='a'
        for p in adjacents(x, y):
            if is_valid_coordinate(p):
                l = myset[p[1]][p[0]]
                if l == "E": l = 'z'
                if l == 'S': l = 'a'
                if ord(l) - ord(c) <= 1:
                    g[(x,y)].append((p[0],p[1]))
# pprint(g)

# code from https://onestepcode.com/graph-shortest-path-python/
# modified for AOC
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []
p1path = shortest_path(g, s, e)
print(f'Part 1 Answer is {len(p1path) - 1}')
#print(f'Part 2 Answer is:')

