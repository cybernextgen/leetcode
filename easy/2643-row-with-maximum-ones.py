import unittest
from typing import List

data = (
    ([[0, 1], [1, 0]], [0, 1]),
    ([[0, 0, 0], [0, 1, 1]], [1, 2]),
    ([[0, 0], [1, 1], [0, 0]], [1, 2]),
)


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = [0, 0]
        for index, row in enumerate(mat):
            counts = sum(row)
            if counts > result[1]:
                result = [index, counts]
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.rowAndMaximumOnes(input_data))


if __name__ == "__main__":
    unittest.main()
