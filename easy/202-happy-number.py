import unittest
from typing import List, Iterator
import functools

data = ((19, True), (2, False))


class Solution:
    def isHappy(self, n: int) -> bool:
        prev_n = n
        visited = set()
        while True:
            digits = self.__get_digits_from_int(prev_n)
            n = functools.reduce(lambda s, d: s + d**2, digits, 0)
            if n in visited:
                return False
            if n == 1:
                return True
            prev_n = n
            visited.add(n)

    def __get_digits_from_int(self, num: int) -> Iterator[int]:
        result = []
        while num:
            num, last_digit = divmod(num, 10)
            result.append(last_digit)
        return reversed(result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.isHappy(input_data))


if __name__ == "__main__":
    unittest.main()
