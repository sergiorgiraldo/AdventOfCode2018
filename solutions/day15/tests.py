import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = ["#######",
                "#.G...#",
                ",#...EG#",
                ",#.#.#G#",
                ",#..G#E#",
                ",#.....#",
                ",#######"]
        self.assertEqual(solution.battle_pt1(list),27730, "Oops")

        list = ["#######",
                ",#G..#E#",
                ",#E#E.E#",
                ",#G.##.#",
                ",#...#E#",
                ",#...E.#",
                ",#######"]
        self.assertEqual(solution.battle_pt1(list),36334, "Oops")

        list = ["#######",
                ",#E..EG#",
                ",#.#G.E#",
                ",#E.##E#",
                ",#G..#.#",
                ",#..E#.#",
                ",#######"]
        self.assertEqual(solution.battle_pt1(list),39514, "Oops")

        list = ["#######",
                "#E.G#.#",
                "#.#G..#",
                "#G.#.G#",
                "#G..#.#",
                "#...E.#",
                "#######"]
        self.assertEqual(solution.battle_pt1(list),27755, "Oops")

        list = ["#######",
                "#.E...#",
                "#.#..G#",
                "#.###.#",
                "#E#G#G#",
                "#...#G#",
                "#######"]
        self.assertEqual(solution.battle_pt1(list),28944, "Oops")

        list = ["#########",
                "#G......#",
                "#.E.#...#",
                "#..##..G#",
                "#...##..#",
                "#...#...#",
                "#.G...G.#",
                "#.....G.#",
                "#########"]
        self.assertEqual(solution.battle_pt1(list),18740, "Oops")

    def test_part2(self):
        list = ["#######",
                "#.G...#",
                "#...EG#",
                "#.#.#G#",
                "#..G#E#",
                "#.....#",
                "#######"]
        self.assertEqual(solution.battle_pt2(list),4988, "Oops")

        list = ["#######",
                "#E..EG#",
                "#.#G.E#",
                "#E.##E#",
                "#G..#.#",
                "#..E#.#",
                "#######"]
        self.assertEqual(solution.battle_pt2(list),31284, "Oops")       

        list = ["#######",
                "#E.G#.#",
                "#.#G..#",
                "#G.#.G#",
                "#G..#.#",
                "#...E.#",
                "#######"]
        self.assertEqual(solution.battle_pt2(list),3478, "Oops")

        list = ["#######",
                "#.E...#",
                "#.#..G#",
                "#.###.#",
                "#E#G#G#",
                "#...#G#",
                "#######"]
        self.assertEqual(solution.battle_pt2(list),6474, "Oops")

        list = ["#########",
                "#G......#",
                "#.E.#...#",
                "#..##..G#",
                "#...##..#",
                "#...#...#",
                "#.G...G.#",
                "#.....G.#",
                "#########"]
        self.assertEqual(solution.battle_pt2(list),1140, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()