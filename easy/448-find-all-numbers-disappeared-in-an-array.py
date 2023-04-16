import unittest
from typing import List

data = (
    ([4,3,2,7,8,2,3,1], [5, 6]),
    ([1,1], [2])
)

# Memory: O(n)
# Runtime: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        max_number = len(nums)
        numbers_available_set = set(range(1, max_number + 1))
        return list(numbers_available_set.difference(nums))

class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.findDisappearedNumbers(input_data), expected)

if __name__ == "__main__":
    unittest.main()