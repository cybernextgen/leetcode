import unittest
from typing import List

data = (
    (["alice", "bob", "charlie"], "abc", True),
    (["an", "apple"], "a", False),
    (["never", "gonna", "give", "up", "on", "you"], "ngguoy", True),
)


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        
        return "".join(w[0] for w in words) == s


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for words, acr, expected in data:
            self.assertEqual(expected, s.isAcronym(words, acr))


if __name__ == "__main__":
    unittest.main()
