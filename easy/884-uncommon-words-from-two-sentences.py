import unittest
from typing import List
from collections import Counter

data = (
    ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
    ("apple apple", "banana", ["banana"]),
)


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter(f"{s1} {s2}".split())
        return [key for key, count in counts.items() if count == 1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for str1, str2, expected in data:
            self.assertListEqual(s.uncommonFromSentences(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
