import unittest
from typing import List

data = (
    ([1, 6, 7, 5, 2, 4, 10, 6, 4], 68),
    ([5, 6, 2, 7, 4], 34),
    ([4, 2, 5, 9, 7, 4, 8], 64),
)


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_num = 10**5
        pair1 = [max_num, max_num]
        pair2 = [0, 0]
        for n in nums:
            if n < pair1[0]:
                pair1[1] = pair1[0]
                pair1[0] = n
            elif n < pair1[1]:
                pair1[1] = n

            if n > pair2[0]:
                pair2[1] = pair2[0]
                pair2[0] = n
            elif n > pair2[1]:
                pair2[1] = n

        return pair2[0] * pair2[1] - pair1[0] * pair1[1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.maxProductDifference(nums))


if __name__ == "__main__":
    unittest.main()
