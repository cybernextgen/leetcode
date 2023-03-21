import unittest
from typing import List
import itertools

data = (([1, 3, 0, 0, 2, 0, 0, 4], 6), ([0, 0, 0, 2, 0, 0], 9), ([2, 10, 2019], 0))


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        group_len = 0
        for n in itertools.chain(nums, [1]):
            if not n:
                group_len += 1
                continue
            if group_len:
                result += (group_len**2) / 2 + (group_len / 2)
                group_len = 0
        return int(result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.zeroFilledSubarray(input_data))


if __name__ == "__main__":
    unittest.main()
