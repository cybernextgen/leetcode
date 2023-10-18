from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        for num, count in counts.items():
            if count == 1:
                result += num
        return result
