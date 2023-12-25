import unittest
from typing import List

data = (
    ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
)


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        pixels_to_fill = [(sr, sc)]
        color_to_fill = image[sr][sc]
        if color_to_fill == color:
            return image

        while len(pixels_to_fill) > 0:
            current_pixel_r, current_pixel_c = pixels_to_fill.pop()
            for r, c in [
                (current_pixel_r - 1, current_pixel_c),
                (current_pixel_r + 1, current_pixel_c),
                (current_pixel_r, current_pixel_c - 1),
                (current_pixel_r, current_pixel_c + 1),
            ]:
                if (
                    r < 0
                    or r >= len(image)
                    or c < 0
                    or c >= len(image[0])
                    or image[r][c] != color_to_fill
                ):
                    continue
                pixels_to_fill.append((r, c))
            image[current_pixel_r][current_pixel_c] = color
        return image


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for image, sr, sc, color, expected in data:
            self.assertListEqual(expected, s.floodFill(image, sr, sc, color))


if __name__ == "__main__":
    unittest.main()
