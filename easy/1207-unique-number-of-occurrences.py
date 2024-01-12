import unittest
from typing import List
import collections

data = (
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return True

        counts = collections.Counter(arr)
        return len(counts.values()) == len(set(counts.values()))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.uniqueOccurrences(input_data), expected)


if __name__ == "__main__":
    unittest.main()
