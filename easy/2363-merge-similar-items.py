from typing import List
import collections


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        weights1 = collections.Counter({k: v for k, v in items1})
        weights2 = collections.Counter({k: v for k, v in items2})
        merge_result = weights1 + weights2
        return [[k, v] for k, v in sorted(merge_result.items())]


class Solution2:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        weights = collections.defaultdict(int, {k: v for k, v in items1})

        for k, v in items2:
            weights[k] += v

        return [[k, v] for k, v in sorted(weights.items())]


if __name__ == "__main__":
    for list1, list2, expected in (
        ([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]], [[1, 6], [3, 9], [4, 5]]),
        ([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]], [[1, 4], [2, 4], [3, 4]]),
    ):
        assert Solution2().mergeSimilarItems(list1, list2) == expected
