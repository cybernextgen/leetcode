import unittest
from typing import List

data = (([2, 4, 4], []), ([1, 4, 3, 8, 5], [1, 3]))


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result = []
        if len(mountain) < 3:
            return result

        current_index = 2
        while current_index <= len(mountain) - 1:
            peak_index = current_index - 1
            peak = mountain[peak_index]
            if mountain[current_index - 2] < peak and mountain[current_index] < peak:
                result.append(peak_index)
            current_index += 1

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.findPeaks(input_data))


if __name__ == "__main__":
    unittest.main()
