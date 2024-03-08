# puzzle prompt: https://adventofcode.com/2018/day/16

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
import re

class Interpreter:
    def addr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] + status[B]
        return result

    def addi(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] + B
        return result

    def mulr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] * status[B]
        return result

    def muli(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] * B
        return result

    def banr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] & status[B]
        return result

    def bani(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] & B
        return result

    def borr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] | status[B]
        return result

    def bori(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A] | B
        return result

    def setr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = status[A]
        return result

    def seti(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = A
        return result

    def gtir(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if A > status[B] else 0
        return result

    def gtri(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if status[A] > B else 0
        return result

    def gtrr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if status[A] > status[B] else 0
        return result

    def eqir(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if A == status[B] else 0
        return result

    def eqri(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if status[A] == B else 0
        return result

    def eqrr(opcodes, status):
        A, B, C = opcodes[1:]
        result = status.copy()
        result[C] = 1 if status[A] == status[B] else 0
        return result


class Solution(InputAsLinesSolution):
    _year = 2018
    _day = 16

    instructions = [Interpreter.addr, Interpreter.addi, Interpreter.mulr, Interpreter.muli, 
                    Interpreter.banr, Interpreter.bani, Interpreter.borr, Interpreter.bori, 
                    Interpreter.setr, Interpreter.seti, Interpreter.gtir, Interpreter.gtri, 
                    Interpreter.gtrr, Interpreter.eqir, Interpreter.eqri, Interpreter.eqrr]

    def parse(self, lines):
        samples = []
        i = 0

        while lines[i].startswith("Before"):
            status_before   = [int(i) for i in re.findall("\d+", lines[i])]
            opcodes         = [int(i) for i in re.findall("\d+", lines[i+1])]
            status_after    = [int(i) for i in re.findall("\d+", lines[i+2])]
            
            samples.append((status_before, opcodes, status_after))
            
            i += 4

        test_program = [list(map(int, line.split(" "))) for line in lines[i+2:]]

        return samples, test_program
    
    def find_good_samples(self, lines):
        samples, _ = self.parse(lines)
        good_samples = 0

        for observation in samples:
            status_before, opcodes, status_after = observation
            candidates = set(filter(lambda instr: instr(opcodes, status_before) == status_after, self.instructions))
            good_samples += 1 if len(candidates) >= 3 else 0

        return good_samples

    def run_program(self, lines):
        samples, test_program = self.parse(lines)
        registers = [0] * 4
        decoder = {}

        while True:
            unknown_opcodes = { sample[1][0] for sample in samples }.difference(decoder.keys())
            
            if len(unknown_opcodes) == 0:
                break

            # For each unknown opcode, we check if any of the unused instructions is valid for _all_ samples with that opcode
            for code in unknown_opcodes:
                candidates = set(self.instructions).difference(decoder.values())
                for sample in filter(lambda s: s[1][0] == code, samples):
                    status_before, opcodes, status_after = sample
                    removed_candidates = { instr for instr in candidates if instr(opcodes, status_before) != status_after }
                    candidates.difference_update(removed_candidates)
                    
                if len(candidates) == 1:
                    decoder[opcodes[0]] = candidates.pop()

        for opcodes in test_program:
            registers = decoder[opcodes[0]](opcodes, registers)

        return registers[0]

    def part_1(self):
        start_time = time.time()

        res = self.find_good_samples(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.run_program(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()