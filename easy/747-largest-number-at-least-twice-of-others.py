import unittest
from typing import List

data = (([3, 6, 1, 0], 1), ([1, 2, 3, 4], -1))


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        s = sorted(nums)

        max_num = s[-1]
        if max_num >= s[-2] * 2:
            return nums.index(max_num)
        return -1


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.dominantIndex(input_data), result)


if __name__ == "__main__":
    unittest.main()
