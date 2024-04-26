class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiplier = 0
        while True:
            r = n + multiplier * n
            if r % 2 == 0:
                return r
            multiplier += 1


if __name__ == "__main__":
    for input_data, expected in ((5, 10), (6, 6)):
        assert Solution().smallestEvenMultiple(input_data) == expected
