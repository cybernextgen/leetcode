import unittest
from datetime import datetime

data = (("2019-01-09", 9), ("2019-02-10", 41))


class Solution:
    def dayOfYear(self, date_as_str: str) -> int:
        date = datetime.strptime(date_as_str, "%Y-%m-%d")
        return (date - datetime(date.year, 1, 1)).days + 1


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for date, expected in data:
            self.assertEqual(s.dayOfYear(date), expected)


if __name__ == "__main__":
    unittest.main()
