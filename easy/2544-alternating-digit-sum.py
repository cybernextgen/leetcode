import unittest
from typing import List

data = ((521, 4), (111, 1), (886996, 0))


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        while n > 9:
            n, rem = divmod(n, 10)
            digits.append(rem)
        digits.append(n)

        return sum(
            d if not (index % 2) else -d for index, d in enumerate(reversed(digits))
        )


class Solution2:
    def alternateDigitSum(self, n: int) -> int:
        positive = True
        result = 0
        for ch in str(n):
            if positive:
                result += int(ch)
            else:
                result -= int(ch)
            positive = not positive
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.alternateDigitSum(input_data))


if __name__ == "__main__":
    unittest.main()
