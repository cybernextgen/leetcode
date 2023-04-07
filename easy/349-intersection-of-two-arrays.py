import unittest
from typing import List

data = (([1, 2, 2, 1], [2, 2], [2]), ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]))


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for l1, l2, expected in data:
            self.assertListEqual(expected, s.intersection(l1, l2))


if __name__ == "__main__":
    unittest.main()
