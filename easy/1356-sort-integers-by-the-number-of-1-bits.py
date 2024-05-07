from typing import List
import functools


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cmp = lambda a, b: f"{a:b}".count("1") - f"{b:b}".count("1") or a - b

        return sorted(arr, key=functools.cmp_to_key(cmp))


if __name__ == "__main__":
    for input_data, expected in (
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
        (
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ):
        assert Solution().sortByBits(input_data) == expected
