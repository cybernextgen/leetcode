import unittest
from typing import Callable
from functools import partial

data = ((5, 4, 4), (1, 1, 1))

isBadVersion: Callable


def isBadVersionProducer(n: int, bad_version: int) -> bool:
    if n >= bad_version:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_index = 0
        right_index = n
        while left_index < right_index:
            median_index = left_index + (right_index - left_index) // 2
            if isBadVersion(median_index):
                right_index = median_index
                continue
            left_index = median_index + 1
        return left_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        global isBadVersion

        for input_data, bad_version, result in data:
            isBadVersion = partial(isBadVersionProducer, bad_version=bad_version)
            self.assertEqual(result, s.firstBadVersion(input_data))


if __name__ == "__main__":
    unittest.main()
