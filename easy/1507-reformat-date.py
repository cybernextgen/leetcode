import unittest
import re

data = (
    ("20th Oct 2052", "2052-10-20"),
    ("6th Jun 1933", "1933-06-06"),
    ("26th May 1960", "1960-05-26"),
    ("22nd Apr 2023", "2023-04-22"),
)


class Solution:
    def reformatDate(self, date: str) -> str:
        parsed_date = re.search(r"(?P<day>\d+)\w+ (?P<month>\w+) (?P<year>\d+)", date)
        month_mapping = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
        }
        if parsed_date:
            return f"{parsed_date.group('year')}-{month_mapping[parsed_date.group('month')]:02}-{int(parsed_date.group('day')):02}"
        return ""


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.reformatDate(input_data))


if __name__ == "__main__":
    unittest.main()
