import unittest
from typing import List

data = (([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8))


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = set(range(0, len(nums) + 1))
        result = all_nums - set(nums)
        return result.pop()


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.missingNumber(input_data))


if __name__ == "__main__":
    unittest.main()
