import unittest

data = ((5, 2), (7, 0), (10, 5))


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        digits_count = len(f"{n:b}")
        complete = int("1" * digits_count, 2)
        return complete - n


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.bitwiseComplement(input_data), expected)


if __name__ == "__main__":
    unittest.main()
