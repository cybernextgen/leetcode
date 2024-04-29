from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len(list(filter(lambda x: x < k, nums)))


if __name__ == "__main__":
    for input_data, k, expected in (
        ([2, 11, 10, 1, 3], 10, 3),
        ([1, 1, 2, 4, 9], 1, 0),
        ([1, 1, 2, 4, 9], 9, 4),
    ):
        assert Solution().minOperations(input_data, k) == expected
