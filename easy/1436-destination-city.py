import unittest
from typing import List, Set

data = (
    (
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
        "Sao Paulo",
    ),
    ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
)


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_set: Set[str] = set()
        dst_set: Set[str] = set()
        for src, dst in paths:
            src_set.add(src)
            dst_set.add(dst)
        result = dst_set - src_set
        return result.pop()


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.destCity(input_data), expected)


if __name__ == "__main__":
    unittest.main()
