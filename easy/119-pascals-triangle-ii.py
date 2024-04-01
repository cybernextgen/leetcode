import unittest
from typing import List


data = ((3, [1, 3, 3, 1]), (0, [1]), (1, [1, 1]))


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        prev_row = self.getRow(rowIndex - 1)
        elements_count = rowIndex + 1
        result = [0] * elements_count

        result[0] = result[-1] = prev_row[0]

        i, has_medium_element = divmod(elements_count, 2)
        for index in range(1, i):
            result[index] = result[-index - 1] = prev_row[index - 1] + prev_row[index]
        if has_medium_element:
            result[i] = prev_row[i] + prev_row[i - 1]
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.getRow(input_data))


if __name__ == "__main__":
    unittest.main()
