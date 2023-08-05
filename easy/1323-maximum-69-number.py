import unittest

data = ((9669, 9969), (9996, 9999), (9999, 9999))


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.maximum69Number(input_data), expected)


if __name__ == "__main__":
    unittest.main()
