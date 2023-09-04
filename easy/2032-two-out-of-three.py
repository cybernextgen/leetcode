import unittest
import collections
from typing import List

data = (
    ([1, 1, 3, 2], [2, 3], [3], [3, 2]),
    ([3, 1], [2, 3], [1, 2], [2, 3, 1]),
    ([1, 2, 2], [4, 3, 3], [5], []),
)


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        total_counts = (
            collections.Counter(set(nums1))
            + collections.Counter(set(nums2))
            + collections.Counter(set(nums3))
        )
        return [key for key, val in total_counts.items() if val > 1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, nums2, nums3, expected in data:
            self.assertListEqual(expected, s.twoOutOfThree(nums1, nums2, nums3))


if __name__ == "__main__":
    unittest.main()
