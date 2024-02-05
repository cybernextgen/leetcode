import unittest
import math

data = ((16, True), (14, False))


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num) % 1 == 0


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.isPerfectSquare(input_data), result)


if __name__ == "__main__":
    unittest.main()
