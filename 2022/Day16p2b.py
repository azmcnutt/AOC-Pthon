from copy import deepcopy
from pprint import pprint
from aocd import get_data
import re
from time import time
import sys
import itertools



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 16:  ---                                                                        #
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
myset = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input
myset = get_data(day=16, year=2022).splitlines()

# for i,d in enumerate(myset):
#    print(f'{i}: {d}')
starttime = time()
# y = 10

time_limit = 30

tunnels = {}
flowrate = {}
paths = {}
opened = []
scores = []

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






for x in myset:
    _,v,r,t = re.split('Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ',x)
    #print(re.split('Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ',x))
    tunnels[v] = t.split(', ')
    flowrate[v] = int(r)
#pprint(tunnels)
#pprint(flowrate)
for v,data in tunnels.items():
    paths[v] = {}
    for d,destdata in tunnels.items():
        if v == d: continue
        else:
            path = shortest_path(tunnels,v,d)
            paths[v][d] = path = shortest_path(tunnels,v,d)
#pprint(paths)

def under_pressure(path: set, time: int):
    p = 0
    current = ''
    for x in path:
        if not current:
            current = x
            continue
        time -= len(paths[current][x]) - 1
        if time <= 0: return 0
        current = x
        time -= 1
        p += (flowrate[current] * time)
    return p


v = []
for a,b in flowrate.items():
    if b != 0:
        v.append(a)
test = []
for x in range(2,len(v) + 1):
    test.extend(map(list,itertools.permutations(v,x)))
#print(test)

for x in test:
    z = ['AA']
    z.extend(x)
    s = under_pressure(z,26)
    if s:
        if z == ['AA', 'JJ','BB','CC']:
            pass
        if z == ['AA', 'DD','HH','EE']:
            pass
        scores.append([s,z])

p2ans = []
for a,x in scores:
    for b,y in scores:
        if len(x[1:]) and len(y[1:]) and not set(x[1:]) & set(y[1:]):
            if x[1:] == ['JJ','BB','CC'] and y[1:] == ['DD','HH','EE']:
                pass
            p2ans.append(a+b)
print(f'Part 2 Answer is: {max(p2ans)}   {time() - starttime}')
#test = [
#    ['AA','JJ','BB','CC'],
#    ['AA', 'DD','HH','EE'],
#]

#for a in test:
#    print(under_pressure(a,26))
