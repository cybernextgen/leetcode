import unittest
from typing import Tuple, Union

data = (
    ("aba", True),
    ("abca", True),
    ("abc", False),
    ("axbcbaba", False),
)


class Solution1:
    def validPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        char_deleted = False
        left_variant_wrong = False
        right_variant_wrong = False
        while right_index > left_index:
            if not char_deleted:
                if s[left_index] != s[right_index]:
                    char_deleted = True
                    continue
            else:
                left_variant_wrong |= s[left_index + 1] != s[right_index]
                right_variant_wrong |= s[left_index] != s[right_index - 1]
                if left_variant_wrong and right_variant_wrong:
                    return False
            left_index += 1
            right_index -= 1
        return True


class Solution2:
    def __is_valid_palindrome(
        self, s: str, left_index: int, right_index: int
    ) -> Tuple[bool, int, int]:
        while right_index > left_index:
            if s[left_index] != s[right_index]:
                return False, left_index, right_index

            right_index -= 1
            left_index += 1
        return True, left_index, right_index

    def validPalindrome(self, s: str) -> bool:
        is_valid, left_index, right_index = self.__is_valid_palindrome(s, 0, len(s) - 1)
        return (
            is_valid
            or self.__is_valid_palindrome(s, left_index + 1, right_index)[0]
            or self.__is_valid_palindrome(s, left_index, right_index - 1)[0]
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, expected in data:
            self.assertEqual(expected, s.validPalindrome(input_data), input_data)


if __name__ == "__main__":
    unittest.main()
