import unittest
from typing import List
import functools

data = (([-1, -2, -3, -4, 3, 2, 1], 1), ([1, 5, 0, 2, -3], 0), ([-1, 1, -1, 1, -1], -1))


class Solution1:
    def arraySign(self, nums: List[int]) -> int:
        product = functools.reduce(lambda x, y: x * y, nums, 1)
        if not product:
            return 0
        return 1 if product > 0 else -1


class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if not n:
                return 0
            if n < 0:
                sign = -sign
        return sign


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, expected in data:
            self.assertEqual(s.arraySign(input_data), expected)


if __name__ == "__main__":
    unittest.main()
