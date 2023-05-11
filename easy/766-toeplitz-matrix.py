import unittest
from typing import List

data = (([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True), ([[1, 2], [2, 2]], False))


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True

        prev_row = matrix[0]
        if len(prev_row) == 1:
            return True

        for current_row in matrix[1:]:
            if prev_row[:-1] != current_row[1:]:
                return False
            prev_row = current_row
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.isToeplitzMatrix(input_data), expected)


if __name__ == "__main__":
    unittest.main()
