import unittest
from typing import List

data = (
    (["./", "../", "./"], 0),
    (["d1/", "d2/", "../", "d21/", "./"], 2),
    (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
    (["d1/", "../", "../", "../"], 0),
)


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deep = 0
        current_dir = "./"
        parent_dir = "../"
        for op in logs:
            if op == parent_dir and deep:
                deep -= 1
                continue
            if op != current_dir and op != parent_dir:
                deep += 1
        return deep


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.minOperations(input_data))


if __name__ == "__main__":
    unittest.main()
