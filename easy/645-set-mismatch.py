import unittest
from typing import List

data = (([1, 2, 2, 4], [2, 3]), ([1, 1], [1, 2]))


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_nums_set = sum(set(nums))
        return [
            sum(nums) - sum_nums_set,
            len(nums) * (len(nums) + 1) // 2 - sum_nums_set,
        ]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.findErrorNums(nums), expected)


if __name__ == "__main__":
    unittest.main()
