import unittest
from typing import List
import collections

data = (([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6], [3, 4]), ([3, 4, 2, 3], [1, 5], [0, 0]))


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = collections.Counter(nums1)
        nums2_counts = collections.Counter(nums2)
        nums_intersection = nums1_counts & nums2_counts

        result = [0, 0]
        for num in nums_intersection.keys():
            result[0] += nums1_counts[num]
            result[1] += nums2_counts[num]

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, nums2, expected in data:
            self.assertListEqual(expected, s.findIntersectionValues(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
