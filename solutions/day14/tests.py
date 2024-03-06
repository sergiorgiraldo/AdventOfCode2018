import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        res,_ = solution.cook("9")
        self.assertEqual(res, "5158916779", "Oops")
        res,_ = solution.cook("5")
        self.assertEqual(res, "0124515891", "Oops")
        res,_ = solution.cook("18")
        self.assertEqual(res, "9251071085", "Oops")
        res,_ = solution.cook("2018")
        self.assertEqual(res, "5941429882", "Oops")

    def test_part2(self):
        _,res = solution.cook("51589")
        self.assertEqual(res, 9, "Oops")
        _,res = solution.cook("01245")
        self.assertEqual(res, 5, "Oops")
        _,res = solution.cook("92510")
        self.assertEqual(res, 18, "Oops")
        _,res = solution.cook("59414")
        self.assertEqual(res, 2018, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()