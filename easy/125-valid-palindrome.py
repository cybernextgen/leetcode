import unittest
import re

data = (
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("aba", True),
    ("0P", False),
)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_string = re.sub(r"[^a-z0-9]", "", s.lower())
        right_index = len(test_string) - 1
        left_index = 0
        while right_index > left_index:
            if test_string[left_index] != test_string[right_index]:
                return False
            right_index -= 1
            left_index += 1
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.isPalindrome(input_data))


if __name__ == "__main__":
    unittest.main()
