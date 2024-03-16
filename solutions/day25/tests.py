import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
                "0,0,0,0",
                "3,0,0,0",
                "0,3,0,0",
                "0,0,3,0",
                "0,0,0,3",
                "0,0,0,6",
                "9,0,0,0",
                "12,0,0,0"
        ]
        self.assertEqual(solution.count_constellations(list), 2, "Oops")

        list = [
                "-1,2,2,0",
                "0,0,2,-2",
                "0,0,0,-2",
                "-1,2,0,0",
                "-2,-2,-2,2",
                "3,0,2,-1",
                "-1,3,2,2",
                "-1,0,-1,0",
                "0,2,1,-2",
                "3,0,0,0"]
        self.assertEqual(solution.count_constellations(list), 4, "Oops")

        list = [
                "1,-1,0,1",
                "2,0,-1,0",
                "3,2,-1,0",
                "0,0,3,1",
                "0,0,-1,-1",
                "2,3,-2,0",
                "-2,2,0,0",
                "2,-2,0,-1",
                "1,-1,0,-1",
                "3,2,0,2"]
        self.assertEqual(solution.count_constellations(list), 3, "Oops")
        
        list = [
                "1,-1,-1,-2",
                "-2,-2,0,1",
                "0,2,1,3",
                "-2,3,-2,1",
                "0,2,3,-2",
                "-1,-1,1,-2",
                "0,-2,-1,0",
                "-2,2,3,-1",
                "1,2,2,0",
                "-1,-2,0,-2"]
        self.assertEqual(solution.count_constellations(list), 8, "Oops")

    #def test_part2(self):
    #    self.assertEqual(solution.part2(), "", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()