# puzzle prompt: https://adventofcode.com/2018/day/13

import time
import sys
sys.path.insert(0, "..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 13

    rail_map = []
    carts = []

    _next_char = {
        ">-"   : ">",
        ">/"   : "^",
        ">\\"  : "v",
        
        "<-"   : "<",
        "</"   : "v",
        "<\\"  : "^",
        
        "^|"   : "^",
        "^/"   : ">",
        "^\\"  : "<",
        
        "v|"   : "v",
        "v/"   : "<",
        "v\\"  : ">",
        
        ">+0"  : "^",
        ">+1"  : ">",
        ">+2"  : "v",
        
        "<+0"  : "v",
        "<+1"  : "<",
        "<+2"  : "^",
        
        "^+0"  : "<",
        "^+1"  : "^",
        "^+2"  : ">",
        
        "v+0"  : ">",
        "v+1"  : "v",
        "v+2"  : "<",
    }

    _next_location = {
        ">": lambda x,y: (x+1, y),
        "<": lambda x,y: (x-1, y),
        "^": lambda x,y: (x, y-1),
        "v": lambda x,y: (x, y+1)
    }

    def get_next_location(self,x,y,char):
        return self._next_location[char](x,y);
        
    def get_next_char(self,char,rail,turn):
        return self._next_char[char+rail+(turn if rail == "+" else "")]

    def arrange_carts(self,carts):
        sorted_cart = []
        while len(carts) > 0:
            idx = 0
            if len(carts) > 1:
                for i in range(1,len(carts)):
                    if (carts[idx][1] > carts[i][1]) or (carts[idx][1] == carts[i][1] and carts[idx][0] > carts[i][0]):
                        idx = i
            sorted_cart.append(carts.pop(idx))
        
        return sorted_cart

    def parse(self, lines):
        self.carts = []
        self.rail_map = []

        for idx in range(0, len(lines)):
            line = lines[idx]
            self.carts += [(i,idx,char,0,False) for i, char in enumerate(line) if char in ['>','<','^','v']]
            self.rail_map.append(line.replace(">","-").replace("<","-").replace("^","|").replace("v","|"))

    def get_first_crash(self, lines):
        self.parse(lines)

        crash = ()
        while True:
            try:
                for i,cart in enumerate(self.carts):
                    next_x, next_y = self.get_next_location(cart[0],cart[1],cart[2])
                    
                    next_char = self.get_next_char(cart[2],self.rail_map[next_y][next_x],str(cart[3]))
                    
                    next_cart = (next_x, next_y, next_char, 
                                (cart[3]+1)%3 if self.rail_map[next_y][next_x] == "+" else cart[3])
                    
                    crash = next((any_cart for any_cart in self.carts 
                                  if any_cart[0] == next_cart[0] and any_cart[1] == next_cart[1]), None)

                    if crash: raise StopIteration
                    
                    self.carts[i] = next_cart
            except StopIteration:
                break

            self.carts = self.arrange_carts(self.carts)
            
        return str(crash[0]) + "," + str(crash[1])

    def get_last_cart(self, lines):
        self.parse(lines)

        last_cart = []
        while True:
            for idx,cart in enumerate(self.carts):
                if cart[4]:
                    continue
                next_x, next_y = self.get_next_location(cart[0],cart[1],cart[2])

                next_char = self.get_next_char(cart[2],self.rail_map[next_y][next_x],str(cart[3]))

                next_cart = (next_x, next_y, next_char, 
                            (cart[3]+1)%3 if self.rail_map[next_y][next_x] == "+" else cart[3], False)

                for i, any_cart in enumerate(self.carts):
                    if not any_cart[4] and any_cart[0] == next_cart[0] and any_cart[1] == next_cart[1]:
                        self.carts[i] = (any_cart[0], any_cart[1], any_cart[2], any_cart[3], True)
                        next_cart = (next_cart[0], next_cart[1], next_cart[2], next_cart[3], True)
                
                self.carts[idx] = next_cart
            
            if len([cart for cart in self.carts if not cart[4]]) == 1:
                last_cart = [cart for cart in self.carts if not cart[4]]
                break
            
            self.carts = self.arrange_carts(self.carts)
            
        return str(last_cart[0][0]) + "," + str(last_cart[0][1])

    def part_1(self):
        start_time = time.time()

        res = self.get_first_crash(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_last_cart(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
