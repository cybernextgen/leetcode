import unittest
from typing import List, Optional

data = (
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
)


class Solution:
    def __add_range(
        self,
        ranges: List[str],
        first_range_number: int,
        last_range_number: Optional[int],
    ) -> None:
        if last_range_number:
            ranges.append(f"{first_range_number}->{last_range_number}")
            return
        ranges.append(str(first_range_number))

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        first_range_number = nums[0]
        last_range_number = None
        prev_number = first_range_number
        for current_number in nums[1:]:
            if current_number - prev_number > 1:
                self.__add_range(ranges, first_range_number, last_range_number)
                first_range_number = current_number
                last_range_number = None
            else:
                last_range_number = current_number
            prev_number = current_number
        self.__add_range(ranges, first_range_number, last_range_number)
        return ranges


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.summaryRanges(input_data), expected)


if __name__ == "__main__":
    unittest.main()
