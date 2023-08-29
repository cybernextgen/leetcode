import unittest
import itertools
from typing import List

data = (([1, 2, 1], [1, 2, 1, 1, 2, 1]), ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]))


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return list(itertools.chain(nums, nums))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.getConcatenation(input_data))


if __name__ == "__main__":
    unittest.main()
