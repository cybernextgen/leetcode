import unittest
from typing import List
import bisect

data = (([1, 2, 2, 6, 6, 6, 6, 7, 10], 6), ([1, 1], 1))


# O(n) time O(1) space
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        len_arr = len(arr)
        counts_required = len_arr // 4
        for index in range(len_arr):
            current_element = arr[index]
            if current_element == arr[index + counts_required]:
                return current_element
        return 0


class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts_required = len(arr) // 4
        if not counts_required:
            return arr[0]
        for n in arr[::counts_required]:
            if bisect.bisect(arr, n) - bisect.bisect_left(arr, n) > counts_required:
                return n
        return 0


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_list, expected in data:
            self.assertEqual(expected, s.findSpecialInteger(input_list))


if __name__ == "__main__":
    unittest.main()
