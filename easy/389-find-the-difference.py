import unittest
from collections import Counter
from typing import Optional
import functools

data = (("abcd", "abcde", "e"), ("", "y", "y"))


class Solution1:
    def findTheDifference(self, s: str, t: str) -> Optional[str]:
        chars_count = Counter(s)
        for char in t:
            if char in chars_count and chars_count[char] > 0:
                chars_count[char] -= 1
                continue
            return char


class Solution2:
    def findTheDifference(self, s: str, t: str) -> Optional[str]:
        return chr(functools.reduce(lambda x, y: x ^ ord(y), s + t, 0))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for str1, str2, expected in data:
            self.assertEqual(s.findTheDifference(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
