import unittest
from typing import List

data = (([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0]))


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        transfer = 1
        last_index = len(digits) - 1
        for index in range(last_index, -1, -1):
            digit = digits[index] + transfer
            transfer, digits[index] = divmod(digit, 10)
            if transfer == 0:
                return digits
        if transfer:
            digits.insert(0, 1)
        return digits


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(result, s.plusOne(input_data))


if __name__ == "__main__":
    unittest.main()
