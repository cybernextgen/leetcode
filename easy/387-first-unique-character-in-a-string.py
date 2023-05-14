import unittest
import collections

data = (("leetcode", 0), ("loveleetcode", 2), ("aabb", -1))


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_counts = collections.Counter(s)
        for char, counts in chars_counts.items():
            if counts == 1:
                return s.index(char)
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.firstUniqChar(input_data), expected)


if __name__ == "__main__":
    unittest.main()
