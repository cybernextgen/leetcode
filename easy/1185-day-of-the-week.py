import unittest
import math

data = (
    (28, 2, 2100, "Sunday"),
    (31, 8, 2100, "Tuesday"),
    (18, 7, 1999, "Sunday"),
    (15, 8, 1993, "Sunday"),
)


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        is_leap_year = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

        year_code = year * 1.25 % 7

        delta = 0
        if year >= 2100:
            delta = -1

        month_code = {
            1: 5,
            2: 1,
            3: 1,
            4: 4,
            5: 6,
            6: 2,
            7: 4,
            8: 0,
            9: 3,
            10: 5,
            11: 1,
            12: 3,
        }[month]

        if is_leap_year and month <= 2:
            month_code -= 1

        day_code = int((year_code + month_code + day) % 7) + delta
        day_names = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        return day_names[day_code]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for day, month, year, expected in data:
            self.assertEqual(s.dayOfTheWeek(day, month, year), expected)


if __name__ == "__main__":
    unittest.main()
