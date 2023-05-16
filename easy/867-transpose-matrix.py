import unittest
from typing import List
from operator import itemgetter

data = (
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
)


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        cols_count = len(matrix[0])
        return [list(map(itemgetter(n), matrix)) for n in range(cols_count)]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.transpose(input_data), expected)


if __name__ == "__main__":
    unittest.main()
