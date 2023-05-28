import unittest
import operator
from typing import List

data = ((["cba", "daf", "ghi"], 1), (["a", "b"], 0), (["zyx", "wvu", "tsr"], 3))


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col_index in range(len(strs[0])):
            prev_ord = 0
            for row_index in range(len(strs)):
                current_ord = ord(strs[row_index][col_index])
                if current_ord < prev_ord:
                    result += 1
                    break
                prev_ord = current_ord
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.minDeletionSize(input_data), expected)


if __name__ == "__main__":
    unittest.main()
