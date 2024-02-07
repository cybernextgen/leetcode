import unittest
from typing import List
import collections

data = (([1, 3, 2, 2, 5, 2, 3, 7], 5), ([1, 2, 3, 4], 2), ([1, 1, 1, 1], 0))


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        result = 0
        for key in counts:
            new_key = key + 1
            if new_key not in counts:
                continue

            new_result = counts[key] + counts[key + 1]
            result = max(result, new_result)

        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findLHS(input_data), expected)


if __name__ == "__main__":
    unittest.main()
