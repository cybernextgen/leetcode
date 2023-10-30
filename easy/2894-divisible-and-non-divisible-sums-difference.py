class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) / 2
        divisable_sum = sum(num for num in range(1, n + 1) if num % m == 0)
        not_divisable_sum = total_sum - divisable_sum
        return int(not_divisable_sum - divisable_sum)
