import unittest
from typing import List

data = (([1, 2, 3, 3], 3), ([2, 1, 2, 5, 3, 2], 2), ([5, 1, 5, 2, 5, 3, 5, 4], 5))


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return 0


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.repeatedNTimes(input_data), expected)


if __name__ == "__main__":
    unittest.main()
