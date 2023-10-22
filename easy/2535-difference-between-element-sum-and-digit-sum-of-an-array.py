import unittest
from typing import List

data = (([1, 15, 6, 3], 9), ([1, 2, 3, 4], 0))


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        array_sum = sum(nums)
        digits_str = "".join(str(d) for d in nums)
        digits_sum = sum(int(d) for d in "".join(digits_str))
        return abs(array_sum - digits_sum)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.differenceOfSum(nums))


if __name__ == "__main__":
    unittest.main()
