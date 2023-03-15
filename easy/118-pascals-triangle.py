import unittest
from typing import List
import math

data = (
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (
        9,
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
        ],
    ),
)


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        result = []
        for current_row_number in range(1, numRows + 1):
            current_row_result = [1] * current_row_number
            mediane_index = math.ceil(current_row_number / 2)
            for element_index in range(1, mediane_index):
                if element_index == 1:
                    current_row_result[element_index] = current_row_number - 1
                elif element_index == 2:
                    current_row_result[element_index] = (
                        (current_row_number - 1) * (current_row_number - 2) // 2
                    )
                elif element_index == 3:
                    n = current_row_number - element_index
                    current_row_result[element_index] = n * (n + 1) * (n + 2) // 6
                elif element_index > 3:
                    current_row_result[element_index] = math.comb(
                        current_row_number - 1, element_index
                    )
            if current_row_number > 3:
                current_row_result[
                    mediane_index : current_row_number - 1
                ] = current_row_result[(current_row_number // 2) - 1 : 0 : -1]
            result.append(current_row_result)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.generate(input_data))


if __name__ == "__main__":
    unittest.main()
