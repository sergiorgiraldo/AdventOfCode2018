# puzzle prompt: https://adventofcode.com/2018/day/6

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 6

    def get_manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def parse_grid(self, lines, total = 10_000):
        coords = [list(map(int, line.split(", "))) for line in lines if "," in line]

        max_x = max(point[0] for point in coords)
        max_y = max(point[1] for point in coords)

        grid = [[None] * (max_y + 1) for i in range(max_x + 1)]

        counts = [0] * len(coords)

        safe_count = 0

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                min_dist = float("inf")
                min_count = 0
                min_idx = None
                
                total_manh_distance = 0
                
                for idx, point in enumerate(coords):
                    dist = self.get_manhattan_distance((x, y), point)
                    total_manh_distance += dist
                    if dist < min_dist:
                        min_dist = dist
                        min_count = 1
                        min_idx = idx
                    elif dist == min_dist:
                        min_count += 1
                
                if min_count == 1:
                    grid[x][y] = min_idx
                    counts[min_idx] += 1
                
                if total_manh_distance < total:
                    safe_count += 1

        # Input coordinates have infinite area if they "dominate" a border point
        border_points = [(x, 0) for x in range(0, max_x + 1)] +\
                        [(x, max_y) for x in range(0, max_x + 1)] +\
                        [(0, y) for y in range(1, max_y + 1)] +\
                        [(max_x, y) for y in range(1, max_y + 1)]

        for x, y in border_points:
            i = grid[x][y]
            if i is not None:
                counts[i] = -1

        return max(counts), safe_count

    def part_1(self):
        start_time = time.time()

        res, _ = self.parse_grid(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        _, res = self.parse_grid(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()