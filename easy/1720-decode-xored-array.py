from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for n in encoded:
            first = first ^ n
            result.append(first)
        return result


if __name__ == "__main__":
    for input_data, first, expected in (
        ([1, 2, 3], 1, [1, 0, 2, 1]),
        ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4]),
    ):
        assert Solution().decode(input_data, first) == expected
