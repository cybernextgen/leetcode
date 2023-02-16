import unittest
from typing import List

data = (
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current_sum = 0
        for n in nums:
            current_sum += n
            result.append(current_sum)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(result, s.runningSum(input_data))


if __name__ == "__main__":
    unittest.main()
