from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = -1
        for num in nums_set:
            if -num not in nums_set:
                continue
            positive_num = abs(num)
            result = positive_num if positive_num > result else result
        return result


if __name__ == "__main__":
    for input_data, expected in (
        ([-1, 2, -3, 3], 3),
        ([-1, 10, 6, 7, -7, 1], 7),
        ([-10, 8, 6, 7, -2, -3], -1),
    ):
        assert Solution().findMaxK(input_data) == expected
