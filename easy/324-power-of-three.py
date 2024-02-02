import unittest

data = ((27, True), (0, False), (-1, False))


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        remain: float = n
        while remain > 1 and remain % 1 == 0:
            remain = remain / 3.0
        return remain == 1


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.isPowerOfThree(input_data), result)


if __name__ == "__main__":
    unittest.main()
