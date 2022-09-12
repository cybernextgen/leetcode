from math import remainder
from typing import List, Optional
import unittest


data = [
    # ([2, 7, 11, 15], 9, [0, 1]),
    # ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
]


class Solution1:
    """
    Trivial O(n^2) solution
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0
        for num1 in nums:
            for num2 in nums:
                if i != j and (num1 + num2) == target:
                    return [i, j]
                j += 1
            i += 1
            j = 0
        return []


class Solution2:
    """
    Binary search solution for ordered data
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        for n in nums:
            second_index = self.__binarySearch(nums, target - n, first_index + 1)
            if second_index and second_index != first_index:
                return [first_index, second_index]
            first_index += 1
        return []

    def __binarySearch(self, nums: List[int], target: int, left_index) -> Optional[int]:
        """
        Returns index of target in nums list
        """
        right_index = len(nums) - 1
        while left_index != right_index:
            median_index = (right_index + left_index) // 2
            median_value = nums[median_index]
            if median_value > target:
                right_index = median_index - 1
            elif median_value < target:
                left_index = median_index + 1
            else:
                return median_index
        if nums[left_index] == target:
            return left_index


class Solution3:
    """
    Dictionary based solution
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        current_index = 0
        for num1 in nums:
            num2 = target - num1
            if num2 in nums_dict:
                return [nums_dict[num2], current_index]
            nums_dict[num1] = current_index
            current_index += 1
        return []


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution3()

        for nums, target, result in data:
            self.assertEqual(result, s.twoSum(nums, target))


if __name__ == "__main__":
    unittest.main()
