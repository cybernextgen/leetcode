import unittest
from typing import List

data = (
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        current_row_index = left_col_index = result = 0
        cols_count = len(mat[0])
        while current_row_index < len(mat):
            current_row = mat[current_row_index]
            result += current_row[left_col_index]
            right_col_index = cols_count - left_col_index - 1
            if right_col_index != left_col_index:
                result += current_row[right_col_index]
            current_row_index += 1
            left_col_index += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.diagonalSum(input_data))


if __name__ == "__main__":
    unittest.main()
