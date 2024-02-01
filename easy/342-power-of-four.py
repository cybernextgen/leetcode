import unittest

data = ((2, False), (16, True), (5, False), (1, True))


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        binary_repr = f"{n:b}"
        if binary_repr[0] != "1" or len(binary_repr) % 2 == 0:
            return False
        return binary_repr.count("1", 1) == 0


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & n - 1) == 0 and (n & 0x55555555) == n


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution2()

        for input_data, result in data:
            self.assertEqual(s.isPowerOfFour(input_data), result)


if __name__ == "__main__":
    unittest.main()
