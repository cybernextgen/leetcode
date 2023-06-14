import unittest
from typing import List
import heapq
import operator
import bisect

data = (
    (1, 2, 0, 0, [[0, 0], [0, 1]]),
    (2, 2, 0, 1, [[0, 1], [0, 0], [1, 1], [1, 0]]),
    (2, 3, 1, 2, [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]),
)


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, center_rows: int, center_cols: int
    ) -> List[List[int]]:
        heap = []
        for current_row in range(rows):
            for current_col in range(cols):
                distance = abs(current_col - center_cols) + abs(
                    current_row - center_rows
                )
                heapq.heappush(heap, (distance, [current_row, current_col]))

        return [heapq.heappop(heap)[1] for i in range(len(heap))]


class Solution2:
    def allCellsDistOrder(
        self, rows: int, cols: int, center_row: int, center_col: int
    ) -> List[List[int]]:
        result = []
        for current_row in range(rows):
            for current_col in range(cols):
                distance = abs(current_col - center_col) + abs(current_row - center_row)
                bisect.insort_right(
                    result,
                    (distance, [current_row, current_col]),
                    key=operator.itemgetter(0),
                )
        return list(map(operator.itemgetter(1), result))


class Solution3:
    def allCellsDistOrder(
        self, rows: int, cols: int, center_row: int, center_col: int
    ) -> List[List[int]]:
        return sorted(
            [[r, c] for r in range(rows) for c in range(cols)],
            key=lambda x: abs(x[0] - center_row) + abs(x[1] - center_col),
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution3()

        for rows, cols, rCenter, cCenter, expected in data:
            self.assertListEqual(
                s.allCellsDistOrder(rows, cols, rCenter, cCenter), expected
            )


if __name__ == "__main__":
    unittest.main()
