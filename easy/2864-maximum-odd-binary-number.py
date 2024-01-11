import unittest

data = (("010", "001"), ("0101", "1001"))


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        zeroes_count = len(s) - ones_count

        return "1" * (ones_count - 1) + ("0" * zeroes_count) + "1"


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.maximumOddBinaryNumber(input_data))


if __name__ == "__main__":
    unittest.main()
