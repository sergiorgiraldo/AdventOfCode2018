# puzzle prompt: https://adventofcode.com/2018/day/17

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import re
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 17

    def fill(self,m: dict[tuple[int,int],str], x: int, y: int, d: int):
        while m[x,y] == "|":
            m[x,y] = "~"
            x += d

    def flow(self,m: dict[tuple[int,int],str], ymax: int, x: int, y: int, d: int, print=False):
        if print: self.show_off(m)

        if y > ymax:
            return True
        
        if m[x,y] != ".": #water flows
            return m[x,y] == "|"

        m[x,y] = "|"
        
        if self.flow(m,ymax,x,y+1,0,print):
            return True

        if (d != 1 and self.flow(m,ymax,x-1,y,-1,print)) | (d != -1 and self.flow(m,ymax,x+1,y,1,print)):
            return True

        if d == 0: #water settles ...
            self.fill(m,x,y,-1)     # to the left
            self.fill(m,x+1,y,1)    # to the right

        return False

    def show_off(self,m: dict[tuple[int,int],str]):
        minx, maxx = min(x for x,_ in m), max(x for x,_ in m)
        miny, maxy = min(y for _,y in m), max(y for _,y in m)

        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                print(m[x,y],end="")
            print()
        print()

    def simulate_water_flow(self, lines, print=False) -> tuple[int, int]:
        self.ground = self.parse(lines)

        ymin, ymax = min(y for _,y in self.ground), max(y for _,y in self.ground)
        
        self.flow(self.ground,ymax,500,0,0,print)
        
        water = sum(self.ground[x,y] == "~" for x,y in self.ground if y >= ymin)
        
        flows = sum(self.ground[x,y] == "|" for x,y in self.ground if y >= ymin)
        
        return water+flows, water

    def parse(self, lines):
        ground = defaultdict(lambda: ".")
        
        for line in lines:
            fixed,start,end = [int(i) for i in re.findall("\d+",line)]
            
            is_horizontal = (line[0] == "x")
            
            for offset in range(start,end+1):
                ground[(fixed,offset) if is_horizontal else (offset,fixed)] = "#"

        return ground

    def part_1(self):
        start_time = time.time()

        res,_ = self.simulate_water_flow(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        _,res = self.simulate_water_flow(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()