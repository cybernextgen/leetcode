import unittest
import re

data = (("hello world", "ad", 1), ("leet code", "lt", 1), ("leet code", "e", 0))


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return len(re.findall(rf"\b[^{brokenLetters}\s]+\b", text))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for text, broken_letters, expected in data:
            self.assertEqual(expected, s.canBeTypedWords(text, broken_letters))


if __name__ == "__main__":
    unittest.main()
