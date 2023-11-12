class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_difference = float("inf")
        result = []
        for num1, num2 in pairwise(sorted(arr)):
            current_difference = num2 - num1
            current_pair = [num1, num2]
            if current_difference == min_difference:
                result.append(current_pair)
            elif current_difference < min_difference:
                min_difference = current_difference
                result = [current_pair]
        return result
