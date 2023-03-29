import unittest
from typing import List

data = (
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        default_zeroe_index = len(nums)
        zeroe_index = default_zeroe_index
        for index, current_num in enumerate(nums):
            if current_num == 0:
                if zeroe_index > index:
                    zeroe_index = index
                continue
            if zeroe_index < index:
                nums[zeroe_index] = current_num
                nums[index] = 0

                for new_zeroe_index in range(zeroe_index + 1, len(nums)):
                    if nums[new_zeroe_index] == 0:
                        zeroe_index = new_zeroe_index
                        break


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            s.moveZeroes(input_data)
            self.assertEqual(result, input_data)


if __name__ == "__main__":
    unittest.main()
