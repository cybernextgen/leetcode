import unittest

data = ((5, 2), (8, 3))


class Solution:
    def arrangeCoins(self, n: int) -> int:
        current_level = 1
        while n >= current_level:
            n -= current_level
            current_level += 1
        return current_level - 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.arrangeCoins(input_data), expected)


if __name__ == "__main__":
    unittest.main()
