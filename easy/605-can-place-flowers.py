import unittest
from typing import List

data = (([1, 0, 0, 0, 1], 1, True), ([1, 0, 0, 0, 1], 2, False))


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots_awailable = 0
        current_free_plots = 1
        for plot in flowerbed:
            if plot:
                plots_awailable += (current_free_plots - 1) // 2
                current_free_plots = 0
                continue
            current_free_plots += 1

        plots_awailable += current_free_plots // 2
        return plots_awailable >= n


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for flowerbed, n, expected in data:
            self.assertEqual(expected, s.canPlaceFlowers(flowerbed, n))


if __name__ == "__main__":
    unittest.main()
