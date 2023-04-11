import unittest
from collections import Counter

data = (("ababababa", 9), ("abccccdd", 7), ("a", 1))


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        palindrome_pairs = 0
        has_single_char = False
        chars_map = Counter(s)
        for current_char, current_char_count in chars_map.most_common():
            if current_char_count == 1:
                has_single_char = True
                break

            pairs, mod = divmod(current_char_count, 2)
            palindrome_pairs += pairs
            has_single_char = has_single_char or bool(mod)
        return int(has_single_char) + palindrome_pairs * 2


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.longestPalindrome(input_data), expected)


if __name__ == "__main__":
    unittest.main()
