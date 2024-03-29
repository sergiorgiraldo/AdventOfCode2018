# puzzle prompt: https://adventofcode.com/2018/day/12

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from collections import defaultdict

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 12

    def parse(self, lines):
        state = defaultdict(int)

        initial_status = list(map(lambda chr: 0 if chr == "." else 1, lines[0].strip().split(" ")[2]))

        for i, has_plant in enumerate(initial_status):
            state[i] = has_plant #0 or 1

        rules = [0] * 32
        for line in lines[2:]:
            src, dst = map(lambda x: int(x.replace(".", "0").replace("#", "1"), 2), line.split(" => "))
            rules[src] = dst

        return state, rules

    def grow(self, state, rules):
        snapshot = state.copy()
        min_i = min(snapshot.keys())
        max_i = max(snapshot.keys())
        
        for i in range(min_i-2, max_i+3):
            rule = (((snapshot[i-2]*2 + snapshot[i-1])*2 + snapshot[i])*2 + snapshot[i+1])*2 + snapshot[i+2]
            state[i] = rules[rule]
            if state[i] == 0:
                del state[i]
                        
    def simulate(self, lines):
        state, rules = self.parse(lines)

        for _ in range(20):
            self.grow(state, rules)

        pots = sum(filter(lambda i: state[i] == 1, state.keys()))

        return pots

    # after 167 iterations, the number of plants increase by 26 for each generation  
    # It was out of observation, see commented piece below 
    # tried with 100 and 500, then narrowed down to 167
    def simulate_till_today(self, lines, offset=167):
        state, rules = self.parse(lines)

        # prev = 0
        # for gen in range(limit):
        #     self.grow(state, rules)
        #     tmp = sum(filter(lambda i: state[i] == 1, state.keys()))
        #     print("gen-", gen, "-pots-", tmp, "-diff-", (tmp -prev)) 
        #     prev = tmp

        generations = 50_000_000_000

        for _ in range(offset):
            self.grow(state, rules)

        pots = sum(filter(lambda i: state[i] == 1, state.keys()))
        pots = pots + 26*(generations - offset)

        return pots

    def part_1(self):
        start_time = time.time()

        res = self.simulate(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        #self.simulate_till_today(self.input, 200)
        res = self.simulate_till_today(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()