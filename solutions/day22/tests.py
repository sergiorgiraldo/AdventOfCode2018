import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "depth: 510",
            "target: 10,10"
        ]
        self.assertEqual(solution.get_risk_in_cave(list), 114, "Oops")

    def test_part2(self):
        list = [
            "depth: 510",
            "target: 10,10"
        ]
        self.assertEqual(solution.rescue_buddy(list), 45, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()