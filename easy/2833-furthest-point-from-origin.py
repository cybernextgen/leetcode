import unittest
import collections


data = (("L_RL__R", 3), ("_R__LL_", 5), ("_______", 7))


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts = collections.Counter(moves)
        return abs(counts["L"] - counts["R"]) + counts["_"]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.furthestDistanceFromOrigin(input_data))


if __name__ == "__main__":
    unittest.main()
