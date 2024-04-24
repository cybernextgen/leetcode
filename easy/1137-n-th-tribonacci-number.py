from functools import cache


class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return (
                self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            )


if __name__ == "__main__":
    for input_data, expected in (
        (4, 4),
        (25, 1389537),
    ):
        assert Solution().tribonacci(input_data) == expected
