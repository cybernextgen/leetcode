import unittest
from typing import List

data = (("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"), ("abc", [0, 1, 2], "abc"))


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for index, ch in enumerate(s):
            result[indices[index]] = ch
        return "".join(result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, indices, expected in data:
            self.assertEqual(expected, s.restoreString(input_data, indices))


if __name__ == "__main__":
    unittest.main()
