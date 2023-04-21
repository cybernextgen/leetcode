import unittest
from typing import Tuple

data = (
    ("11", "123", "134"),
    ("456", "77", "533"),
    ("22", "", "22"),
    ("990", "11", "1001"),
)


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        if not num2:
            return num1

        num2 = num2.zfill(len(num1))
        zero_ord = 48
        result = ""
        carry = 0
        for index in range(-1, -(len(num1) + 1), -1):
            d1 = ord(num1[index]) - zero_ord
            d2 = ord(num2[index]) - zero_ord
            s = d1 + d2 + carry
            if s > 9:
                carry = 1
                s = s - 10
            else:
                carry = 0
            result = f"{s}{result}"
        if carry:
            return f"1{result}"
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for num1, num2, expected in data:
            self.assertEqual(s.addStrings(num1, num2), expected)


if __name__ == "__main__":
    unittest.main()
