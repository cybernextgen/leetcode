class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for index in range(1, len(nums), 2):
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
        return nums
        
