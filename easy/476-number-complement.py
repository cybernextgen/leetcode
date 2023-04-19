import unittest

data = ((5, 2), (1, 0))


class Solution:
    def findComplement(self, num: int) -> int:
        bin_repr = f"{num:b}"
        complement_repr = ["0" if ch == "1" else "1" for ch in bin_repr]
        return int("".join(complement_repr), 2)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findComplement(input_data), expected)


if __name__ == "__main__":
    unittest.main()
