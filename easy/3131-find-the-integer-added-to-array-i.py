from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) // len(nums2)) - (sum(nums1) // len(nums1))


if __name__ == "__main__":
    for nums1, nums2, expected in (
        ([2, 6, 4], [9, 7, 5], 3),
        ([10], [5], -5),
        ([1, 1, 1, 1], [1, 1, 1, 1], 0),
    ):
        assert Solution().addedInteger(nums1, nums2) == expected
