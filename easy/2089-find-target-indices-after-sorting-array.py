import unittest
from typing import List
import bisect

data = (
    ([1, 2, 5, 2, 3], 2, [1, 2]),
    ([1, 2, 5, 2, 3], 3, [3]),
    ([1, 2, 5, 2, 3], 5, [4]),
)


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        current_index = bisect.bisect_left(sorted_nums, target)
        result = []
        while True:
            if current_index == len(sorted_nums):
                return result

            current_num = sorted_nums[current_index]
            if current_num == target:
                result.append(current_index)
                current_index += 1
            else:
                return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, target, expected in data:
            self.assertEqual(expected, s.targetIndices(nums, target))


if __name__ == "__main__":
    unittest.main()
