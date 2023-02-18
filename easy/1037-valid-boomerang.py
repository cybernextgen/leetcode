import unittest
from typing import List


data = (
    ([[1, 1], [2, 3], [3, 2]], True),
    ([[1, 1], [2, 2], [3, 3]], False),
    ([[0, 0], [1, 0], [2, 2]], False),
    ([[0, 0], [1, 1], [1, 1]], False),
)


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points
        tg1 = self.__get_tg(p1, p2)
        tg2 = self.__get_tg(p2, p3)
        tg3 = self.__get_tg(p1, p3)
        return tg1 != tg2 and tg1 != tg3 and tg2 != tg3

    def __get_tg(self, p1: List[int], p2: List[int]) -> float:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return float("Inf")
        else:
            return dy / dx


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.isBoomerang(input_data), result)


if __name__ == "__main__":
    unittest.main()
