import unittest

data = (
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("badc", "baba", False),
)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_mapping = {}
        used_chars = set()
        for ch1, ch2 in zip(s, t):
            if ch1 not in chars_mapping:
                if ch2 not in used_chars:
                    chars_mapping[ch1] = ch2
                    used_chars.add(ch2)
                    continue
                return False
            if chars_mapping[ch1] != ch2:
                return False
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for str1, str2, expected in data:
            self.assertEqual(expected, s.isIsomorphic(str1, str2))


if __name__ == "__main__":
    unittest.main()
