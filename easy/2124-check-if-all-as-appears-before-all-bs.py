import unittest

data = (("aaabbb", True), ("abab", False), ("bbb", True))


class Solution:
    def checkString(self, s: str) -> bool:
        return s.find("ba") == -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.checkString(input_data))


if __name__ == "__main__":
    unittest.main()
