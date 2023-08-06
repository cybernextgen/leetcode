import unittest
from typing import List

data = (
    (
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
        [2, 0, 3],
    ),
    ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2, [0, 2]),
)


class RowsComparator(tuple):
    def __lt__(self, other):
        return self[0] < other[0] or self[1] < other[1]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows_power = [(sum(r), index) for index, r in enumerate(mat)]
        rows_power.sort(key=RowsComparator)
        return [t[1] for t in rows_power[:k]]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, k, expected in data:
            self.assertListEqual(s.kWeakestRows(input_data, k), expected)


if __name__ == "__main__":
    unittest.main()
