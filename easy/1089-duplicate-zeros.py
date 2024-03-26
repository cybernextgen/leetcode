import unittest
from typing import List

data = (([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]), ([1, 2, 3], [1, 2, 3]))


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        result = []
        result_len = len(arr)
        for ch in arr:
            if result_len == 0:
                break
            result.append(ch)
            result_len -= 1
            if ch == 0 and result_len > 0:
                result.append(ch)
                result_len -= 1
                
        for index in range(len(arr)):
            arr[index] = result[index]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            s.duplicateZeros(input_data)
            self.assertListEqual(expected, input_data)


if __name__ == "__main__":
    unittest.main()
