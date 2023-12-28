import unittest
from typing import List


data = (
    ("K1:L2", ["K1", "K2", "L1", "L2"]),
    ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
)


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        cell1, cell2 = s.split(":")
        ord_initial_letter = ord(cell1[0])
        ord_end_letter = ord(cell2[0])
        initial_row_number = int(cell1[1])
        end_row_number = int(cell2[1])
        return [
            f"{chr(l)}{n}"
            for l in range(ord_initial_letter, ord_end_letter + 1)
            for n in range(initial_row_number, end_row_number + 1)
        ]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root, expected in data:
            self.assertListEqual(expected, s.cellsInRange(root))


if __name__ == "__main__":
    unittest.main()
