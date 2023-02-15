import unittest
import functools
from typing import List, Tuple


data = (
    ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
    ([2, 7, 4], 181, [4, 5, 5]),
    ([2, 1, 5], 806, [1, 0, 2, 1]),
)


class Solution:
    """
    Monstruos but alive
    """

    def addToArrayForm(self, first_num_list: List[int], second_num: int) -> List[int]:
        result = []
        second_num_list = self.__int_to_list(second_num)

        iterations_count = max(len(first_num_list), len(second_num_list))
        addition = 0
        for i in range(iterations_count):
            s = (
                addition
                + self.__pop_or_default(first_num_list)
                + self.__pop_or_default(second_num_list)
            )
            addition, last_digit = self.__split_last_digit(s)
            result.insert(0, last_digit)

        if addition > 0:
            result.insert(0, addition)

        return result

    def __int_to_list(self, num: int) -> List[int]:
        result = []
        while num > 0:
            num, last_digit = self.__split_last_digit(num)
            result.insert(0, last_digit)
        return result

    def __pop_or_default(self, lst: List[int], default: int = 0) -> int:
        try:
            default = lst.pop()
        finally:
            return default

    def __split_last_digit(self, num: int) -> Tuple[int, int]:
        last_digit = num % 10
        remains = num // 10
        return remains, last_digit


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for a, b, result in data:
            self.assertEqual(result, s.addToArrayForm(a, b))


if __name__ == "__main__":
    unittest.main()
