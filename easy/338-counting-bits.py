import unittest
from typing import List

data = ((2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2]))


class Solution:
    def countBits(self, number: int) -> List[int]:
        result = []
        for current_number in range(number + 1):
            result.append(bin(current_number).count("1"))
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for number, expected in data:
            self.assertListEqual(expected, s.countBits(number))


if __name__ == "__main__":
    unittest.main()
