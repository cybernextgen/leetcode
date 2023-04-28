import unittest
from typing import List

data = (
    (
        [
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
        ],
        "abcdefghijklmnopqrstuvwxyz",
        [3, 60],
    ),
    (
        [
            4,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
        ],
        "bbbcccdddaaa",
        [2, 4],
    ),
)


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        if not s:
            return [0, 0]

        first_char_ord = ord("a")
        max_str_width = 100
        current_str_width = 0
        str_count = 1
        for char in s:
            char_width = widths[ord(char) - first_char_ord]
            if current_str_width + char_width > max_str_width:
                str_count += 1
                current_str_width = char_width
                continue
            current_str_width += char_width
        return [str_count, current_str_width]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for widths, input_str, expected in data:
            self.assertListEqual(s.numberOfLines(widths, input_str), expected)


if __name__ == "__main__":
    unittest.main()
