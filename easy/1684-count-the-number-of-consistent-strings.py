import unittest
from typing import List

data = (
    ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
    ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
    ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
)


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum([0 if set(w) - allowed_set else 1 for w in words])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for allowed, words, expected in data:
            self.assertEqual(s.countConsistentStrings(allowed, words), expected)


if __name__ == "__main__":
    unittest.main()
