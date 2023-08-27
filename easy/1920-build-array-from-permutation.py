import unittest
from typing import List

data = (
    ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
    ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
)


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.buildArray(input_data))


if __name__ == "__main__":
    unittest.main()
