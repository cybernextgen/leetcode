class Solution:
    def isSameAfterReversals(self, num: int) -> bool:        
        return num == 0 or num % 10 != 0
        # return num == 0 or str(num)[-1] != "0"
