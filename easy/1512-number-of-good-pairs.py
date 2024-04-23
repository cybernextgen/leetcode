from typing import List, Dict
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        counts: Dict[int, int] = defaultdict(int)
        for val in nums:
            result += counts[val]
            counts[val] += 1
        return result


if __name__ == "__main__":
    for input_data, expected in (
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ):
        assert Solution().numIdenticalPairs(input_data) == expected
