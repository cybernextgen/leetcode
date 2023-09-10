import unittest
from typing import List

data = (([1, 1, 2, 2, 3, 3], 3), ([1, 1, 2, 3], 2), ([6, 6, 6, 6], 1))


class Solution:
    def distributeCandies(self, candy_types: List[int]) -> int:
        if not candy_types:
            return 0
        candy_types_count = len(set(candy_types))
        candy_count_to_eat = len(candy_types) // 2
        return min([candy_types_count, candy_count_to_eat])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for candy_type, expected in data:
            self.assertEqual(expected, s.distributeCandies(candy_type))


if __name__ == "__main__":
    unittest.main()
