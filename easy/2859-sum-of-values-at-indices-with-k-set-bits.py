import unittest
from typing import List

data = (([5, 10, 1, 5, 2], 1, 13), ([4, 3, 2, 1], 2, 1))


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(nums[i] for i, n in enumerate(nums) if f"{i:b}".count("1") == k)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, k, expected in data:
            self.assertEqual(expected, s.sumIndicesWithKSetBits(nums, k))


if __name__ == "__main__":
    unittest.main()
