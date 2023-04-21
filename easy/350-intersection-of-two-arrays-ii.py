import unittest
from typing import List
from collections import Counter

data = (([1, 2, 2, 1], [2, 2], [2, 2]), ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]))


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = Counter(nums1)
        nums2_counts = Counter(nums2)
        intersect_keys = nums1_counts & nums2_counts
        result = []
        for key in intersect_keys:
            intersect_counts = nums1_counts[key]
            counts2 = nums2_counts[key]
            if intersect_counts > counts2:
                intersect_counts = counts2

            while intersect_counts > 0:
                result.append(key)
                intersect_counts -= 1
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for list1, list2, expected in data:
            self.assertListEqual(s.intersect(list1, list2), expected)


if __name__ == "__main__":
    unittest.main()
