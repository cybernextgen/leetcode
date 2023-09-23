import unittest
import re

data = (
    ("1 box has 3 blue 4 red 6 green and 12 yellow marbles", True),
    ("hello world 5 x 5", False),
    ("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s", False),
)


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_number = -1
        for match in re.finditer(r"(\d+)", s):
            current_number = int(match.group())
            if current_number <= prev_number:
                return False
            prev_number = current_number
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for words, expected in data:
            self.assertEqual(expected, s.areNumbersAscending(words))


if __name__ == "__main__":
    unittest.main()
