import os
import sys
import copy
from pprint import pprint
import time
#from aocd.models import Puzzle
#puzzle = Puzzle(year=2022, day=2)
from aocd import get_data
print(os.environ['AOC_SESSION'])
#myset = open(os.path.join(sys.path[0], '2022\\input2.txt')).readlines()
myset = get_data(day=21, year=2015).splitlines()
pprint(myset)
#print(type(myset))