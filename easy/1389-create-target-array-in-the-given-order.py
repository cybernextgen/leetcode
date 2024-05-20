from typing import List


class Solution:
    def createTargetArray(
        self, nums: List[int], target_indexes: List[int]
    ) -> List[int]:
        result = []
        for index, num in enumerate(nums):
            target_index = target_indexes[index]
            result = result[:target_index] + [num] + result[target_index:]
        return result


if __name__ == "__main__":
    for nums, indexes, expected in (
        ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]),
    ):
        assert Solution().createTargetArray(nums, indexes) == expected
