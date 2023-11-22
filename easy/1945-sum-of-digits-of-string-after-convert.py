import unittest
from typing import List

data = (("iiii", 1, 36), ("leetcode", 2, 6), ("zbax", 2, 8))


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ""
        for ch in s:
            digits += str(ord(ch) - 96)
        result = self.__get_digits_sum(digits)
        while k > 1:
            result = self.__get_digits_sum(str(result))
            k -= 1
        return result

    @staticmethod
    def __get_digits_sum(digits: str) -> int:
        result = 0
        for ch in digits:
            result += int(ch)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for d, k, expected in data:
            self.assertEqual(expected, s.getLucky(d, k))


if __name__ == "__main__":
    unittest.main()
