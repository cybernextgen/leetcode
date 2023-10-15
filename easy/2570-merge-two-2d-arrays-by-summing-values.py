import unittest
from typing import List

data = (
    (
        [[1, 2], [2, 3], [4, 5]],
        [[1, 4], [3, 2], [4, 1]],
        [[1, 6], [2, 3], [3, 2], [4, 6]],
    ),
    (
        [[2, 4], [3, 6], [5, 5]],
        [[1, 3], [4, 3]],
        [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]],
    ),
)


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        mapping = {key: val for (key, val) in nums1}
        for key, val in nums2:
            if key in mapping:
                mapping[key] += val
            else:
                mapping[key] = val

        return [[key, mapping[key]] for key in sorted(mapping.keys())]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, nums2, expected in data:
            self.assertListEqual(expected, s.mergeArrays(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
