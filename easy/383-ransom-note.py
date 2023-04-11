import unittest
from collections import Counter

data = (("", "ab", True), ("a", "b", False), ("aa", "ab", False), ("aa", "aab", True))


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True

        magazine_chars_map = Counter(magazine)
        for char in ransomNote:
            if char not in magazine_chars_map or magazine_chars_map[char] == 0:
                return False

            magazine_chars_map[char] -= 1
        return True


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for ransomNote, magazine, expected in data:
            self.assertEqual(s.canConstruct(ransomNote, magazine), expected)


if __name__ == "__main__":
    unittest.main()
