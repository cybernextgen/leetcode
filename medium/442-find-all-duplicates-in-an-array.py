import unittest
from typing import List

data = (([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]), ([1, 1, 2], [1]), ([1], []))


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                result.append(abs(n))
            else:
                nums[index] *= -1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.findDuplicates(input_data))


if __name__ == "__main__":
    unittest.main()
