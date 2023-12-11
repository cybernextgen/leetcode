import unittest
from typing import List

data = (([-5, 1, 5, 0, -7], 1), ([-4, -3, -2, -1, 4, 3, 2], 0))


class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height = 0
        for g in gain:
            current_height += g
            max_height = max(current_height, max_height)
        return max_height


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        initial_height = 0
        current_height = initial_height
        result = max(current_height := (current_height + g) for g in gain)
        return result if result > initial_height else initial_height


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for gain, expected in data:
            self.assertEqual(expected, s.largestAltitude(gain))


if __name__ == "__main__":
    unittest.main()
