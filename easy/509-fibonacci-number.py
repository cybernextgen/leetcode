import unittest
from functools import cache

data = ((2, 1), (3, 2), (4, 3))


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.fib(input_data), expected)


if __name__ == "__main__":
    unittest.main()
