import unittest
from typing import List

data = ((["alic3", "bob", "3", "4", "00000"], 5), (["1", "01", "001", "0001"], 1))


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            try:
                current_val = int(s)
            except ValueError as e:
                current_val = len(s)
            max_val = max(max_val, current_val)
        return max_val


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.maximumValue(input_data))


if __name__ == "__main__":
    unittest.main()
