import unittest
from typing import List
from collections import Counter

data = (
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)
        return res.most_common(1)[0][0]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.majorityElement(input_data))


if __name__ == "__main__":
    unittest.main()
