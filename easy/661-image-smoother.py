import unittest
from typing import List, Optional

data = (
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (
        [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
        [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
    ),
)


Matrix = List[List[int]]


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> Matrix:
        result: Matrix = []
        for row_index, row in enumerate(img):
            result.append([])
            for col_index, _ in enumerate(row):
                near_pixels_count = 0
                near_pixels_sum = 0

                for y in range(row_index - 1, row_index + 2):
                    for x in range(col_index - 1, col_index + 2):
                        if x >= 0 and x < len(row) and y >= 0 and y < len(img):
                            near_pixels_count += 1
                            near_pixels_sum += img[y][x]

                new_pixel_value = near_pixels_sum // near_pixels_count
                result[row_index].append(new_pixel_value)

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.imageSmoother(input_data))


if __name__ == "__main__":
    unittest.main()
