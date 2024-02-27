# puzzle prompt: https://adventofcode.com/2018/day/5

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import string

class Solution(InputAsStringSolution):
    _year = 2018
    _day = 5

    def build_polymer(self, units):
        units = list(units)
        index = 0

        while index < len(units) - 1:
            unit1 = units[index]
            unit2 = units[index + 1]

            if (unit1 != unit2 and unit1.upper() == unit2.upper()):
                del units[index:index + 2] #reacted, remove both

                if index > 0:
                    index -= 1
            else:
                index += 1

        return len(units)

    def enhance_polymer(self, units):
        alphabet = string.ascii_lowercase

        min_len = 999_999_999 

        for chr in alphabet:
            better_units = units.replace(chr,"").replace(chr.upper(),"")

            polymer_len = self.build_polymer(better_units)
            
            min_len = min(min_len, polymer_len)

        return min_len

    def part_1(self):
        start_time = time.time()

        res = self.build_polymer(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.enhance_polymer(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()