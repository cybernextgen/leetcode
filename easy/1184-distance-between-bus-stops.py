import unittest
from typing import List

data = (
    ([3, 6, 7, 2, 9, 10, 7, 16, 11], 6, 2, 28),
    ([1, 2, 3, 4], 0, 1, 1),
    ([1, 2, 3, 4], 0, 3, 4),
)


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        distance_cw = 0
        distance_ccw = 0

        index_cw = start
        index_ccw = start
        while index_cw != destination:
            distance_cw += distance[index_cw]
            index_cw = (index_cw + 1) % len(distance)

        while index_ccw != destination:
            index_ccw = (index_ccw - 1) % len(distance)
            distance_ccw += distance[index_ccw]

        return distance_cw if distance_cw < distance_ccw else distance_ccw


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for distance, start, destination, expected in data:
            self.assertEqual(
                s.distanceBetweenBusStops(distance, start, destination), expected
            )


if __name__ == "__main__":
    unittest.main()
