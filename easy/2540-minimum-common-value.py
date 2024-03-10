import unittest
from typing import List

data = (([1, 2, 3], [2, 4], 2), ([1, 2, 3, 6], [2, 3, 4, 5], 2))


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            element1 = nums1[index1]
            element2 = nums2[index2]
            if element1 == element2:
                return element1
            if element1 > element2:
                index2 += 1
            else:
                index1 += 1
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, nums2, expected in data:
            self.assertEqual(expected, s.getCommon(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
