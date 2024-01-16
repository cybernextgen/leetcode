import unittest
from typing import List
import itertools

data = (([-1, 1, 2, 3, 1], 2, 3), ([-6, 2, 5, -2, -7, -1, 3], -2, 10))


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        for a, b in itertools.combinations(nums, 2):
            if a + b < target:
                result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, target, expected in data:
            self.assertEqual(s.countPairs(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
