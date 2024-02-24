import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        chgs = ["+1", "-2", "+3", "+1"]
        self.assertEqual(solution.get_final_frequency(chgs), 3, "Oops")

    def test_part2(self):
        chgs = ["+1", "-2", "+3", "+1"]
        self.assertEqual(solution.get_repeating_frequency(chgs), 2, "Oops")

        chgs = ["+1", "-1"]
        self.assertEqual(solution.get_repeating_frequency(chgs), 0, "Oops")

        chgs = ["+3", "+3", "+4", "-2", "-4"]
        self.assertEqual(solution.get_repeating_frequency(chgs), 10, "Oops")

        chgs = ["-6", "+3", "+8", "+5", "-6"]
        self.assertEqual(solution.get_repeating_frequency(chgs), 5, "Oops")

        chgs = ["+7", "+7", "-2", "-7", "-4"]
        self.assertEqual(solution.get_repeating_frequency(chgs), 14, "Oops")

    def test_sanity_check(self):    
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()