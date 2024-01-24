import unittest
from typing import List

data = (([[3, 6], [1, 5], [4, 7]], 7), ([[1, 3], [5, 8]], 7))


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result = set()
        for start_point, end_point in nums:
            for point in range(start_point, end_point + 1):
                result.add(point)
        return len(result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.numberOfPoints(nums), expected)


if __name__ == "__main__":
    unittest.main()
