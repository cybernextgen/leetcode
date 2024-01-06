import unittest

data = (("egcfe", "efcfe"), ("abcd", "abba"))


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if not s:
            return s

        result = ""
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            left_ch = s[left_index]
            right_ch = s[right_index]
            result += left_ch if left_ch < right_ch else right_ch
            left_index += 1
            right_index -= 1

        middle_ch = ""
        if left_index == right_index:
            middle_ch = s[left_index]
        return f"{result}{middle_ch}{result[::-1]}"


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.makeSmallestPalindrome(input_data))


if __name__ == "__main__":
    unittest.main()
