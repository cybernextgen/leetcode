import unittest

data = ((100, "202"), (-7, "-10"))


class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"

        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        res = ""
        while True:
            num, m = divmod(num, 7)
            res = f"{m}{res}"
            if not num:
                break

        return f"{sign}{res}"


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.convertToBase7(input_data), expected)


if __name__ == "__main__":
    unittest.main()
