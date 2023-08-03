import unittest
from typing import List

data = (
    (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
    (47, 85, [48, 55, 66, 77]),
    (
        110,
        708,
        [
            66,
            77,
            88,
            99,
            111,
            112,
            115,
            122,
            124,
            126,
            128,
            132,
            135,
            144,
            155,
            162,
            168,
            175,
            184,
            212,
            216,
            222,
            224,
            244,
            248,
            264,
            288,
            312,
            315,
            324,
            333,
            336,
            366,
            384,
            396,
            412,
            424,
            432,
            444,
            448,
            488,
            515,
            555,
            612,
            624,
            636,
            648,
            666,
            672,
        ],
    ),
)


def get_digits(num) -> List[int]:
    if num < 10:
        return [num]
    result = []
    while True:
        d, m = divmod(num, 10)
        result.append(m)
        if d < 10:
            result.append(d)
            return result
        num = d


def is_self_dividing(num) -> bool:
    for digit in get_digits(num):
        if digit == 0 or num % digit != 0:
            return False
    return True


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                result.append(n)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for left, right, expected in data:
            self.assertEqual(expected, s.selfDividingNumbers(left, right), expected)


if __name__ == "__main__":
    unittest.main()
