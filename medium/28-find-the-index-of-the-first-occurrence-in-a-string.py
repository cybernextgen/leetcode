import unittest

data = (("sadbutsad", "sad", 0), ("leetcode", "leeto", -1))


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for index in range(0, len(haystack) - needle_len + 1):
            if haystack[index : index + needle_len] == needle:
                return index
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for haystack, needle, index in data:
            self.assertEqual(index, s.strStr(haystack, needle))


if __name__ == "__main__":
    unittest.main()
