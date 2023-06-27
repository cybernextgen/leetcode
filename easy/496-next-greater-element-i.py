import unittest
from typing import List

data = (([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]), ([2, 4], [1, 2, 3, 4], [3, -1]))


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {num: index for index, num in enumerate(nums2)}
        result = []
        last_index = len(nums2) - 1
        for num in nums1:
            index = indexes[num]

            while index < last_index:
                index += 1
                next_num = nums2[index]
                if next_num > num:
                    result.append(next_num)
                    break
            else:
                result.append(-1)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums1, nums2, expected in data:
            self.assertEqual(s.nextGreaterElement(nums1, nums2), expected)


if __name__ == "__main__":
    unittest.main()
