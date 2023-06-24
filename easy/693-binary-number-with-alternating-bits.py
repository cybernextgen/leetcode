import unittest
import re

data = ((5, True), (7, False), (11, False))


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not re.search(r"11|00", f"{n:b}")


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.hasAlternatingBits(input_data), expected)


if __name__ == "__main__":
    unittest.main()
