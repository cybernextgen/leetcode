import unittest
from typing import List

data = (
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5, [1, 2, 3, 4, 5, 6]),
)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]
        index1 = 0
        index2 = 0
        max_index1 = m
        while index1 < max_index1 and index2 < n:
            element1 = nums1[index1]
            element2 = nums2[index2]
            if element2 < element1:
                nums1.pop()
                nums1.insert(index1, element2)
                max_index1 += 1
                index2 += 1
            index1 += 1
        if index2 != n:
            nums1[m + index2 : m + n] = nums2[index2:n]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, m, nums2, n, expected in data:
            s.merge(nums1, m, nums2, n)
            self.assertListEqual(expected, nums1)


if __name__ == "__main__":
    unittest.main()
