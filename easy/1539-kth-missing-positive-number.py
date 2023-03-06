import unittest
from typing import List

data = (([2, 3, 4, 7, 11], 5, 9), ([1, 2, 3, 4], 2, 6))


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        input_set = set(arr)
        missing_integer_count = 0
        current_integer = 0
        while missing_integer_count < k:
            current_integer += 1
            if current_integer not in input_set:
                missing_integer_count += 1
        return current_integer


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_list, kth, expected in data:
            self.assertEqual(expected, s.findKthPositive(input_list, kth))


if __name__ == "__main__":
    unittest.main()
