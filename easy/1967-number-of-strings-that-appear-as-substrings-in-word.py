import unittest
from typing import List

data = (
    (["a", "abc", "bc", "d"], "abc", 3),
    (["a", "b", "c"], "aaaaabbbbb", 2),
    (["a", "a", "a"], "ab", 3),
)


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([p in word for p in patterns])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for patterns, word, expected in data:
            self.assertEqual(expected, s.numOfStrings(patterns, word))


if __name__ == "__main__":
    unittest.main()
