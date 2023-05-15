import unittest
from typing import List
import re

data = (
    ("abbxxxxzyy", [[3, 6]]),
    ("abc", []),
    ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
)


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        compiled_regex = re.compile(r"(\w)\1{2,}")
        return [
            [match.start(), match.end() - 1] for match in compiled_regex.finditer(s)
        ]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.largeGroupPositions(input_data), expected)


if __name__ == "__main__":
    unittest.main()
