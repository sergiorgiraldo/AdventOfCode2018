import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        serial = 18
        self.assertEqual(solution.get_best_3x3square(serial), "33,45", "Oops")
        serial = 42
        self.assertEqual(solution.get_best_3x3square(serial), "21,61", "Oops")

    def test_part2(self):
        serial = 18
        self.assertEqual(solution.get_best_square(serial), "90,269,16", "Oops")
        serial = 42
        self.assertEqual(solution.get_best_square(serial), "232,251,12", "Oops")
       
    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()