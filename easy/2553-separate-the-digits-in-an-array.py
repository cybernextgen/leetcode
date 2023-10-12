import unittest
from typing import List

data = (([13, 25, 83, 77], [1, 3, 2, 5, 8, 3, 7, 7]), ([7, 1, 3, 9], [7, 1, 3, 9]))


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num < 10:
                result.append(num)
            else:
                for ch in str(num):
                    result.append(int(ch))
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.separateDigits(input_data))


if __name__ == "__main__":
    unittest.main()
