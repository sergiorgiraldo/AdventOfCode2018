# puzzle prompt: https://adventofcode.com/2018/day/25

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import re

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 25

    def get_manhattan_distance(self, star1, star2):
        return sum(abs(a-b) for a, b in zip(star1, star2))

    def check_if_in_constellation(self, stars, single_star):
        if single_star not in stars:
            return

        stars.remove(single_star)

        for other_star in [star_in_constellation for star_in_constellation in stars
                           if self.get_manhattan_distance(single_star, star_in_constellation) < 4]:
            self.check_if_in_constellation(stars, other_star)

    def count_constellations(self, lines):
        stars = [[int(i) for i in re.findall("-?\d+", line)] for line in lines]

        constellations = 0

        while stars:
            self.check_if_in_constellation(stars, stars[0])
            constellations += 1

        return constellations

    def part_1(self):
        start_time = time.time()

        res = self.count_constellations(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        arr = self.input
        res = ""

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == '__main__':
    solution = Solution()

    solution.part_1()

    # solution.part_2()
