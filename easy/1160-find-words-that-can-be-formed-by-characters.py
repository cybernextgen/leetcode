import unittest
from typing import List
import collections

data = (
    (["cat", "bt", "hat", "tree"], "atach", 6),
    (["hello", "world", "leetcode"], "welldonehoneyr", 10),
)


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not words:
            return 0

        result = 0
        chars_awailable = collections.Counter(chars)
        for word in words:
            word_chars = collections.Counter(word)
            if word_chars - chars_awailable:
                continue
            result += len(word)
        return result


class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = collections.Counter(chars)
        result = 0
        for word in words:
            c = dict(counts)
            for ch in word:
                if ch in c and c[ch] > 0:
                    c[ch] -= 1
                else:
                    break
            else:
                result += len(word)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, chars, expected in data:
            self.assertEqual(s.countCharacters(input_data, chars), expected)


if __name__ == "__main__":
    unittest.main()
