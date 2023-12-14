import unittest
from typing import List

data = (([1, 1, 2, 1, 3], 3), ([0, 1, 2], 2))


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        for n in batteryPercentages:
            result += 1 if n - result > 0 else 0
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.countTestedDevices(input_data))


if __name__ == "__main__":
    unittest.main()
