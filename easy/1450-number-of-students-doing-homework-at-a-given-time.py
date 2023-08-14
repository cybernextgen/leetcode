import unittest
from typing import List


data = (([1, 2, 3], [3, 2, 7], 4, 1), ([4], [4], 4, 1))


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        result = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for startTime, endTime, queryTime, expected in data:
            self.assertEqual(expected, s.busyStudent(startTime, endTime, queryTime))


if __name__ == "__main__":
    unittest.main()
