# puzzle prompt: https://adventofcode.com/2018/day/9

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

# looking in reddit, i saw that using a deque would be easier to implement, just rotate and pop ¯\_(ツ)_/¯
# but my double linked list done the job :-)
class Marble:
	def __init__(self, value, prev_marble = None, next_marble = None):
		self.value = value
		self.prev_marble = prev_marble
		self.next_marble = next_marble
	
	def get_previous(self, offset):
		res = self
            
		for _ in range(offset):
			res = res.prev_marble
                  
		return res
	
	def delete(self):
		self.prev_marble.next_marble = self.next_marble
		self.next_marble.prev_marble = self.prev_marble

class Solution(InputAsStringSolution):
    _year = 2018
    _day = 9

    def play_marbles(self, input, boost = False):
        players = int(input.split(" ")[0])
        last_marble_value = int(input.split(" ")[6]) * (100 if boost else 1)

        cur_marble = Marble(0)
        cur_marble.next_marble = cur_marble
        cur_marble.prev_marble = cur_marble

        cur_player = 0

        scores = [0] * players

        for i in range(1, last_marble_value+1):
            if i % 23 != 0:
                new_prev = cur_marble.next_marble
                new_next = new_prev.next_marble
                                
                cur_marble = Marble(i, new_prev, new_next)
                new_prev.next_marble = cur_marble
                new_next.prev_marble = cur_marble
            else:
                scores[cur_player] += i

                removed_marble = cur_marble.get_previous(7)
                removed_marble.delete()
                
                scores[cur_player] += removed_marble.value
                
                cur_marble = removed_marble.next_marble
            
            cur_player = (cur_player + 1) % players	

        return max(scores)

    def part_1(self):
        start_time = time.time()

        res = self.play_marbles(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.play_marbles(self.input, True)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()