from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(c + extraCandies) >= max_candies for c in candies]


if __name__ == "__main__":
    for input_data, extra_candies, expected in (
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
    ):
        assert Solution().kidsWithCandies(input_data, extra_candies) == expected
