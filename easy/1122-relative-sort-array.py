import unittest
from typing import List
import collections

data = (
    (
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
        [2, 1, 4, 3, 9, 6],
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    ),
    ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
)


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = collections.Counter(arr1)
        result = []

        for n in arr2:
            result += [n] * counts[n]
            del counts[n]

        for key in sorted(counts.keys()):
            result += [key] * counts[key]

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for arr1, arr2, expected in data:
            self.assertEqual(s.relativeSortArray(arr1, arr2), expected)


if __name__ == "__main__":
    unittest.main()
