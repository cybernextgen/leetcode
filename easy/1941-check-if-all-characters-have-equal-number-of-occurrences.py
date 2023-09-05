import unittest
import collections

data = (("abacbc", True), ("aaabb", False))


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = collections.Counter(s)
        return len(set(counts.values())) == 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for word, expected in data:
            self.assertEqual(expected, s.areOccurrencesEqual(word))


if __name__ == "__main__":
    unittest.main()
