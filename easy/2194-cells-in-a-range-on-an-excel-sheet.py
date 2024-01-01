import unittest
from typing import List


data = (
    ("K1:L2", ["K1", "K2", "L1", "L2"]),
    ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
)

w


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root, expected in data:
            self.assertListEqual(expected, s.cellsInRange(root))


if __name__ == "__main__":
    unittest.main()
