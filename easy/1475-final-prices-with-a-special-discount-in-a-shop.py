import unittest
from typing import List

data = (
    # ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
    # ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 1, 1, 6], [9, 0, 1, 6]),
)


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        prices_length = len(prices)
        for index, price in enumerate(prices):
            ptr = index + 1
            while ptr < prices_length:
                discont = prices[ptr]
                if discont <= price:
                    result.append(price - discont)
                    break
                ptr += 1
            else:
                result.append(price)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.finalPrices(input_data))


if __name__ == "__main__":
    unittest.main()
