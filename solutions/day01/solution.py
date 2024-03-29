# puzzle prompt: https://adventofcode.com/2018/day/1

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 1

    def get_final_frequency(self, changes)->int:
        changes = list(map(int, changes))

        return sum(changes)

    def get_repeating_frequency(self, changes)->int:
        changes = list(map(int, changes))
        
        seen = {0}
        freq = 0
        found = False

        while not found:
            for chg in changes:
                freq += chg
                if freq in seen:
                    found = True
                    break
                seen.add(freq)

        return freq
                
    def part_1(self):
        start_time = time.time()

        res = self.get_final_frequency(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_repeating_frequency(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()