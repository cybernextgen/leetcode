from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_x_coords = sorted([x for x, y in points])
        return max(x2 - x1 for x1, x2 in zip(sorted_x_coords, sorted_x_coords[1:]))


if __name__ == "__main__":
    for input_data, expected in (
        ([[8, 7], [9, 9], [7, 4], [9, 7]], 1),
        ([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3),
    ):
        assert Solution().maxWidthOfVerticalArea(input_data) == expected
