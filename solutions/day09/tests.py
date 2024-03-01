import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        input = "9 players; last marble is worth 25 points"
        self.assertEqual(solution.play_marbles(input), 32, "Oops")

        input = "10 players; last marble is worth 1618 points"
        self.assertEqual(solution.play_marbles(input), 8317, "Oops")

        input = "13 players; last marble is worth 7999 points"
        self.assertEqual(solution.play_marbles(input), 146373, "Oops")

        input = "17 players; last marble is worth 1104 points"
        self.assertEqual(solution.play_marbles(input), 2764, "Oops")

        input = "21 players; last marble is worth 6111 points"
        self.assertEqual(solution.play_marbles(input), 54718, "Oops")

        input = "30 players; last marble is worth 5807 points"
        self.assertEqual(solution.play_marbles(input), 37305, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()