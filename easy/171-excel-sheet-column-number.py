import unittest

data = (("A", 1), ("AB", 28), ("ZY", 701))


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for index, char in enumerate(reversed(columnTitle)):
            result += (ord(char) - 64) * (26**index)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.titleToNumber(input_data))


if __name__ == "__main__":
    unittest.main()
