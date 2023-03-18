import unittest
import functools

data = ((128, 1), (11, 3), (4294967293, 31))


class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(f"{n:b}".replace("0", ""))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.hammingWeight(input_data))


if __name__ == "__main__":
    unittest.main()
