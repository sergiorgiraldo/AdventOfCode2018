# puzzle prompt: https://adventofcode.com/2018/day/4

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import re
from collections import defaultdict, Counter

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 4

    def parse(self, lines):
        records = []
        
        # [1518-03-20 23:57] Guard #1297 begins shift
        # [1518-10-17 00:21] falls asleep
        # [1518-03-19 00:23] wakes up
        
        for line in lines:
            matches = re.findall("\[1518-(\d+)-(\d+) (\d+):(\d+)\] (.+)", line)[0]
            month, day, hour, minute = [int(i) for i in matches[:4]]
            records.append([month, day, hour, minute, matches[4].split(" ")[1]])
        
        return records

    def get_asleep_guards(self, lines)->list[int]:
        records = self.parse(lines)

        asleep, guard, slept = 0, -1, defaultdict[int, Counter[int]](Counter)

        for _, _, _, minute, record in sorted(records):
            match record:
                case "up":
                    slept[guard].update(range(asleep, minute))
                case "asleep":
                    asleep = minute
                case _:
                    guard = int(record[1:])

        g1 = max(slept, key=lambda g: sum(slept[g].values()))
        g2 = max(slept, key=lambda g: slept[g].most_common(1)[0][1])
            
        return [g * slept[g].most_common(1)[0][0] for g in [g1,g2]]


    def part_1(self):
        start_time = time.time()

        res = self.get_asleep_guards(self.input)[0]

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_asleep_guards(self.input)[1]

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()