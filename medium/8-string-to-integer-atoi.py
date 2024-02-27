import unittest

data = (("42", 42), ("   -42", -42), ("4193 with words", 4193))


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        s = s.lstrip()
        sign = 1

        if s[0] in ["+", "-"]:
            sign = 1 if s[0] == "+" else -1
            s = s[1:]

        result = 0
        ord_0 = ord("0")
        ord_9 = ord("9")

        for ch in s:
            ord_ch = ord(ch)
            if ord_ch < ord_0 or ord_ch > ord_9:
                break

            result = result * 10 + ord_ch - ord_0
        result *= sign
        return max(-(2**31), min(result, (2**31) - 1))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.myAtoi(input_data), expected)


if __name__ == "__main__":
    unittest.main()
