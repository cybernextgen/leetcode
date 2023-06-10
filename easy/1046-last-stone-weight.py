import unittest
from typing import List
import bisect

data = (([2, 7, 4, 1, 8, 1], 1), ([1], 1))


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x < y:
                bisect.insort_left(stones, y - x)
        return stones[0]


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()
        for input_data, result in data:
            self.assertEqual(s.lastStoneWeight(input_data), result)


if __name__ == "__main__":
    unittest.main()
