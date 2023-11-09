import unittest
from typing import List

data = (
    (
        ["one.two.three", "four.five", "six"],
        ".",
        ["one", "two", "three", "four", "five", "six"],
    ),
    (["$easy$", "$problem$"], "$", ["easy", "problem"]),
    (["|||"], "|", []),
)


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [
            word
            for several_words in words
            for word in several_words.split(separator)
            if word
        ]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for words, separator, expected in data:
            self.assertListEqual(expected, s.splitWordsBySeparator(words, separator))


if __name__ == "__main__":
    unittest.main()
