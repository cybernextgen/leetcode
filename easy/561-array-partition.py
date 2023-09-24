import unittest
from typing import List
import heapq

data = (([1, 4, 3, 2], 4), ([6, 2, 6, 5, 1, 2], 9))


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        heapq.heapify(nums)
        while nums:
            result += heapq.heappop(nums)
            heapq.heappop(nums)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for nums, expected in data:
            self.assertEqual(expected, s.arrayPairSum(nums))


if __name__ == "__main__":
    unittest.main()
