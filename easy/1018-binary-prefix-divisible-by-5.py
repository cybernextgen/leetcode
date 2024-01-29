import unittest
from typing import List

data = (([0, 1, 1], [True, False, False]), ([1, 1, 1], [False, False, False]))


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        bin_repr = ""
        result = []
        for ch in nums:
            bin_repr = f"{bin_repr}{ch}"
            num = int(bin_repr, 2)
            result.append(num % 5 == 0)
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(s.prefixesDivBy5(input_data), result)


if __name__ == "__main__":
    unittest.main()
