import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        tree, _ = solution.parse([int(chr) for chr in s.split(' ')],0)
        res = solution.sum_metadata_entries(tree)

        self.assertEqual(res, 138, "Oops")

    def test_part2(self):
        s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        tree, _ = solution.parse([int(chr) for chr in s.split(' ')],0)
        res = solution.get_rootnode_value(tree)

        self.assertEqual(res, 66, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()