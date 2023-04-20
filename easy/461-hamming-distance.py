import unittest

data = ((1, 4, 2), (3, 1, 1))


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        repr_x = f"{x:b}"
        repr_y = f"{y:b}"
        len_repr_x = len(repr_x)
        len_repr_y = len(repr_y)

        if len_repr_x > len_repr_y:
            repr_y = repr_y.zfill(len_repr_x)
        elif len_repr_y > len_repr_x:
            repr_x = repr_x.zfill(len_repr_y)

        return sum(xi != yi for xi, yi in zip(repr_x, repr_y))


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for num1, num2, expected in data:
            self.assertEqual(s.hammingDistance(num1, num2), expected)


if __name__ == "__main__":
    unittest.main()
