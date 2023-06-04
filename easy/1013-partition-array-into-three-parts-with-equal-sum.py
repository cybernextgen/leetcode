import unittest
from typing import List

data = (
    ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
    ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
    ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
    ([1, -1, 1, -1], False),
)


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        equal_sum = sum(arr) / 3

        parts_count = 0
        part_sum = 0
        last_index = len(arr) - 1
        for index, num in enumerate(arr):
            part_sum += num
            if part_sum == equal_sum:
                part_sum = 0
                parts_count += 1
            if parts_count == 2 and index != last_index:
                return True
        return False


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.canThreePartsEqualSum(input_data), result)


if __name__ == "__main__":
    unittest.main()
