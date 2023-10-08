import unittest

data = ((7, 1), (121, 2), (1248, 4))


class Solution:
    def countDigits(self, num: int) -> int:
        if num < 10:
            return 1

        result = 0
        d = num
        while d > 0:
            d, m = divmod(d, 10)
            if not num % m:
                result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.countDigits(input_data))


if __name__ == "__main__":
    unittest.main()
