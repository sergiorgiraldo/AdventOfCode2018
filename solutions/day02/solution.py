# puzzle prompt: https://adventofcode.com/2018/day/2

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from collections import Counter
from itertools import combinations

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 2

    def compute_checksum(self, box_ids):
        c = Counter[int]()

        for id in box_ids:
            c.update(set(Counter(id).values()))
        
        return c[2]*c[3]

    def get_correct_label(self, box_ids):
        for a,b in combinations(box_ids, r=2):
            ans = [c1 for c1,c2 in zip(a,b) if c1 == c2]
            if len(ans) + 1 == len(a):
                return "".join(ans)

    def part_1(self):
        start_time = time.time()

        res = self.compute_checksum(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_correct_label(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()