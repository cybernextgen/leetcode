import unittest
from typing import List
import itertools

data = ((["aba", "aabb", "abcd", "bac", "aabc"], 2), (["aabb", "ab", "ba"], 3))


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        result = 0
        for a, b in itertools.combinations(words, 2):
            if set(a) == set(b):
                result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.similarPairs(input_data))


if __name__ == "__main__":
    unittest.main()
