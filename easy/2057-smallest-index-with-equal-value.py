class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        if not nums:
            return -1
        res = [index for index, num in enumerate(nums) if index % 10 == num]
        if not res:
            return -1
        return min(res)
