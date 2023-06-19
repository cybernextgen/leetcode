import unittest
import functools

data = ((234, 15), (4421, 21))


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits = 0
        product_digits = 1
        div = n
        while div > 9:
            div, mod = divmod(div, 10)
            sum_digits += mod
            product_digits *= mod
        sum_digits += div
        product_digits *= div

        return product_digits - sum_digits


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.subtractProductAndSum(input_data), expected)


if __name__ == "__main__":
    unittest.main()
