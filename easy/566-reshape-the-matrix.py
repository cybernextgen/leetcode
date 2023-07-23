import unittest
from typing import List
import itertools

data = (
    ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
    ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
)


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return mat

        src_rows_count = len(mat)
        src_cols_count = len(mat[0])
        cells_count = src_rows_count * src_cols_count
        if r * c != cells_count:
            return mat
        result = []
        mat_iterator = itertools.chain.from_iterable(mat)
        for current_row in range(r):
            result.append([])
            for current_col in range(c):
                result[current_row].append(next(mat_iterator))
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, r, c, expected in data:
            self.assertEqual(s.matrixReshape(input_data, r, c), expected)


if __name__ == "__main__":
    unittest.main()
