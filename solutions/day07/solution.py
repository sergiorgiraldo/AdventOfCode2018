# puzzle prompt: https://adventofcode.com/2018/day/7

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from collections import defaultdict

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 7

    def get_order_of_execution(self, lines) -> str:
        order = ""

        tasks, succ, depth = self.parse(lines)

        available_tasks = { task for task in tasks if depth[task] == 0 }

        while len(available_tasks) > 0:
            task = min(available_tasks) #get task with lowest depth

            order += task

            for dest in succ[task]:
                depth[dest] -= 1
                if depth[dest] == 0:
                    available_tasks.add(dest)
            
            available_tasks.remove(task)

        return order

    def get_execution_time(self,lines, workers=5, offset=60) -> int:
        tasks, succ, depth = self.parse(lines)

        worker_end_time = [0] * workers
        task_end_time = {}

        available_tasks = { task for task in tasks if depth[task] == 0 }
        task_start_time_bound = defaultdict(lambda: 0)  # lower bound for the start time of a task

        while len(available_tasks) > 0:            
            next_worker = min(range(workers), key=lambda i: worker_end_time[i])
                
            # Find the first available task, if tied get the one with the lowest letter
            task = min(available_tasks, 
                       key=lambda task: (max(worker_end_time[next_worker], task_start_time_bound[task]), task))

            task_end_time = max(worker_end_time[next_worker], task_start_time_bound[task]) + offset + 1 + ord(task) - ord("A")
            worker_end_time[next_worker] = task_end_time

            for dest in succ[task]:
                depth[dest] -= 1
                if depth[dest] == 0:
                    available_tasks.add(dest)
                
                task_start_time_bound[dest] = max(task_start_time_bound[dest], task_end_time) # +1 goes here?
            
            available_tasks.remove(task)

        return max(worker_end_time)

    #priority queue in disguise. for each destination, I add 1 to the depth
    #e.g. if A depends on B, I add 1 to depth[B]
    #if a task has no dependencies, its depth is 0 i.e. a starter
    def parse(self, lines):
        tasks = set()
        succ = defaultdict(set)  # set of successors
        depth = defaultdict(lambda: 0)

        for line in lines:
            parts = line.split()
            src = parts[1]
            dst = parts[7]
            tasks.update([src, dst])
            depth[dst] += 1
            succ[src].add(dst)

        return tasks, succ, depth
        
    def part_1(self):
        start_time = time.time()

        res = self.get_order_of_execution(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_execution_time(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()