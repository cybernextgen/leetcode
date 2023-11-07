import unittest


data = (("B0B6G0R6R0R6G9", 1), ("B0R0G0R9R0B0G0", 1), ("G4", 0))


class Solution:
    def countPoints(self, rings: str) -> int:
        colors_for_rods = [set() for i in range(0, 10)]

        for index in range(0, len(rings), 2):
            color = rings[index]
            rod = int(rings[index + 1])
            colors_for_rods[rod].add(color)

        return len(list(filter(lambda x: len(x) == 3, colors_for_rods)))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for rings, expected in data:
            self.assertEqual(expected, s.countPoints(rings))


if __name__ == "__main__":
    unittest.main()
