import unittest
import functools
from typing import Generator

data = ((5, 0, 8), (4, 3, 8))


def items_generator(n, start) -> Generator[int, None, None]:
    current_index = 0
    while current_index < n:
        yield start + current_index * 2
        current_index += 1


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        g = items_generator(n, start)
        return functools.reduce(lambda x, y: x ^ y, g)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for n, start, expected in data:
            self.assertEqual(expected, s.xorOperation(n, start))


if __name__ == "__main__":
    unittest.main()
