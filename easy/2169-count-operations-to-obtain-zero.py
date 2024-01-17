import unittest

data = ((2, 3, 3), (10, 10, 1))


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for num1, num2, expected in data:
            self.assertEqual(s.countOperations(num1, num2), expected)


if __name__ == "__main__":
    unittest.main()
