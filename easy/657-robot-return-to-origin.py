import unittest
import collections


data = (("UD", True), ("LL", False), ("URDL", True))


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_counts = collections.Counter(moves)
        return (
            moves_counts["U"] == moves_counts["D"]
            and moves_counts["L"] == moves_counts["R"]
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for moves, expected in data:
            self.assertEqual(expected, s.judgeCircle(moves))


if __name__ == "__main__":
    unittest.main()
