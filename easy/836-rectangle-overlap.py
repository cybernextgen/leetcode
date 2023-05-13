import unittest
from typing import List

data = (
    ([0, 0, 2, 2], [1, 1, 3, 3], True),
    ([0, 0, 1, 1], [1, 0, 2, 1], False),
    ([0, 0, 1, 1], [2, 2, 3, 3], False),
    ([7, 8, 13, 15], [10, 8, 12, 20], True),
)


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])
        if left < right and bottom < top:
            return True
        return False


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for rect1, rect2, expected in data:
            self.assertEqual(s.isRectangleOverlap(rect1, rect2), expected)


if __name__ == "__main__":
    unittest.main()
