import unittest

data = (("ababa", 1), ("abb", 2), ("baabb", 2))


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return 2
            left_index += 1
            right_index -= 1
        return 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.removePalindromeSub(input_data), expected)


if __name__ == "__main__":
    unittest.main()
