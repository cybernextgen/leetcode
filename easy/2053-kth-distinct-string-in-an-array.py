import unittest
from typing import List
import collections

data = (
    (["d", "b", "c", "b", "c", "a"], 2, "a"),
    (["aaa", "aa", "a"], 1, "aaa"),
    (["a", "b", "a"], 3, ""),
)


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = collections.Counter(arr)
        distinct_counts = 0
        for s in arr:
            if counts[s] > 1:
                continue
            distinct_counts += 1
            if distinct_counts == k:
                return s
        return ""


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for arr, k, expected in data:
            self.assertEqual(expected, s.kthDistinct(arr, k))


if __name__ == "__main__":
    unittest.main()
