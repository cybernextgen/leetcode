import unittest
import re

data = (("()", True), ("()[]{}", True), ("(]", False), ("{[]}", True))


class Solution:
    def isValid(self, input_str: str) -> bool:
        stack = []
        close_signs_mapping = {")": "(", "]": "[", "}": "{"}
        for sign in input_str:
            if sign in close_signs_mapping:
                if stack:
                    last_open_sign = stack.pop()
                    if last_open_sign != close_signs_mapping[sign]:
                        return False
                    continue
                return False
            else:
                stack.append(sign)
        if stack:
            return False
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.isValid(input_data))


if __name__ == "__main__":
    unittest.main()
