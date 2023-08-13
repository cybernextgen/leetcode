import unittest
from typing import List

data = (
    ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
    ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
)


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for index in range(n):
            result.append(nums[index])
            result.append(nums[index + n])
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, n, expected in data:
            self.assertListEqual(expected, s.shuffle(nums, n))


if __name__ == "__main__":
    unittest.main()
