import unittest
import functools
from typing import List

data = (("1010", "1011", "10101"), ("11", "1", "100"))


class Solution:
    def addBinary(self, *args: str) -> str:
        result = functools.reduce(lambda res, arg: res + int(arg, 2), args, 0)
        return f"{result:b}"


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for a, b, result in data:
            self.assertEqual(result, s.addBinary(a, b))


if __name__ == "__main__":
    unittest.main()
