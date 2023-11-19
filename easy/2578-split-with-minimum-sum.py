import unittest
import heapq

data = ((4325, 59), (687, 75))


class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        heapq.heapify(digits)
        num1, num2 = "", ""
        try:
            while True:
                num1 += str(heapq.heappop(digits))
                num2 += str(heapq.heappop(digits))
        finally:
            return int(num1) + int(num2)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for num, expected in data:
            self.assertEqual(expected, s.splitNum(num))


if __name__ == "__main__":
    unittest.main()
