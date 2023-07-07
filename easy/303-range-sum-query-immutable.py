import unittest
from typing import List
import itertools


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        for index in range(1, len(nums)):
            self.nums[index] += self.nums[index - 1]

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(s.sumRange(0, 2), 1)
        self.assertEqual(s.sumRange(2, 5), -1)
        self.assertEqual(s.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
