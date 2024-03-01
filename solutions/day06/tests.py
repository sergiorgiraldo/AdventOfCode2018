import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ]

        res, _ = solution.parse_grid(list)

        self.assertEqual(res, 17, "Oops")

    def test_part2(self):
        list = [
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ]

        _, res = solution.parse_grid(list, 32)

        self.assertEqual(res, 16, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()