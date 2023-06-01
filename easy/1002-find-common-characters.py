import unittest
from typing import List
import collections
import functools

data = (
    (["bella", "label", "roller"], ["e", "l", "l"]),
    (["cool", "lock", "cook"], ["c", "o"]),
)


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        initial = collections.Counter(words[0])
        intersection = functools.reduce(
            lambda x, y: x & collections.Counter(y), words[1:], initial
        )
        return list(intersection.elements())


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.commonChars(input_data), expected)


if __name__ == "__main__":
    unittest.main()
