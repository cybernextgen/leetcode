import unittest
from typing import List

data = (([1, 2, 3, 4, 5], 3, 18), ([5, 5, 5], 2, 11))


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        return int(k * (max_num + max_num + k - 1) / 2)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, k, expected in data:
            self.assertEqual(s.maximizeSum(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
