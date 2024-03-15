# puzzle prompt: https://adventofcode.com/2018/day/22

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import re

class PriorityQueue:
    def __init__(self, x, y):
        self.queue = []
        self.counter = 0
        self.target_x, self.target_y = x, y

    def heuristic(self, location):
        x, y, xx, yy = location[0], location[1], self.target_x, self.target_y
        return abs(x-xx) + abs(y-yy)

    def is_worse_than(self, position, new_list):
        position = int(position)
        """checks if item in given position is worse than new_list"""
        thisCost = self.queue[position][0] + \
            self.heuristic(self.queue[position][1])
        newCost = new_list[0] + self.heuristic(new_list[1])
        if thisCost > newCost:  # check cost
            return True
        elif thisCost == newCost:
            if self.queue[position][3] > new_list[3]:  # check counter
                return True
        return False

    def queue_is_empty(self):
        if len(self.queue) < 1:
            return True

    # should receive [cost_so_far, location, tool]
    def add(self, list_with_cost):
        cost_so_far, location, tool = list_with_cost
        self.counter += 1
        push_me = [cost_so_far, location, tool, self.counter]
        if self.queue_is_empty():
            self.queue[0:0] = [push_me]
            return
        low, mid, high = 0, 0, len(self.queue)-1
        while low < high-1:
            mid = (low+high)/2
            if self.is_worse_than(mid, push_me):
                high = mid-1
            else:
                low = mid+1

        low, mid, high = int(low), int(mid), int(high)  # cast to integer

        # the better cost should be lower in the PriorityQueue.
        # push_me is better than low and replaces it
        if self.is_worse_than(low, push_me):
            self.queue[low:low] = [push_me]
        # push_me is worse than high and comes above it
        elif not self.is_worse_than(high, push_me):
            self.queue[high+1:high+1] = [push_me]
        else:  # push_me is between low and high and replaces high
            self.queue[high:high] = [push_me]

    def pop(self):
        return self.queue.pop(0)


class Rescuer:
    def __init__(self, lines):
        self.depth, self.target_x, self.target_y, self.cave = Solution.parse(
            self, lines, True)
        self.min_time_to_target = 999_999_999

        for row, area in enumerate(self.cave):  # fill cave with tool numbers
            for col, _ in enumerate(area):
                self.cave[row][col] = self.cave[row][col] % 3

        max_x, max_y = self.target_x+100, self.target_y+100

        self.minimal_distances = []
        self.minimal_distances.append(
            [[-1]*(max_x+1) for y in range(max_y+1)])  # init torch
        self.minimal_distances.append(
            [[-1]*(max_x+1) for y in range(max_y+1)])  # init climbing
        self.minimal_distances.append(
            [[-1]*(max_x+1) for y in range(max_y+1)])  # init neither

    def pick_tool(self, curr, region):
        if region == 0:  # rocky can use torch or climbing
            if curr == 0:
                return 1
            elif curr == 1:
                return 0
            else:
                raise Exception("bad tool")
        elif region == 1:  # wet can use climbing or neither
            if curr == 1:
                return 2
            elif curr == 2:
                return 1
            else:
                raise Exception("bad tool")
        elif region == 2:  # narrow can use torch or neither
            if curr == 0:
                return 2
            elif curr == 2:
                return 0
            else:
                raise Exception("bad tool")
        else:
            raise Exception("bad region")

    def is_tool_valid(self, x, y, tool):
        tool1, tool2 = -1, -1
        valid = False
        if x >= 0 and x <= (self.target_x + 100) and y >= 0 and y <= (self.target_y + 100):
            tool1 = tool
            tool2 = ((tool-1) % 3)
            if self.cave[y][x] in [tool1, tool2]:
                valid = True

        return valid

    def update_distance(self, x, y, tool, val):
        self.minimal_distances[tool][y][x] = val

    # use A* algorithm to find santa's friend
    def rescue(self, x, y, mins, tool):
        rounds = 0

        pq = PriorityQueue(self.target_x, self.target_y)
        # pq items look like this: [cost, [coordinates], tool, counter]
        pq.add([mins, [x, y], tool])

        while not pq.queue_is_empty():
            rounds += 1

            curr_visit = pq.pop()

            cost, location, current_tool, _ = curr_visit

            curr_x, curr_y = location

            next_tool = self.pick_tool(current_tool, self.cave[curr_y][curr_x])

            if (location == [self.target_x, self.target_y]):  # found buddy
                if self.minimal_distances[0][self.target_y][self.target_x] != -1 and self.minimal_distances[0][self.target_y][self.target_x] < self.min_time_to_target:
                    self.min_time_to_target = self.minimal_distances[0][self.target_y][self.target_x]
                if self.minimal_distances[1][self.target_y][self.target_x] != -1 and self.minimal_distances[1][self.target_y][self.target_x]+7 < self.min_time_to_target:
                    self.min_time_to_target = self.minimal_distances[1][self.target_y][self.target_x]+7
            else:  # didn't find buddy
                # add neighbours with their cost and tool
                # go right with same tool
                if self.is_tool_valid(curr_x+1, curr_y, current_tool):
                    if cost+1 < self.minimal_distances[current_tool][curr_y][curr_x+1] or self.minimal_distances[current_tool][curr_y][curr_x+1] == -1:
                        pq.add([cost+1, [curr_x+1, curr_y], current_tool])
                        self.update_distance(
                            curr_x+1, curr_y, current_tool, cost+1)

                # go right with diff tool
                if self.is_tool_valid(curr_x+1, curr_y, next_tool):
                    if cost+8 < self.minimal_distances[next_tool][curr_y][curr_x+1] or self.minimal_distances[next_tool][curr_y][curr_x+1] == -1:
                        pq.add([cost+8, [curr_x+1, curr_y], next_tool])
                        self.update_distance(
                            curr_x+1, curr_y, next_tool, cost+8)

                # go down with same tool
                if self.is_tool_valid(curr_x, curr_y+1, current_tool):
                    if cost+1 < self.minimal_distances[current_tool][curr_y+1][curr_x] or self.minimal_distances[current_tool][curr_y+1][curr_x] == -1:
                        pq.add([cost+1, [curr_x, curr_y+1], current_tool])
                        self.update_distance(
                            curr_x, curr_y+1, current_tool, cost+1)

                # go down with diff tool
                if self.is_tool_valid(curr_x, curr_y+1, next_tool):
                    if cost+8 < self.minimal_distances[next_tool][curr_y+1][curr_x] or self.minimal_distances[next_tool][curr_y+1][curr_x] == -1:
                        pq.add([cost+8, [curr_x, curr_y+1], next_tool])
                        self.update_distance(
                            curr_x, curr_y+1, next_tool, cost+8)

                # go left with same tool
                if self.is_tool_valid(curr_x-1, curr_y, current_tool):
                    if cost+1 < self.minimal_distances[current_tool][curr_y][curr_x-1] or self.minimal_distances[current_tool][curr_y][curr_x-1] == -1:
                        pq.add([cost+1, [curr_x-1, curr_y], current_tool])
                        self.update_distance(
                            curr_x-1, curr_y, current_tool, cost+1)

                # go left with diff tool
                if self.is_tool_valid(curr_x-1, curr_y, next_tool):
                    if cost+8 < self.minimal_distances[next_tool][curr_y][curr_x-1] or self.minimal_distances[next_tool][curr_y][curr_x-1] == -1:
                        pq.add([cost+8, [curr_x-1, curr_y], next_tool])
                        self.update_distance(
                            curr_x-1, curr_y, next_tool, cost+8)

                # go up with same tool
                if self.is_tool_valid(curr_x, curr_y-1, current_tool):
                    if cost+1 < self.minimal_distances[current_tool][curr_y-1][curr_x] or self.minimal_distances[current_tool][curr_y-1][curr_x] == -1:
                        pq.add([cost+1, [curr_x, curr_y-1], current_tool])
                        self.update_distance(
                            curr_x, curr_y-1, current_tool, cost+1)

                if self.is_tool_valid(curr_x, curr_y-1, next_tool):  # go up with diff tool
                    if cost+8 < self.minimal_distances[next_tool][curr_y-1][curr_x] or self.minimal_distances[next_tool][curr_y-1][curr_x] == -1:
                        pq.add([cost+8, [curr_x, curr_y-1], next_tool])
                        self.update_distance(
                            curr_x, curr_y-1, next_tool, cost+8)


class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 22

    def parse(self, lines, to_rescue=False):
        input = [list(re.split(",| ", line)) for line in lines]

        depth = int(input[0][1])
        target_x, target_y = map(int, input[1][1:])

        if to_rescue:
            bound_y = target_y+100
            bound_x = target_x+100
        else:
            bound_y = target_y
            bound_x = target_x

        cave = [[0]*(bound_x+1) for _ in range(bound_y+1)]

        for row, area in enumerate(cave):
            for col, _ in enumerate(area):
                # get geologic index
                if col == target_x and row == target_y:
                    geo_index = 0
                elif col == 0:
                    geo_index = row*48271
                elif row == 0:
                    geo_index = col*16807
                else:
                    geo_index = (cave[row-1][col])*(cave[row][col-1])

                # erosion
                erosion = (geo_index+depth) % 20183
                cave[row][col] = erosion

        return depth, target_x, target_y, cave

    def get_risk_in_cave(self, lines):
        _, _, _, cave = self.parse(lines)

        risk = 0

        for row, area in enumerate(cave):
            for col, _ in enumerate(area):
                erosion = cave[row][col]
                risk += erosion % 3

        return risk

    def rescue_buddy(self, lines):
        rescuer = Rescuer(lines)

        rescuer.update_distance(0, 0, 0, 0)  # starting region is torch
        rescuer.rescue(0, 0, 0, 0)

        return rescuer.min_time_to_target

    def part_1(self):
        start_time = time.time()

        res = self.get_risk_in_cave(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.rescue_buddy(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == '__main__':
    solution = Solution()

    solution.part_1()

    solution.part_2()
