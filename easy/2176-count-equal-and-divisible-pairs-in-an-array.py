import unittest
from typing import List

data = (([3, 1, 2, 2, 2, 1, 3], 2, 4), ([1, 2, 3, 4], 1, 0))


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        indexes = {}
        result = 0
        for index, n in enumerate(nums):
            if n not in indexes:
                indexes[n] = [index]
                continue

            for stored_index in indexes[n]:
                if (stored_index * index) % k == 0:
                    result += 1
            indexes[n].append(index)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, k, expected in data:
            self.assertEqual(expected, s.countPairs(nums, k))


if __name__ == "__main__":
    unittest.main()
