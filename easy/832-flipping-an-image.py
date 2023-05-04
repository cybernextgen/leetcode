import unittest
from typing import List

data = (
    ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
    (
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
        [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
    ),
)


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            result_row = []
            result.append(result_row)
            for col in reversed(row):
                result_row.append(col ^ 1)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.flipAndInvertImage(input_data), expected)


if __name__ == "__main__":
    unittest.main()
