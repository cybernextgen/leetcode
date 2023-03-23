import unittest
from typing import List
import functools

data = (
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda s, e: s ^ e, nums)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.singleNumber(input_data))


if __name__ == "__main__":
    unittest.main()
