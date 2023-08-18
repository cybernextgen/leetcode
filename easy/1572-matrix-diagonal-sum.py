import unittest
from typing import List

data = (
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        current_index = result = 0
        cols_count = len(mat[0])
        while current_index < cols_count:
            current_row = mat[current_index]
            result += current_row[current_index]
            current_row[current_index] = 0
            right_col_index = cols_count - current_index - 1
            result += current_row[right_col_index]
            current_index += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.diagonalSum(input_data))


if __name__ == "__main__":
    unittest.main()
