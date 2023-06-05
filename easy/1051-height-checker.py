import unittest
from typing import List

data = (([1, 1, 4, 2, 1, 3], 3), ([5, 1, 2, 3, 4], 5), ([1, 2, 3, 4, 5], 0))


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        result = 0
        for h1, h2 in zip(heights, sorted_heights):
            if h1 != h2:
                result += 1
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.heightChecker(input_data), result)


if __name__ == "__main__":
    unittest.main()
