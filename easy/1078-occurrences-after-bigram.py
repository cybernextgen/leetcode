import unittest
from typing import List
import re

data = (
    ("alice is a good girl she is a good student", "a", "good", ["girl", "student"]),
    ("we will we will rock you", "we", "will", ["we", "rock"]),
    ("alice is aa good girl she is a good student", "a", "good", ["student"]),
    ("we we we we will rock you", "we", "we", ["we", "we", "will"]),
)


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words_list = text.split()
        result = []
        for word1, word2, word3 in zip(words_list, words_list[1:], words_list[2:]):
            if word1 == first and word2 == second:
                result.append(word3)
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()
        for text, a, b, result in data:
            self.assertListEqual(s.findOcurrences(text, a, b), result)


if __name__ == "__main__":
    unittest.main()
