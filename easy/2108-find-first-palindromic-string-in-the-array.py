import unittest
from typing import List

data = (
    (["abc", "car", "ada", "racecar", "cool"], "ada"),
    (["notapalindrome", "racecar"], "racecar"),
    (["def", "ghi"], ""),
)


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for words, expected in data:
            self.assertEqual(expected, s.firstPalindrome(words))


if __name__ == "__main__":
    unittest.main()
