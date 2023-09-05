import unittest
from typing import List

data = (
    (
        [
            "alice and bob love leetcode",
            "i think so too",
            "this is great thanks very much",
        ],
        6,
    ),
    (["please wait", "continue to fight", "continue to win"], 3),
)


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(w.split()) for w in sentences])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for sentences, expected in data:
            self.assertEqual(expected, s.mostWordsFound(sentences))


if __name__ == "__main__":
    unittest.main()
