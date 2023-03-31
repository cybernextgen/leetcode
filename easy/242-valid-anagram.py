import unittest
from collections import Counter

data = (("anagram", "nagaram", True), ("rat", "car", False))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_s = Counter(s)
        chars_t = Counter(t)
        return chars_s == chars_t


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for s1, s2, expected in data:
            self.assertEqual(expected, s.isAnagram(s1, s2))


if __name__ == "__main__":
    unittest.main()
