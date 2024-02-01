import unittest

data = ((0, False), (1, True), (2, True), (3, False), (16, True))


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.isPowerOfTwo(input_data), result)


if __name__ == "__main__":
    unittest.main()
