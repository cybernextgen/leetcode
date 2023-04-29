import unittest
from typing import List

data = (([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2))


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones_count = 0
        current_lines_count = 0
        for n in nums:
            if n:
                current_lines_count += 1
                if current_lines_count > max_ones_count:
                    max_ones_count = current_lines_count
                continue
            current_lines_count = 0
        return max_ones_count


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findMaxConsecutiveOnes(input_data), expected)


if __name__ == "__main__":
    unittest.main()
