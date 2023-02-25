import unittest
from typing import List

data = (([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
                continue

            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.maxProfit(input_data))


if __name__ == "__main__":
    unittest.main()
