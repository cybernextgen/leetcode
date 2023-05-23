import unittest
import re

data = (
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
)


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left_index = 0
        right_index = len(s) - 1
        result = list(s)
        pattern = r"[a-zA-Z]"
        while left_index < right_index:
            left_char = result[left_index]
            right_char = result[right_index]
            if not re.match(pattern, left_char):
                left_index += 1
                continue
            if not re.match(pattern, right_char):
                right_index -= 1
                continue

            result[left_index], result[right_index] = (
                result[right_index],
                result[left_index],
            )
            right_index -= 1
            left_index += 1
        return "".join(result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.reverseOnlyLetters(input_data), expected)


if __name__ == "__main__":
    unittest.main()
