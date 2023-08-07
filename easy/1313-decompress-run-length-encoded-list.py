import unittest
from typing import List


data = (([1, 2, 3, 4], [2, 4, 4, 4]), ([1, 1, 2, 3], [1, 3, 3]))


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for count, number in zip(nums[::2], nums[1::2]):
            result += count * [number]
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.decompressRLElist(input_data), expected)


if __name__ == "__main__":
    unittest.main()
