import unittest
from typing import List

data = (([69, 91, 78, 19, 40, 13], 94, 62), ([1, 2, 2], 3, 0), ([3, 2, 3], 3, 3))


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_prices = [float("inf"), float("inf")]

        for p in prices:
            if p < min_prices[0]:
                min_prices[1] = min_prices[0]
                min_prices[0] = p
            elif p < min_prices[1]:
                min_prices[1] = p

        remain = int(money - sum(min_prices))
        return remain if remain >= 0 else money


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for prices, money, expected in data:
            self.assertEqual(expected, s.buyChoco(prices, money))


if __name__ == "__main__":
    unittest.main()
