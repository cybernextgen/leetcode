import unittest
from typing import List

data = ((["cd", "ac", "dc", "ca", "zz"], 2), (["ab", "ba", "cc"], 1))


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        if len(words) <= 1:
            return 0

        words_set = set(words)

        result = 0
        while len(words_set) > 1:
            word = words_set.pop()
            reversed_word = word[::-1]
            if reversed_word in words_set:
                result += 1
                words_set.remove(reversed_word)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for words, expected in data:
            self.assertEqual(expected, s.maximumNumberOfStringPairs(words))


if __name__ == "__main__":
    unittest.main()
