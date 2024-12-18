# import os
# import sys
# import copy
# from pprint import pprint
from aocd import get_data
# from aocd import submit
import time

import heapq


DIRECTIONS = [
    {"x": 1, "y": 0},
    {"x": 0, "y": 1},
    {"x": -1, "y": 0},
    {"x": 0, "y": -1},
]


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 16: Reindeer Maze --- #
    # # # # # # # # # # # # # # # # #

    # Code from:
    # https://github.com/ayoubzulfiqar/advent-of-code/blob/main/2024/Python/Day16/part_1.py
    # Leaning how dijkstra and heapq works


    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()
    # 7036

    aoc_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()
    # 11048

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=16, year=2024).splitlines()
    # 328104 Too high

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    parsed = parse_grid(aoc_input)
    distances = dijkstra(parsed["forward"], parsed["start"], False)
    
    p1 = distances.get(f"{parsed['end']['x']},{parsed['end']['y']}", float("inf"))

    from_start = dijkstra(parsed["forward"], parsed["start"], False)
    to_end = dijkstra(parsed["reverse"], parsed["end"], True)

    end_key = f"{parsed['end']['x']},{parsed['end']['y']}"
    target = from_start[end_key]
    spaces = set()

    for position in from_start:
        if (
            position != end_key
            and from_start[position] + to_end.get(position, float("inf")) == target
        ):
            x, y, *_ = position.split(",")  # Unpack and ignore direction in the key
            spaces.add(f"{x},{y}")
    p2 = len(spaces)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

class MinHeap:
    """
    Min heap implementation using heapq library
    """

    def __init__(self):
        self.heap = []

    def insert(self, element):
        heapq.heappush(self.heap, element)

    def extract_min(self):
        return heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)

def dijkstra(graph, start, directionless):
    queue = MinHeap()
    distances = {}

    starting_key = (
        f"{start['x']},{start['y']},0"
        if not directionless
        else f"{start['x']},{start['y']}"
    )
    queue.insert((0, starting_key))
    distances[starting_key] = 0

    while queue.size() > 0:
        current_score, current_node = queue.extract_min()

        if distances[current_node] < current_score:
            continue

        if current_node not in graph:
            continue

        for next_node, weight in graph[current_node].items():
            new_score = current_score + weight
            if next_node not in distances or distances[next_node] > new_score:
                distances[next_node] = new_score
                queue.insert((new_score, next_node))

    return distances

def parse_grid(grid):
    width, height = len(grid[0]), len(grid)

    start = {"x": 0, "y": 0}
    end = {"x": 0, "y": 0}
    forward = {}
    reverse = {}

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                start = {"x": x, "y": y}
            if grid[y][x] == "E":
                end = {"x": x, "y": y}

            if grid[y][x] != "#":
                for i, direction in enumerate(DIRECTIONS):
                    position = {"x": x + direction["x"], "y": y + direction["y"]}

                    key = f"{x},{y},{i}"
                    move_key = f"{position['x']},{position['y']},{i}"

                    if (
                        0 <= position["x"] < width
                        and 0 <= position["y"] < height
                        and grid[position["y"]][position["x"]] != "#"
                    ):
                        forward.setdefault(key, {})[move_key] = 1
                        reverse.setdefault(move_key, {})[key] = 1

                    for rotate_key in [
                        f"{x},{y},{(i + 3) % 4}",
                        f"{x},{y},{(i + 1) % 4}",
                    ]:
                        forward.setdefault(key, {})[rotate_key] = 1000
                        reverse.setdefault(rotate_key, {})[key] = 1000

    for i in range(len(DIRECTIONS)):
        key = f"{end['x']},{end['y']}"
        rotate_key = f"{end['x']},{end['y']},{i}"

        forward.setdefault(rotate_key, {})[key] = 0
        reverse.setdefault(key, {})[rotate_key] = 0

    return {"start": start, "end": end, "forward": forward, "reverse": reverse}

if __name__ == '__main__':
    main()
 