import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        regex = "^WNE$"
        self.assertEqual(solution.find_doors(regex)[0], 3, "Oops")

        regex = "^ENWWW(NEEE|SSE(EE|N))$"
        self.assertEqual(solution.find_doors(regex)[0], 10, "Oops")

        regex = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
        self.assertEqual(solution.find_doors(regex)[0], 18, "Oops")

        regex = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
        self.assertEqual(solution.find_doors(regex)[0], 23, "Oops")

        regex = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
        self.assertEqual(solution.find_doors(regex)[0], 31, "Oops")

    #def test_part2(self):
    #    self.assertEqual(solution.part2(), "", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()