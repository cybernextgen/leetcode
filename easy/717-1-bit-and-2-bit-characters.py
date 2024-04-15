import unittest
from typing import List

data = (([1, 0, 0], True), ([1, 1, 1, 0], False))


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index, last_index = 0, len(bits) - 1
        while index < last_index:
            index += bits[index] == 1
            index += 1
        return index == last_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.isOneBitCharacter(input_data))


if __name__ == "__main__":
    unittest.main()
