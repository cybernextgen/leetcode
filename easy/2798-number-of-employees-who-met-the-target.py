import unittest
from typing import List

data = (([0, 1, 2, 3, 4], 2, 3), ([5, 1, 4, 2, 2], 6, 0))


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len(list(filter(lambda x: x >= target, hours)))


class Solution2:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result = 0
        for h in hours:
            result += 1 if h >= target else 0
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for hours, target, expected in data:
            self.assertEqual(expected, s.numberOfEmployeesWhoMetTarget(hours, target))


if __name__ == "__main__":
    unittest.main()
