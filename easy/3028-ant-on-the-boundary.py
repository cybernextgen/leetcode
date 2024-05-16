from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sum = 0
        result = 0
        for n in nums:
            sum += n
            if sum == 0:
                result += 1
        return result


if __name__ == "__main__":
    for input_data, expected in (([2, 3, -5], 1), ([3, 2, -3, -4], 0)):
        assert Solution().returnToBoundaryCount(input_data) == expected
