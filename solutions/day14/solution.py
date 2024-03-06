# puzzle prompt: https://adventofcode.com/2018/day/14

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2018
    _day = 14

    # i brute-forced it, almost 5 minutes running but life is too short to optimize it :)
    def cook(self, num_recipes_):
        num_recipes = int(num_recipes_)
        len_num_recipes = len(num_recipes_)

        scores = [3, 7] #magic numbers given by the puzzle

        pos = [0, 1]

        found_position = None

        while len(scores) < num_recipes + 10 or found_position is None:
            score = scores[pos[0]] + scores[pos[1]]

            cur_len_scores = len(scores)

            if score >= 10: scores.append(1)
            scores.append(score % 10)

            new_len_scores = len(scores)

            for elf in range(2): #number of elves in the puzzle
                pos[elf] = (pos[elf] + scores[pos[elf]] + 1) % len(scores)

                for i in range(cur_len_scores, new_len_scores):
                    if not found_position:
                        if num_recipes_ == "".join(map(str, scores[i-len_num_recipes:i])):
                            found_position = i - len_num_recipes

        return ("".join(map(str, scores[num_recipes:num_recipes+10]))), (found_position)

    def part_1(self):
        start_time = time.time()

        res, _ = self.cook(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        _,res = self.cook(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()