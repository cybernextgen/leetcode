import unittest

data = ((123, 321), (-123, -321), (120, 21))


class Solution:
    def reverse(self, x: int) -> int:
        is_positive = x >= 0
        x = x if is_positive else x * -1
        as_string = str(x)[::-1]
        as_int = int(as_string)
        result = as_int if is_positive else as_int * -1
        return result if -2_147_483_648 <= result <= 2_147_483_647 else 0


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.reverse(input_data), result)


if __name__ == "__main__":
    unittest.main()
