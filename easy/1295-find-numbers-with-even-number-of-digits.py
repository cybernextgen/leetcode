import unittest
from typing import List
import functools

data = (
    ([12, 345, 2, 6, 7896], 2),
    ([555, 901, 482, 1771], 1),
)


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return functools.reduce(
            lambda x, y: x + 1 if not len(str(y)) % 2 else x, nums, 0
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findNumbers(input_data), expected)


if __name__ == "__main__":
    unittest.main()
