import unittest

data = ((8, 6), (1, 1), (4, -1))


class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = n * (n + 1) / 2
        left_sum = 0
        for num in range(1, n + 1):
            left_sum += num
            if right_sum == left_sum:
                return num
            right_sum -= num
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.pivotInteger(input_data))


if __name__ == "__main__":
    unittest.main()
