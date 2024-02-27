import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solution.build_polymer("dabAcCaCBAcCcaDA"), 10, "Oops")

    def test_part2(self):
       self.assertEqual(solution.enhance_polymer("dabAcCaCBAcCcaDA"), 4, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()