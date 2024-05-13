from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result_dict = dict()
        for index, num in enumerate(sorted_nums):
            if num not in result_dict:
                result_dict[num] = index

        return [result_dict[num] for num in nums]


if __name__ == "__main__":
    for input_data, expected in (
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ):
        assert Solution().smallerNumbersThanCurrent(input_data) == expected
