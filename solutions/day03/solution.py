# puzzle prompt: https://adventofcode.com/2018/day/3

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 3

    SIZE = 1000 # input from the puzzle

    def parse(self, lines)-> tuple[list, list[list[int]]]:
        claims = []

        for line in lines:
            _, rect = line.split(" @ ")
            coords, size = rect.split(": ")
            x, y = map(lambda t: int(t) - 1, coords.split(","))
            w, h = map(int, size.split("x"))
            
            claims.append((x, y, w, h))
        
        grid = [[0] * self.SIZE for _ in range(self.SIZE)]

        for claim in claims:
            x, y, w, h = claim
            
            for i in range(x, x+w):
                for j in range(y, y+h):
                    grid[i][j] += 1

        return claims, grid

    def get_overlapped_claims(self, lines)->int:        
        _, grid = self.parse(lines)

        overlapped = 0
        for i in range(0, self.SIZE):
            for j in range(0, self.SIZE):
                if grid[i][j] >= 2:
                    overlapped += 1

        return overlapped

    def get_untouched_claim(self, lines)->int:
        claims, grid = self.parse(lines)

        for id, claim in enumerate(claims):
            x, y, w, h = claim
            
            untouched = True
            
            for i in range(x, x+w):
                if not untouched:
                    break
                for j in range(y, y+h):
                    if grid[i][j] != 1:
                        untouched = False
                        break
            
            if untouched:
                return (id + 1)        

    def part_1(self):
        start_time = time.time()

        res = self.get_overlapped_claims(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_untouched_claim(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()