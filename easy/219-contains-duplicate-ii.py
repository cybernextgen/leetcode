import unittest
from typing import List

data = (
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_numbers = dict()
        for index, number in enumerate(nums):
            if number not in seen_numbers:
                seen_numbers[number] = index
                continue

            seen_index = seen_numbers[number]
            if index - seen_index <= k:
                return True
            seen_numbers[number] = index
        return False


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_list, distance, result in data:
            self.assertEqual(result, s.containsNearbyDuplicate(input_list, distance))


if __name__ == "__main__":
    unittest.main()
