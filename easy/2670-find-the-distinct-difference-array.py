import unittest
from typing import List, Dict


data = (([1, 2, 3, 4, 5], [-3, -1, 1, 3, 5]), ([3, 2, 3, 4, 2], [-2, -1, 0, 2, 3]))


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        def add_element_to_map(map: Dict[int, int], n: int):
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        def subtract_element_from_map(map: Dict[int, int], n: int):
            if n not in map:
                return
            map[n] -= 1
            if map[n] == 0:
                del map[n]

        left_elements_map = dict()
        add_element_to_map(left_elements_map, nums[0])
        right_elements_map = dict()
        for n in nums[1:]:
            add_element_to_map(right_elements_map, n)

        result = []

        for index, n in enumerate(nums):
            if index:
                add_element_to_map(left_elements_map, n)
                subtract_element_from_map(right_elements_map, n)

            left_distinct_elements_count = len(left_elements_map.keys())
            right_distinct_elements_count = len(right_elements_map.keys())

            result.append(left_distinct_elements_count - right_distinct_elements_count)

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.distinctDifferenceArray(nums))


if __name__ == "__main__":
    unittest.main()
