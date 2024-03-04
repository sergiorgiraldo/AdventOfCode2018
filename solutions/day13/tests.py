import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "/->-\\        ",
            "|   |  /----\\",
            "| /-+--+-\\  |",
            "| | |  | v  |",
            "\\-+-/  \\-+--/",
            "  \\------/   "
        ]
        res = solution.get_first_crash(list)
        self.assertEqual(res, "7,3", "Oops")

    def test_part2(self):
        list =[
            "/>-<\\  ",
            "|   |  ",
            "| /<+-\\",
            "| | | v",
            "\\>+</ |",
            "  |   ^",
            "  \\<->/"
        ]
        self.assertEqual(solution.get_last_cart(list), "6,4", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()