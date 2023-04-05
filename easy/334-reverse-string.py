import unittest
from typing import List

data = (
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for index in range(len(s) // 2):
            right_index = -1 - index
            s[index], s[right_index] = s[right_index], s[index]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            s.reverseString(input_data)
            self.assertEqual(result, input_data)


if __name__ == "__main__":
    unittest.main()
