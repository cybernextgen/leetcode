import unittest
from typing import List
import collections

data = (([1, 2, 2, 3, 1, 4], 4), ([1, 2, 3, 4, 5], 5))


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len(nums) < 2:
            return len_nums

        counts = collections.Counter(nums)

        result = 0
        sorted_counts = counts.most_common()
        max_freq = sorted_counts[0][1]
        for n, f in counts.most_common():
            if f != max_freq:
                break
            result += 1

        return result * max_freq


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.maxFrequencyElements(nums), expected)


if __name__ == "__main__":
    unittest.main()
