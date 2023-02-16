import unittest
import re

data = (("()", True), ("()[]{}", True), ("(]", False), ("{[]}", True))


class Solution:
    def isValid(self, input_str: str) -> bool:
        stack = []
        close_signs_mapping = {")": "(", "]": "[", "}": "{"}
        try:
            for sign in input_str:
                if sign in close_signs_mapping:
                    last_open_sign = stack.pop()
                    if last_open_sign != close_signs_mapping[sign]:
                        return False
                    continue
                stack.append(sign)
        except IndexError:
            return False
        return not stack


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.isValid(input_data))


if __name__ == "__main__":
    unittest.main()
